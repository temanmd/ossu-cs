from pyfiglet import Figlet
import sys

figlet = Figlet()

if len(sys.argv) > 1:
    available_args = ["-f", "--font"]
    available_fonts = figlet.getFonts()
    if (
        len(sys.argv) == 3 and
        sys.argv[1] in available_args and
        sys.argv[2] in available_fonts
    ):
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Wrong arguments")

text = input("Input: ").strip()
print("Output:")
print(figlet.renderText(text))
