def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    return {"total_carrito": total}

def costo_envio(request):
    envio = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            total = sum(total_carrito(request).values())
            envio = int(total * 0.05)
    return {"costo_envio": envio}

def total_final(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            subTotal = sum(total_carrito(request).values())
            envio = sum(costo_envio(request).values())
            total = subTotal + envio
    return {"total_final": total}