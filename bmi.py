# helper functions to convert imperial to metric #
def lb_to_kg(lb):
    return lb * 0.45359237

def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

def bmi(weight, height):
# first testing if the weight/height in metric is out of boundary conditions #
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2

print (bmi(52.5, 1.65))
