def multiple_number(n):
    digits = [x for x in str(n)]
    product = 1
    for x in digits:
        aux = product
        product = aux * int(x)
    if product >= 10:
        return MultipleNumber(product)
    else:
        return int(product)
