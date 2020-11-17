# API Rest do Desafio Mobile Developer - Agriness

Projeto desenvolvido como requisito para o Desafio Mobile Developer - Agriness,
que disponibiliza uma API Rest que lista os animais de uma granja para ser consumido no app [agriness-granja-app](https://github.com/tyagogoulart/agriness-granja-app).


## Configurando o projeto

Após clonar este repositório e criar e ativar uma virtualenv, entre na pasta `granja-api` e execute o comando para instalar as dependências:

`pip install -r requirements.txt`
    
Crie um novo banco de dados PostgreSQL com nome `granjas` e execute o migrate (pode ser preciso modificar o DATABASES no settings.py):

`python manage.py migrate`

### Dados

Para facilitar a inicialização do projeto, é possível iniciá-lo com as fixtures (recomendado), executando o comando abaixo:

`python manage.py loaddata granja/data/dados_completos.json`

Os usuários do fixtures são:

Responsável das granjas 1 e 2

`login: tyagogoulartn@gmail.com senha: admin123`

Responsável da granja 3

`login: teste@email.com senha: 123`


Ou caso prefira, você pode criar manualmente os dados, para isso crie o superuser para acessar a administração (http://localhost:8000/admin)

`python manage.py createsuperuser`

Mesmo que tenha optado por criar manualmente os dados, também é possível realizar uma carga dos dados dos animais, assim tendo melhor visibilidade sobre os dados, tanto no app como na api, para questões de paginação etc. Para isso, navegue até a pasta `granja/data` e execute o comando:

`python script_carregar_animais.py`

Modificações necessárias: antes de executar, será necessário modificar as configurações de `PATH` e `VIRTUALENV`, nas linhas 6 e 7 do arquivo `script_carregar_animais.py`.

Execute o projeto

`python manage.py runserver SEU_IP:8000`

Modificações necessárias: Como estaremos rodando o `agriness-granja-app` em um ambiente virtual android/ios, será necessário informar o IP local da sua máquina na hora da inicialização do projeto. Por exemplo: `python manage.py runserver 10.0.0.101:8000` e este mesmo IP deverá ser configurado no app conforme o readme do `agriness-granja-app` descreve.


## Documentação

A documentação das APIs do projeto está disponível em http://localhost:8000/docs

## Testando

Um arquivo com a collection das consultas à API no Postman está disponível na pasta `postman`. Importe-o no postman para ter as consultas pré-configuradas para teste.

Será necessário sempre utilizar a Autenticação JWT para obter o token access e reutilizar nas demais consultas, passando-o através do header Authorization, no formato: `Bearer {token}`

### Testes unitários

O projeto conta com testes unitários e para rodá-los, execute:

`python manage.py test`
