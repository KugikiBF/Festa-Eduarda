# 🎉 Convite de Aniversário Digital (Full Stack)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-07405e?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

> Um sistema de RSVP (Respondez S'il Vous Plaît) personalizado, desenvolvido para gerenciar a lista de convidados de um evento real.

---

## 📖 Sobre o Projeto

A ideia desse projeto nasceu de uma necessidade real: criar uma forma única e interativa de convidar os amigos para o aniversário da minha namorada. Eu queria fugir dos formulários genéricos e listas de papel.

Este é meu **primeiro projeto Full Stack**, onde apliquei conhecimentos de Back-end (Python/Flask) integrados a um Front-end responsivo, com persistência de dados em banco relacional.

## 🚀 Funcionalidades

* **Confirmação de Presença:** Interface amigável para o convidado inserir nome, confirmação (Sim/Não) e quantidade de acompanhantes.
* **Validação de Dados (Back-end):**
    * Correção automática de formatação de nomes (Capitalize/Strip).
    * Verificação se o nome contém apenas letras.
    * Limite de acompanhantes (Regra de negócio: máx. 5 pessoas) para evitar superlotação.
    * Prevenção de duplicatas (checa se o convidado já confirmou).
* **Painel Administrativo:** Rota segura (`/lista`) para visualizar todos os convidados confirmados em tempo real.
* **Feedback Visual:** Mensagens de sucesso ou erro renderizadas dinamicamente via Jinja2.

## 🛠️ Tecnologias Utilizadas

* **Back-end:** Python 3, Flask.
* **Banco de Dados:** SQLite3 (Nativo do Python, sem necessidade de servidor externo).
* **Front-end:** HTML5, CSS3 (Design Responsivo), Jinja2 (Template Engine).
* **Bibliotecas:** `Werkzeug`, `Click`, `Jinja2` (via requirements.txt).

## 🧩 Arquitetura e Código

O projeto segue boas práticas de programação, incluindo **Orientação a Objetos**:

* **Classe `Convidado`:** Centraliza a lógica de negócios. Métodos como `processar_resposta()`, `checar_lista()` e `salvar_no_banco()` garantem que o controlador (rotas do Flask) fique limpo e organizado.
* **Tratamento de Erros:** Blocos `try/except` robustos para garantir que entradas inválidas (como letras no campo de quantidade) não quebrem a aplicação.

## 📸 Screenshots

*(Você pode adicionar prints da tela inicial e da tela de lista aqui)*

## 📦 Como Rodar o Projeto

Pré-requisitos: Python 3 instalado.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/KugikiBF/NOME-DO-SEU-REPO.git](https://github.com/KugikiBF/NOME-DO-SEU-REPO.git)
    cd NOME-DO-SEU-REPO
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute a aplicação:**
    ```bash
    python app.py
    ```
    *O banco de dados `festa.db` será criado automaticamente na primeira execução.*

4.  **Acesse no navegador:**
    * Convite: `http://127.0.0.1:5000`
    * Lista de Presença: `http://127.0.0.1:5000/lista`

---

## 👨‍💻 Autor

**Bruno Felipe Mafra Lacerda**

* 💼 [LinkedIn](https://www.linkedin.com/in/bruno-felipe-7956bb351/)
* 🐙 [GitHub](https://github.com/KugikiBF)

---
*Desenvolvido com 💙 e muito café.*

