import sqlite3

class Convidado:
    lista_convidados=[]
    def __init__(self,nome,resposta,quantidade=0):
        self.nome=nome
        self.quantidade= quantidade
        self.resposta = resposta

    def checar_lista(self):
        conn= sqlite3.connect('festa.db')
        cursor= conn.cursor()
        cursor.execute("SELECT nome FROM convidados WHERE nome = ?",(self.nome,))
        resultado= cursor.fetchone()
        conn.close()
        if resultado:
            return True
        else:
            return False
        
    def salvar_no_banco(self):
        conn= sqlite3.connect('festa.db')
        cursor=conn.cursor()
        cursor.execute('INSERT INTO convidados VALUES(?, ?, ?)',
                       (self.nome,self.resposta,self.quantidade))

        conn.commit()
        conn.close()

    def processar_resposta(self):
        
        self.nome = self.nome.capitalize().strip()
        self.resposta = self.resposta.upper().strip()
        nome_correcao = self.nome.replace(" ","")
        if not nome_correcao.isalpha():
            
            return 'ERRO: Seu nome está errado, tente novamente.', True
        try:
            self.quantidade_total=int(self.quantidade)
            if self.quantidade_total<=0 or self.quantidade_total>5:
                
                return 'ERRO: Capacidade de acompanhantes excedida.', True
        except ValueError:
            
            return 'Voltar', False
        if self.resposta == 'SIM':
            if self.checar_lista():
                
                return 'Voce já está confirmado', True
                    
            self.confirmado = True
            self.salvar_no_banco()
            return f"Oba! {self.nome} confirmou presença com {self.quantidade-1} acompanhantes.", False
        else:
            self.confirmado = False
            self.salvar_no_banco()
            return "Que pena! Fica para a próxima.", False
            
        

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
    quantidade_site = int (quantidade_site)
    pessoa = Convidado(nome_site,reposta_site,quantidade_site)
    mensagem_recebida,houve_erro= pessoa.processar_resposta()
    return render_template('index.html', mensagem_na_tela=mensagem_recebida,
                           erro=houve_erro)


@app.route('/lista')
def ver_lista():
    conexao= sqlite3.connect('festa.db')
    cursor= conexao.cursor()
    cursor.execute("SELECT * FROM convidados")
    pessoas = cursor.fetchall()
    conexao.close()
    return render_template ('lista.html', lista_pessoas=pessoas)

def criar_tabela_no_inicio():
    conn = sqlite3.connect('festa.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS convidados (
            nome TEXT,
            resposta TEXT,
            quantidade INTEGER
        )
    ''')
    conn.commit()
    conn.close()

if __name__=='__main__':
    criar_tabela_no_inicio()
    app.run(debug=True)

    