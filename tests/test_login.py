# test_login.py
# Pruebas del inicio de sesión en https://www.saucedemo.com

from playwright.sync_api import expect

from conftest import USUARIO_VALIDO, PASSWORD_VALIDA


def test_login_exitoso(pagina_login):
    """Con credenciales válidas se llega a la página de productos."""
    page = pagina_login

    page.locator('[data-test="username"]').fill(USUARIO_VALIDO)
    page.locator('[data-test="password"]').fill(PASSWORD_VALIDA)
    page.locator('[data-test="login-button"]').click()

    # Verificamos la URL y el título de la página de productos
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")


def test_login_password_incorrecta(pagina_login):
    """Con una contraseña incorrecta aparece un mensaje de error."""
    page = pagina_login

    page.locator('[data-test="username"]').fill(USUARIO_VALIDO)
    page.locator('[data-test="password"]').fill("clave_incorrecta")
    page.locator('[data-test="login-button"]').click()

    # Seguimos en la página de login y se muestra el error esperado
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Username and password do not match"
    )


def test_login_usuario_bloqueado(pagina_login):
    """Un usuario bloqueado no puede entrar y ve un mensaje explicando por qué."""
    page = pagina_login

    page.locator('[data-test="username"]').fill("locked_out_user")
    page.locator('[data-test="password"]').fill(PASSWORD_VALIDA)
    page.locator('[data-test="login-button"]').click()

    expect(page.locator('[data-test="error"]')).to_contain_text("locked out")



def test_login_usuario_vacio(pagina_login):
    page = pagina_login

     # ACTUAR: no escribimos nada en el usuario, solo en la contraseña
    page.locator('[data-test="password"]').fill(PASSWORD_VALIDA)
    page.locator('[data-test="login-button"]').click()

    # VERIFICAR: debe aparecer el mensaje de error
    expect(page.locator('[data-test="error"]')).to_contain_text("Epic sadface: Username is required")
