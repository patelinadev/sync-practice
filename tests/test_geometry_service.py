from service.geometry_service import GeometryService
from dto import *

# create a instance for test
geometry_service = GeometryService()

def test_draw_solid_square_side_length_03():
    request = SquareRequestDto(side_length=3)
    expected_output = "***\n***\n***\n"
    result = geometry_service.draw_solid_square(request)
    assert result == expected_output

def test_draw_hollow_square_side_length_03():
    request = SquareRequestDto(side_length=3)
    expected_output = "***\n* *\n***\n"
    result = geometry_service.draw_hollow_square(request)
    assert result == expected_output

def test_draw_equilateral_triangle_05():
    request = EquilateralTriangleRequestDto(base_length=5)
    expected_output = "  *  \n *** \n*****\n"
    result = geometry_service.draw_equilateral_triangle(request)
    assert result == expected_output

def test_draw_isosceles_triangle01_05():
    request = IsoscelesTriangle01RequestDto(base_length=5)
    expected_output = "  *\n ***\n*****\n"
    result = geometry_service.draw_isosceles_triangle01(request)
    assert result == expected_output

def test_draw_isosceles_triangle02_05():
    request = IsoscelesTriangle02RequestDto(base_length=5, height=3)
    expected_output = "  *\n ***\n*****\n"
    result = geometry_service.draw_isosceles_triangle02(request)
    assert result == expected_output

def test_draw_hollow_isosceles_triangle01_05():
    request = HollowIsoscelesTriangle01RequestDto(base_length=5)
    expected_output = "   *\n  * *\n *****\n"
    result = geometry_service.draw_hollow_isosceles_triangle01(request)
    assert result == expected_output

def test_draw_hollow_isosceles_triangle02_05():
    request = HollowIsoscelesTriangle02RequestDto(base_length=5, height=3)
    expected_output = "  *\n * *\n*****\n"
    result = geometry_service.draw_hollow_isosceles_triangle02(request)
    assert result == expected_output