#Katheleen Hill
#4/18/2024
#P4HW2
#Edit and enhance employee's gross pay

totOvertime = 0
totRegPay = 0
totGrossPay = 0
count = 0
employee = input("Enter employee's" + ' name or "Done" to terminate: ')
while employee != 'Done':

    hours_worked = float(input('Enter number of hours worked: '))
    pay_rate = float(input("Enter employee's pay rate: "))
    if hours_worked > 40:
             regular_hours = 40
             overtime_hours = hours_worked - 40
             regular_pay = regular_hours * pay_rate
             overtime_pay = overtime_hours * (pay_rate * 1.5)
             gross_pay = regular_pay + overtime_pay
    else:
             regular_hours = hours_worked
             overtime_hours = 0
             regular_pay = regular_hours * pay_rate
             overtime_pay = 0
             gross_pay = regular_pay + overtime_pay
    totOvertime = totOvertime + overtime_pay
    totRegPay = totRegPay + regular_pay
    totGrossPay = totGrossPay + gross_pay
    count = count + 1
    #count++
    print('-'*37)
    print("Employee name: " + employee)
    print()
    print('Hours Worked Pay Rate OverTime OverTime Pay RegHour Pay Gross Pay')
    print('-'*100)
    print(f'{regular_hours:<14.2f} {pay_rate:<11.2f} {overtime_hours:<11.2f} {overtime_pay:<19.2f} {regular_pay:<19.2f} {gross_pay:<21.2f}')
    print()
    
    
    employee = input("Enter employee's" + 'name or "Done" to terminate: ')
print("Total number of employee's entered: " + str(count))
print("Total amount paid for overtime: $" + str(format(totOvertime,'.2f')))
print("Total amount paid for regular hour: $" + str(format(totRegPay,'.2f')))
print("Total amount paid in gross: $" + str(format(totRegPay,'.2f')))

print("Program has exited")


































                                                    
print(totOvertime)
print(totRegPay)
print(totGrossPay)
      
 
