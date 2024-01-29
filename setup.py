from setuptools import setup, find_packages

setup(
    name='pyWebCrawler',
    version='1.0.2',
    description='pyWebCrawler is a Python-based web crawling tool designed to automatically extract URLs, subdomains, and JavaScript files from websites.',
    author='Aashishsec',
    url='https://github.com/aashishsec/pyWebCrawler',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
    ],
    extras_require={
        'dev': ['argparse', 'concurrent.futures','re','random'],
    },
    entry_points={
        'console_scripts': [
            'pyWebCrawler = pyWebCrawler.pyWebCrawler:main',
        ],
    },
)
