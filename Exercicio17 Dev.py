import math
catetooposto = float(input('Digite o comprimento do cateto oposto:'))
catetoadjacente = float(input('Agora digite o comprimeto do cateto adjacente:'))
hipotenusa = math.hypot(catetooposto, catetoadjacente)
print('A hipotenusa vai medir: {:.2}'.format(hipotenusa))