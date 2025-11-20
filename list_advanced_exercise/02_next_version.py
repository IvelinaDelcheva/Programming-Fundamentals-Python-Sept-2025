version_of_software = input().split('.')

software_as_int = int(''.join(version_of_software))
software_as_int += 1
print('.'.join(str(software_as_int)))