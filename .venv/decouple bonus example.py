feet_i = input("enter feet and inches")

def convert(feet_i):
    parts = feet_i.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters

result = convert(feet_i)

if result <1:
    print("to small")
else:
    print("kid can use slide")