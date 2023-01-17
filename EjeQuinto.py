def p_triangulo(cateno1:float, cateno2:float)->float:
    hipotenusa = cal_hip(cateno1, cateno2)
    return cateno1 + cateno2 + hipotenusa
