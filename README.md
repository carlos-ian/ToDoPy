# ToDoPy - Gerenciador de Tarefas

O **ToDoPy** é uma aplicação full-stack de gerenciamento de tarefas que utiliza uma interface estilo Kanban para organizar a produtividade. O projeto conta com um backend em Python/FastAPI e um frontend moderno com gradientes dinâmicos e filtros em tempo real. Ademais, o objetivo desse projeto/repositório é consolidar e praticar fundamentos como autenticação, autorização e CRUD utilizando FastAPI.

## 🚀 Funcionalidades

* **Autenticação JWT e Autorização:** Proteção de rotas para que cada usuário veja apenas suas tarefas.
* **Quadro Kanban:** Quadro com três colunas interativas (To Do, In Progress, Done) que permitem visualizar todas tarefas do usuário autenticado.
* **Filtros Inteligentes:** Filtragem de tarefas por categoria, nível de importância e data.
* **CRUD Completo:** Criação, leitura, atualização de status e exclusão de tarefas.

## 🛠️ Tecnologias Utilizadas

### Backend
* **Python 3.14.2**
* **FastAPI:** Framework web de alta performance.
* **SQLAlchemy:** ORM para manipulação do banco de dados.
* **PostgreSQL:** Banco de dados relacional para armazenamento de dados.

### Frontend
* **HTML & CSS:** Uso de Grid, Flexbox, variáveis customizadas e telas do frontend.
* **JavaScript:** Manipulação de DOM e Fetch API para integração assíncrona.
* **FontAwesome:** Ícones para melhor experiência visual.

## 🔧 Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/todopy.git](https://github.com/seu-usuario/todopy.git)
   cd todopy

2. **Configure o Ambiente Virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

4. **Inicialize e Rode o servidor:**
   ```bash
   uvicorn main:app --reload

4. **Execute o Frontend:**
   No VS Code, instale a extensão Live Server, clique com o botão direito em Templates/login.html e selecione "Open with Live Server".

   Utilizando Python, executa o comando abaixo na raiz da pasta /Templates e depois acesse http://localhost:8080/login.html no seu navegador.
   ```bash
   python -m http.server 8080
