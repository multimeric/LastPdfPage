import click
import sys

from last_pdf_page import simplify_pdf


@click.command()
@click.argument('pdf', type=click.Path())
@click.option('--select', type=click.Choice(['first', 'last']), default='last', help='Whether to choose the first, or '
                                                                                     'last page for each number')
def main(pdf: str, select: str):
    simplify_pdf(pdf, select, sys.stdout.buffer)


if __name__ == '__main__':
    main()
