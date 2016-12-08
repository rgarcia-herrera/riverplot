from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='riverplot',
      version='0.1',
      description='River-like timelines',
      long_description=readme(),
      url='https://github.com/rgarcia-herrera/riverplot',
      author='Rodrigo Garcia',
      author_email='rgarcia@riseup.net',
      license='GPL3',
      packages=['riverplot'],
      install_requires=['svgwrite',
                        'pandas',
                        'pytest',],
      include_package_data=True,
      scripts=['bin/riverplot'],
      zip_safe=False
      #TODO: include tests in setup
      
)
