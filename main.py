"""
Щелкаем по эталонной тройке в 2 местах.
В первом будем делать бин, а во втором характеристику.

"""
from data import *
from clicker import *
from characteristicity import *


def fit_A_event_diam(A, h_fixed, pics_train, pics_test):
    step =20
    grid_diams = range(20, 100, step)
    powers = []
    for diam in grid_diams:
        A.A_min = A.etalon - diam / 2
        A.A_max = A.A_min + diam
        power = measure_charactericity_for_non_bin(h_fixed, A, pics_train, pics_test, nbins=20)
        powers.append(power)
    return grid_diams, powers





def fit_h_u_rad(A_fixed, h, pics1, pics2, logger):
    pass

def create_A_and_h(Ax, Ay, hx, hy, pic, A_sens_rad, h_sens_rad, h_u_rad):
    return A, h


def exp0(A_sens_rad, h_sens_rad, h_u_rad, logger):
    pic = etalons_of3()[0]  # эталон
    pics_train = get_numbers_of_type(3)[0:40]  # генерация гипотезы
    pics_test = get_numbers_of_type(3)[50:130]  # проверка гипотезы

    X, Y = select_coord_on_pic(pic)
    Ax, Ay, hx, hy = X[0], Y[0], X[1], Y[1]
    A, h = create_A_and_h(Ax, Ay, hx, hy, pic, A_sens_rad, h_sens_rad, h_u_rad)

    grid_diams, powers = fit_A_event_diam(A, h, pics_train, pics_test)



