import math

def figure_rectengle(x1, y1, x2, y2):
    '''(x1, y1)-нижня ліва точка, (x2, y2)-верхня права точка

    визначимо (x3, y3)-верхню ліву, (x4, y4)-нижню праву'''
    x3 = x1
    y3 = y2
    x4 = x2
    y4 = y1
    side_1 = side(x1, y1, x3, y3)
    side_2 = side(x1, y1, x4, y4)
    perim_rect = perimitre_rectengle(side_1, side_2)
    area_regt = area_regtengle(side_1, side_2)
    return 'Rectangle Area:{} Perimeter:{}'.format(perim_rect, area_regt)

def figure_square(side_square):
    return 'Square Area:{} Perimeter:{}'.format(perimetre_squre(side_square), area_square(side_square))

def side(x_1, y_1, x_2, y_2):
    '''знаходимо сторону фігури з двома точками'''
    return ((x_2-x_1)**2+(y_2-y_1)**2)**(1/2)

def perimetre_squre(side):
    return 4*side

def perimitre_rectengle(side1, side2):
    return (side1*2)+(side2*2)

def area_square(side_squre):
    '''знаходимо площу квадрату'''
    return side_squre**2

def area_regtengle(side1, side2):
    '''знаходимо площу прямокутника'''
    return side1*side2

def figure_triangle(x1, x2, x3, y1, y2, y3):
    side1 = side(x1, y1, x2, y2)
    side2 = side(x2, y2, x3, y3)
    side3 = side(x3, y3, x1, y1)
    per_tr = perimetr_triangle(side1, side2, side3)
    area_tr = area_triangle(side1, side2, side3)
    print('Triangle Area:{} Perimeter:{}'.format(per_tr, area_tr))

def area_triangle(side_1, side_2, side_3):
    p = (side_1+side_2+side_3)/2
    return (p*(p-side_1)*(p-side_2)*(p-side_3))**(1/2)

def perimetr_triangle(side_1, side_2, side_3):
    return side_1+side_2+side_3

def figure_circle(r):
    area_sircle = math.pi*(r**2)
    perim = 2*math.pi*r
    print('Circle Area:{} Perimeter:{}'.format(perim, area_sircle))

#вводиться фігура, розташування, точки

print('This program calculates the area and perimeter for a square, rectangle, triangle, and circle. ')
print('If you want to exit the app, enter the number 5.')

while True:
    f = input('Enter your figure geometriqe:')
    if f=='square':
        print('Enter: x1 y1 side')
        x_1, y_1, side_1 = map(int, input('Maintain shape data separated by a space:').split())
        print(figure_square(side_1))
    elif f=='rectangle':
        print('Enter: x1 y1 x2 y2')
        x_1, y_1, x_2, y_2 = map(int, input('Maintain shape data separated by a space:').split())
        print(figure_rectengle(x_1, y_1, x_2, y_2))
    elif f=='circle':
        print('Enter: x1 y1 radius')
        x_1, y_1, radius = map(int, input('Maintain shape data separated by a space:').split())
        print(figure_circle(radius))
    elif f=='triangle':
        print('Enter: x1 x2 x3 y1 y2 y3')
        x_1, y_1, x_2, y_2, x_3, y_3 = map(int, input('Maintain shape data separated by a space:').split())
        print(figure_triangle(x_1, x_2, x_3, y_1, y_2, y_3))
    elif f=='5':
        print('By!')
        break
    else:
        print('NameError: There is no figure with this name. Please enter one of the following names:'
              'square, rectangle, circle, triangle')
        break
    else:
        print('NameError: There is no figure with this name. Please enter one of the following names:'
              'square, rectangle, circle, triangle')
