import tax_level1

standard_deduction = 50_000
taxable_income = tax_level1.gross_annual_salary - standard_deduction
print(f'Standard Deduction = {standard_deduction}')
print(f'Taxable Income = {taxable_income}')
