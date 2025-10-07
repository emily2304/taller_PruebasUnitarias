"""
Suite de Pruebas Unitarias para el Sistema de Inventario
Utilizando unittest - framework nativo de Python
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from inventario import Producto, Inventario


class TestProducto(unittest.TestCase):
    """Tests para la clase Producto"""
    
    def setUp(self):
        """Se ejecuta antes de cada test - Preparación"""
        self.producto = Producto("Laptop", 1000, 5)
    
    def tearDown(self):
        """Se ejecuta después de cada test - Limpieza"""
        self.producto = None
    
    # TESTS DE CASOS POSITIVOS
    def test_crear_producto_valido(self):
        """Verifica que se pueda crear un producto con datos válidos"""
        producto = Producto("Mouse", 25.50, 10)
        self.assertEqual(producto.nombre, "Mouse")
        self.assertEqual(producto.precio, 25.50)
        self.assertEqual(producto.cantidad, 10)
    
    def test_calcular_valor_total(self):
        """Verifica el cálculo del valor total del inventario"""
        valor = self.producto.calcular_valor_total()
        self.assertEqual(valor, 5000)  # 1000 * 5
    
    def test_aplicar_descuento(self):
        """Verifica que se aplique correctamente un descuento"""
        nuevo_precio = self.producto.aplicar_descuento(10)
        self.assertEqual(nuevo_precio, 900)  # 1000 - 10%
    
    def test_agregar_stock(self):
        """Verifica que se pueda agregar stock correctamente"""
        nuevo_stock = self.producto.agregar_stock(3)
        self.assertEqual(nuevo_stock, 8)  # 5 + 3
    
    def test_reducir_stock(self):
        """Verifica que se pueda reducir stock correctamente"""
        nuevo_stock = self.producto.reducir_stock(2)
        self.assertEqual(nuevo_stock, 3)  # 5 - 2
    
    def test_producto_disponible(self):
        """Verifica que un producto con stock esté disponible"""
        self.assertTrue(self.producto.esta_disponible())
    
    # TESTS DE CASOS NEGATIVOS (Manejo de Errores)
    def test_crear_producto_precio_negativo(self):
        """Verifica que no se pueda crear un producto con precio negativo"""
        with self.assertRaises(ValueError):
            Producto("Producto Inválido", -100, 5)
    
    def test_crear_producto_cantidad_negativa(self):
        """Verifica que no se pueda crear un producto con cantidad negativa"""
        with self.assertRaises(ValueError):
            Producto("Producto Inválido", 100, -5)
    
    def test_descuento_invalido_mayor_100(self):
        """Verifica que no se pueda aplicar un descuento mayor a 100%"""
        with self.assertRaises(ValueError):
            self.producto.aplicar_descuento(150)
    
    def test_descuento_invalido_negativo(self):
        """Verifica que no se pueda aplicar un descuento negativo"""
        with self.assertRaises(ValueError):
            self.producto.aplicar_descuento(-10)
    
    def test_reducir_stock_insuficiente(self):
        """Verifica que no se pueda reducir más stock del disponible"""
        with self.assertRaises(ValueError):
            self.producto.reducir_stock(10)  # Solo hay 5
    
    def test_agregar_stock_cantidad_invalida(self):
        """Verifica que no se pueda agregar cantidad negativa o cero"""
        with self.assertRaises(ValueError):
            self.producto.agregar_stock(0)
    
    # TESTS DE CASOS LÍMITE (Boundary)
    def test_producto_sin_stock_no_disponible(self):
        """Verifica que un producto sin stock no esté disponible"""
        producto = Producto("Agotado", 100, 0)
        self.assertFalse(producto.esta_disponible())
    
    def test_descuento_100_porciento(self):
        """Verifica el caso límite de descuento del 100%"""
        nuevo_precio = self.producto.aplicar_descuento(100)
        self.assertEqual(nuevo_precio, 0)


class TestInventario(unittest.TestCase):
    """Tests para la clase Inventario"""
    
    def setUp(self):
        """Preparación antes de cada test"""
        self.inventario = Inventario()
        self.producto1 = Producto("Laptop", 1000, 5)
        self.producto2 = Producto("Mouse", 25, 10)
    
    def test_agregar_producto(self):
        """Verifica que se pueda agregar un producto al inventario"""
        self.inventario.agregar_producto(self.producto1)
        self.assertIn("Laptop", self.inventario.productos)
    
    def test_agregar_producto_duplicado(self):
        """Verifica que no se pueda agregar un producto duplicado"""
        self.inventario.agregar_producto(self.producto1)
        with self.assertRaises(ValueError):
            self.inventario.agregar_producto(self.producto1)
    
    def test_obtener_producto_existente(self):
        """Verifica que se pueda obtener un producto existente"""
        self.inventario.agregar_producto(self.producto1)
        producto = self.inventario.obtener_producto("Laptop")
        self.assertEqual(producto.nombre, "Laptop")
    
    def test_obtener_producto_no_existente(self):
        """Verifica el error al buscar un producto que no existe"""
        with self.assertRaises(KeyError):
            self.inventario.obtener_producto("Inexistente")
    
    def test_calcular_valor_total_inventario(self):
        """Verifica el cálculo del valor total del inventario"""
        self.inventario.agregar_producto(self.producto1)
        self.inventario.agregar_producto(self.producto2)
        valor_total = self.inventario.calcular_valor_total_inventario()
        self.assertEqual(valor_total, 5250)  # (1000*5) + (25*10)
    
    def test_contar_productos_disponibles(self):
        """Verifica el conteo de productos con stock"""
        self.inventario.agregar_producto(self.producto1)
        self.inventario.agregar_producto(self.producto2)
        producto_sin_stock = Producto("Agotado", 50, 0)
        self.inventario.agregar_producto(producto_sin_stock)
        
        disponibles = self.inventario.contar_productos_disponibles()
        self.assertEqual(disponibles, 2)  # Solo laptop y mouse


# Ejecutar las pruebas si se ejecuta directamente este archivo
if __name__ == '__main__':
    unittest.main(verbosity=2)