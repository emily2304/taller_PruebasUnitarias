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
git clone <url-del-repositorio>
cd taller_pruebas_unitarias

# O descarga el ZIP y extráelo

No se requieren dependencias externas (unittest viene con Python).
Para funcionalidades opcionales (cobertura de código):

pip install coverage

Opción 2: Crear el Proyecto desde Cero
Paso 1: Crear la estructura de carpetas
# Windows
mkdir taller_pruebas_unitarias
cd taller_pruebas_unitarias
mkdir src
mkdir tests

# Linux/Mac
mkdir -p taller_pruebas_unitarias/{src,tests}
cd taller_pruebas_unitarias

Paso 2: Crear archivos vacíos
# Windows
type nul > src\inventario.py
type nul > tests\test_inventario.py
type nul > README.md

# Linux/Mac
touch src/inventario.py
touch tests/test_inventario.py
touch README.md

Paso 3: Copiar el código

Copia el contenido de los archivos proporcionados en el taller:

src/inventario.py - Código de la aplicación

tests/test_inventario.py - Suite de pruebas

📁 Estructura del Proyecto
taller_pruebas_unitarias/
│
├── README.md                   # Este archivo
├── requirements.txt            # Dependencias (opcional)
│
├── src/
│   └── inventario.py           # Código fuente de la aplicación
│
└── tests/
    └── test_inventario.py      # Pruebas unitarias

🚀 Guía Paso a Paso
PASO 1: Configuración Inicial (2 minutos)

1.1. Navega al directorio del proyecto

cd taller_pruebas_unitarias


1.2. Verifica que los archivos existan

# Windows
dir /s

# Linux/Mac
ls -R


1.3. Revisa el código fuente
Abre src/inventario.py en tu editor para familiarizarte con:

Clase Producto: gestión de productos individuales

Clase Inventario: gestión del inventario completo

PASO 2: Ejecución Básica de Pruebas (2 minutos)
# Opción 1: Ejecución estándar
python -m unittest tests.test_inventario

# Opción 2: Con modo verboso (recomendado para aprendizaje)
python -m unittest tests.test_inventario -v

# Opción 3: Ejecutar el archivo directamente
python tests/test_inventario.py


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

PASO 3: Ejecutar Pruebas Específicas (1 minuto)
# Solo pruebas de la clase Producto
python -m unittest tests.test_inventario.TestProducto -v

# Solo pruebas de la clase Inventario
python -m unittest tests.test_inventario.TestInventario -v

# Ejecutar un test individual
python -m unittest tests.test_inventario.TestProducto.test_aplicar_descuento -v

PASO 4: Demostración de Detección de Bugs (2 minutos)

Edita src/inventario.py, línea 18 del método calcular_valor_total:

# ANTES (correcto):
def calcular_valor_total(self):
    return self.precio * self.cantidad

# DESPUÉS (con bug):
def calcular_valor_total(self):
    return self.precio * self.cantidad + 10  # Bug agregado


Ejecuta las pruebas nuevamente:

python -m unittest tests.test_inventario -v


Salida:

FAIL: test_calcular_valor_total (test_inventario.TestProducto)
AssertionError: 5010 != 5000


Corrige el bug eliminando el + 10 y vuelve a ejecutar las pruebas.

PASO 5: Medición de Cobertura de Código (2 minutos - OPCIONAL)
pip install coverage
coverage run -m unittest tests.test_inventario
coverage report -m


Salida esperada:

Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/inventario.py            45      0   100%
tests/test_inventario.py     87      0   100%
-------------------------------------------------------
TOTAL                       132      0   100%


Reporte HTML (opcional):

coverage html


Abre htmlcov/index.html en tu navegador.

PASO 6: Análisis de los Tests (1 minuto)

Ejemplo:

def test_nombre_descriptivo(self):
    """Documentación del propósito del test"""
    # 1. ARRANGE
    producto = Producto("Laptop", 1000, 5)
    # 2. ACT
    valor = producto.calcular_valor_total()
    # 3. ASSERT
    self.assertEqual(valor, 5000)


Tipos de tests:

✅ Positivos

❌ Negativos

🔄 Límite

🎯 Ejercicios Prácticos
Ejercicio 1: Agregar Nuevo Método y Tests (5 minutos)

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

python -m unittest tests.test_inventario -v

Ejercicio 2: TDD - Test Driven Development (10 minutos)

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

Ejercicio 3: Debuggear con Tests (5 minutos)
def test_reducir_stock_exacto(self):
    producto = Producto("Ratón", 15, 5)
    producto.reducir_stock(5)
    self.assertEqual(producto.cantidad, 0)

def test_reducir_mas_stock_del_disponible(self):
    producto = Producto("Ratón", 15, 5)
    with self.assertRaises(ValueError):
        producto.reducir_stock(10)

📚 Recursos Adicionales
Documentación Oficial

unittest - Python Docs

coverage.py - Documentación

Comandos Útiles
python -m unittest discover
python -m unittest tests.test_inventario -q
python -m unittest tests.test_inventario --failfast
python -m unittest --help

Assertions Más Comunes
Assertion	Uso
assertEqual(a, b)	Verifica que a == b
assertNotEqual(a, b)	Verifica que a != b
assertTrue(x)	Verifica que x es True
assertFalse(x)	Verifica que x es False
assertRaises(Exception)	Verifica que se lance una excepción
assertIn(a, b)	Verifica que a esté en b
assertIsNone(x)	Verifica que x es None
assertGreater(a, b)	Verifica que a > b
🔍 Solución de Problemas

Problema 1: ModuleNotFoundError: No module named 'inventario'
Causa: Python no encuentra el módulo.
Solución:

cd taller_pruebas_unitarias
python -m unittest tests.test_inventario


Problema 2: No module named coverage
Solución:

pip install coverage


Problema 3: Los tests pasan pero no deberían
Solución:

Revisa los valores esperados en los assertEqual

Agrega prints para debug:

print(f"Resultado obtenido: {resultado}")


Ejecuta con -v para más detalles.

Problema 4: python: command not found
Solución:

python3 -m unittest tests.test_inventario
# O en Windows:
py -m unittest tests.test_inventario