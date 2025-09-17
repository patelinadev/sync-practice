from fastapi import APIRouter
from dto import TrapezoidResponseDto, TrapezoidRequestDto
from service.geometry_service import geometry_service


router = APIRouter(
    prefix="/trapezoid",
    tags=["trapezoid"]
)

@router.post("/draw_trapezoid", response_model = TrapezoidResponseDto)
async def draw_trapezoid(request_dto: TrapezoidRequestDto):
    ascii_shape = geometry_service.draw_trapezoid(request_dto)
    return TrapezoidResponseDto(result = ascii_shape)