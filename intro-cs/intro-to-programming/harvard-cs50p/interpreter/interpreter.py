x, y, z = input("Expression: ").split()
x, z = [int(x), int(z)]

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z

formated_result = round(float(result), 1)
print(formated_result)
