from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDateTime
from loin.xml import LangValue

__NAMESPACE__ = "http://tempuri.org/XMLSchema.xsd"


class BaseType(Enum):
    ONE = "ONE"
    TWO = "TWO"
    E = "E"
    PI = "PI"
    TEN = "TEN"


class DatatypeTypeName(Enum):
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"
    RATIONAL = "RATIONAL"
    REAL = "REAL"
    COMPLEX = "COMPLEX"
    STRING = "STRING"
    DATETIME = "DATETIME"


@dataclass
class ReferenceType:
    class Meta:
        name = "referenceType"

    resource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    node_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "nodeID",
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )


class ScaleType(Enum):
    LINEAR = "LINEAR"
    LOGARITHMIC = "LOGARITHMIC"


@dataclass
class MultilingualTextType:
    class Meta:
        name = "multilingualTextType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class ValuesType:
    class Meta:
        name = "valuesType"

    value: List["ValuesType.Value"] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "min_occurs": 1,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )

    @dataclass
    class Value:
        value: Optional[object] = field(
            default=None
        )
        order: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class ConceptType:
    class Meta:
        name = "conceptType"

    name: List[MultilingualTextType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "min_occurs": 1,
        }
    )
    definition: List[MultilingualTextType] = field(
        default_factory=list,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    reference_document: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceDocument",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    about: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    node_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "nodeID",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DatatypeType:
    """
    :ivar min_inclusive: MinInclusive is the inclusive lower bound of
        the value for a datatype
    :ivar max_inclusive: MaxInclusive is the inclusive upper bound of
        the value for a datatype
    :ivar min_exclusive: MinExclusive is the exclusive lower bound of
        the value for a datatype
    :ivar max_exclusive: MaxExclusive is the exclusive upper bound of
        the value for a datatype
    :ivar pattern: Pattern is a constraint on the value of a datatype
        which is achieved by constraining the value to literals which
        macht a specific pattern. The value of pattern must be a regular
        expression
    :ivar enumeration: Enumeration constrains the value to a specified
        set of values
    :ivar name:
    """
    class Meta:
        name = "datatypeType"

    min_inclusive: Optional["DatatypeType.MinInclusive"] = field(
        default=None,
        metadata={
            "name": "MinInclusive",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    max_inclusive: Optional["DatatypeType.MaxInclusive"] = field(
        default=None,
        metadata={
            "name": "MaxInclusive",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    min_exclusive: Optional["DatatypeType.MinExclusive"] = field(
        default=None,
        metadata={
            "name": "MinExclusive",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    max_exclusive: Optional["DatatypeType.MaxExclusive"] = field(
        default=None,
        metadata={
            "name": "MaxExclusive",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    pattern: Optional["DatatypeType.Pattern"] = field(
        default=None,
        metadata={
            "name": "Pattern",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    enumeration: Optional["DatatypeType.Enumeration"] = field(
        default=None,
        metadata={
            "name": "Enumeration",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    name: Optional[DatatypeTypeName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class MinInclusive:
        value: Optional[object] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class MaxInclusive:
        value: Optional[object] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class MinExclusive:
        value: Optional[object] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class MaxExclusive:
        value: Optional[object] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Pattern:
        value: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Enumeration:
        unit: Optional[ReferenceType] = field(
            default=None,
            metadata={
                "name": "Unit",
                "type": "Element",
                "namespace": "http://tempuri.org/XMLSchema.xsd",
            }
        )
        values: List[ValuesType] = field(
            default_factory=list,
            metadata={
                "name": "Values",
                "type": "Element",
                "namespace": "http://tempuri.org/XMLSchema.xsd",
                "min_occurs": 1,
            }
        )


@dataclass
class DataTemplateType(ConceptType):
    class Meta:
        name = "dataTemplateType"

    object_value: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Object",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    data_template: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "DataTemplate",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    property: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    set_of_properties: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "SetOfProperties",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )


@dataclass
class DimensionType(ConceptType):
    class Meta:
        name = "dimensionType"

    dimension_exponent_for_amount_of_substance: Optional[int] = field(
        default=None,
        metadata={
            "name": "DimensionExponentForAmountOfSubstance",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    dimension_exponent_for_electric_current: Optional[int] = field(
        default=None,
        metadata={
            "name": "DimensionExponentForElectricCurrent",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    dimension_exponent_for_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "DimensionExponentForLength",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    dimension_exponent_for_luminous_intensity: Optional[int] = field(
        default=None,
        metadata={
            "name": "DimensionExponentForLuminousIntensity",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    dimension_exponent_for_mass: Optional[int] = field(
        default=None,
        metadata={
            "name": "DimensionExponentForMass",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    dimension_exponent_for_thermodynamic_temperature: Optional[int] = field(
        default=None,
        metadata={
            "name": "DimensionExponentForThermodynamicTemperature",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    dimension_exponent_for_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "DimensionExponentForTime",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )


@dataclass
class GroupOfPropertiesType(ConceptType):
    class Meta:
        name = "groupOfPropertiesType"

    property: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    set_of_properties: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "SetOfProperties",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )


@dataclass
class ObjectType(ConceptType):
    class Meta:
        name = "objectType"

    object_value: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Object",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )


@dataclass
class PhysicalQuantityType(ConceptType):
    class Meta:
        name = "physicalQuantityType"

    dimensions: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "Dimensions",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )


@dataclass
class PropertyType(ConceptType):
    class Meta:
        name = "propertyType"

    data_type: Optional[DatatypeType] = field(
        default=None,
        metadata={
            "name": "DataType",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    symbol: Optional[str] = field(
        default=None,
        metadata={
            "name": "Symbol",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    unit: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    physical_quantity: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "PhysicalQuantity",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    property: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )


@dataclass
class ReferenceDocumentType(ConceptType):
    class Meta:
        name = "referenceDocumentType"

    date_of_publication: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DateOfPublication",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    isbn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    publisher: Optional[str] = field(
        default=None,
        metadata={
            "name": "Publisher",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
        }
    )


@dataclass
class UnitType(ConceptType):
    class Meta:
        name = "unitType"

    symbol: List[MultilingualTextType] = field(
        default_factory=list,
        metadata={
            "name": "Symbol",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "min_occurs": 1,
        }
    )
    dimension: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    scale: Optional[ScaleType] = field(
        default=None,
        metadata={
            "name": "Scale",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    base: Optional[BaseType] = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    coefficient: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coefficient",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )
    offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://tempuri.org/XMLSchema.xsd",
            "required": True,
        }
    )


@dataclass
class Library:
    class Meta:
        namespace = "http://tempuri.org/XMLSchema.xsd"

    name: List[MultilingualTextType] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
        }
    )
    data_template: List[DataTemplateType] = field(
        default_factory=list,
        metadata={
            "name": "DataTemplate",
            "type": "Element",
        }
    )
    property: List[PropertyType] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
        }
    )
    physical_quantity: List[PhysicalQuantityType] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalQuantity",
            "type": "Element",
        }
    )
    set_of_properties: List[GroupOfPropertiesType] = field(
        default_factory=list,
        metadata={
            "name": "SetOfProperties",
            "type": "Element",
        }
    )
    purpose: List[GroupOfPropertiesType] = field(
        default_factory=list,
        metadata={
            "name": "Purpose",
            "type": "Element",
        }
    )
    intended_use: List[GroupOfPropertiesType] = field(
        default_factory=list,
        metadata={
            "name": "IntendedUse",
            "type": "Element",
        }
    )
    user_defined: List[GroupOfPropertiesType] = field(
        default_factory=list,
        metadata={
            "name": "UserDefined",
            "type": "Element",
        }
    )
    reference_document: List[ReferenceDocumentType] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceDocument",
            "type": "Element",
        }
    )
    object_value: List[ObjectType] = field(
        default_factory=list,
        metadata={
            "name": "Object",
            "type": "Element",
        }
    )
    dimension: List[DimensionType] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
        }
    )
    unit: List[UnitType] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
        }
    )
    node_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "nodeID",
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
