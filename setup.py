"Package setup file"
from setuptools import setup


def readme():
    "Load README.md"
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='HazeCrate',
    version='0.1',
    description='Steam Deck DOSBox compatibility tool',
    long_description=readme(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    url='https://github.com/HazeCrate/HazeCrate',
    author='Austin Warren',
    license='MIT',
    entry_points={
        'console_scripts': ['main'],
    },
    include_package_data=True,
    )
