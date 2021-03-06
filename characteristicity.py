from binary import *
from nonbinary import *
from sampling import *
from utils import *

import numpy as np

def measure_charactericity_for_non_bin(non_binary_h, binary, pics_train, pics_test, nbins):
    sample_size_unconditional = 200
    sample_size_train = 20
    sample_size_test = 250

    # прикидываем условную и безусловную гистограмму non_binary_h
    uncond_sample = get_unconditional_non_binary_sample(non_binary_h, sample_size_unconditional, pics_train)
    cond_sample = get_conditional_non_binary_sample(non_binary_h, binary.apply2, sample_size_train, pics_train)
    probs_uncond, bins = get_hist(uncond_sample, nbins)
    probs_cond, _ = get_hist(cond_sample, nbins)

    # затем начинаем второй этап - замер ошибки предсказания при его семплинге из двух разных гист
    ground_true = get_conditional_non_binary_sample(non_binary_h, binary.apply2, sample_size_test, pics_test)
    uncond_prediction = sample_from_hist(probs_uncond, bins, sample_size_test)
    cond_prediction = sample_from_hist(probs_cond, bins, sample_size_test)
    naive_error = count_error_btw_two_samples(ground_true, prediction=uncond_prediction)
    clever_error = count_error_btw_two_samples(ground_true, prediction=cond_prediction)
    return naive_error - clever_error # чем больше тем лучше



