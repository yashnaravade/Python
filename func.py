def cal_tax(amount, tax_rate):
    return round((amount * tax_rate) / 100, 2)

print(cal_tax(100, 33.338))