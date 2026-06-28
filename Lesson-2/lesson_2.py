# pyint: disable=invalid-name
# Lesson 2

f_name = 'Muhammad'
l_name = 'Umais'
full_name = 'Muhammad Umais'
country = 'Narnia'
city = 'Emerald City'
age = 21
year = 2005
is_married = False
is_true = True
is_light_on = False
gender, availability = 'M', 'Yes'

# level 2

print(type(f_name))
print(len(f_name))
if len(f_name) > len(l_name):
    print('First name is longer!')
elif len(f_name) < len(l_name):
    print('Last name is longer!')
else:
    print('Both are equal!')

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_one % num_two
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

# Circle Operations

radius = float(input('Enter radius of a circle: '))
area = 3.14 * (radius ** 2)
print('Area of circle: ', area)
circum = 2 * 3.14 * radius
print('Circumference of a circle: ', circum)
