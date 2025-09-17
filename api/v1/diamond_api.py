from fastapi import APIRouter, Depends
from dto import *
from service.geometry_service import GeometryService, get_geometry_service

router = APIRouter(
    prefix="/diamond",
    tags=["diamond"]
)

@router.post("/draw_diamond",response_model = DiamondResponseDto)
async def draw_diamond(request_dto: DiamondRequestDto, service: GeometryService = Depends(get_geometry_service)):
    ascii_shape = service.draw_diamond(request_dto)
    return DiamondResponseDto(result = ascii_shape)

@router.post("/draw_hollow_diamond", response_model = HollowDiamondResponseDto)
async def draw_hollow_diamond(request_dto: HollowDiamondRequestDto, service: GeometryService = Depends(get_geometry_service)):
    ascii_shape = service.draw_hollow_diamond(request_dto)
    return HollowDiamondResponseDto(result = ascii_shape)

@router.post("/draw_hollow_rectangle_diamond", response_model = HollowRectangleDiamondResponseDto)
async def draw_hollow_rectangle_diamond(request_dto: HollowRectangleDiamondRequestDto, service: GeometryService = Depends(get_geometry_service)):
    ascii_shape = service.draw_hollow_rectangle_diamond(request_dto)
    return HollowRectangleDiamondResponseDto(result = ascii_shape)
