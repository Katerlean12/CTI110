#Katheleen Hill 
#3/26/2024 
#P3HW2
#Formatting strings to make them display nicely.

employee = input("Enter employee's name: ")
hrs = float(input('Enter number of hours worked: '))
rate = float(input("Enter employee's pay rate: "))
##print('-'*37)
##print("Emloyee name:" + employee)
##print('Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay')
##print('-'*100)

ovt_pay = 0
ovt_hrs = 0
if hrs >40:
    reg_pay = rate * 40
    ovt_hrs = hrs - 40
    ovt_rate = 1.5 * rate
    ovt_pay = ovt_hrs * ovt_rate
    gross_pay = reg_pay + ovt_pay
else:
   ovt_pay = 0
   ovt_hrs = 0
   reg_pay = rate * hrs
   gross_pay = reg_pay + ovt_pay
##print('Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay')
print('-'*37)
print("Employee name:   " + employee)
print()
print('Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay')
print('-'*100)
print(f'{hrs:<14.1f} {rate:<11.1f} {ovt_hrs:<11.1f} {ovt_pay:<19.1f} {reg_pay:<19.1f} {gross_pay:<21.1f}') 
##print(hrs)
##print(rate)
##print(ovt_hrs)
##print(ovt_pay)
##print(reg_pay)
##print(gross_pay)

