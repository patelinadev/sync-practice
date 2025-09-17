from fastapi import APIRouter
from dto import *
from service.geometry_service import geometry_service

router = APIRouter(
    prefix="/squares",
    tags=["Squares"],
)

@router.post("/draw-squares", response_model = SquareResponseDto)
async def draw_square_endpoint(request_dto: SquareRequestDto):
    ascii_shape = geometry_service.draw_solid_square(request_dto)
    return SquareResponseDto(result=ascii_shape)

@router.post("/draw-hollow-squares", response_model = HollowSquareResponseDto)
async def draw_hollow_square_endpoint(request_dto: HollowSquareRequestDto):
    ascii_shape = geometry_service.draw_hollow_square(request_dto)
    return HollowSquareResponseDto(result=ascii_shape)
