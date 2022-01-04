# weight = float(input('Type your weight in Kg: '))
# height = float(input('Type your height in m: '))

# bmi = weight / height **2

# classification = 'Obesity'

# if (bmi <= 18.5) :
#     classification = 'Underweight'
# elif ( bmi > 18.5 and bmi <= 24.9) :
#     classification = 'Normal weight'
# elif ( bmi > 24.9 and bmi <= 29.9) :
#     classification = 'Overweight'

# print("Yo're ", classification, ' and bmi are: ', bmi)

# # Error Handling

# number = input('Type a number')

# try:
#     number = float(number)
#     print('the number is : ', number)
# except:
#     print('Invalid number')


# Function
def say_hello(person1, person2='the director'):
    print('Hello', person1, "I'm your", person2)

say_hello("Jane!")

def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius

print('Celsius: ', round(fahr2celsius(100)), '°')
print('Kelvin: ', round(fahr2celsius(100) + 273.5), 'K')