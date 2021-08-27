"""
Щелкаем по эталонной тройке в 2 местах.
В первом будем делать бин, а во втором характеристику.

"""
from data import *
from clicker import *
from characteristicity import *
from logger import *
from utils import *


def fit_A_event_diam(A, h_fixed, pics_train, pics_test):
    step =10
    grid_diams = range(0, 700, step)
    powers = []
    etalon = A.A_min + int((A.A_max-A.A_min)/2)
    for diam in grid_diams:
        A.A_min = etalon - int(diam / 2)
        A.A_max = A.A_min + diam
        power = measure_charactericity_for_non_bin(h_fixed, A, pics_train, pics_test, nbins=20)
        powers.append(power)
    return grid_diams, powers


def fit_h_u_rad(A_fixed, h, pics1, pics2, logger):
    pass

def create_A_and_h(Ax, Ay, hx, hy, pic, A_sens_rad, h_sens_rad, h_u_rad):
    A_etalon = make_measurement(pic,Ax,Ay,A_sens_rad)
    A = BinaryUnit(u_radius=0, sensor_field_radius=A_sens_rad, etalon=A_etalon, event_diameter=0, dx=0,dy=0)
    h_etalon = make_measurement(pic,hx, hy,h_sens_rad)
    h = NonBinaryUnit(u_radius=h_u_rad, sensor_field_radius=h_sens_rad, etalon=h_etalon, dx=hx-Ax, dy=hy-Ay)
    return A, h


def exp0(A_sens_rad, h_sens_rad, h_u_rad, logger):
    pic = etalons_of3()[0]  # эталон
    pics_train = get_numbers_of_type(3)[0:50]  # генерация гипотезы
    pics_test = get_numbers_of_type(3)[50:160]  # проверка гипотезы

    X, Y = select_coord_on_pic(pic)
    Ax, Ay, hx, hy = X[0], Y[0], X[1], Y[1]
    A, h = create_A_and_h(Ax, Ay, hx, hy, pic, A_sens_rad, h_sens_rad, h_u_rad)

    grid_diams, powers = fit_A_event_diam(A, h, pics_train, pics_test)

    logger.add_text("vary event diam on A:")
    logger.add_text(str(vars(A)))
    logger.add_text("characteristica=:")
    logger.add_text(str(vars(h)))
    logger.add_fig(plot_points_on_pic_first_red(pic, X,Y))
    logger.add_fig(plot_graph(grid_diams, powers))


if __name__ == "__main__":
    logger = HtmlLogger("exp0-vary event diam")
    exp0(A_sens_rad=0, h_sens_rad=0, h_u_rad=0, logger=logger)
    logger.close()

