from pydantic import BaseModel, Field
from typing import Literal

class Car(BaseModel):
    brand: str
    model: str
    model_year: int = Field(..., ge=1990, le=2025)
    mileage: float = Field(..., ge=0)
    fuel_type: Literal[
        'Gasoline',
        'Hybrid',
        'Diesel',
        'E85 Flex Fuel',
        'Plug-In Hybrid'
    ]
    accident: Literal['Yes', 'No']
    clean_title: Literal['Yes', 'No']
    engine_size: float = Field(..., ge=1.0, le=8.3)
    engine_turbo: bool
    color_ext: str
    color_int: str
    metallic: bool
    type_transmission: Literal[
        'Automatic',
        'Manual',
        'CVT',
        'DCT',
        'Single',
        'Other'
    ]

    speed_num: int = Field(..., ge=1, le=10)

