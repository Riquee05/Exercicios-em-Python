Plano de Estudos de Python com Exemplos de Código
Módulo 1: Fundamentos de Python (4 semanas)
Semana 1: Introdução à Programação com Python

Teoria:

O que é Python e suas aplicações.
Instalação e configuração do ambiente (Anaconda, Jupyter Notebook, VS Code).
Sintaxe básica do Python.
Tipos de dados: números, strings, listas, tuplas e dicionários.

Prática:

# Números e operações básicas
    a = 10
    b = 5
    print("Soma:", a + b)
    print("Subtração:", a - b)
    print("Multiplicação:", a * b)
    print("Divisão:", a / b)

# Strings
    nome = "João"
    print("Olá, " + nome)

# Listas
    lista = [1, 2, 3, 4, 5]
    print("Primeiro elemento:", lista[0])
    lista.append(6)
    print("Lista após adição:", lista)

# Dicionários
    pessoa = {"nome": "Maria", "idade": 30}
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])

Semana 2: Estruturas de Controle

Teoria:

Condicionais (if, elif, else).
Laços de repetição (for, while).

Prática:

# Condicionais
    idade = 20
    if idade >= 18:
    print("Você é maior de idade")
    else:
    print("Você é menor de idade")

# Laços de repetição
    for i in range(5):
    print("Número:", i)

    contador = 0
    while contador < 5:
    print("Contador:", contador)
    contador += 1

Semana 3: Funções e Módulos

Teoria:

Definição e chamada de funções.
Argumentos e parâmetros.
Módulos e pacotes.

Prática:

# Funções
    def saudacao(nome):
    return "Olá, " + nome

    print(saudacao("Carlos"))

# Módulos
    import math
    print("Raiz quadrada de 16:", math.sqrt(16))

Semana 4: Manipulação de Arquivos

Teoria:

Leitura e escrita de arquivos.
Manipulação de arquivos CSV.

Prática:

# Leitura de arquivos
    with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Escrita em arquivos
    with open('saida.txt', 'w') as arquivo:
    arquivo.write("Este é um arquivo de exemplo.")

# Manipulação de arquivos CSV
    import csv
    with open('dados.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)

Módulo 2: Programação Orientada a Objetos (4 semanas)
Semana 1: Introdução à POO

Teoria:

Conceitos básicos: classes e objetos.
Atributos e métodos.

Prática:

# Definição de classe
    class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Instanciação de objetos
    pessoa1 = Pessoa("Alice", 25)
    print(pessoa1.saudacao())

Semana 2: Herança e Polimorfismo

Teoria:

Herança: classes pai e filho.
Sobrescrita de métodos.
Polimorfismo.

Prática:

# Herança
    class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        pass

    class Cachorro(Animal):
    def fazer_som(self):
        return "Au au"

    class Gato(Animal):
    def fazer_som(self):
        return "Miau"

# Polimorfismo
    animais = [Cachorro("Rex"), Gato("Mimi")]
    for animal in animais:
    print(f"{animal.nome}: {animal.fazer_som()}")

Semana 3: Encapsulamento e Abstração

Teoria:

Encapsulamento: público, privado e protegido.
Abstração.

Prática:

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")
    
    def consultar_saldo(self):
        return self.__saldo

    conta = ContaBancaria("João", 1000)
    conta.depositar(500)
    print("Saldo:", conta.consultar_saldo())
    conta.sacar(200)
    print("Saldo:", conta.consultar_saldo())

Semana 4: Tratamento de Exceções

Teoria:

Introdução a exceções.
Try, except, finally.
Criação de exceções personalizadas.

Prática:

# Tratamento de exceções
    try:
    resultado = 10 / 0
    except ZeroDivisionError:
    print("Erro: Divisão por zero")
    finally:
    print("Execução finalizada")

# Exceção personalizada
    class SaldoInsuficienteError(Exception):
    pass

    def sacar(valor, saldo):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente")
    return saldo - valor

    try:
    novo_saldo = sacar(1000, 500)
    except SaldoInsuficienteError as e:
    print(e)

Módulo 3: Bibliotecas e Ferramentas Essenciais (4 semanas)
Semana 1: Numpy e Pandas

Teoria:

Introdução ao Numpy.
Introdução ao Pandas.

Prática:

    import numpy as np

# Operações com Numpy
    arr = np.array([1, 2, 3, 4, 5])
    print("Array:", arr)
    print("Soma:", np.sum(arr))
    print("Média:", np.mean(arr))

    import pandas as pd

# Operações com Pandas
    dados = {'Nome': ['Ana', 'Pedro', 'Maria'], 'Idade': [28, 22, 32]}
    df = pd.DataFrame(dados)
    print(df)
    print("Idade média:", df['Idade'].mean())

Semana 2: Matplotlib e Seaborn

Teoria:

Introdução ao Matplotlib.
Introdução ao Seaborn.

Prática:

import matplotlib.pyplot as plt

# Gráficos com Matplotlib
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfico de X vs Y')
    plt.show()

    import seaborn as sns

# Gráficos com Seaborn
    sns.set(style="darkgrid")
    dados = sns.load_dataset("iris")
    sns.pairplot(dados, hue="species")
    plt.show()

Semana 3: Requests e BeautifulSoup

Teoria:

Introdução ao Requests.
Introdução ao BeautifulSoup.

Prática:

    import requests
    from bs4 import BeautifulSoup

# Requisições HTTP
    resposta = requests.get('https://www.example.com')
    print("Status:", resposta.status_code)
    print("Conteúdo:", resposta.text)

# Web scraping com BeautifulSoup
    html_doc = resposta.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.title.string)

Semana 4: Selenium e Scrapy

Teoria:

Introdução ao Selenium.
Introdução ao Scrapy.

Prática:

    from selenium import webdriver

# Automação de navegador com Selenium
    driver = webdriver.Chrome()
    driver.get('https://www.example.com')
    titulo = driver.title
    print("Título da página:", titulo)
    driver.quit()

Módulo 4: Desenvolvimento Web com Django e Flask (4 semanas)
Semana 1: Introdução ao Flask

Teoria:

Conceitos básicos do Flask.
Estrutura de um projeto Flask.

Prática:

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def home():
    return "Olá, Flask!"

    if __name__ == '__main__':
    app.run(debug=True)

Semana 2: Introdução ao Django

Teoria:

Conceitos básicos do Django.
Estrutura de um projeto Django.

Prática:

    bash

# Criação de um projeto Django
    django-admin startproject meu_projeto
    cd meu_projeto
    anage.py startapp minha_app

# Exemplo de view no Django
# Em minha_app/views.py
    from django.http import HttpResponse

    def home(request):
    return HttpResponse("Olá, Django!")

# Configuração de URL
# Em meu_projeto/urls.py
    from django.contrib import admin
    from django.urls import path
    from minha_app import views

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    ]

Semana 3: Banco de Dados com Django

Teoria:

Modelos do Django.
ORM (Object-Relational Mapping).

Prática:

# Definição de modelos
# Em minha_app/models.py
    from django.db import models

    class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

# Migrar o banco de dados
    anage.py makemigrations
    anage.py migrate

# Interação com o banco de dados
# Em um shell Django
    anage.py shell

    from minha_app.models import Pessoa
    p1 = Pessoa(nome='Ana', idade=28)
    p1.save()
    print(Pessoa.objects.all())

Semana 4: Autenticação e Autorização com Django

Teoria:

Sistema de autenticação do Django.
Gerenciamento de usuários e permissões.

Prática:

# Configuração de URLs de autenticação
# Em meu_projeto/urls.py
    from django.urls import include

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('accounts/', include('django.contrib.auth.urls')),
    ]

# Criação de uma view protegida
# Em minha_app/views.py
    from django.contrib.auth.decorators import login_required

    @login_required
    def painel(request):
    return HttpResponse("Bem-vindo ao painel!")

Módulo 5: Tópicos Avançados (4 semanas)
Semana 1: Programação Assíncrona

Teoria:

Conceitos de programação assíncrona.
Uso de async e await.

Prática:

    import asyncio

    async def dizer_ola():
    print("Olá")
    await asyncio.sleep(1)
    print("Mundo!")

# Executando a função assíncrona
    asyncio.run(dizer_ola())

Semana 2: Testes Automatizados

Teoria:

Introdução ao unittest e pytest.
Testes unitários e de integração.

Prática:

    import unittest

# Função a ser testada
    def soma(a, b):
    return a + b

# Testes unitários
    class TestSoma(unittest.TestCase):
    def test_soma_positiva(self):
        self.assertEqual(soma(1, 2), 3)
    
    def test_soma_negativa(self):
        self.assertEqual(soma(-1, -2), -3)

    if __name__ == '__main__':
    unittest.main()

Semana 3: Processamento de Dados com PySpark

Teoria:

Introdução ao PySpark.
Conceitos básicos de processamento distribuído.

Prática:

    from pyspark.sql import SparkSession

# Inicializando Spark
    spark = SparkSession.builder.appName("ExemploPySpark").getOrCreate()

# Criação de um DataFrame
    dados = [("Ana", 28), ("Pedro", 22), ("Maria", 32)]
    colunas = ["Nome", "Idade"]
    df = spark.createDataFrame(dados, colunas)

# Operações com DataFrame
    df.show()
    df.filter(df["Idade"] > 25).show()

    Semana 4: Machine Learning com Scikit-Learn

    Teoria:

    Introdução ao Machine Learning.
    Algoritmos básicos de Machine Learning.

Prática:

    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score

# Carregando o dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

# Dividindo os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando o modelo
    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)

# Fazendo previsões
    y_pred = modelo.predict(X_test)

# Avaliando o modelo
    acuracia = accuracy_score(y_test, y_pred)
    print("Acurácia:", acuracia)

    Projetos Práticos
    Projeto 1: Aplicação Web Completa (4 semanas)

    Objetivo: Desenvolver uma aplicação web completa utilizando Django, incluindo sistema de autenticação, banco de dados e interface de usuário.

Passos:

    Planejamento do projeto.
    Desenvolvimento do backend com Django.
    Implementação do frontend com HTML, CSS e JavaScript.
    Testes e deploy.

Projeto 2: Análise de Dados (4 semanas)

Objetivo: Realizar uma análise completa de um conjunto de dados, utilizando Pandas, Numpy, Matplotlib e Seaborn.

Passos:

    Escolha do dataset.
    Limpeza e preparação dos dados.
    Análise exploratória e visualização.
    Conclusões e apresentação dos resultados.

Projeto 3: Automação com Selenium (4 semanas)

Objetivo: Criar um bot para automatizar tarefas na web utilizando Selenium.

Passos:

    Definição das tarefas a serem automatizadas.
    Desenvolvimento do bot com Selenium.
    Testes e melhorias.

Projeto 4: Sistema de Recomendação (4 semanas)

Objetivo: Implementar um sistema de recomendação utilizando técnicas de Machine Learning.

Passos:

    Escolha do tipo de sistema de recomendação (baseado em conteúdo ou colaborativo).
    Implementação do modelo de recomendação com Scikit-Learn.
    Avaliação e melhorias do modelo.

Este plano de estudos oferece uma abordagem prática e detalhada para aprender Python desde o nível iniciante até o avançado, com exemplos de código para facilitar a compreensão e aplicação dos conceitos. Boa sorte nos seus estudos!