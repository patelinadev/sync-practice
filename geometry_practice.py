def square(side_length: int):
    for _ in range(side_length):
        print("*" * side_length)

def hollow_square(side_length:int):
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            print('*' * side_length)
        else:
            print('*' + ' ' * (side_length - 2) + '*' )

def equilateral_triagnle(base_length: int):
    #   *
    #  ***
    # *****
    #*******
    row  = (base_length + 1) // 2
    for i in range(row):
        left_space = row - i
        star = 2 * i + 1
        print(f"{' ' * left_space}{star * '*'}")

def isosceles_triangle01(base_length: int): 
    row  = (base_length + 1) // 2
    for i in range(row):
        left_space = row - i
        star = 2 * i + 1
        print(f"{' ' * left_space}{star * '*'}")

def isosceles_triangle02(base_length: int, height: int):
    growth_rate = (base_length - 1) / (2 * (height - 1))
    for i in range(height):
        star = round(1 + growth_rate * i * 2)
        left_space = (base_length  - star) // 2
        print(f"{' ' * left_space}{'*' * star}")


def hollow_isosceles_triangle01(base_length:int):
    row = (base_length + 1) // 2
    for i in range(row):
        left_space = row - i
        if i ==0 or i == row - 1:
            star = 2 * i + 1
            print(f"{' ' * left_space}{star * '*'}")
        else:
            hollow = 2 * i - 1
            print(f"{' ' * left_space}*{hollow * ' '}*")

def hollow_isosceles_triangle02(base_length:int, height:int):
    growth_rate = (base_length - 1) / (2 * (height - 1))
    for i in range(height):
        star = round(1 + growth_rate * i * 2)
        left_space = (base_length  - star) // 2
        if i == 0 or i == height - 1:
            print(f"{left_space * ' '}{'*' * star}")
        else:
            hollow = round(growth_rate * i * 2 - 1)
            print(f"{' ' * left_space}*{hollow * ' '}*")

def trapezoid(base_length: int, height:int):
    #  **  
    # ****
    #******

    #   ***   
    #  *****  
    # ******* 
    #*********
    top_length = base_length - ((height - 1) * 2) 
    if top_length < 2:
        top_length = 2
    for i in range(height):
        star = top_length + 2 * i
        left_length = (base_length - star) // 2
        print(f"{left_length * ' '}{star * '*'}")


def diamond(side_length: int):
    #   *   
    #  ***  
    # ***** 
    #*******
    # ***** 
    #  ***  
    #   *   
    half_row = (side_length + 1) //2
    for i in range(half_row):
        star = 2 * i + 1
        left_length = (side_length - star) // 2
        print(f"{left_length * ' '}{star * '*'}")
    for i in range(half_row - 1):
        star = side_length - 2 * (i + 1)
        left_length = (side_length - star) // 2
        print(f"{left_length * ' '}{star * '*'}")
        

def hollow_diamond(side_length:int):
    #   *   
    #  * *  
    # *   * 
    #*     *
    # *   * 
    #  * *  
    #   *   

    #  *  
    # * *
    #*   *
    # * *
    #  *  
    if (side_length + 1) // 2 == 0:
        side_length + 1
    upper_row = (side_length + 1) // 2
    lower_row = upper_row - 1
    for i in range(upper_row):
        if i == 0:
            half_space = (side_length - 1) // 2
            print(f"{half_space * ' '}*{half_space * ' '}")
        else:
            front_space = half_space - i
            middle_space = 2 * i - 1
            print(f"{front_space * ' '}*{middle_space * ' '}*")
    for i in range(lower_row):
        if i == lower_row - 1:
            half_space = (side_length - 1) // 2
            print(f"{half_space * ' '}*{half_space * ' '}")
        else:
            middle_space = side_length - 4 - 2 * i 
            front_space = (side_length - middle_space - 2) // 2
            print(f"{front_space * ' '}*{middle_space * ' '}*")


def hollow_rectangle_with_diamond(side_length:int):
    #*********
    #**** ****
    #***   ***
    #**     **
    #*       *
    #**     **
    #***   ***
    #**** ****
    #*********
        if (side_length + 1) // 2 == 0:
            side_length + 1
        rectangle_col = rectangle_row = side_length + 2
        center_x = (rectangle_col - 1) // 2
        center_y = (rectangle_row - 1) // 2
        diamond_raduis = (side_length - 1) // 2 
        for i in range(rectangle_row):# y-axis
            for j in range(rectangle_col):# x-axis
                distance = abs(i - center_y) + abs(j - center_x)
                if distance <= diamond_raduis:
                    print(" ", end = "")
                else:
                    print("*", end = "")
            print()


def five_pointed_star(size:int):
    pass

def hexagon(side_length:int):
    #  ***
    # *****
    #*******
    #*******
    #*******
    # *****
    #  ***
    
    # total_row = side_length * 3 - 2
    trapezoid_row = side_length - 1
    middle_width = side_length * 3 - 2

    for i in range(trapezoid_row): 
        star = side_length + 2 * i
        left_space = (middle_width - star) // 2
        print(f"{left_space * ' '}{star * '*'}")
    for _ in range(side_length):
        print(f"{middle_width * '*'}")
    for i in reversed(range(trapezoid_row)):
        star = side_length + 2 * i
        left_space = (middle_width - star) // 2
        print(f"{left_space * ' '}{star * '*'}")

    

    

def n_side_polygon(n: int, size: int):
    pass

if __name__ == "__main__":
    
    # equilateral_triagnel(7)
    # isosceles_triangle(9,5)
    # hollow_isosceles_triangle(9,5)
    # trapezoid(6,3)
    # diamond(7)
    # hollow_diamond(9)
    # hollow_rectangle_with_diamond(5)
    hexagon(5)