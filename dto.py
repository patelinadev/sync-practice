from pydantic import BaseModel


class SquareRequestDto(BaseModel):
    side_length: int

class SquareResponseDto(BaseModel):
    result: str

class HollowSquareRequestDto(BaseModel):
    side_length: int

class HollowSquareResponseDto(BaseModel):
    result: str