# -*- coding: utf-8 -*-
"""
    pybde: A module to access Database Statistics from Mauro Borges Institute (IMB) 
    (c) 2023 Bernard Silva de Oliveira [bernard.oliveira@goias.gov.br]

"""

import requests
import json


class BDEquery:

    # Initialize variables
    def __init__(self):

        self.ulrMain = 'http://painelmunicipal.imb.go.gov.br/visao/'
        self.parameters = {
            "variableDescribe": 'variavel.php?formatado=0&json=1&codigovariavel=',
            "unidadeMedida": "unidade.php?formatado=0&json=1&codigounidade=",
            "localidades": 'localidade.php?formatado=0&json=1&codigolocalidade=&codigoibge=',
            "dados": '''dados.php?parametros=0|1|{locbde}|{codibge}|{codvarbde}|{anoinicial}|
                                {anofinal}|{ultimoano}|{periodo}|{seriehistorica}|{auxvar}|{auxund}|{auxvarfnt}|
                                {auxfnt}|{auxvarnota}|{auxnota}|'''
        }

    # Get variables datasets from databases statistics
    def getVariables(self, codvar=None):
        """
            Access variables (codes)  in Statistics Database in IMB
        """
        if codvar is None:
            url = self.ulrMain + self.parameters['variableDescribe']
        else:
            url = self.ulrMain + self.parameters['variableDescribe'] + str(codvar)

        # Information requests
        data = requests.get(url)
        data = data.text
        data = json.loads(data)

        return data

    # Get units datasets from databases statistics
    def getUnits(self, codund=None):
        """
            Access units from data  in Statistics Database in IMB
        """
        if codund is None:
            url = self.ulrMain + self.parameters['unidadeMedida']
        else:
            url = self.ulrMain + self.parameters['unidadeMedida'] + str(codund)

        # Requisicao da informacao
        data = requests.get(url)
        data = data.text
        data = json.loads(data)

        return data

    # Get locations datasets from databases statistics
    @property
    def getLocations(self):
        """
            Access data places (counties) in Statistics Database - IMB
        """
        # Requisicao da informacao
        url = self.ulrMain + self.parameters['localidades']
        data = requests.get(url)
        data = data.text
        data = json.loads(data)

        return data

    # Get datas from databases statistics
    def getdata(self, codvarbde, **kwargs):

        """

            |   Access data in Statistics Database - IMB
            |
            |   Parameters
            |   ----------
            |   codvarbde: str
            |       Variable code of the BDE. To acquire the code of the variables in the BDE, use the function getVariables of the pybde.
            |       To query multiples variables, use semicolon in between codes.
            |
            |   codibge: str, optional
            |       IBGE locality code, but use 'T' to show all municipalities. The value 'T' is default.
            |
            |   initialyear:str, optional
            |       Initial year you want to view the information.
            |
            |   finalyear:str, optional
            |       Final year for which information is to be viewed.
            |
            |   timeseries:int, optional
            |       Number of year of the values of the variable, the starting point being the last year
            |
            |   Returns
            |   -------
            |   data: dict
            |
            |   Examples
            |   --------
            |   import pybde.query as bde
            |
            |   bdeObj = bde.BDEquery()
            |
            |   bdeObj.getdata(codvarbde='1;2',codibge='5208707') -> Access data from Goiãnia City.
            |   bdeObj.getdata(codvarbde='15',codibge='5208707',timeseries=10) -> Access data from Goiãnia City in 10 years.
            |   bdeObj.getdata(codvarbde='15',codibge='5208707',initialyear=2013,finalyear=2019) -> Access data from Goiãnia City in between 2013 and 2019.
            |   bdeObj.getdata(codvarbde='15',codibge='5208707',initialyear=2013,finalyear=2019,timeseries=5) -> Access data from Goiãnia City of the last 5 years in between 2013 and 2019.



        """

        #Parâmetros da API
        param = {
            "codibge": 'T',
            "initialyear": None,
            "finalyear": None,
            "timeseries": None,
        }

        for kp in kwargs.keys():
            try:param[kp] = kwargs[kp]
            except:continue

        if (param['initialyear'] is not None) and (param['initialyear'] is not None):
            ultimoano = 0
            periodo = None
        else:
            ultimoano = 1
            periodo = 1


        # URL dos dados
        url = self.ulrMain + self.parameters['dados']
        url = url.format(locbde=None, codibge=param['codibge'], codvarbde=codvarbde,
                         anoinicial=param['initialyear'],anofinal=param['finalyear'],
                         ultimoano=ultimoano, periodo=periodo,seriehistorica=param["timeseries"],
                         auxvar=1, auxund=1,auxvarfnt=1, auxfnt=1,auxvarnota=1, auxnota=1)

        # Requisicao da informacao
        # Initial Time request
        data = requests.get(url)
        data = data.text
        data = json.loads(data)
        listData = []
        # End Time request
        # Initial Time Format
        for row in data:
            dicData = {}
            for j in row.keys():

                if j == 'anos':
                    fulldic = dict()
                    dataYear = row[j]
                    count = 1

                    for k in dataYear.items():
                        new = dicData.copy()
                        new['ano'] = k[0]
                        new['valor'] = k[1]
                        fulldic[str(count)] = new
                        count += 1

                    for i in fulldic.values():
                        listData.append(i)

                else:
                    dicData[j] = row[j]

        # End Time format
        data = listData
        return data
