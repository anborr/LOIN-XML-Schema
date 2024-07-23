from dataclasses import dataclass
from typing import List
from loin.en_17412_3 import (
    LevelOfInformationNeed,
    Specification,
    SpecificationPerObjectType,
    ObjectType,
)
from loin.iso_23887 import (
    DataTemplateType,
    DatatypeType,
    DatatypeTypeName,
    MultilingualTextType,
    ScaleType,
    PropertyType,
    ReferenceType,
    UnitType,
    BaseType,
)
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime


# Define a container dataclass to hold objects of different types
@dataclass
class Container:
    Loin: List[LevelOfInformationNeed]
    Object: List[ObjectType]
    Unit: List[UnitType]
    Property: List[PropertyType]


# Instantiate the objects of the generated classes
my_loin = LevelOfInformationNeed()
my_specification = Specification()
my_loin.specification.append(my_specification)

# Populate the objects with data
my_specification.description = "LOIN for Bridge data at handover to client"
my_specification.name = "Bridge_Handover_to_Client"

specification_for_wingwalls = SpecificationPerObjectType()
my_specification.specification_per_object_type.append(
    specification_for_wingwalls)

# not required because default is empty list
# specification_for_wingwalls.alphanumerical_information = None
# specification_for_wingwalls.documentation = None
# not required anymore, because the ConceptType default constructor aready creates one
# specification_for_wingwalls.uuid = "10108f20-34b2-4996-aa7d-5ec9ba182234"

date = XmlDateTime(2024, 6, 14, 10, 17, 3)
my_object_type = ObjectType(date=date)
# my_object_type.node_id = "3b7802f6-b9a2-4062-ab23-69fa92c4984f"
my_object_type.name.append(MultilingualTextType("Wing Wall", "en"))
my_object_type.name.append(MultilingualTextType("Flügelmauer", "de"))
my_object_type_ref = ReferenceType(node_id=my_object_type.node_id)
# QUESTION: why does this not need to be a reference? See DataTemplateType
specification_for_wingwalls.object_type = my_object_type

real_type = DatatypeType()
real_type.name = DatatypeTypeName.REAL

centimeter_unit = UnitType(date=date)
# centimeter_unit.node_id = "ebdfe50c-474a-482e-9bd6-db93bcaac3d1"
centimeter_unit.name.append(MultilingualTextType("Centimeter", "en"))
centimeter_unit.symbol.append(MultilingualTextType("cm", "en"))
centimeter_unit.definition.append(MultilingualTextType(
    "Centimeter according to ISO 80000", "en"))
centimeter_unit.scale = ScaleType.LINEAR
centimeter_unit.base = BaseType.TEN
centimeter_unit.coefficient = 100
centimeter_unit.offset = 0
centimeter_unit_ref = ReferenceType(node_id=centimeter_unit.node_id)

width_property = PropertyType(date=date)
# width_property.node_id = "8ef0be47-929f-428a-9016-ec1e1f1f7616"
width_property.name.append(MultilingualTextType("Width", "en"))
width_property.data_type = real_type
width_property.unit.append(centimeter_unit_ref)
width_property_ref = ReferenceType(node_id=width_property.node_id)

length_property = PropertyType(date=date)
# length_property.node_id = "c4a14d69-1ad7-4e66-bacc-7985e21493ba"
length_property.name.append(MultilingualTextType("Length", "en"))
length_property.data_type = real_type
length_property.unit.append(centimeter_unit_ref)
length_property_ref = ReferenceType(node_id=length_property.node_id)

my_data_template = DataTemplateType(date=date)
# my_data_template.object_value = my_object_type  # not allowed, must use ref
my_data_template.object_value.append(my_object_type_ref)
my_data_template.property = [width_property_ref, length_property_ref]
specification_for_wingwalls.alphanumerical_information.append(my_data_template)

# Create a container object to hold objects of different types
container = Container(Loin=[my_loin],
                      Object=[my_object_type],  # PD: Fix for double definition of object could be to not pass it here, but use an empty list. Then the Object property of the Container would not be needed anymore.
                      Unit=[centimeter_unit],
                      Property=[width_property, length_property])


# Create a SerializerConfig with custom settings
serializer_config = SerializerConfig(
    # Enable pretty-printing (adds line breaks and indentation)
    pretty_print=True,
    pretty_print_indent="    "  # Indentation using 4 spaces (adjust as needed)
)

# Serialize the object into an XML instance file
serializer = XmlSerializer(config=serializer_config)
xml_instance = serializer.render(container)

# Write the XML instance to a file
with open("output.xml", "w") as f:
    f.write(xml_instance)
