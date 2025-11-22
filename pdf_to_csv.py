import tabula

def convert_pdf_to_csv_direct(pdf_path, output_csv_path):
    """
    Directly converts tables in a PDF file into a CSV file.
    """
    tabula.convert_into(
        pdf_path,
        output_csv_path,
        output_format="csv",
        pages="all"
    )
    print(f"Successfully converted {pdf_path} to {output_csv_path}")

# Example usage:
input_pdf = "attendance.pdf"
output_csv = "attendance.csv"
convert_pdf_to_csv_direct(input_pdf, output_csv)