from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from loin.iso_23387 import (
    DataTemplateType,
    DimensionType,
    GroupOfPropertiesType,
    ObjectType,
    PhysicalQuantityType,
    PropertyType,
    ReferenceDocumentType,
    UnitType,
)

__NAMESPACE__ = "https://iso.org/2024/LOIN"


class AppearanceEnum(Enum):
    NO_COLOR = "NoColor"
    SINGLE_COLOR = "SingleColor"
    MATERIAL_COLOR = "MaterialColor"
    TEXTURES = "Textures"


class DetailEnum(Enum):
    L1 = "L1"
    L2 = "L2"
    L3 = "L3"
    L4 = "L4"
    L5 = "L5"


class DimensionalityEnum(Enum):
    D0 = "D0"
    D1 = "D1"
    D2 = "D2"
    D3 = "D3"


class LocationEnum(Enum):
    ABSOLUTE = "Absolute"
    RELATIVE = "Relative"


class ParametricBehaviourEnum(Enum):
    EXPLICIT_GEOMETRY = "ExplicitGeometry"
    CONSTRUCTIVE_GEOMETRY = "ConstructiveGeometry"
    PARAMETRIC_GEOMETRY = "ParametricGeometry"


@dataclass
class Prerequisites:
    node_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "nodeID",
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    purpose: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    information_delivery_milestone: Optional[str] = field(
        default=None,
        metadata={
            "name": "informationDeliveryMilestone",
            "type": "Attribute",
        }
    )
    sending_actor: Optional[str] = field(
        default=None,
        metadata={
            "name": "sendingActor",
            "type": "Attribute",
        }
    )
    receiving_actor: Optional[str] = field(
        default=None,
        metadata={
            "name": "receivingActor",
            "type": "Attribute",
        }
    )


@dataclass
class RequiredDocument:
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )
    purpose: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: Optional[str] = field(
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


@dataclass
class Documentation:
    required_document: List[RequiredDocument] = field(
        default_factory=list,
        metadata={
            "name": "RequiredDocument",
            "type": "Element",
            "namespace": "",
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


@dataclass
class GeometricalInformation:
    detail: Optional[DetailEnum] = field(
        default=None,
        metadata={
            "name": "Detail",
            "type": "Element",
            "namespace": "",
        }
    )
    dimensionality: Optional[DimensionalityEnum] = field(
        default=None,
        metadata={
            "name": "Dimensionality",
            "type": "Element",
            "namespace": "",
        }
    )
    location: Optional[LocationEnum] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "",
        }
    )
    appearance: Optional[AppearanceEnum] = field(
        default=None,
        metadata={
            "name": "Appearance",
            "type": "Element",
            "namespace": "",
        }
    )
    parametric_behaviour: Optional[ParametricBehaviourEnum] = field(
        default=None,
        metadata={
            "name": "ParametricBehaviour",
            "type": "Element",
            "namespace": "",
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


@dataclass
class SpecificationPerObjectType(DataTemplateType):
    documentation: Optional[Documentation] = field(
        default=None,
        metadata={
            "name": "Documentation",
            "type": "Element",
            "namespace": "",
        }
    )
    geometrical_information: Optional[GeometricalInformation] = field(
        default=None,
        metadata={
            "name": "GeometricalInformation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Specification:
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "",
        }
    )
    prerequisites: Optional[Prerequisites] = field(
        default=None,
        metadata={
            "name": "Prerequisites",
            "type": "Element",
            "namespace": "",
        }
    )
    specification_per_object_type: List[SpecificationPerObjectType] = field(
        default_factory=list,
        metadata={
            "name": "SpecificationPerObjectType",
            "type": "Element",
            "namespace": "",
            "nillable": True,
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LevelOfInformationNeed:
    """
    Level of Information Need as defined by ISO 7817.
    """
    class Meta:
        namespace = "https://iso.org/2024/LOIN"

    specification: List[Specification] = field(
        default_factory=list,
        metadata={
            "name": "Specification",
            "type": "Element",
            "namespace": "",
        }
    )
    object_types: Optional["LevelOfInformationNeed.ObjectTypes"] = field(
        default=None,
        metadata={
            "name": "ObjectTypes",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    alphanumerical_information: List["LevelOfInformationNeed.AlphanumericalInformation"] = field(
        default_factory=list,
        metadata={
            "name": "AlphanumericalInformation",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class ObjectTypes:
        object_type: List[ObjectType] = field(
            default_factory=list,
            metadata={
                "name": "ObjectType",
                "type": "Element",
                "namespace": "",
            }
        )

    @dataclass
    class AlphanumericalInformation:
        property: List[PropertyType] = field(
            default_factory=list,
            metadata={
                "name": "Property",
                "type": "Element",
                "namespace": "",
            }
        )
        physical_quantity: List[PhysicalQuantityType] = field(
            default_factory=list,
            metadata={
                "name": "PhysicalQuantity",
                "type": "Element",
                "namespace": "",
            }
        )
        set_of_properties: List[GroupOfPropertiesType] = field(
            default_factory=list,
            metadata={
                "name": "SetOfProperties",
                "type": "Element",
                "namespace": "",
            }
        )
        purpose: List[GroupOfPropertiesType] = field(
            default_factory=list,
            metadata={
                "name": "Purpose",
                "type": "Element",
                "namespace": "",
            }
        )
        intended_use: List[GroupOfPropertiesType] = field(
            default_factory=list,
            metadata={
                "name": "IntendedUse",
                "type": "Element",
                "namespace": "",
            }
        )
        user_defined: List[GroupOfPropertiesType] = field(
            default_factory=list,
            metadata={
                "name": "UserDefined",
                "type": "Element",
                "namespace": "",
            }
        )
        reference_document: List[ReferenceDocumentType] = field(
            default_factory=list,
            metadata={
                "name": "ReferenceDocument",
                "type": "Element",
                "namespace": "",
            }
        )
        dimension: List[DimensionType] = field(
            default_factory=list,
            metadata={
                "name": "Dimension",
                "type": "Element",
                "namespace": "",
            }
        )
        unit: List[UnitType] = field(
            default_factory=list,
            metadata={
                "name": "Unit",
                "type": "Element",
                "namespace": "",
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
