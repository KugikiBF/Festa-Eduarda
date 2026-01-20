import sqlite3

class Convidado:
    lista_convidados=[]
    def __init__(self,nome,resposta,quantidade=0):
        self.nome=nome
        self.quantidade= quantidade
        self.resposta = resposta

    def salvar_no_banco(self):
        conn= sqlite3.connect('festa.db')
        cursor=conn.cursor()

        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS convidados (
                       nome TEXT,
                       resposta TEXT,
                       quantidade INTEGER
            )
        ''')

        cursor.execute('INSERT INTO convidados VALUES(?, ?, ?)',
                       (self.nome,self.resposta,self.quantidade))

        conn.commit()
        conn.close()

    def processar_resposta(self):
        
        self.nome = self.nome.capitalize().strip()
        self.resposta = self.resposta.upper().strip()
        nome_correcao = self.nome.replace(" ","")
        if not nome_correcao.isalpha():
            return'''
                <h1> Erro no nome!</h1>
                <a href='/'>Corrigir</a>
            '''
        try:
            self.quantidade_total=int(self.quantidade)
            if self.quantidade_total<=0 or self.quantidade_total>6:
                return "<h1> Erro</h1> <p> <a href='/'>Voltar</a>"
        except ValueError:
            return "<h1> Erro</h1> <p> <a href='/'>Voltar</a>"
        if self.resposta == 'SIM':
            self.confirmado = True
            self.salvar_no_banco()
            return f"Oba! {self.nome} confirmou presença com {self.quantidade} acompanhantes."
        else:
            self.confirmado = False
            return "Que pena! Fica para a próxima."
        

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def mostrar_convite():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def receber_resposta():
    nome_site = request.form['campo_nome']
    reposta_site = request.form["campo_resposta"]
    quantidade_site = request.form["campo_quantidade"]


    pessoa = Convidado(nome_site,reposta_site,quantidade_site)

    resultado= pessoa.processar_resposta()
    return resultado

if __name__=='__main__':
    app.run(debug=True)

    