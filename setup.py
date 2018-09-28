from setuptools import setup

setup(
    name = 'cled',
    version = '1.0',
    py_module = ['newsapi'],
    install_requires = ['click','requests'],
    entry_points =''' 
                ['console_scripts']
                cled=newsapi:cli
    ''',                
            
)