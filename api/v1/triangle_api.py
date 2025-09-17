from fastapi import APIRouter,Depends
from dto import *
from service.geometry_service import GeometryService, get_geometry_service

router = APIRouter(
    prefix="/triangle",
    tags=["triangle"]
)

@router.post("/draw_equilateral_triangle",response_model = EquilateralTriangleResponseDto)
async def draw_equilateral_triangle(request_dto: EquilateralTriangleRequestDto, service: GeometryService = Depends(get_geometry_service)):
    ascii_shape = service.draw_equilateral_triangle(request_dto)
    return EquilateralTriangleResponseDto(result = ascii_shape)

@router.post("/draw_isosceles_triangle01", response_model = IsoscelesTriangle01ResponseDto)
async def draw_equilateral_triangle01(request_dto: IsoscelesTriangle01RequestDto, service: GeometryService = Depends(get_geometry_service)):
    ascii_shape = service.draw_isosceles_triangle01(request_dto)
    return IsoscelesTriangle01ResponseDto(result = ascii_shape)

@router.post("/draw_isosceles_triangle02", response_model = IsoscelesTriangle02ResponseDto)
async def draw_isosceles_triangle02(request_dto: IsoscelesTriangle02RequestDto, service: GeometryService = Depends(get_geometry_service)):
    ascii_shape = service.draw_isosceles_triangle02(request_dto)
    return IsoscelesTriangle02ResponseDto(result = ascii_shape)

@router.post("/draw_hollow_isosceles_triangle01", response_model = HollowIsoscelesTriangle01ResponseDto)
async def draw_hollow_isosceles_triangle01(request_dto: HollowIsoscelesTriangle01RequestDto, service: GeometryService = Depends(get_geometry_service)):
    ascii_shape = service.draw_hollow_isosceles_triangle01(request_dto)
    return HollowIsoscelesTriangle01ResponseDto(result = ascii_shape)

@router.post("/draw_hollow_isosceles_triangle02", response_model = HollowIsoscelesTriangle02ResponseDto)
async def draw_hollow_isosceles_triangle02(request_dto: HollowIsoscelesTriangle02RequestDto, service: GeometryService = Depends(get_geometry_service)):
    ascii_shape = service.draw_hollow_isosceles_triangle02(request_dto)
    return HollowIsoscelesTriangle02ResponseDto(result = ascii_shape)
