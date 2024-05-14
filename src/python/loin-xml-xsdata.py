from loin.en_17412_3 import *
from loin.iso_23887 import *
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

# Define a container dataclass to hold objects of different types
@dataclass
class Container:
    Loin: List[LevelOfInformationNeed]
    Object: List[ObjectType]
    Unit : List[UnitType]
    Property : List[PropertyType]

# Instantiate the objects of the generated classes
my_loin = LevelOfInformationNeed()
my_specification = Specification()
my_loin.specification = my_specification

# Populate the objects with data
my_specification.description = "LOIN for Bridge data at handover to client"
my_specification.name = "Bridge_Handover_to_Client"

specification_for_wingwalls = SpecificationPerObjectType()
my_specification.specification_per_object_type = specification_for_wingwalls

specification_for_wingwalls.alphanumerical_information = None
specification_for_wingwalls.documentation = None
specification_for_wingwalls.uuid = "10108f20-34b2-4996-aa7d-5ec9ba182234"


my_object_type = ObjectType()
specification_for_wingwalls.object_type = my_object_type
my_object_type.node_id = "3b7802f6-b9a2-4062-ab23-69fa92c4984f"
my_object_type.name = "Wing Wall"
my_object_type_ref = ReferenceType(node_id=my_object_type.node_id)

string_type = DatatypeType()
string_type.name = "REAL"

centimeter_unit = UnitType()
centimeter_unit.node_id = "ebdfe50c-474a-482e-9bd6-db93bcaac3d1"
centimeter_unit.name = "Centimeter"
centimeter_unit.definition ="Centimeter according to ISO 80000"
centimeter_unit.scale = "LINEAR"
centimeter_unit.base = "TEN"
centimeter_unit.coefficient = 100
centimeter_unit.offset = 0
centimeter_unit_ref = ReferenceType(node_id=centimeter_unit.node_id)

width_property = PropertyType()
width_property.node_id = "8ef0be47-929f-428a-9016-ec1e1f1f7616"
width_property.name = "width"
width_property.data_type = "REAL"
width_property.unit = centimeter_unit_ref
width_property_ref =ReferenceType(node_id=width_property.node_id)

length_property = PropertyType()
length_property.node_id = "c4a14d69-1ad7-4e66-bacc-7985e21493ba"
length_property.name= "length"
length_property.data_type = "REAL"
length_property.unit = centimeter_unit_ref
length_property_ref =ReferenceType(node_id=length_property.node_id)

my_data_template = DataTemplateType()
specification_for_wingwalls.alphanumerical_information = [my_data_template]
#my_data_template.object_value = my_object_type  # not allowed, must use ref
my_data_template.object_value = my_object_type_ref
my_data_template.property = [width_property_ref, length_property_ref]

# Create a container object to hold objects of different types
container = Container(Loin=[my_loin], Object=[my_object_type], Unit=[centimeter_unit], Property=[width_property, length_property])


# Create a SerializerConfig with custom settings
serializer_config = SerializerConfig(
    pretty_print=True,          # Enable pretty-printing (adds line breaks and indentation)
    pretty_print_indent="    "  # Indentation using 4 spaces (adjust as needed)
)

# Serialize the object into an XML instance file
serializer = XmlSerializer(config=serializer_config)
xml_instance = serializer.render(container)

# Write the XML instance to a file
with open("output.xml", "w") as f:
    f.write(xml_instance)
