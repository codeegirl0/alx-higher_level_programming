#!/usr/bin/python3
"""lazy_matrix_mul module
Matrix double .
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """double m_a and m_b by
    matmul, and return result.
    """
    return numpy.matmul(m_a, m_b)
