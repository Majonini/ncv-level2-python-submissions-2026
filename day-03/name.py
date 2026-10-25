raw = " nomsa DLAMINI "
name = raw.strip().title()
parts = name.split()
print("Name:  ", name)
print("Surname:", parts[-1].upper())