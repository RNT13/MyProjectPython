# 🚀 Guia de Inicialização de um Projeto Django

Este guia mostra passo a passo como criar um novo projeto Django do zero, utilizando Git e GitHub para versionamento e controle de branches.

---

## 🧩 1. Criar o repositório no GitHub

1. Acesse o GitHub e clique em **New Repository**.
2. Dê um nome ao seu repositório (exemplo: `django_app`).
3. Marque as opções:
   - ✅ Adicionar arquivo **README.md**
   - ✅ Adicionar **.gitignore** e selecione **Python**
4. Clique em **Create repository**.

---

## 💻 2. Clonar o repositório no computador

No terminal (ou PowerShell), navegue até a pasta onde deseja salvar o projeto e execute:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Entre na pasta do projeto:

```bash
cd nome-do-repositorio
```

---

## 🐍 3. Criar o ambiente virtual Python

```bash
python -m venv env
```

---

## ⚙️ 4. Ativar o ambiente virtual

- **Windows:**
  ```bash
  .\env\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source env/bin/activate
  ```

---

## 🌱 5. Criar uma nova branch de configuração inicial

```bash
git checkout -b project-setup
```

---

## 📦 6. Instalar o Django

```bash
pip install Django
```

Confirme a instalação:

```bash
django-admin --version
```

---

## 🧱 7. Criar o projeto Django

```bash
django-admin startproject core .
```

O ponto final (`.`) garante que o projeto seja criado na raiz da pasta atual.

---

## 🧪 8. Testar o servidor

```bash
python manage.py runserver
```

Acesse no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📋 9. Criar o arquivo requirements.txt

```bash
pip freeze > requirements.txt
```

---

## 🗃️ 10. Adicionar e commitar os arquivos

```bash
git add .
git commit -m "Configuração inicial do projeto Django"
```

---

## ☁️ 11. Enviar a branch para o GitHub

```bash
git push -u origin project-setup
```

---

## 🔄 12. Criar o Pull Request

1. Vá até o repositório no GitHub.
2. Você verá uma mensagem sugerindo o **Pull Request** da branch `project-setup`.
3. Clique em **Compare & pull request**.
4. Revise as alterações e clique em **Create pull request**.

---

## ✅ 13. Mesclar a branch no GitHub

Após revisar:

1. Clique em **Merge pull request**.
2. Depois em **Confirm merge**.
3. (Opcional) Exclua a branch `project-setup` no GitHub.

---

## 🔄 14. Atualizar o repositório local após o merge

De volta ao terminal:

```bash
git checkout main
git pull origin main
```

---

## 🧰 15. (Opcional) Criar um app dentro do projeto

```bash
python manage.py startapp nome_do_app
```

---

Feito! 🎉  
Seu projeto Django está configurado, versionado no GitHub e pronto para receber novas funcionalidades.

---

📘 **Autor:** _Renato Minoita_  
💻 **Tecnologia:** Django + Git + GitHub  
📅 **Atualizado:** Outubro de 2025
