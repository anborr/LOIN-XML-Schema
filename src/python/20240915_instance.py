from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from loin.iso_7817_3 import (
    AppearanceEnum,
    DetailEnum,
    DimensionalityEnum,
    GeometricalInformation,
    LevelOfInformationNeed,
    LocationEnum,
    ParametricBehaviourEnum,
    RequiredDocument,
    Specification,
    SpecificationPerObjectType,
    ObjectType,
    Prerequisites,
    Documentation,
)
from loin.iso_23887 import (
    DatatypeType,
    DatatypeTypeName,
    GroupOfPropertiesType,
    MultilingualTextType,
    PhysicalQuantityType,
    PropertyType,
    ReferenceType,
    UnitType,
    DimensionType,
)


loin = LevelOfInformationNeed()

# first, fill the information content with what we need

real_type = DatatypeType()
real_type.name = DatatypeTypeName.REAL
real_type.min_inclusive = DatatypeType.MinInclusive(value=0.0)

# references to external definitions 
centimeter_unit_external_ref = ReferenceType(
    resource="https://datadictionary2.org/cm")
length_quantity_external_ref = ReferenceType(
    resource="https://datadictionary3.org/length")

length_dimension = DimensionType()
length_dimension.name.append(MultilingualTextType("Length", "en"))
length_dimension.name.append(MultilingualTextType("Länge", "de"))
length_dimension.dimension_exponent_for_length = 1
loin.alphanumericalinformation.dimension.append(length_dimension)
length_dimension_reference = ReferenceType(node_id=length_dimension.node_id)

centimeter_unit = UnitType()
centimeter_unit.name.append(MultilingualTextType("Centimeter", "en"))
centimeter_unit.name.append(MultilingualTextType("Zentimeter", "de"))
centimeter_unit.definition.append(MultilingualTextType(
    "Centimeter according to ISO 80000", "en"))
centimeter_unit.dimension = length_dimension_reference
loin.alphanumericalinformation.unit.append(centimeter_unit)
centimeter_unit_ref = ReferenceType(node_id=centimeter_unit.node_id)

length_quantity = PhysicalQuantityType()
length_quantity.name.append(MultilingualTextType("Length", "en"))
length_quantity.name.append(MultilingualTextType("Länge", "de"))
length_quantity.definition.append(MultilingualTextType(
    "Definition of Length physical quantity.", "en"))
length_quantity.dimensions = length_dimension_reference
loin.alphanumericalinformation.physical_quantity.append(length_quantity)
length_quantity_ref = ReferenceType(node_id=length_quantity.node_id)

wingwall = ObjectType()
wingwall.name.append(MultilingualTextType("Wing Wall", "en"))
wingwall.name.append(MultilingualTextType("Flügelmauer", "de"))
wingwall.definition.append(MultilingualTextType(
    "The lateral wall of a bridge abutment.", "en"))
loin.object_types.object_type.append(wingwall)
wingwall_ref = ReferenceType(node_id=wingwall.node_id)

length = PropertyType()
length.name.append(MultilingualTextType("Length", "en"))
length.name.append(MultilingualTextType("Länge", "de"))
length.definition.append(MultilingualTextType(
    "Length according to ISO XXX-YYYY.", "en"))
length.data_type = real_type
length.unit.append(centimeter_unit_external_ref)
length.physical_quantity = length_quantity_external_ref
loin.alphanumericalinformation.property.append(length)
length_ref = ReferenceType(node_id=length.node_id)

width = PropertyType()
width.name.append(MultilingualTextType("Width", "en"))
width.name.append(MultilingualTextType("Breite", "de"))
width.definition.append(MultilingualTextType(
    "Width according to ISO XXX-YYYY.", "en"))
width.data_type = real_type
width.unit.append(centimeter_unit_ref)
width.physical_quantity = length_quantity_ref
loin.alphanumericalinformation.property.append(width)
width_ref = ReferenceType(node_id=width.node_id)

dimensions = GroupOfPropertiesType()
dimensions.name.append(MultilingualTextType("Dimensions", "en"))
dimensions.name.append(MultilingualTextType("Abmessungen", "de"))
dimensions.definition.append(MultilingualTextType(
    "Definition of Dimensions group of properties.", "en"))
dimensions.property.append(length_ref)
dimensions.property.append(width_ref)
loin.alphanumericalinformation.set_of_properties.append(dimensions)
dimensions_ref = ReferenceType(node_id=dimensions.node_id)


# generate the specification using the parts we defined before
specification = Specification()
specification.name = "Bridge Handover to Client"
specification.description = "Defines the requirements for bridge models when handed over to the client."
loin.specification.append(specification)

prerequisities = Prerequisites(purpose="Operation and Maintenance",
                               information_delivery_milestone="Handover", sending_actor="Contractor",
                               receiving_actor="Client")
specification.prerequisites = prerequisities

spec_per_object_type = SpecificationPerObjectType(
    about="http://www.company.org/cum/sonoras")
spec_per_object_type.name.append(
    MultilingualTextType("Specification for Wing Wall", "en"))
spec_per_object_type.definition.append(MultilingualTextType(
    "The lateral wall of a bridge abutment.", "en"))
spec_per_object_type.reference_document.append(ReferenceType(
    resource="https://identifier.buildingsmart.org/uri/nbs/uniclass2015/1/class/Ss_20_50_10_95"))

spec_per_object_type.object_value.append(wingwall_ref)
spec_per_object_type.set_of_properties.append(dimensions_ref)

required_document = RequiredDocument(
    type_value="Technical Drawing", purpose="Archive", content="Horizontal Projection")
doc = Documentation()
doc.required_document.append(required_document)
spec_per_object_type.documentation = doc

geom_info = GeometricalInformation(detail=DetailEnum.L4, dimensionality=DimensionalityEnum.D0, location=LocationEnum.RELATIVE,
                                   appearance=AppearanceEnum.TEXTURES, parametric_behaviour=ParametricBehaviourEnum.CONSTRUCTIVE_GEOMETRY)
spec_per_object_type.geometrical_information = geom_info
specification.specification_per_object_type.append(spec_per_object_type)


# Create a SerializerConfig with custom settings
serializer_config = SerializerConfig(
    # Enable pretty-printing (adds line breaks and indentation)
    pretty_print=True,
    pretty_print_indent="    "  # Indentation using 4 spaces (adjust as needed)
)

# Serialize the object into an XML instance file
serializer = XmlSerializer(config=serializer_config)
xml_instance = serializer.render(loin)

# Write the XML instance to a file
with open("20240915_instance.xml", "w") as f:
    f.write(xml_instance)
