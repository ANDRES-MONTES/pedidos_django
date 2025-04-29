class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carro = self.session.get('carro')
        
        if not self.carro:
            self.carro = self.session['carro'] = {}
        else:
            self.carro = self.carro
            
    
    def add_product(self, producto):
        if str(producto.id) not in self.carro:
            self.carro[str(producto.id)] = {
                                    'producto_id':producto.id,
                                    'nombre':producto.name,
                                    'precio':round(producto.precio, 2),
                                    'cantidad':1,
                                    'imagen':producto.imagen.url
                                }
        else:
            self.carro[str(producto.id)]['cantidad'] += 1
            nuevo_precio = self.carro[str(producto.id)]['precio'] + float(producto.precio)
            self.carro[str(producto.id)]['precio'] = round(nuevo_precio, 2)
        
        
        self.guardar_carro()
        
            
    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
        
    def delete_product(self, producto):
        if str(producto.id) in self.carro:
            del self.carro[str(producto.id)]
            self.guardar_carro()
            
    def restar_unidades(self, producto):
        if self.carro[str(producto.id)]['cantidad'] == 1:
            self.delete_product(producto)
        else:
            self.carro[str(producto.id)]['cantidad'] -= 1
            self.carro[str(producto.id)]['precio'] -= round(float(producto.precio), 2)
            self.guardar_carro()
        
        
    def delete_all(self):
        self.session['carro'] = {}
        self.session.modified = True
                            
    
