from distutils.command.clean import clean
from glob import glob
from re import M


print('----------------------------------------------')
print('Welcome To IBM calculator Bot By Mr.TekTaki')
print('-----------------------------------------------')

q = input('If You Want To Know What Is The BMI Click (y), If Not Click (n): ')
if q == 'y':
    print('--------------------------------------------------------------------------------------------------------------------------------------------')
    print('Body mass index is a value derived from the mass and height of a person. The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m², resulting from mass in kilograms and height in metres.')
    print('--------------------------------------------------------------------------------------------------------------------------------------------')

else:
    pass


skinny = 'you have skinny body '
healthy = 'you have a healthy body'
unhealthy = 'you have unhealthy body'
fat = 'you have a fat body'
doc = 'you need a doctor !!'

def m2():
    q1 = input('do you know your m² (y/n): ')
    if q1 == 'y':
        q2 = float(input('enter your m² here: '))
        q3 = float(input('enter your Kg here: '))
        bmi = q3 / q2
        print(f'your BMI is {bmi}')
        if bmi >= 18 <= 25:
            print('--------------------------------')
            print(healthy)
            print('--------------------------------')

        elif bmi < 18:
            print('--------------------------------')
            print(skinny)
            print('--------------------------------')
        elif bmi > 25:
            print('--------------------------------')
            print(unhealthy)
            print('--------------------------------')
        elif bmi > 30:
            print('--------------------------------')
            print(fat)
            print('--------------------------------')
        elif bmi > 40:
            print('--------------------------------')
            print(doc)
            print('--------------------------------')
    else:
        cm = int(input('enter your Cm  here: '))
        m = cm / 100
        m22 = m * 2
        print(f'Your m² is: {m22}')
        m2()


m2()