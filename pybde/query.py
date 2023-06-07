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

        self.ulrMain = 'http://painelmunicipal.imb.go.gov.br/visao/variavel.php?'
        self.urls = dict(
            variableDescribe='http://painelmunicipal.imb.go.gov.br/visao/variavel.php?formatado=0&json=1&codigovariavel=',
            unidadeMedida='http://painelmunicipal.imb.go.gov.br/visao/unidade.php?formatado=0&json=1&codigounidade=',
            localidades='http://painelmunicipal.imb.go.gov.br/visao/localidade.php?formatado=0&json=1&codigolocalidade=&codigoibge=',
            dados='''http://painelmunicipal.imb.go.gov.br/visao/dados.php?parametros=0|1|{locBDE}|{codIBGE}|{codVarBDE}|{anoInicial}|
                                {anoFinal}|{ultimoAno}|{periodo}|{seriehistorica}|{auxVar}|{auxUnd}|{auxVarFnt}|{auxFnt}|{auxVarNota}|{auxNota}|'''
        )

    # Get variables datasets from databases statistics
    def getVariablesBDE(self, codVar = None):

        if codVar is None:
            url = self.urls['variableDescribe']
        else:
            url = self.urls['variableDescribe'] + str(codVar)

        # Information requests
        data = requests.get(url)
        data = data.text
        data = json.loads(data)

        return data

    # Get units datasets from databases statistics
    def getUnidadeBDE(self, codUnd=None):

        if codUnd is None:
            url = self.urls['unidadeMedida']
        else:
            url = self.urls['unidadeMedida'] + str(codUnd)

        # Requisicao da informacao
        data = requests.get(url)
        data = data.text
        data = json.loads(data)

        return data

    # Get locations datasets from databases statistics
    def getLocalidadesBDE(self):

        # Requisicao da informacao
        data = requests.get(self.urls['localidades'])
        data = data.text
        data = json.loads(data)

        return data

    # Get datas from databases statistics
    def getdadosBDE(self, locBDE=None, codIBGE=None, codVarBDE=None, anoInicial=None, anoFinal=None, ultimoAno=1,
                    periodo=None, seriehistorica=None,
                    auxVar=1, auxUnd=1, auxVarFnt=1, auxFnt=1, auxVarNota=1, auxNota=1):

        ##----------------------Parâmetros da pesquisa --------------------------
        # locBDE = Código da localidade no BDE e/ou 'T' para todos os municipios
        # codIBGE = Código da localidade no IBGE e/ou 'T' para todos os municipios
        # codVarBDE = Código da variável do BDE
        # anoInicial = O valor do ano inicial da variavel
        # anoFinal = O valor do ano final da variavel
        # periodo = Mostrar todas a série de dados da variavel
        # seriehistorica = Quantidade de ano dos valores da variável, sendo o ponto de partida o ultimo ano

        if (anoInicial != None) or (anoFinal != None) or periodo != None:
            ultimoAno = None

        # URL dos dados
        url = self.urls['dados']
        url = url.format(locBDE=locBDE, codIBGE=codIBGE, codVarBDE=codVarBDE, anoInicial=anoInicial, anoFinal=anoFinal,
                         ultimoAno=ultimoAno, periodo=periodo, seriehistorica=seriehistorica, auxVar=auxVar,
                         auxUnd=auxUnd,
                         auxVarFnt=auxVarFnt, auxFnt=auxFnt, auxVarNota=auxVarNota, auxNota=auxNota)

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
                # print(j)
                if j == 'anos':
                    fulldic = dict()
                    dataYear = row[j]
                    # for k in dataYear.keys():
                    count = 1
                    for k in dataYear.items():
                        new = dicData.copy()
                        new['ano'] = k[0]
                        new['valor'] = k[1]
                        fulldic[str(count)] = new
                        count += 1
                        # dicData[k] = dataYear[k]
                # elif j == 'fontes':
                #    dataFonte = list(row[j].keys())
                #    dicData[j] = dataFonte[0]

                else:
                    dicData[j] = row[j]
            for i in fulldic.values():
                listData.append(i)
        # End Time format
        data = listData
        return data
