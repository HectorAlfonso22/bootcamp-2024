from clases.Carrito import Carrito
from clases.Categoria import Categoria
from clases.RopaHombre import RopaHombre
from clases.RopaMujer import RopaMujer
from clases.Tienda import Tienda
from clases.Zapatilla import Zapatilla
from clases.Zapato import Zapato

if __name__ == "__main__":
    # Crear productos
    ropahombre1 = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
    ropahombre2 = RopaHombre("Pantalon de Hombre", 30.00, 30, "L")
    ropahombre3 = RopaHombre("Chaqueta de Hombre", 55.00, 20, "G")

    ropamujer1 = RopaMujer("Falda de Mujer", 28.00, 15, "L")
    ropamujer2 = RopaMujer("Blusa de Mujer", 22.00, 40, "XL")
    ropamujer3 = RopaMujer("Vestido de Mujer", 45.00, 10, "P")

    zapato = Zapato("Zapato de Hombre", 60.00, 25, "P")
    zapatilla = Zapatilla("Zapatilla de Mujer", 30.00, 30, "P")

    # Crear categorías y agregar productos
    categoria_ropa = Categoria("Ropa")
    categoria_calzado = Categoria("Calzado")
    
    categoria_ropa.agregar_producto(ropahombre1)
    categoria_ropa.agregar_producto(ropahombre2)
    categoria_ropa.agregar_producto(ropahombre3)
    categoria_ropa.agregar_producto(ropamujer1)
    categoria_ropa.agregar_producto(ropamujer2)
    categoria_ropa.agregar_producto(ropamujer3)

    categoria_calzado.agregar_producto(zapato)
    categoria_calzado.agregar_producto(zapatilla)

    # Crear tienda y agregar categorías
    tienda = Tienda()
    tienda.agregar_categoria(categoria_ropa)
    tienda.agregar_categoria(categoria_calzado)

    # Crear carrito
    carrito = Carrito()

    # Menú para interacción del usuario
    while True:
        print("\n1: Ver productos")
        print("2: Agregar producto al carrito")
        print("3: Ver carrito y finalizar compra")
        print("4: Salir")

        opcion = input("Selecciona una opcion: ").strip()  # Limpia espacios en blanco


        if opcion == '1':
            tienda.mostrar_categorias()
        elif opcion == '2':
            nombre_producto = input("Ingresa el nombre del producto que deseas agregar al carrito: ")
            producto_encontrado = False

            # Buscar el producto en las categorías
            for categoria in tienda._categorias:
                for producto in categoria.get_productos():
                    if producto._nombre.lower() == nombre_producto.lower():
                        carrito.agregar_producto(producto)
                        print(f"{nombre_producto} agregado al carrito.")
                        producto_encontrado = True

            # Si no se encuentra el producto, lanzar un error
            if not producto_encontrado:
                print(f"Error: '{nombre_producto}' no se encuentra en el catálogo. Por favor, intenta nuevamente.")
                continue  # Redirige al menú

        elif opcion == '3':
            carrito.mostrar_carrito()
            break
        elif opcion == '4':
            print("Gracias por visitar nuestra tienda.")
            break
        else:
            print("Opción inválida.")
