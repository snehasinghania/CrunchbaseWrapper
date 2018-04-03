from setuptools import setup

setup(
    name='crunchbasescraper',
    version='0.1.0',
    author='Sneha Singhania',
    author_email='sneha.a@iiitb.org',
    scripts=['crunchbase.py', 'database_orm.py', 'simple_scraper.py', 're_demo.py', 'database_json.py'],
    license='MIT',
    description='Useful to scrape data from Crunchbase and storing it in a database',
    long_description=open('README.md').read(),
    python_requires='>=3.5',
    install_requires=[
        "requests == 2.18.4",
        "sqlalchemy == 1.2.6",
        "pynlp == 0.3.5",
    ],
)
