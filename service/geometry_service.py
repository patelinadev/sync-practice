from dto import SquareRequestDto
from geometry_utils import draw_square, draw_hollow_square

# service
class GeometryService:
    def draw_solid_square(self, request_dto: SquareRequestDto) -> str:
        return draw_square(side_length=request_dto.side_length)

    def draw_hollow_square(self, request_dto: SquareRequestDto) -> str:
        return draw_hollow_square(side_length=request_dto.side_length)

# instance
geometry_service = GeometryService()
