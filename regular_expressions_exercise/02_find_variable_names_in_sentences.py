import re

line = input()
pattern = r'\b_{1}([A-Za-z0-9]+)\b'

variable_names = re.findall(pattern, line)

print(','.join(variable_names))