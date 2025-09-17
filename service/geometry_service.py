from dto import *
from geometry_utils import *


# service
class GeometryService:
    # --- Square ---
    def draw_solid_square(self, request_dto: SquareRequestDto) -> str:
        return draw_square(side_length = request_dto.side_length)

    def draw_hollow_square(self, request_dto: HollowSquareRequestDto) -> str:
        return draw_hollow_square(side_length = request_dto.side_length)
    # --- Triangle ---
    def draw_equilateral_triangle(self, request_dto:EquilateralTriangleRequestDto) -> str:
        return draw_equilateral_triangle(base_length = request_dto.base_length)

    def draw_isosceles_triangle01(self, request_dto: IsoscelesTriangle01RequestDto) -> str:
        return draw_isosceles_triangle01(base_length = request_dto.base_length)

    def draw_isosceles_triangle02(self, request_dto: IsoscelesTriangle02RequestDto) -> str:
        return draw_isosceles_triangle02(base_length = request_dto.base_length, height = request_dto.height)

    def draw_hollow_isosceles_triangle01(self, request_dto: HollowIsoscelesTriangle01RequestDto) -> str:
        return draw_hollow_isosceles_triangle01(base_length = request_dto.base_length)

    def draw_hollow_isosceles_triangle02(self, request_dto: HollowIsoscelesTriangle02RequestDto) -> str:
        return draw_hollow_isosceles_triangle02(base_length = request_dto.base_length, height = request_dto.height)
    # --- Trapezoid ---
    def draw_trapezoid(self, request_dto: TrapezoidRequestDto) -> str:
        return draw_trapezoid(base_length =  request_dto.base_length, height = request_dto.height)
    # --- Diamond ---
    def draw_diamond(self, request_dto: DiamondRequestDto) -> str:
        return draw_diamond(side_length = request_dto.side_length)

    def draw_hollow_diamond(self, request_dto: HollowDiamondRequestDto) -> str:
        return draw_hollow_diamond(side_length = request_dto.side_length)

    def draw_hollow_rectangle_diamond(self, request_dto: HollowRectangleDiamondRequestDto) -> str:
        return draw_hollow_rectangle_diamond(side_length = request_dto.side_length)
    # --- Hexagon ---
    def draw_hexagon(self, request_dto: HexagonRequestDto) -> str:
        return draw_hexagon(side_length = request_dto.side_length)

# instance
geometry_service = GeometryService()
