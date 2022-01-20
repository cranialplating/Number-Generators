# Created by Ryan Holmes on 01/20/22

import numpy as np
import matplotlib.pyplot as plt
from binarygen import Binary

if __name__ == '__main__':

    b1 = Binary(100000, 10, 1000)

    b1.calc_hist()
