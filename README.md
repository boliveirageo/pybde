## pybde - a module to access IMB data



This is a module to access data from IMB (Mauro Borges Statistic and Socioeconomic Institute). Such information
can be found at https://painelmunicipal.imb.go.gov.br/ by entering variable code, IBGE code or location IMB code.

Install from github: pip install git+https://github.com/boliveirageo/pybde.git.

 Usage:

      #Import modules pybde and pandas
      import pybde.query as bde 
      import pandas as pd
      
      #Object instance
      bdeObj = bde.BDEquery()
      
      #Variables information from Statistics Database of IMB 
      variables = pd.DataFrame(data=a.getVariables())
      
      #Variables units information from Statistics Database of IMB
      units = pd.DataFrame(data=a.getUnits())
      
      #Municipalites information from Statistics Database of IMB
      location = pd.DataFrame(data=a.getLocations)
      
      #Access data from Statistics Database of IMB in variables code of 1 and 2,
      #all location in Goias at last 5 years.
      data = pd.DataFrame(data=a.getdata(codvarbde='1;2',codibge='T',seriehistorica=5))