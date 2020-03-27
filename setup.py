from setuptools import setup, find_packages

setup(
    name='Chatbot',
    version='0.1.0',
    description='Simple and funny chat bot',
    # long_description=readme,
    author='Sarunas Venckus',
    author_email='venckus.sarunas@gmail.com',
    url='https://github.com/Venckus/tribeofai_workshop_class_e.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)