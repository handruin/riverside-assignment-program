from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='AssignmentProgram',
    version='0.1.0',
    description='Commandline utility designed to parse Community Partner data from Mass Health, ACO/MCO, and CPs and'
                ' assign a Business Unit (AP) to each client.',
    long_description=readme,
    author='Doug Cahill',
    author_email='handruin@gmail.com',
    url='https://github.com/handruin/riverside-assignment-program',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
