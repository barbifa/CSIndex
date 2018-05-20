#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Barbara
#
# Created:     20/05/2018
# Copyright:   (c) Barbara 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv
import sys
import os
#questao 2
def numeroPubliNoConjuntoDeConferenciasDeUmaArea(area):
    nPublicacoes = 0
    filename = "./data/"+ area + "-out-papers.csv"
    with open(filename, 'r') as file:
        data = csv.DictReader(file, delimiter=';', quotechar='|')
        for row in data :
            nPublicacoes = nPublicacoes + 1

    return nPublicacoes


#questao 4
def scoreDeUmDepartamentoEmUmaArea(departamento, area):
    filename = "./data/"+ area + "-out-scores.csv"
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data :
            if(row[0] == departamento):
                return row[1]



#questao 6
def numeroDeProfessoresDeUmDepartamentoQuePublicaramEmUmaArea(departamento,area):
    filename = "./data/"+ area + "-out-profs.csv"
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data :
            if(row[0] == departamento):
                return row[1]

#questao 8

def PapersDeUmaAreaEmUmDeterminadoAno(ano,area):
    filename = "./data/"+ area + "-out-papers.csv"
    papers = []
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data :
            if(row[0]==ano):
                papers.append(row[2])

    return papers

#questao 10

def TodosOsPapersDeUmProfessor(nomeProfessor):
    folder = "./data/profs/"
    papers = []
    for item in os.listdir(folder):
        if nomeProfessor in item:
            with open(folder + item, 'r') as file:
                data = csv.reader(file)
                for row in data:
                    papers.append(row[2])
    return papers







def main():
    #print(numeroPubliNoConjuntoDeConferenciasDeUmaArea("arch"))
    #print(scoreDeUmDepartamentoEmUmaArea("UFMG", "chi"))
    #print(numeroDeProfessoresDeUmDepartamentoQuePublicaramEmUmaArea("PUC-RJ","ai"))
    #print(PapersDeUmaAreaEmUmDeterminadoAno("2014","arch"))
    print(TodosOsPapersDeUmProfessor("Rodrygo-Santos"))
    pass

if __name__ == '__main__':
    main()
