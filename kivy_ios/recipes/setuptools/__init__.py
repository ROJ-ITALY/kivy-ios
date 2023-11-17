# pure-python package, this can be removed when we'll support any python package
from kivy_ios.toolchain import PythonRecipe

class SetuptoolsRecipe(PythonRecipe):
    version = '51.3.3'
    url = 'https://pypi.python.org/packages/source/s/setuptools/setuptools-{version}.tar.gz'

recipe = SetuptoolsRecipe()
