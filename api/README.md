# REST API CSIndex
# Requisitos
  - Flask 1.0.2 ou superior instalado
  - Python 2.7.12 ou superior instalado
 
# Executando
- Faca Download do Repositorio 
- Em CSIndex/api/ execute o seguinte command para iniciar o servidor
```sh
$ python api.py
```
ou 
```sh
$ FLASK_APP=teste.py flask run
```

# GET questoes
1. Número de publicações em uma determinada conferência de uma área <br />
    http://localhost:5000/nPubConferenciasDeUmaArea/#conferencia/#area <br />

    #conferencia: qualquer abreviacao das conferências
    #area: pode ser qualquer abreviacao das areas em CSIndex/data

2. Número de publicações no conjunto de conferências de uma área<br />
    http://localhost:5000/numeroPubliNoConjuntoDeConferenciasDeUmaArea/#area<br />

    #area: pode ser qualquer abreviacao  das areas em CSIndex/data
    
3. Scores de todos os departamentos em uma área<br />
    http://localhost:5000/scoresDepartamentosDaArea/#area <br />

    #area: pode ser qualquer abreviacao das areas em CSIndex/data

4. Score de um determinado departamento em uma área.<br />
    http://localhost:5000/scoreDeUmDepartamentoEmUmaArea/#departamento/#area

    #departamento: Qualquer abreviacao das universidades do CSIndex<br />
    #area: pode ser qualquer abreviacao  das areas em CSIndex/data

5. Número de professores que publicam em uma determinada área (organizados por departamentos)<br />
    http://localhost:5000/nProfessoresArea/#area <br />

    #area: pode ser qualquer abreviacao das areas em CSIndex/data
    
6. Número de professores de um determinado departamento que publicam em uma área<br />
    http://localhost:5000/numeroDeProfessoresDeUmDepartamentoQuePublicaramEmUmaArea/#departamento/#area<br />

    #departamento: Qualquer abreviacao das universidades do CSIndex<br />
    #area: pode ser qualquer abreviacao  das areas em CSIndex/data

7. Todos os papers de uma área (ano, título, deptos e autores)<br />
    http://localhost:5000/papersArea/#area <br />

    #area: pode ser qualquer abreviacao das areas em CSIndex/data

8. Todos os papers de uma área em um determinado ano<br />
    http://localhost:5000/PapersDeUmaAreaEmUmDeterminadoAno/#ano/#area<br />

    #area:  abreviacao  das areas em CSIndex/data<br />
    #ano: Ano da publicacao

9. Todos os papers de um departamento em uma área<br />
    http://localhost:5000/papersDepartamentoArea/#departamento/#area <br />

    #departamento: qualquer abreviacao das universidades do CSIndex
    #area: pode ser qualquer abreviacao das areas em CSIndex/data

10. Todos os papers de um professor (dado o seu nome)<br />
    http://localhost:5000/TodosOsPapersDeUmProfessor/#snomeProfessor<br />

     #nomeProfessor: Nome valido de professor






