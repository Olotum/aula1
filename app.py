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
@app.route('/navbar')
#Esta linha é um decorador que associa uma função a um caminho URL específico.
# Neste caso, ele conecta a função hello_world ao caminho raiz do aplicativo (/).
#Quando um usuário visita a página inicial do aplicativo (geralmente http://localhost:5000/ por padrão), esta função será executada para lidar com a solicitação.
def navBar():
#Esta linha define uma função chamada hello_world.
#Esta função é responsável por gerar a resposta que será enviada de volta ao navegador da web do usuário.
    #Renderiza um modelo
    return render_template("navBar.html")
#Nesse exemplo estamos usando o <usuario> para passar dados como parametro pela rota.
@app.route('/sobre/<usuario>')
def sobre(usuario):
    return f"<h3>Sobre mim,{usuario}</h3>"

@app.route('/')
def curriculo():
    return render_template("curriculo.html")

@app.route('/chamados')

def pagina_chamados():
    chamados = [{"id": 1, "codusuario": 1, "usuarionome": "lucas",
    "deschamado": "pc lento"},{"id": 2, "codusuario": 2, "usuarionome": "matheus",
    "deschamado": "pc não ligar"}, {"id": 3, "codusuario": 3, "usuarionome": "ivone",
    "deschamado": "vscode não instala script"}]

    return render_template("tarefaChamados.html", chamados=chamados)
    
if __name__ == '__main__':
    app.run(debug=True)
#Esta linha testa se o módulo atual é o módulo principal. Se for, executa a função app.run().