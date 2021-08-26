"""
Щелкаем по эталонной тройке в 2 местах.
В первом будем делать бин, а во втором характеристику.

"""
from data import *
from clicker import *


def fit_A_event_diam(A, h_fixed, pics1, pics2, logger):
    step =20
    grid_diams = range(20, 100, step)
    results = []
    for diam in grid_diams:
        A.A_min = A.etalon - diam / 2
        A.A_max = A.A_min + diam




def fit_h_u_rad(A_fixed, h, pics1, pics2, logger):
    pass

def create_A_and_h(Ax, Ay, hx, hy, pic, A_sens_rad, h_sens_rad, h_u_rad):
    return A, h


def exp0(A_sens_rad, h_sens_rad, h_u_rad, logger):
    pic = etalons_of3()[0]  # эталон
    pics1 = get_numbers_of_type(3)[0:40]  # генерация гипотезы
    pics2 = get_numbers_of_type(3)[50:130]  # проверка гипотезы

    X, Y = select_coord_on_pic(pic)
    Ax, Ay, hx, hy = X[0], Y[0], X[1], Y[1]
    A, h = create_A_and_h(Ax, Ay, hx, hy, pic, A_sens_rad, h_sens_rad, h_u_rad)

    fit_A_event_rad(A, h, pics1, pics2, logger)


