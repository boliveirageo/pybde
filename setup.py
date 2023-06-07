from setuptools import setup

setup(name='pybde',
      version='0.1',
      description='A module to access data from the Mauro Borges Statistic and Socioeconomic Institute (IMB), Goias - Brazil ',
      url='https://github.com/boliveirageo/pybde',
      author='Bernard Silva de Oliveira',
      author_email="bernard.oliveira@goias.gov.br",
      license='MIT',
      packages=['pybde'],
      zip_safe=False,
      install_requires=['requests', 'json'],
      )