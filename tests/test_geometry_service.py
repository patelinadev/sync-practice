from service.geometry_service import GeometryService
from dto import SquareRequestDto

# create a instance for test
geometry_service = GeometryService()

def test_draw_solid_square_side_length_03():
    request = SquareRequestDto(side_length=3)
    result = geometry_service.draw_solid_square(request)
    expected_output = "***\n***\n***\n"
    assert result == expected_output

def test_draw_hollow_square_side_length_03():
    request = SquareRequestDto(side_length=3)
    result = geometry_service.draw_hollow_square(request)
    expected_output = "***\n* *\n***\n"
    assert result == expected_output
