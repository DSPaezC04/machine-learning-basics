# 🧠 Comandos más usados en Git Bash

## 📁 Navegación
- pwd → Muestra la ruta actual
- ls → Lista archivos
- ls -la → Lista todo (incluye ocultos)
- cd carpeta → Entrar a carpeta
- cd .. → Subir nivel
- cd ~ → Ir al home

## 📂 Archivos y carpetas
- mkdir nombre → Crear carpeta
- touch archivo.txt → Crear archivo
- rm archivo.txt → Eliminar archivo
- rm -r carpeta → Eliminar carpeta
- cp archivo destino → Copiar
- mv archivo destino → Mover/Renombrar

## ⚙️ Configuración Git
- git config --global user.name "TuNombre"
- git config --global user.email "correo@email.com"
- git config --list

## 📦 Repositorios
- git init → Crear repo
- git clone URL → Clonar repo

## 🔍 Estado
- git status → Estado actual
- git add archivo → Añadir archivo
- git add . → Añadir todo
- git diff → Ver cambios

## 💾 Commits
- git commit -m "mensaje"
- git commit -am "mensaje"

## 🌿 Ramas
- git branch → Ver ramas
- git branch nombre → Crear rama
- git checkout nombre → Cambiar rama
- git checkout -b nombre → Crear y cambiar
- git merge rama → Unir ramas
- git branch -d nombre → Eliminar rama

## 🔄 Remoto
- git remote add origin URL
- git push -u origin main
- git push
- git pull
- git fetch

## 🕓 Historial
- git log
- git log --oneline

## 🚫 Deshacer
- git checkout -- archivo
- git reset archivo
- git reset --hard ⚠️

## 🆘 Ayuda
- git help comando
- git comando --help