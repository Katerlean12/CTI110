# Katheleen Hill
# 5 March 2024
# P2HW2
# Make a list of grades

my_list = []
x = float(input('Enter a grade for Module 1: '))
my_list.append(x)
x = float(input('Enter a grade for Module 2: '))
my_list.append(x)
x = float(input('Enter a grade for Module 3: '))
my_list.append(x)
x = float(input('Enter a grade for Module 4: '))
my_list.append(x)
x = float(input('Enter a grade for Module 5: '))
my_list.append(x)
x = float(input('Enter a grade for Module 6: '))
my_list.append(x)
print()
print('-'*12, 'Results', '-'*12)

lowest = min(my_list)
#lowest = format(lowest,',.2f')
print('Lowest Grade:         ' + str(format(lowest,',.2f')))
highest = max(my_list)
print('Highest Grade:        ' + str(format(highest,',.2f')))
length = len(my_list)
sum1 = sum(my_list)
print('Sum of Grades:        ' + str(format(sum1,',.2f')))
average = sum1/length
print('Average:              ' + str(format(average,',.2f')))
print('-'*40)
