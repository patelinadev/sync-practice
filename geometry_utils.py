def draw_square(side_length: int):
    result = ""
    for _ in range(side_length):
        result += "*" * side_length
        result += "\n"

    return result

def draw_hollow_square(side_length: int):
    result = ""
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            result += "*" * side_length
            result += "\n"
        else:
            result += "*"
            result += " " * (side_length - 2)
            result += "*"
            result += "\n"

    return result

def draw_equilateral_triangle(base_length: int):
    result = ""
    row = (base_length + 1) // 2
    for i in range(row):
        left_space = row - i
        star = 2 * i + 1
        result += " " * left_space
        result += star * "*"
    return result

def draw_isosceles_triagnle01(base_length: int):
    result = ""
    row = (base_length + 1) // 2
    for i in range(row):
        left_space = row - i
        star = 2 * i + 1
        result += " " * left_space
        result += star * "*"
        result += "\n"
    return result

def draw_isosceles_triangle02(base_length: int, height: int):
    result = ""
    growth_rate = (base_length - 1) / (2 * (height - 1))
    for i in range(height):
        star = round(1 + growth_rate * i * 2)
        left_space = (base_length - star) // 2
        result += " " * left_space
        result += "*" * star
        result += "\n"
    return result

def draw_hollow_isosceles_trangle01(base_length: int):
    result = ""
    row = (base_length + 1) // 2
    for i in range(row):
        left_space =  row - i
        if i == 0 or i == row - 1:
            star = 2 * i + 1
            result += " " * left_space
            result += "*" * star
            result += "\n"
        else:
            hollow = 2 * i - 1
            result += " " * left_space
            result += "*"
            result += " " * hollow
            result += "*"
            result += "\n"
    return result

def draw_hollow_isosceles_trangle02(base_length: int, height: int):
    result = ""
    growth_rate = (base_length - 1) / (2 * (height - 1))
    for i in range(height):
        star = round(1 + growth_rate * i * 2)
        left_space = (base_length - star) // 2
        if i == 0 or i == height - 1:
            result += " " * left_space
            result += "*" * star
            result += "\n"
        else:
            hollow = round(growth_rate * i * 2 - 1)
            result += " " * left_space
            result += "*"
            result += " " * hollow
            result += "*"
            result += "\n"
    return result

def draw_trapezoid(base_length: int, height: int):
    result = ""
    top_length = base_length - ((height - 1) * 2)
    if top_length < 2:
        top_length = 2
    for i in range(height):
        star = top_length + 2 * i
        left_length = (base_length - star) // 2
        result += " " * left_length
        result += "*" * star
        result += "\n"
    return result

def draw_diamond(side_length: int):
    result = ""
    half_row = (side_length + 1) // 2
    for i in range(half_row):
        star = 2 * i + 1
        left_length = (side_length - star) // 2
        result += " " * left_length
        result += "*" * star
        result += "\n"
    for i in range(half_row - 1):
        star = side_length - 2 * (i + 1)
        left_length = (side_length - star) // 2
        result += " " * left_length
        result += "*" * star
        result += "\n"
    return result

def draw_hollow_diamond(side_length: int):
    result = ""
    if (side_length + 1) // 2 == 0:
        side_length + 1
    upper_row = (side_length + 1) // 2
    lower_row = upper_row - 1
    for i in(upper_row):
        if i == 0:
            half_space = (side_length - 1) // 2
            result += " " * half_space
            result += "*"
            result += " " * half_space
            result += "\n"
        else:
            front_space = half_space - 1 
            middle_space = 2 * i - 1
            result += " " * front_space
            result += "*"
            result += " "* middle_space
            result += "*"
            result += "\n"
    for i in range(lower_row):
        if i == lower_row - 1:
            half_space = (side_length - 1) // 2
            result += " " * half_space
            result += "*"
            result += " " * half_space
            result += "\n"
        else:
            middle_space = side_length - 4 - 2 * i
            front_space = (side_length - middle_space - 2) // 2 
            result += " " * front_space
            result += "*"
            result += " "* middle_space
            result += "*"
            result += "\n"
    return result

def draw_hollow_rectangle_with_diamond(side_length: int):
    result = ""
    if (side_length + 1) // 2 == 0:
        side_length + 1
    rectangle_col = rectangle_row = side_length + 2
    center_x = (rectangle_col - 1) // 2
    center_y = (rectangle_row - 1) // 2
    diamond_raduis = (side_length - 1) // 2
    for i in range(rectangle_row):
        for j in  range(rectangle_col):
            distance = abs(i - center_y) + abs(j - center_x)
            if distance <= diamond_raduis:
                result += " "
            else:
                result += "*"
            result += "\n"
    return result

def hexagon(side_length: int):
    result = ""
    trapezoid_row = side_length - 1
    middle_width = side_length * 3 - 2
    for i in range(trapezoid_row):
        star = side_length + 2 * i
        left_space = (middle_width - star) // 2
        result += " " * left_space
        result += "*" * star
        result += "\n"
    for _ in range(side_length):
        result += "*" * middle_width 
    for i in reversed(range(trapezoid_row)):
        star = side_length + 2 * i 
        left_space = (middle_width - star) // 2
        result += " " * left_space
        result += "*" * star
        result += "/n"
    return result

