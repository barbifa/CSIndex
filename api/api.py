from flask import Flask
from flask import make_response
import StringIO
import csv
import StringIO
from flask import request
import sys
import os

app = Flask(__name__, template_folder='templates')

#1. Numero de publicacoes em uma determinada conferencia de uma area
@app.route('/nPubConferenciasDeUmaArea/<string:conferencia>/<string:area>')
def nPubConferenciasDeUmaArea(conferencia, area):
    filename = "../data/"+ area + "-out-confs.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data :
            if(row[0] == conferencia):
                #return str(row[1])
                DATA.append(row)

    with open('Resultado_nPub_'+conferencia+'_'+area+'.csv', 'w') as csvfile:

        header = ['Conferencia da area ' + area, 'Quantidade de publicacoes']
        writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames= header)
        writer.writeheader()

        for row in DATA:
            writer.writerow({'Conferencia da area ' + area: row[0], 'Quantidade de publicacoes': row[1]})

    return 'Arquivo salvo!'

#questao 2
@app.route('/numeroPubliNoConjuntoDeConferenciasDeUmaArea/<area>')
def numeroPubliNoConjuntoDeConferenciasDeUmaArea(area):
	nPublicacoes = 0
	filename = "../data/"+ area + "-out-papers.csv"
	with open(filename, 'r') as file:
		data = csv.DictReader(file, delimiter=';', quotechar='|')
		for row in data :
			nPublicacoes = nPublicacoes + 1

	si = StringIO.StringIO()
	cw = csv.writer(si)
	cw.writerow([str(nPublicacoes)])
	output = make_response(si.getvalue())
	output.headers["Content-Disposition"] = "attachment; filename=Q2numeroPubliNoConjuntoDeConferenciasDeUmaArea.csv"
	output.headers["Content-type"] = "text/csv"
	return output


#3. Scores de todos os departamentos em uma area
@app.route('/scoresDepartamentosDaArea/<string:area>')
def scoresDepartamentosDaArea(area):
    filename = "../data/"+ area + "-out-scores.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data :
            DATA.append(row)

    with open('scoresDepartamentos_'+area+'.csv', 'w') as csvfile:

        header = ['Departamento da area ' + area, 'Score']
        writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames= header)
        writer.writeheader()

        for row in DATA:
            writer.writerow({'Departamento da area ' + area: row[0], 'Score': row[1]})

    return 'Arquivo salvo!'

#questao 4
@app.route('/scoreDeUmDepartamentoEmUmaArea/<departamento>/<area>')
def scoreDeUmDepartamentoEmUmaArea(departamento, area):
    filename = "../data/"+ area + "-out-scores.csv"
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data :
            if(row[0] == departamento):
				si = StringIO.StringIO()
				cw = csv.writer(si)
				cw.writerow([str(row[1])])
				output = make_response(si.getvalue())
				output.headers["Content-Disposition"] = "attachment; filename=Q4scoreDeUmDepartamentoEmUmaArea.csv"
				output.headers["Content-type"] = "text/csv"
				return output


#5. Numero de professores que publicam em uma determinada area (organizados por departamentos)
@app.route('/nProfessoresArea/<string:area>')
def nProfessoresArea(area):
    filename = "../data/"+ area + "-out-profs.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data :
            DATA.append(row)

    with open('nProfessoresArea'+area+'.csv', 'w') as csvfile:

        header = ['Departamento da area ' + area, 'Numero de professores']
        writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames= header)
        writer.writeheader()

        for row in DATA:
            writer.writerow({'Departamento da area ' + area: row[0], 'Numero de professores': row[1]})

    return 'Arquivo salvo!'

#questao 6
@app.route('/numeroDeProfessoresDeUmDepartamentoQuePublicaramEmUmaArea/<departamento>/<area>')
def numeroDeProfessoresDeUmDepartamentoQuePublicaramEmUmaArea(departamento,area):
    filename = "../data/"+ area + "-out-profs.csv"
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data :
            if(row[0] == departamento):
				si = StringIO.StringIO()
				cw = csv.writer(si)
				cw.writerow([str(row[1])])
				output = make_response(si.getvalue())
				output.headers["Content-Disposition"] = "attachment; filename=Q6numeroDeProfessoresDeUmDepartamentoQuePublicaramEmUmaArea.csv"
				output.headers["Content-type"] = "text/csv"
				return output

#7. Todos os papers de uma area (ano, titulo, deptos e autores)
@app.route('/papersArea/<string:area>')
def papersArea( area):
    filename = "../data/"+ area + "-out-papers.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data :
            DATA.append(row)

    with open('papers_'+area+'.csv', 'w') as csvfile:

        header = ['Ano', 'Titulo', 'Departamento', 'Autores']
        writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames= header)
        writer.writeheader()

        for row in DATA:
            writer.writerow({'Ano': row[0], 'Titulo': row[2], 'Departamento':row[3], 'Autores':row[4]})

    return 'Arquivo salvo!'	
	
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
	output.headers["Content-Disposition"] = "attachment; filename=Q8PapersDeUmaAreaEmUmDeterminadoAno.csv"
	output.headers["Content-type"] = "text/csv"

    return output

#9. Todos os papers de um departamento em uma area
@app.route('/papersDepartamentoArea/<string:departamento>/<string:area>')
def papersDepartamentoArea(departamento, area):
    filename = "../data/"+ area + "-out-papers.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data :
            if(row[1] == departamento):
                DATA.append(row)

    with open('papers_'+departamento+'_'+area+'.csv', 'w') as csvfile:

        header = ['Departamento da area ' + area, 'Paper']
        writer = csv.DictWriter(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames= header)
        writer.writeheader()

        for row in DATA:
            writer.writerow({'Departamento da area ' + area: row[1], 'Paper': row[2]})

    return 'Arquivo salvo!'

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
	output.headers["Content-Disposition"] = "attachment; filename=Q10TodosOsPapersDeUmProfessor.csv"
	output.headers["Content-type"] = "text/csv"
    return output






if __name__ == '__main__':		
	app.run(debug=True)
