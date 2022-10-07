from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject


# From https://stackoverflow.com/questions/58898542/update-a-fillable-pdf-using-pypdf2/58898710#58898710
def set_need_appearances_writer(writer: PdfFileWriter):
    # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)
            })

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        # del writer._root_object["/AcroForm"]['NeedAppearances']
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer

def init_pdf_writer_from_reader(reader: PdfFileReader) -> PdfFileWriter:
    """
    Initializes a PdfFileWriter that can be used to write data to the given PDF
    stored inside of the PdfFileReader.

    IMPORTANT: Using this init function ensures that the data written is visible
               both in a PDF Viewer Application and in a Preview context (i.e. an email client)
    """
    if not reader or reader.getNumPages() == 0:
        raise Exception(f"Error initializing PdfFileWriter, given PdfFileReader "
                        f"is either null or contains no pages.")

    pdf_writer = PdfFileWriter()

    # Add all PDF pages from reader -> writer
    pdf_writer.appendPagesFromReader(reader)

    # Copy over additional data from reader -> writer
    pdf_writer._info = reader.trailer["/Info"]
    reader_trailer = reader.trailer["/Root"]
    pdf_writer._root_object.update(
        {
            key: reader_trailer[key]
            for key in reader_trailer
            if key in ("/AcroForm", "/Lang", "/MarkInfo")
        }
    )

    # Set written data appearances to be visible
    set_need_appearances_writer(pdf_writer)
    if "/AcroForm" in pdf_writer._root_object:
        pdf_writer._root_object["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})

    return pdf_writer
