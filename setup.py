from setuptools import setup

setup(
    name='pyakb48',
    version='0.0.0',
    author='Moriyoshi Koizumi',
    author_email='mozo@mozo.jp',
    packages=['akb48', 'akb48.member'],
    url='http://pypi.python.org./pypi/akb48/',
    license='LICENSE.txt',
    description='A port of a useful Perl module',
    long_description=open('README.txt').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Python License Version 2",
        ],
    )
