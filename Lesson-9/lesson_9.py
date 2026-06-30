# Lesson-8

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive!")
else:
    print(f"You need {18-age} more years to drive.")

my_age = 21
your_age = int(input("Enter your age: "))
if your_age > my_age:
    print(f"You are {your_age - my_age} years older than me.")
elif your_age < my_age:
    print(f"I am {my_age - your_age} years older than you.")
else:
    print("We are the same age.")

month = str.lower(input("Enter a month: "))
if month in ["september", "october", "november"]:
    print("The Season is Autumn!")
elif month in ["december", "january", "february"]:
    print("The Season is Winter!")
elif month in ["march", "april", "may"]:
    print("The Season is Spring!")
elif month in ["june", "july", "august"]:
    print("The Season is Summer!")
else:
    print("Invalid month entered.")

person = {
    'first_name': 'Muhammad',
    'last_name': 'Umais',
    'age': 21,
    'country': 'Finland',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person:
    print(person["skills"][len(person["skills"])//2])
    if "Python" in person["skills"]:
        print("Python is present in the skills.")
    if person["skills"] == ["Javascript", "React"]:
        print("He is a front end developer.")

if not person["is_married"] and person["country"] == "Finland":
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married.")
