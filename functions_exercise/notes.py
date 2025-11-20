import builtins

# positional arguments are the ones that are mandatory

# optional are the ones that have default value and are always written at the end
# Func will return None if we don't give parameters
# or we don't print or we don't have code at all

# the type of the variables are called annotations
# (first_num: int) -> str or int

# """ doc strings are important
# :param first_number: - write all parameters
# :return: say what returns
#  """

# Pep8 standartds for writing code

# print(dir(builtins))

# cjecks if string has only numbers or digits
string = '345hgt'
print(string.isalnum())