# API Rest do Desafio Mobile Developer - Agriness

Projeto desenvolvido como requisito para o Desafio Mobile Developer - Agriness,
que disponibiliza uma API Rest que lista os animais de uma granja.

## Rodando o projeto

\
Após clonar este repositório e criar uma virtualenv, instale as dependências

`pip install -r requirements.txt`
    
Crie um novo banco de dados PostgreSQL com nome `granja` e execute o migrate

`python manage.py migrate`

Caso deseje criar novos objetos, crie o superuser para acessar a administração (http://localhost:8000/admin)

`python manage.py createsuperuser`

Execute o projeto

`python manage.py runserver`


## Documentação

A documentação das APIs do projeto está disponível em http://localhost:8000/docs
