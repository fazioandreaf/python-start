# # return the initials
# name = str(input('Your name: '))
# middleName = str(input('Your middleName: '))
# lastname = str(input('Your lastname: '))
# print(name[0]+middleName[0]+'. '+lastname[0])

# import math
# radius = float(input('Write the radius: '))
# circumference = math.ceil(math.pi * radius * 2)
# area = math.ceil(math.pi * radius ** 2)
# print('The circumference: ', circumference, 'm')
# print('The area: ', area, 'm^2')

# # Give the name month's of his birthday
# month= str(input('Write your birthday in this format DD-MM-YY: '))
# months= ('Gen', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
# index= int((month[3:5]))-1
# print(months[index])

# # Get information from a dictionary person
# person = {'name': 'Andrea', 'gender': 'male', 'age': 28, 'address': 'Gravina di Catania' }
# key = str(input('What information do you want to know about the person? ')).lower()
# print(person.get(key, 'That information is not avaible'))

my_age = 28
user_age = int(input('Type your age: '))
if (user_age > my_age):
    print("Yo're older than me")
elif (user_age < my_age):
    print("I'm older than you")
else:
    print('We are the same age')