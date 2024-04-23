import sys
from PIL import Image, ImageOps


def check_files_extensions(input_filename, output_filename):
    available_extensions = ["jpg", "jpeg", "png"]
    input_file_extension = input_filename.rsplit(".", maxsplit=1)[1].lower()
    output_file_extension = output_filename.rsplit(".", maxsplit=1)[1].lower()

    if input_file_extension != output_file_extension:
        sys.exit("Input and output have different extensions")
    if input_file_extension not in available_extensions:
        sys.exit("Invalid output")


def generate_shirt(input_filename, output_filename):
    try:
        input_image = Image.open(input_filename)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_image = Image.open("shirt.png")
    resized_image = ImageOps.fit(input_image, size=shirt_image.size)
    resized_image.paste(shirt_image, mask=shirt_image)
    resized_image.save(output_filename)


def main():
    args_length = len(sys.argv)
    if args_length < 3:
        sys.exit("Too few command-line arguments")
    if args_length > 3:
        sys.exit("Too many command-line arguments")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    check_files_extensions(input_filename, output_filename)
    generate_shirt(input_filename, output_filename)


if __name__ == "__main__":
    main()
