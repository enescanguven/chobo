from pypdf import PdfReader



def pdf_edit(pdf_file, pdf_file_new, image_path):
    """Edit pdf file by adding image to the first page."""
    reader = PdfReader(pdf_file)
    print(reader.pages[0].Contents.stream)

pdf_edit('test.pdf', 'test_new.pdf', 'test_1.png')