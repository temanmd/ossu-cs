from fpdf import FPDF, Align


class MyPDF(FPDF):
    def __init__(self, name):
        super().__init__(orientation="portrait", format="A4")
        self._my_name = name
        self.set_top_margin(40)

    def header(self):
        self.set_font("helvetica", "B", 45)
        self.cell(center=True, text="CS50 Shirtificate")

    def footer(self):
        self.set_y(70)
        self.image("shirtificate.png", x=Align.C, h=180)
        self.set_font("helvetica", size=20)
        self.set_text_color(255, 255, 255)
        self.cell(text=f"{self._my_name} took CS50", h=-240, center=True)


def main():
    name = input("Name: ").strip()
    pdf = MyPDF(name)
    pdf.add_page()
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
