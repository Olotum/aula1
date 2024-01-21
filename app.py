from cgitb import html
from flask import Flask, render_template
#Esta linha importa a classe Flask do módulo Flask.
#Esta classe é essencial para criar aplicativos web com Flask. 
# #Ela fornece a funcionalidade principal para contruir e executar servidores web.
# lidar com solicitações e renderizar respostas.
app = Flask(__name__)
#Esta linha cria uma enstacia da classe Flask e a atribui a variavel app.
# Essa instância representa seu aplicativo web.
#_name_ é uma variável especial em Python que contém o nome do módulo atual.
# É usado aqui para determinar o caminho raiz do aplicativo,
# garantindo que recursos como modelos e arquivos estáticos possam ser encontrados corretamente
@app.route('/')
#Esta linha é um decorador que associa uma função a um caminho URL específico.
# Neste caso, ele conecta a função hello_world ao caminho raiz do aplicativo (/).
#Quando um usuário visita a página inicial do aplicativo (geralmente http://localhost:5000/ por padrão), esta função será executada para lidar com a solicitação.
def hello_word():
#Esta linha define uma função chamada hello_world.
#Esta função é responsável por gerar a resposta que será enviada de volta ao navegador da web do usuário.
    return "<h2>Auça Flask11</h2>"
#Nesse exemplo estamos usando o <usuario> para passar dados como parametro pela rota.
@app.route('/sobre/<usuario>')
def sobre(usuario):
    return f"<h3>Sobre mim,{usuario}</h3>"

@app.route('/home')
def curriculo():
    #Renderiza um modelo
    return render_template("home.html")

@app.route('/curriculo')
def home():
    return render_template("curriculo.html")
#Esta linha retorna uma string HTML contendo um cabeçalho "H2"
#Com o texto "Hello World".Esta string será o conteúdo da página da web
#Que o usuário vê quando visita o URL raiz do aplicativo.
if __name__ == '__main__':
    app.run(debug=True)
#Esta linha testa se o módulo atual é o módulo principal. Se for, executa a função app.run().