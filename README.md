# 📒 Bloco de Notas

Aplicação web de bloco de notas organizado por **centrais**. Cada central é acessada por um código único e contém suas próprias notas.

---

## ✨ Funcionalidades

- Criar ou acessar uma central pelo código
- Criar, editar e deletar notas
- Cada central nova já vem com uma nota de boas-vindas
- Notas ordenadas da mais recente para a mais antiga

---

## 🛠️ Tecnologias

- [Python](https://www.python.org/) + [Flask](https://flask.palletsprojects.com/)
- [MySQL](https://www.mysql.com/)
- [Tailwind CSS](https://tailwindcss.com/)

---

## 🚀 Como rodar localmente

```bash
# 1. Clone o repositório
git clone https://github.com/kersilva/desafio4.git

# 2. Acesse o diretório
cd desafio4

# 3. Crie um ambiente virtual
python -m venv venv

# 4. Instale as dependências
# No Windows:
.\venv\Scripts\pip install -r requirements.txt
# No Linux/Mac:
./venv/bin/pip install -r requirements.txt

# 5. Crie o banco de dados
# No Windows:
.\venv\Scripts\python -c "import setup"
# No Linux/Mac:
mysql -u root -p < setup.sql

# 6. Execute a aplicação
# No Windows:
.\venv\Scripts\python src/app.py
# No Linux/Mac:
./venv/bin/python src/app.py
```

Acesse em `http://localhost:5000`