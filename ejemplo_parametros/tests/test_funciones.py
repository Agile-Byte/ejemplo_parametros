# -*- coding: utf-8 -*-
"""Pruebas calculadora AVANZADA"""

import unittest
from unittest import mock

import numpy
from ejemplo_parametros.src.proyecto.funciones import calculadora_precio

class TestFunciones(unittest.TestCase):
    """Test Ejemplo TDD"""
    def calculadora_precio(self):
        """Test hello_world"""
        self.assertEqual(type(calculadora_precio()), numpy.float64)


if __name__ == '__main__':
    unittest.main()
