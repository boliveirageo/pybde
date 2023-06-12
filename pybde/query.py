# -*- coding: utf-8 -*-
"""
    pybde: A module to access Database Statistics from Mauro Borges Institute (IMB) 
    (c) 2023 Bernard Silva de Oliveira [bernard.oliveira@goias.gov.br]

"""

import requests
import json


class BDEquery:

    # Initialize variables
    def __init__(self):# -*- coding: utf-8 -*-
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
            "dados": '''dados.php?parametros=0|1|{locbde}|{codibge}|{codVarBDE}|{anoinicial}|
                                {anofinal}|{ultimoano}|{periodo}|{seriehistorica}|{auxVar}|{auxund}|{auxvarfnt}|
                                {auxfnt}|{auxvarnota}|{auxnota}|'''
        }

    # Get variables datasets from databases statistics
    def getVariablesBDE(self, codvar=None):

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
    def getUnidadeBDE(self, codund=None):

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
    def getLocalidadesBDE(self):

        # Requisicao da informacao
        url = self.ulrMain + self.parameters['localidades']
        data = requests.get(url)
        data = data.text
        data = json.loads(data)

        return data

    # Get datas from databases statistics
    def getdadosBDE(self, locbde=None, codibge=None, codvarbde=None, anoinicial=None, anofinal=None, ultimoano=1,
                    periodo=None, seriehistorica=None, auxvar=1, auxund=1, auxvarfnt=1, auxfnt=1, auxvarnota=1,
                    auxnota=1):

        # ----------------------Parâmetros da pesquisa --------------------------
        # locBDE = Código da localidade no BDE e/ou 'T' para todos os municipios
        # codIBGE = Código da localidade no IBGE e/ou 'T' para todos os municipios
        # codVarBDE = Código da variável do BDE
        # anoInicial = O valor do ano inicial da variavel
        # anoFinal = O valor do ano final da variavel
        # periodo = Mostrar todas a série de dados da variavel
        # seriehistorica = Quantidade de ano dos valores da variável, sendo o ponto de partida o ultimo ano

        if (anoinicial is not None) or (anofinal is not None) or (periodo is not None):
            ultimoano = None

        # URL dos dados
        url = self.ulrMain + self.parameters['dados']
        url = url.format(locbde=locbde, codibge=codibge, codvarbde=codvarbde, anoInicial=anoinicial, anoFinal=anofinal,
                         ultimoAno=ultimoano, periodo=periodo, seriehistorica=seriehistorica, auxVar=auxvar,
                         auxUnd=auxund, auxVarFnt=auxvarfnt, auxFnt=auxfnt, auxVarNota=auxvarnota, auxNota=auxnota)

        # Requisicao da informacao
        # Initial Time request
        data = requests.get(url)
        data = data.text
        data = json.loads(data)
        #listData = []
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

                    listData = [i for i in fulldic.values()]

                else:
                    dicData[j] = row[j]

        # End Time format
        data = listData
        return data


        self.ulrMain = 'http://painelmunicipal.imb.go.gov.br/visao/'
        self.parameters = {
            "variableDescribe": 'variavel.php?formatado=0&json=1&codigovariavel=',
            "unidadeMedida": "unidade.php?formatado=0&json=1&codigounidade=",
            "localidades": 'localidade.php?formatado=0&json=1&codigolocalidade=&codigoibge=',
            "dados": '''dados.php?parametros=0|1|{locbde}|{codibge}|{codVarBDE}|{anoinicial}|
                                {anofinal}|{ultimoano}|{periodo}|{seriehistorica}|{auxVar}|{auxund}|{auxvarfnt}|
                                {auxfnt}|{auxvarnota}|{auxnota}|'''
        }

    # Get variables datasets from databases statistics
    def getVariablesBDE(self, codvar=None):

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
    def getUnidadeBDE(self, codund=None):

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
    def getLocalidadesBDE(self):

        # Requisicao da informacao
        url = self.ulrMain + self.parameters['localidades']
        data = requests.get(url)
        data = data.text
        data = json.loads(data)

        return data

    # Get datas from databases statistics
    def getdadosBDE(self, locbde=None, codibge=None, codvarbde=None, anoinicial=None, anofinal=None, ultimoano=1,
                    periodo=None, seriehistorica=None, auxvar=1, auxund=1, auxvarfnt=1, auxfnt=1, auxvarnota=1,
                    auxnota=1):

        # ----------------------Parâmetros da pesquisa --------------------------
        # locBDE = Código da localidade no BDE e/ou 'T' para todos os municipios
        # codIBGE = Código da localidade no IBGE e/ou 'T' para todos os municipios
        # codVarBDE = Código da variável do BDE
        # anoInicial = O valor do ano inicial da variavel
        # anoFinal = O valor do ano final da variavel
        # periodo = Mostrar todas a série de dados da variavel
        # seriehistorica = Quantidade de ano dos valores da variável, sendo o ponto de partida o ultimo ano

        if (anoinicial is not None) or (anofinal is not None) or (periodo is not None):
            ultimoano = None

        # URL dos dados
        url = self.ulrMain + self.parameters['dados']
        url = url.format(locbde=locbde, codibge=codibge, codvarbde=codvarbde, anoInicial=anoinicial, anoFinal=anofinal,
                         ultimoAno=ultimoano, periodo=periodo, seriehistorica=seriehistorica, auxVar=auxvar,
                         auxUnd=auxund, auxVarFnt=auxvarfnt, auxFnt=auxfnt, auxVarNota=auxvarnota, auxNota=auxnota)

        # Requisicao da informacao
        # Initial Time request
        data = requests.get(url)
        data = data.text
        data = json.loads(data)
        # listData = []
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

                    listData = [i for i in fulldic.values()]

                else:
                    dicData[j] = row[j]

        # End Time format
        data = listData
        return data
