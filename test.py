weight = float(input('Type your weight in Kg: '))
height = float(input('Type your height in m: '))

bmi = weight / height **2

classification = 'Obesity'

if (bmi <= 18.5) :
    classification = 'Underweight'
elif ( bmi > 18.5 and bmi <= 24.9) :
    classification = 'Normal weight'
elif ( bmi > 24.9 and bmi <= 29.9) :
    classification = 'Overweight'

print("Yo're ", classification, ' and bmi are: ', bmi)
