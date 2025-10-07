# 🧪 Taller de Pruebas Unitarias con Python

## 📋 Tabla de Contenidos
- Descripción
- Requisitos Previos
- Instalación
- Estructura del Proyecto
- Guía Paso a Paso
- Ejercicios Prácticos
- Recursos Adicionales
- Solución de Problemas

---

## 📖 Descripción
Este taller práctico demuestra la implementación de pruebas unitarias en Python utilizando el framework **unittest**. A través de un caso de uso real (sistema de gestión de inventario), aprenderás a:

✅ Escribir pruebas unitarias efectivas  
✅ Validar casos positivos, negativos y límite  
✅ Identificar y corregir bugs mediante tests  
✅ Medir la cobertura de código  
✅ Aplicar buenas prácticas de testing  

**Duración estimada:** 8-10 minutos

---

## 🔧 Requisitos Previos

### Software Necesario

| Software | Versión Mínima | Descarga |
|-----------|----------------|-----------|
| Python | 3.8 o superior | [python.org](https://www.python.org) |
| pip | Incluido con Python | - |
| Editor de código | Cualquiera | [VS Code (recomendado)](https://code.visualstudio.com) |

### Verificación de Requisitos

```bash
# Verificar Python
python --version
# o en algunos sistemas:
python3 --version

# Verificar pip
pip --version
# o:
pip3 --version

```

### Instalación
Opción 1: Instalación Rápida 

Clona o descarga el repositorio:

# Si tienes git instalado:
git clone <https://github.com/emily2304/taller_PruebasUnitarias.git>
cd taller_pruebasunitarias

# O descarga el ZIP y extráelo

No se requieren dependencias externas (unittest viene con Python).
```bash

pip install coverage

```


# Guía para el taller
PASO 1: Configuración Inicial 

1.1. Navega al directorio del proyecto

cd taller_pruebasunitarias

1.2. Revisa el código fuente
Abre inventario.py podras ver:

Clase Producto: gestión de productos individuales

Clase Inventario: gestión del inventario completo

PASO 2: Ejecución Básica de Pruebas 
# Opción 1: Ejecución estándar
```bash
python -m unittest test_inventario
```

# Opción 2: Con modo verboso 
```bash
python -m unittest test_inventario -v
```

# Opción 3: Ejecutar el archivo directamente
```bash
python test_inventario.py
```

✅ Salida exitosa:

test_agregar_producto (test_inventario.TestInventario) ... ok
test_agregar_producto_cantidad_invalida (test_inventario.TestProducto) ... ok
...
----------------------------------------------------------------------
Ran 20 tests in 0.005s
OK


❌ Salida con fallos:

FAIL: test_calcular_valor_total (test_inventario.TestProducto)
AssertionError: 5010 != 5000
----------------------------------------------------------------------
Ran 20 tests in 0.006s
FAILED (failures=1)

# PASO 3: Ejecutar Pruebas Específicas 
### Solo pruebas de la clase Producto
```bash
python -m unittest test_inventario.TestProducto -v
```

### Solo pruebas de la clase Inventario
```bash
python -m unittest test_inventario.TestInventario -v
```

### Ejecutar un test individual
```bash
python -m unittest test_inventario.TestProducto.test_aplicar_descuento -v
```

# PASO 4: Demostración de Detección de Bugs 

Edita inventario.py, línea 18 del método calcular_valor_total:

### ANTES (correcto):
def calcular_valor_total(self):
    return self.precio * self.cantidad

### DESPUÉS (con bug):
def calcular_valor_total(self):
    return self.precio * self.cantidad + 10  # Bug agregado


#### Ejecuta las pruebas nuevamente:
```bash
python -m unittest tests.test_inventario -v
```

### Salida:

FAIL: test_calcular_valor_total (test_inventario.TestProducto)
AssertionError: 5010 != 5000


Corrige el bug eliminando el + 10 y vuelve a ejecutar las pruebas.

# PASO 5: Medición de Cobertura de Código (OPCIONAL)
```bash
pip install coverage
```
```bash
coverage run -m unittest test_inventario
```
```bash
coverage report -m
```

Salida esperada:

Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/inventario.py            45      0   100%
tests/test_inventario.py     87      0   100%
-------------------------------------------------------
TOTAL                       132      0   100%


# Ejercicios Prácticos
## Ejercicio 1: Agregar Nuevo Método y Tests 

Objetivo: Implementar y probar un nuevo método

def es_producto_premium(self):
    """Un producto es premium si su precio es mayor a 500"""
    return self.precio > 500


Tests:

def test_producto_premium(self):
    producto = Producto("MacBook Pro", 1500, 2)
    self.assertTrue(producto.es_producto_premium())

def test_producto_no_premium(self):
    producto = Producto("Cable USB", 10, 50)
    self.assertFalse(producto.es_producto_premium())

def test_producto_limite_premium(self):
    producto = Producto("Teclado Mecánico", 500, 5)
    self.assertFalse(producto.es_producto_premium())


Ejecuta:

```bash
python -m unittest tests.test_inventario -v
```
## Ejercicio 2: TDD - Test Driven Development 

Objetivo: Escribir primero el test, luego la implementación

def test_calcular_precio_con_iva(self):
    producto = Producto("Monitor", 200, 3)
    precio_con_iva = producto.calcular_precio_con_iva(13)
    self.assertEqual(precio_con_iva, 226)


Implementación:

def calcular_precio_con_iva(self, porcentaje_iva):
    if porcentaje_iva < 0:
        raise ValueError("El IVA no puede ser negativo")
    iva = self.precio * (porcentaje_iva / 100)
    return self.precio + iva

## Solución de Problemas

Problema 1: ModuleNotFoundError: No module named 'inventario'
Causa: Python no encuentra el módulo.
Solución:

cd taller_pruebasunitarias
```bash
python -m unittest tests.test_inventario
```

Problema 2: No module named coverage
Solución:
```bash
pip install coverage
```

Problema 3: Los tests pasan pero no deberían
Solución:

Revisa los valores esperados en los assertEqual

Agrega prints para debug:

print(f"Resultado obtenido: {resultado}")

Ejecuta con -v para más detalles.

Problema 4: python: command not found
Solución:
```bash
python3 -m unittest tests.test_inventario
```