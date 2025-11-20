import re

count_of_barcodes = int(input())
pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'

for _ in range(count_of_barcodes):
    barcode = input()

    match = re.match(pattern, barcode)

    if match:
        product_group = ''.join(filter(str.isdigit, match.group(1))) or '00'
        print(f'Product group: {product_group}')
    else:
        print(f'Invalid barcode')