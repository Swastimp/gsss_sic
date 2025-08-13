name = 'swasti'
id = 1101
basic_monthly_salary = 189000
bonus_percentage = 12
monthly_allowance = 7000
gross_monthly_salary = basic_monthly_salary + monthly_allowance

bonus_amount = gross_monthly_salary * bonus_percentage / 100
gross_annual_salary = gross_monthly_salary * 12 + bonus_amount

print(f'Employee Id = {id}')
print(f'Employee Name = {name}')
print(f'Monthly Gross Salary = {gross_monthly_salary}')
print(f'Annual Gross Salary = {gross_annual_salary}')
#-------------------------------------

