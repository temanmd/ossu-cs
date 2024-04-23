def convert(string):
    string_0 = string.replace(":)", "🙂")
    return(string_0.replace(":(", "🙁"))

def main():
    string = input("Write any text with smiles: ")
    result = convert(string)
    print(f"Text with converted smiles: {result}")

main()
