#!/usr/bin/python3
"""Defines a function that does matrix multiplication using NumPy."""
import numpy as NumP


def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of two elements.

    Args:
        m_a: First matrix.
        m_b: Second matrix.
    """

    return (NumP.matmul(m_a, m_b))
