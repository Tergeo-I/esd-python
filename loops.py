def multiplie(a, b):
    """
    Multiplie deux nombres par additions successives.
    """
    result = 0
    for v in range(b):
        result += a
    return result

def puissance(base, exposant):
    """
    Calcule la puissance d'un nombre par multiplication successives.
    """
    result = 1
    for k in range(exposant):
        result = multiplie(result, base)
    return result

print(multiplie(17,5))
print(puissance(17,4))