def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        carro =  request.session.get('carro')
        if carro:
            for i in carro:
                total += float(carro[i]['precio'])
        
    return {'TOTAL_CARRO':total}  