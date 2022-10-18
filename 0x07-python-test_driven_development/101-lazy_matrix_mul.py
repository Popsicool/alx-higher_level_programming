#!/usr/bin/python3

"""multiply two matrix using numpy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Return:
        Multiplication of the two m,atrix
    Args:
        m_a: The first matrix.
        m_b: The second matrix.
    """

    return (np.matmul(m_a, m_b))
