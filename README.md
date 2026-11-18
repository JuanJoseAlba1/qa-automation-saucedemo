# QA Automation – SauceDemo

Proyecto de práctica de automatización de pruebas con **Python, pytest y Playwright**
sobre [SauceDemo](https://www.saucedemo.com), una tienda online creada para practicar testing.

## Qué se prueba

| Archivo | Caso de prueba | Resultado esperado |
|---|---|---|
| `test_login.py` | Login exitoso | Se llega a la página de productos |
| `test_login.py` | Login con contraseña incorrecta | Aparece un mensaje de error |
| `test_login.py` | Login con usuario bloqueado | Aparece el mensaje "locked out" |
| `test_login.py` | Login con usuario vacío | Aparece el mensaje "Username is required" |
| `test_login.py` | Login con contraseña vacía | Aparece el mensaje "Password is required" |
| `test_carrito.py` | Agregar un producto al carrito | El contador del carrito muestra 1 |
| `test_carrito.py` | Eliminar un producto del carrito | El contador del carrito desaparece |
| `test_carrito.py` | Ordenar productos por precio (menor a mayor) | Los precios quedan en orden ascendente |

## Requisitos

- Python 3.9 o superior

## Instalación

```bash
# 1. Crear y activar un entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac / Linux

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Descargar los navegadores que usa Playwright
playwright install
```

## Cómo ejecutar las pruebas

```bash
pytest                    # ejecuta todos los tests (sin abrir ventana)
pytest --headed           # ejecuta viendo el navegador
pytest tests/test_login.py   # ejecuta solo un archivo
pytest -v                 # muestra el nombre de cada test
```

## Estructura del proyecto

```
qa-automation-saucedemo/
├── tests/
│   ├── conftest.py       # fixtures reutilizables (login, página inicial)
│   ├── test_login.py
│   └── test_carrito.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Próximos pasos

- [ ] Page Object Model
- [ ] Pruebas parametrizadas con varios usuarios
- [ ] Pruebas de API
- [ ] Reportes HTML y capturas de pantalla en fallos
- [ ] GitHub Actions (CI)
