# Logical operators
age = 25
has_licence = True
drunk = True

# AND - both must be true
can_drive = age >= 16 and has_licence and not drunk
print(can_drive)