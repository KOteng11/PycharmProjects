from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 25)
        # Moving the cursor to the right
        self.cell(80)
        # Printing the title
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break
        self.ln(20)


def main():
    name = input("Name: ")
    # Instantiation of inherited class
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)
    # Add image to page
    pdf.image("shirtificate.png", x="C")
    pdf.set_font("helvetica", "B", size=15)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, -280, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
