from setuptools import setup

setup(name='pybde',
      version='0.1',
      description='A module to access data from the Mauro Borges Statistic and Socioeconomic Institute (IMB), Goias - Brazil ',
      url='https://www.imb.go.gov.br/bde/',
      author='Bernard Silva de Oliveira',
      author_email="bernard.oliveira@goias.gov.br",
      keywords='statistics data imb Mauro Borges Brazil',
      license='MIT License',
      packages=['pybde'],
      zip_safe=False,
      install_requires=['requests'],
      )