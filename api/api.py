from flask import Flask
from flask import make_response
import StringIO
import csv
import StringIO
from flask import request
import sys
import os

app = Flask(__name__, template_folder='templates')

#questao 2
@app.route('/numeroPubliNoConjuntoDeConferenciasDeUmaArea/<area>')
def numeroPubliNoConjuntoDeConferenciasDeUmaArea(area):
    nPublicacoes = 0
  
    filename = "../data/"+ area + "-out-papers.csv"
    with open(filename, 'r') as file:
        data = csv.DictReader(file, delimiter=';', quotechar='|')
        for row in data :
            nPublicacoes = nPublicacoes + 1
    
   		
    return str(nPublicacoes)


#questao 4
@app.route('/scoreDeUmDepartamentoEmUmaArea/<departamento>/<area>')
def scoreDeUmDepartamentoEmUmaArea(departamento, area):
    filename = "../data/"+ area + "-out-scores.csv"
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data :
            if(row[0] == departamento):
                return str(row[1])



#questao 6
@app.route('/numeroDeProfessoresDeUmDepartamentoQuePublicaramEmUmaArea/<departamento>/<area>')
def numeroDeProfessoresDeUmDepartamentoQuePublicaramEmUmaArea(departamento,area):
    filename = "../data/"+ area + "-out-profs.csv"
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data :
            if(row[0] == departamento):
                return row[1]

#questao 8
@app.route('/PapersDeUmaAreaEmUmDeterminadoAno/<ano>/<area>')
def PapersDeUmaAreaEmUmDeterminadoAno(ano,area):
    filename = "../data/"+ area + "-out-papers.csv"
    papers = []
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data :
            if(row[0]==ano):
                papers.append(row[2])

    si = StringIO.StringIO()
    cw = csv.writer(si,quoting=csv.QUOTE_ALL)
    cw.writerow(papers)
    output = make_response(si.getvalue())

    return output


#questao 10
@app.route('/TodosOsPapersDeUmProfessor/<string:nomeProfessor>')
def TodosOsPapersDeUmProfessor(nomeProfessor):
    filename = "../data/profs/search/"+ nomeProfessor + ".csv"
    papers = []
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data :
		papers.append(row[2])


    si = StringIO.StringIO()
    cw = csv.writer(si,quoting=csv.QUOTE_ALL)
    cw.writerow(papers)
    output = make_response(si.getvalue())
    return output






if __name__ == '__main__':		
	app.run(debug=True)



