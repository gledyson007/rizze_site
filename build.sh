#!/bin/bash

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Rodando migrações no Neon..."
python manage.py migrate

echo "Criando superusuário..."
python manage.py createsuperuser --noinput || true

echo "Coletando arquivos estáticos (CSS/Imagens)..."
python manage.py collectstatic --noinput --clear