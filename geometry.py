from cmath import pi
import math
def area_circle(radius_cm):
        area = pi*(radius_cm)**2
        return print(f'The area of your circle is {area: .4} cm^2')

def hypotenuse(side1_in,side2_in):
        hyp = (side1_in**2 + side2_in**2)**0.5
        return print(f'The hypotenuse of your triangle is {hyp: .4} in')