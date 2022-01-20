from setuptools import setup
#pip install --editable .

setup(
    name = 'HelloWorld',
    version='1.0',
    py_modules=['hello'],
    install_requires=['Click'],
    entry_points = '''
        [console_scripts]
        hello=hello:cli
    '''
)