#!/usr/bin/python3
"""This is afunction that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    Args:
        m_a: matrice a
        m_b: matrice b

    Raises:
        TypeError: m_a must be a list or m_b must be a list
        TypeError: m_a must be a list of lists or m_b must be a list of lists
        TypeError: m_a should contain only integers or floats or m_b should contain only integers or floats
        ValueError: m_a can't be empty or m_b can't be empty
        TypeError: each row of m_a must be of the same size or each row of m_b must be of the same size
        ValueError: m_a and m_b can't be multiplied
    """
    m_x = []
    m_xpt = []
    if type(m_a) is not (list):
        raise TypeError('m_a must be a list')

    if type(m_b) is not (list):
        raise TypeError('m_b must be a list')

    for x in m_a:
        if type(x) is not (list):
            raise TypeError('m_a must be a list of lists')
        elif len(x) == 0:
            raise ValueError('m_a can\'t be empty')
        for item in x:
            if type(item) not in (int, float):
                raise TypeError('m_a should contain only integers or floats')

    for x in m_b:
        if type(x) is not (list):
            raise TypeError('m_b must be a list of lists')
        elif len(x) == 0:
            raise ValueError('m_b can\'t be empty')
        for item in x:
            if type(item) not in (int, float):
                raise TypeError('m_b should contain only integers or floats')

    if len(m_a) is 0:
        raise ValueError('m_a can\'t be empty')

    if len(m_b) is 0:
        raise ValueError('m_b can\'t be empty')

    if len(set([len(x) for x in m_a])) is not 1:
        raise TypeError('each row of m_a must be of the same size')

    if len(set([len(x) for x in m_b])) is not 1:
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    for y in range(len(m_a)):
        for z in range(len(m_b[0])):
            sum = 0
            for q in range(len(m_b)):
                sum += m_a[y][q] * m_b[q][z]
            m_xpt.append(sum)
        m_x.append(m_xpt)
        m_xpt = []

    return(m_x)
