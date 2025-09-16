from pydantic import BaseModel


class SquareRequestDto(BaseModel):
    side_length: int

class SquareResponseDto(BaseModel):
    result: str

class HollowSquareRequestDto(BaseModel):
    side_length: int

class HollowSquareResponseDto(BaseModel):
    result: str

class EquilateralTriangleRequestDto(BaseModel):
    base_length:int

class EquilateralTriangleResponseDto(BaseModel):
    result: str

class IsoscelesTriangle01RequestDto(BaseModel):
    base_length: int

class IsoscelesTriangle01ResponseDto(BaseModel):
    result: str

class IsoscelesTriangle02RequestDto(BaseModel):
    base_length: int
    height: int

class IsoscelesTriangle02ResponseDto(BaseModel):
    result: str

class HollowIsoscelesTriangle01RequestDto(BaseModel):
    base_length:int

class HollowIsoscelesTriangle01ResponseDto(BaseModel):
    result: str

class HollowIsoscelesTriangle02RequestDto(BaseModel):
    base_length: int
    height: int

class HollowIsoscelesTriangle02ResponseDto(BaseModel):
    result: str
# ---Trapezoid---
class TrapezoidRequestDto(BaseModel):
    base_length: int
    height: int

class TrapezoidResponseDto(BaseModel):
    result: str
# ---Diamond---
class DiamondRequestDto(BaseModel):
    side_length:int

class DiamondResponseDto(BaseModel):
    result: str

class HollowDiamondRequestDto(BaseModel):
    side_length:int

class HollowDiamondResponseDto(BaseModel):
    result:str

class HollowRectangleDiamondRequestDto(BaseModel):
    side_length:int

class HollowRectangleDiamondResponseDto(BaseModel):
    result: str
# ---Hexagon---
class HexagonRequestDto(BaseModel):
    side_length:int

class HexagonResponseDto(BaseModel):
    result: str
