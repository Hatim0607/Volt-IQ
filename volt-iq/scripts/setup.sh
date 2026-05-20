#!/bin/bash
echo "⚡ Volt-IQ — Installation"
echo "========================="

# Vérification Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 requis. Installez-le depuis https://python.org"
    exit 1
fi

# Environnement virtuel Python
echo "→ Création de l'environnement Python..."
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt --quiet

echo "✅ Installation terminée !"
echo ""
echo "Pour démarrer :"
echo "  source venv/bin/activate"
echo "  python backend/api/main.py"
