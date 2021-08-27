from utils import *
from binary import *
from nonbinary import *

def get_unconditional_non_binary_sample(appliable, sample_size, pics):
    # в случайных точках случайгых картинок проводим замер
    # результат (число) записываем в выборку, возвращаем ее
    activations = []
    while True:
        if len(activations) >= sample_size:
            return activations
        pic = select_random_pic(pics)
        x, y = select_random_xoord_on_pic(pic)
        best_match = appliable.apply(pic, x, y)
        activations.append(best_match)
    return activations


def get_conditional_non_binary_sample2(appliable, condition, sample_size, pics):
    # пробегаем по всем картинкам, в каждой точке проверяя condition
    # в тех точках, где condition=True, провоим замер этим юнитом,
    # результат (число) записываем в выборку, возвращаем ее
    ymax = pics[0].shape[0]
    xmax = pics[0].shape[1]

    activations = []
    for pic in pics:
        for y in range(0, ymax):
            for x in range(0, xmax):
                if condition(pic, x, y):
                    best_match = appliable.apply(pic, x, y)
                    activations.append(best_match)
                    if len(activations) >= sample_size:
                        return activations


def get_conditional_non_binary_sample(appliable, condition, sample_size, pics):
    activations = []
    while True:
        if len(activations) >= sample_size:
            return activations
        pic = select_random_pic(pics)
        x, y = select_random_xoord_on_pic(pic)
        if condition(pic, x, y):
            best_match = appliable.apply(pic, x, y)
            activations.append(best_match)