def square(side_length: int):
    for _ in range(side_length):
        print("*" * side_length)

def hollow_square(side_length:int):
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            print('*' * side_length)
        else:
            print('*' + ' ' * (side_length - 2) + '*' )

def equilateral_triagnel(base_length: int):
    #   *
    #  ***
    # *****
    #*******
    row  = (base_length +1) // 2
    for i in range(row):
        left_space =row - i
        star = 2 * i + 1
        print(f"{' ' * left_space}{star * '*'}")


def isosceles_triangle(base_length: int): 
    row  = (base_length +1) // 2
    for i in range(row):
        left_space =row - i
        star = 2 * i + 1
        print(f"{' ' * left_space}{star * '*'}")

def isosceles_triangle(base_length: int, height: int):
    growth_rate = (base_length - 1) / (2 * (height - 1))
    for i in range(height):
        star = round(1 + growth_rate * i * 2)
        left_space = (base_length  - star) // 2
        print(f"{' ' * left_space}{'*' * star}")


def hollow_isosceles_triangle(base_length:int):
    row = (base_length + 1) // 2
    for i in range(row):
        left_space =row - i
        if i ==0 or i == row - 1:
            star = 2 * i + 1
            print(f"{' ' * left_space}{star * '*'}")
        else:
            hollow = 2 * i - 1
            print(f"{' ' * left_space}*{hollow * ' '}*")

def hollow_isosceles_triangle(base_length:int, height:int):
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
    top_length = base_length - (height - 1) * 2 
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
        

if __name__ == "__main__":
    
    # equilateral_triagnel(7)
    # isosceles_triangle(9,5)
    # hollow_isosceles_triangle(9,5)
    # trapezoid(6,3)
    diamond(7)
    
