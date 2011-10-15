from distutils.core import setup

setup(
    name='akb48',
    version='0.0.0',
    author='Moriyoshi Koizumi',
    author_email='mozo@mozo.jp',
    packages=['akb48', 'akb48.member'],
    url='http://pypi.python.org./pypi/akb48/',
    license='LICENSE.txt',
    description='A port of a useful Perl module',
    long_description=open('README.txt').read()
    )
