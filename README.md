<h1 align="center"> Alura receitas API </h1>

## Instalando dependências
```
$ pipenv shell
$ pipenv install --dev
```
## Criando projeto de receitas
```
$ django-admin startproject alurareceitas .
```
## Criando app de receitas
```
$ python manage.py startapp receitas
```
## Criando usuário
```
$ python manage.py createsuperuser
```
## Criando projeto de usuários
```
$ django-admin startproject alurareceitas .
```
## Criando app de usuários
```
$ python manage.py startapp pessoas
```
## Subindo servidor
```
$ exec ./manage.py runserver localhost:8005
```
## Fazendo cópia dos arquivos estáticos
```
$ python manage.py collectstatic
```
## Criando volume e rodando imagem postgres
```
$ docker volume create pgdata
$ docker run -v pgdata:/var/lib/postgresql/data -p 8006:5432 -e POSTGRES_PASSWORD=insertyourpw postgres:10
```
## Passando informações do modelo para o banco de dados
```
$ python manage.py makemigrations
$ python manage.py migrate
```



