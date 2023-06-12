## pybde - a module to access IMB data

### This is a module to access data from IMB (Mauro Borges Statistic and Socioeconomic Institute).
#### Install from github: pip install git+https://github.com/boliveirageo/pybde.git
#### Usage:
#####      import pybde.query as bde 
#####      import pandas as pd
#####      bdeObj = bde.BDEquery()
#####      variables = pd.DataFrame(data=a.getVariablesBDE())
#####      units = pd.DataFrame(data=a.getUnidadeBDE())
#####      location = pd.DataFrame(data=a.getLocalidadesBDE)
#####      data = pd.DataFrame(data=a.getdadosBDE(codVarBDE='1;2',codIBGE='T',seriehistorica=5))