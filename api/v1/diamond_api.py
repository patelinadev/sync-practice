from fastapi import APIRouter
from dto import *
from service.geometry_service import geometry_service

router = APIRouter(
    prefix="/diamond",
    tags=["diamond"]
)

@router.post("/draw_diamond",response_model = DiamondResponseDto)
async def draw_diamond(request_dto: DiamondRequestDto):
    ascii_shape = geometry_service.draw_diamond(request_dto)
    return DiamondResponseDto(result = ascii_shape)

@router.post("/draw_hollow_diamond", response_model = HollowDiamondResponseDto)
async def draw_hollow_diamond(request_dto: HollowDiamondRequestDto):
    ascii_shape = geometry_service.draw_hollow_diamond(request_dto)
    return HollowDiamondResponseDto(result = ascii_shape)

@router.post("/draw_hollow_rectangle_diamond", response_model = HollowRectangleDiamondResponseDto)
async def draw_hollow_rectangle_diamond(request_dto: HollowRectangleDiamondRequestDto):
    ascii_shape = geometry_service.draw_hollow_rectangle_diamond(request_dto)
    return HollowRectangleDiamondResponseDto(result = ascii_shape)
