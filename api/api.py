from flask import Flask
from flask import make_response
import StringIO
import csv
import StringIO
from flask import request
import sys
import os
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

app = Flask(__name__, template_folder='templates')

# Function for allowing HTTP access to the server. =D vide : http://flask.pocoo.org/snippets/56/ 
def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
                attach_to_all=True, automatic_options=True):
    """Decorator function that allows crossdomain requests.
      Courtesy of
      https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
    """
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        """ Determines which methods are allowed
        """
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        """The decorator function
        """
        def wrapped_function(*args, **kwargs):
            """Caries out the actual cross domain code
            """
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

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
@app.route('/numeroPubliNoConjuntoDeConferenciasDeUmaArea/<area>',methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
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
@crossdomain(origin='*')
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
@crossdomain(origin='*')
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
@crossdomain(origin='*')
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
@crossdomain(origin='*')

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


