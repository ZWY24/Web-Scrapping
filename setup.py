from setuptools import setup, find_packages

setup(
    name='zhihu_scraper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'selectolax',
        'beautifulsoup4'
    ]
)
