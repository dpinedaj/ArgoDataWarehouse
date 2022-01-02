from setuptools import setup, find_packages

setup(
    name="argodw",
    version="1.0",
    description="Code to perform data warehouse migration with Argo Flow",
    author="Daniel Pineda",
    author_email="dpinedaj@unal.edu.co",
    install_requires=[
        "requests",
        "pandas",
        "psycopg2-binary",
        "sqlalchemy",
        "click",
        "tqdm"
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points='''
    [console_scripts]
    argodaniel=argodw:cli
    '''
)
