class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.prodId)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.prodId,
                "nombre": producto.prodName,
                "acumulado": producto.prodPrice,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.prodPrice
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.prodId)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.prodId)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.prodPrice
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
    
    def productos(self):
        arreglo = []
        for id in self.carrito.keys():
            if id in self.carrito.keys():
                name = self.carrito[id]["nombre"]
                arreglo.append(name)
            elif id not in self.carrito.keys():
                while id not in self.carrito.keys():
                    id += 1
        return (arreglo)