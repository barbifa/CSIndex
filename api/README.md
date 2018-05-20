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
1. Número de publicações em uma determinada conferência de uma área
2. Número de publicações no conjunto de conferências de uma área
    http://localhost:5000/numeroPubliNoConjuntoDeConferenciasDeUmaArea/<<area>>

    <<area>> pode ser qualquer abreviacao  das areas em CSIndex/data
    
3. Scores de todos os departamentos em uma área
4. Score de um determinado departamento em uma área.
    http://localhost:5000/scoreDeUmDepartamentoEmUmaArea/<departamento>/<area>

    <departamento > Qualquer abreviacao das universidades do CSIndex
    <area> pode ser qualquer abreviacao  das areas em CSIndex/data

5. Número de professores que publicam em uma determinada área (organizados por departamentos)
6. Número de professores de um determinado departamento que publicam em uma área
    http://localhost:5000/numeroDeProfessoresDeUmDepartamentoQuePublicaramEmUmaArea/<departamento>/<area>

    <departamento > Qualquer abreviacao das universidades do CSIndex
    <area> pode ser qualquer abreviacao  das areas em CSIndex/data

7. Todos os papers de uma área (ano, título, deptos e autores)
8. Todos os papers de uma área em um determinado ano
    http://localhost:5000/PapersDeUmaAreaEmUmDeterminadoAno/<ano>/<area>

    <area>  abreviacao  das areas em CSIndex/data
    <ano> Ano da publicacao

9. Todos os papers de um departamento em uma área

10. Todos os papers de um professor (dado o seu nome)
    http://localhost:5000/TodosOsPapersDeUmProfessor/<string:nomeProfessor>

     <nomeProfessor> Nome valido de professor






