# API Academia Crossfit — FastAPI Assíncrona

## 📌 Sobre
Essa API permite criar e consultar:
✔ categorias  
✔ centros de treinamento  
✔ atletas  

Feita com FastAPI e banco assíncrono.  

## �� Rodando com Docker
```bash
docker-compose up -d
```

## 🐍 Instalando dependências
```bash
pip install -r requirements.txt
```

## 📌 Rodar API
```bash
uvicorn app.main:app --reload
```

## 📍 Documentação
Acesse: http://localhost:8000/docs

## 💾 Banco
PostgreSQL com asyncpg.

## 🧠 Como subir no GitHub
```bash
git init
git add .
git commit -m "API pronta"
git remote add origin https://github.com/SEU-USER/api-academia-crossfit.git
git push -u origin main
```
