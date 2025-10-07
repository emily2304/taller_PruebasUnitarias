"""
Sistema de Gestión de Inventario
Módulo principal con lógica de negocio
"""

class Producto:
    def __init__(self, nombre, precio, cantidad):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def calcular_valor_total(self):
        """Calcula el valor total del inventario del producto"""
        return self.precio * self.cantidad
    
    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al precio del producto"""
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        return self.precio
    
    def agregar_stock(self, cantidad):
        """Agrega stock al inventario"""
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva")
        
        self.cantidad += cantidad
        return self.cantidad
    
    def reducir_stock(self, cantidad):
        """Reduce el stock del inventario"""
        if cantidad <= 0:
            raise ValueError("La cantidad a reducir debe ser positiva")
        
        if cantidad > self.cantidad:
            raise ValueError("Stock insuficiente")
        
        self.cantidad -= cantidad
        return self.cantidad
    
    def esta_disponible(self):
        """Verifica si el producto tiene stock disponible"""
        return self.cantidad > 0


class Inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto):
        """Agrega un producto al inventario"""
        if producto.nombre in self.productos:
            raise ValueError("El producto ya existe en el inventario")
        
        self.productos[producto.nombre] = producto
    
    def obtener_producto(self, nombre):
        """Obtiene un producto del inventario"""
        if nombre not in self.productos:
            raise KeyError("Producto no encontrado")
        
        return self.productos[nombre]
    
    def calcular_valor_total_inventario(self):
        """Calcula el valor total de todo el inventario"""
        return sum(p.calcular_valor_total() for p in self.productos.values())
    
    def contar_productos_disponibles(self):
        """Cuenta cuántos productos tienen stock disponible"""
        return sum(1 for p in self.productos.values() if p.esta_disponible())