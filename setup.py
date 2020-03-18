"""
For each page number in a PDF, selects only the last page with that number, and then regenerates the PDF
"""
from setuptools import find_packages, setup

dependencies = [
    'click',
    'pdfrw'
]

setup(
    name='last_pdf_page',
    version='0.0.1',
    url='https://github.com/TMiguelT/last_pdf_page',
    license='GPLv3',
    author='Michael Milton',
    author_email='ttmigueltt@gmail.com',
    description='For each page number in a PDF, selects only the last page with that number, and then regenerates the PDF',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'last-pdf-page = last_pdf_page.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
