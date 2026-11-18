# conftest.py
# Aquí se guardan las "fixtures": piezas reutilizables que pytest
# entrega automáticamente a los tests que las piden por nombre.

import pytest

URL_BASE = "https://www.saucedemo.com"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDA = "secret_sauce"


@pytest.fixture
def pagina_login(page):
    """Abre la página de inicio de sesión y la entrega lista para usar."""
    page.goto(URL_BASE)
    return page


@pytest.fixture
def pagina_logueada(page):
    """Inicia sesión con el usuario válido y entrega la página de productos."""
    page.goto(URL_BASE)
    page.locator('[data-test="username"]').fill(USUARIO_VALIDO)
    page.locator('[data-test="password"]').fill(PASSWORD_VALIDA)
    page.locator('[data-test="login-button"]').click()
    return page
