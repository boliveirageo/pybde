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

            Access data in Statistics Database - IMB

            Parameters
            ----------
            codvarbde: str
                Código da variável do BDE

            codibge: str, optinal
                Código da localidade no IBGE e/ou 'T' para todos os municipios

            anoinicial:str, optional
                O valor do ano inicial da variavel

            anofinal:str, optional
                O valor do ano final da variavel

            periodo:int, optional
                Mostrar todas a série de dados da variavel

            seriehistorica:int, optional
                Quantidade de ano dos valores da variável, sendo o ponto de partida o ultimo ano

            Returns
            -------
            data: dict

        """
       
        #Parâmetros da API
        param = {
            "codibge": 'T',
            "anoinicial": None,
            "anoinicial": None,
            "anofinal": None,
            "ultimoano": 1,
            "periodo": None,
            "seriehistorica": None,

        }

        for kp in kwargs.keys():
            try:param[kp] = kwargs[kp]
            except:continue

        # URL dos dados
        url = self.ulrMain + self.parameters['dados']
        url = url.format(locbde=None, codibge=param['codibge'], codvarbde=codvarbde,
                         anoinicial=param['anoinicial'],anofinal=param['anofinal'],
                         ultimoano=param["ultimoano"], periodo=param["periodo"],
                         seriehistorica=param["seriehistorica"],auxvar=1, auxund=1,
                         auxvarfnt=1, auxfnt=1,auxvarnota=1, auxnota=1)

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
