class Categorias:
    idcategoria = 0
    nombre = ""

class Proveedores:
    idproveedor = 0
    nombre = 0

class Productos:
    idproducto = 0
    CategoriaProducto = Categorias()
    Precio = 0
    Tamaño = 0
    TipoProducto = 0
    CIFProveedor = Proveedores()


p = Productos()
p.CategoriaProducto.nombre
p.CategoriaProducto.idcategoria