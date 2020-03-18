import pdfrw
import typing


def build_page_lookup(labels) -> typing.List[typing.Tuple[int, dict]]:
    """
    Given a PDF label tree (aka the value of pdf['/Root']['/PageLabels']['/Nums']), build it into an array of (index,
    dictionary) tuples
    """
    lookup = []
    it = iter(labels)
    while True:
        try:
            # The PageLabels tree alternates between the page index that begins the current range, and a dictionary that
            # describes the numbering within that range
            range_start = next(it)
            range_dict = next(it)
            lookup.append((int(range_start), dict(range_dict)))
        except StopIteration:
            return lookup


def simplify_pdf(pdf: str, select: str, outfile: typing.TextIO):
    """
    Given a PDF and a metric by which to select the first or last page in a range of pages with the same name,
    remove the unnecessary pages
    """
    in_pdf = pdfrw.PdfFileReader(pdf)
    out_pdf = pdfrw.PdfFileWriter(trailer=in_pdf)
    for index in calculate_pages(in_pdf, select):
        out_pdf.addPage(in_pdf.getPage(index))
    out_pdf.write(outfile)


def calculate_pages(pdf: pdfrw.PdfFileReader, select: str) -> typing.List[int]:
    """
    Given a PDF and a metric by which to select the first or last page in a range of pages with the same name,
    produce a list of page indices
    """
    # The page indexes we want to output
    final_pages = []

    # Note: this is based on section 8.3.1 Page Labels of the PDF spec
    page_lookup = build_page_lookup(pdf['/Root']['/PageLabels']['/Nums'])
    for i, (range_start, range_dict) in enumerate(page_lookup):

        # Calculate the starting index of the next section (or the last index if this is the last section)
        next_start = page_lookup[i + 1][0] if i + 1 < len(page_lookup) else len(pdf.pages)

        if '/S' in range_dict:
            # If there is a numbering style for this range, then each page in the range is unique, and we should
            # use all of them
            final_pages += list(range(range_start, next_start))
        else:
            # If there is no numbering style for this range, each page in the range has the same number, so we
            # have to choose either the first or last page in that range
            if select == 'first':
                final_pages.append(range_start)
            else:
                final_pages.append(next_start - 1)

    return final_pages
