tempe = int(input('type ur temperature:'))
def fahrenheit_converter(C):
     fahrenheit = C * 9/5 + 32
     return str(fahrenheit) + '˚F'
C2F = fahrenheit_converter(tempe)
print(C2F)
