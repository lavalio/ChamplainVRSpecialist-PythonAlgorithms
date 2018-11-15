sale1 = "1.40"
sale2 = "2.30"

total = float(sale1) + float(sale2)

print(round(total, 3))

# v2

import decimal

sale_dec1 = decimal.Decimal(sale1)
sale_dec2 = decimal.Decimal(sale2)

print(sale_dec1 + sale_dec2)