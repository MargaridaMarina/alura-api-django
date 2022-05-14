<h1 align="center"> Alura receitas API </h1>

## Instalando dependências
```
$ pipenv shell
$ pipenv install --dev
```
## Criando projeto
```
$ django-admin startproject alurareceitas .
```
## Criando app
```
$ python manage.py startapp receitas
```
## Subindo servidor
```
$ python manage.py runserver
```
## Fazendo cópia dos arquivos estáticos
```
$ python manage.py collectstatic
```
## Subindo imagem postgres
```
$ docker run -p 5432:5432 -e POSTGRES_PASSWORD=insertyourpasswordhere postgres:10
```
## Criando usuário
```
$ python manage.py createsuperuser
```



