from math import sqrt

def calculo(categoria, subcategoria, rating, Icategoria, Isubcategoria, Irating):
    MultiplicacionVectors = (categoria * Icategoria + subcategoria * Isubcategoria + rating * Irating)
    Modulovectores = (sqrt(pow(categoria, 2) + pow(subcategoria, 2) + pow(rating, 2)) *
                      sqrt(pow(Icategoria, 2) + pow(Isubcategoria, 2) + pow(Irating, 2)))
    resultado = MultiplicacionVectors / Modulovectores
    print(resultado)
    return resultado
