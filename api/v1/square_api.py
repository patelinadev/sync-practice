from fastapi import APIRouter
from dto import SquareRequestDto, SquareResponseDto
from service.geometry_service import geometry_service

router = APIRouter(
    prefix="/squares",
    tags=["Squares"],
)

@router.post("/draw-solid-squares", response_model=SquareResponseDto)
async def draw_solid_square_endpoint(request_dto: SquareRequestDto):
    ascii_shape = geometry_service.draw_solid_square(request_dto)
    return SquareResponseDto(result=ascii_shape)

@router.post("/draw-hollow-squares", response_model=SquareResponseDto)
async def draw_hollow_square_endpoint(request_dto: SquareRequestDto):
    ascii_shape = geometry_service.draw_hollow_square(request_dto)
    return SquareResponseDto(result=ascii_shape)
