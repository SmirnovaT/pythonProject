#def devide(dividend, divisor):
#    if divisor == 0:
#        raise ZeroDivisionError("Divisor cannot be 0.")
#        raise TypeError
 #   return dividend / divisor

#grades = []

#print("Welcome to the average grade program.")
#try:
#    average = devide(sum(grades), len(grades))
#except ZeroDivisionError as e:
#    print(e)
 #   print("There are no grades yet in your list.")
#else:
#    print(f"The average grade is {average}.")

#finally:
#    print("Thank you!")







def devide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
        raise TypeError
    return dividend / divisor

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = devide(sum(grades), len(grades))
        print(f'{name} averaged {average}.')
except ZeroDivisionError:
    print(f'ERROR: {name} has no grades!')
else:
    print('-- All student averages calculated --')

finally:
    print("-- End of student average calculation --")