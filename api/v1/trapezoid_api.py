from fastapi import APIRouter, Depends
from dto import TrapezoidResponseDto, TrapezoidRequestDto
from service.geometry_service import GeometryService, get_geometry_service


router = APIRouter(
    prefix="/trapezoid",
    tags=["trapezoid"]
)

@router.post("/draw_trapezoid", response_model = TrapezoidResponseDto)
async def draw_trapezoid(request_dto: TrapezoidRequestDto, service: GeometryService = Depends(get_geometry_service)):
    ascii_shape = service.draw_trapezoid(request_dto)
    return TrapezoidResponseDto(result = ascii_shape)