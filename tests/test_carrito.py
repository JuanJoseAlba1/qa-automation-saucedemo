# test_carrito.py
# Pruebas del carrito de compras y del ordenamiento de productos

from playwright.sync_api import expect

# Selectores que se repiten en varios tests
BOTON_AGREGAR = '[data-test="add-to-cart-sauce-labs-backpack"]'
BOTON_QUITAR = '[data-test="remove-sauce-labs-backpack"]'
CONTADOR_CARRITO = '[data-test="shopping-cart-badge"]'


def test_agregar_producto_al_carrito(pagina_logueada):
    """Al agregar un producto, el contador del carrito muestra 1."""
    page = pagina_logueada

    page.locator(BOTON_AGREGAR).click()

    expect(page.locator(CONTADOR_CARRITO)).to_have_text("1")


def test_eliminar_producto_del_carrito(pagina_logueada):
    """Al quitar el producto, el contador del carrito desaparece."""
    page = pagina_logueada

    page.locator(BOTON_AGREGAR).click()
    page.locator(BOTON_QUITAR).click()

    # Con el carrito vacío, el contador ya no se muestra
    expect(page.locator(CONTADOR_CARRITO)).to_have_count(0)


def test_ordenar_productos_por_precio_ascendente(pagina_logueada):
    """Al ordenar de menor a mayor precio, los precios quedan en orden."""
    page = pagina_logueada

    # "lohi" significa "low to high" (de menor a mayor)
    page.locator('[data-test="product-sort-container"]').select_option("lohi")

    # Leemos todos los precios de la página, por ejemplo "$7.99"
    textos = page.locator('[data-test="inventory-item-price"]').all_inner_texts()

    # Quitamos el símbolo "$" y los convertimos a números
    precios = [float(texto.replace("$", "")) for texto in textos]

    # Si la lista ya está ordenada, es igual a su versión ordenada
    assert precios == sorted(precios)
