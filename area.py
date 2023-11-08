import math

def figure_inf(figure, x1, y1, x2, y2):
    '''(x1, y1)-нижня ліва точка, (x2, y2)-верхня права точка

    визначимо (x3, y3)-верхню ліву, (x4, y4)-нижню праву'''
    if figure=='squre':
        side_figure_squre=side(x1, y1, x2, y2)
        area_figure_squre=area_squre(side_figure_squre)
        perim_squre=perimetre_squre(side_figure_squre)
        print('Squre Area:{} Perimeter:{}'.format(area_figure_squre, perim_squre))
    elif figure=='rectangle':
        x3=x1
        y3=y2
        x4=x2
        y4=y1
        side_1=side(x1, y1, x3, y3)
        side_2=side(x1, y1, x4, y4)
        perim_regt=perimitre_regtengle(side_1, side_2)
        area_regt=area_regtengle(side_1, side_2)
        print('Squre Area:{} Perimeter:{}'.format(perim_regt, area_regt))

def side(x_1, y_1, x_2, y_2):
    '''знаходимо сторону фігури з двома точками'''
    return ((x_2-x_1)**2+(y_2-y_1)**2)**(1/2)

def perimetre_squre(side):
    return 4*side

def perimitre_regtengle(side1, side2):
    return (side1*2)+(side2*2)

def area_squre(side_squre):
    '''знаходимо площу квадрату'''
    return side_squre**2

def area_regtengle(side1, side2):
    '''знаходимо площу прямокутника'''
    return side1*side2

def triangle_info(x1, x2, x3, y1, y2, y3):
    side1=side(x1, y1, x2, y2)
    side2=side(x2, y2, x3, y3)
    side3=side(x3, y3, x1, y1)
    per_tr=perimetr_triangle(side1, side2, side3)
    area_tr=area_triangle(side1, side2, side3)
    print('Triangle Area:{} Perimeter:{}'.format(per_tr, area_tr))

def area_triangle(side_1, side_2, side_3):
    p=(side_1+side_2+side_3)/2
    return (p*(p-side_1)*(p-side_2)*(p-side_3))**(1/2)

def perimetr_triangle(side_1, side_2, side_3):
    return side_1+side_2+side_3

def sircle_info(r):
    area_sircle=math.pi*(r**2)
    perim=2*math.pi*r
    print('Sircle Area:{} Perimeter:{}'.format(perim, area_sircle))

figur=['squre', 'circle', 'rectangle', 'triangle']
fig=input('Enter figure:')
if fig not in figur:
    print('NameError')
if fig in figur:
    if fig=='rectangle' or fig=='squre':
        k_1=int(input('x1:'))
        k_2=int(input('x2:'))
        r_1=int(input('y1:'))
        r_2=int(input('y2:'))
        print(figure_inf(fig, k_1, r_1, k_2, r_2))
    if fig=='tringle':
        k_1 =int(input('x1:'))
        r_1 =int(input('y1:'))
        k_2 =int(input('x2:'))
        r_2 =int(input('y2:'))
        k_3 =int(input('x3:'))
        r_3 =int(input('y3:'))
        print(triangle_info(k_1, k_2, k_3, r_1, r_2, r_3))
    if fig=='circle':
        radius=int(input('Radius:'))
        print(sircle_info(radius))
