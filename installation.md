# Guide d'installation — Volt-IQ

Ce guide explique comment installer et lancer Volt-IQ sur votre machine, étape par étape.
Aucune expérience avancée n'est requise.

---

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

| Outil | Version minimale | Téléchargement |
|-------|-----------------|----------------|
| Python | 3.10+ | https://python.org/downloads |
| Git | 2.x | https://git-scm.com/downloads |
| Node.js | 18+ | https://nodejs.org |

> **Important (Windows)** : lors de l'installation de Python, cochez la case
> **"Add Python to PATH"** en bas de la fenêtre d'installation.

---

## Installation rapide

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-compte/volt-iq.git
cd volt-iq
```

### 2. Installer les dépendances Python

```bash
pip install -r backend/requirements.txt
```

### 3. Lancer le simulateur de capteurs

```bash
python backend/collector/simulator.py
```

Vous devriez voir des données JSON s'afficher toutes les 2 secondes :

```json
{
  "timestamp": "2026-05-20T14:32:05",
  "site_id": "demo",
  "pv_production_kw": 3.8,
  "consumption_kw": 2.1,
  "grid_import_kw": 0.0,
  "grid_export_kw": 1.7,
  "self_consumption_pct": 100.0
}
```

Appuyez sur **Ctrl + C** pour arrêter.

### 4. Lancer l'API

```bash
python backend/api/main.py
```

L'API est accessible sur : http://localhost:8000
La documentation automatique : http://localhost:8000/docs

---

## Installation avec Docker (recommandé)

Docker lance tout le projet en une seule commande — base de données, API et frontend.

### Prérequis Docker

Installez Docker Desktop : https://docker.com/products/docker-desktop

### Lancer avec Docker

```bash
docker-compose up
```

| Service | URL |
|---------|-----|
| Dashboard | http://localhost:3000 |
| API | http://localhost:8000 |
| InfluxDB | http://localhost:8086 |

Pour arrêter :

```bash
docker-compose down
```

---

## Configuration d'un site

Chaque bâtiment est décrit par un fichier JSON dans `config/sites/`.
Des exemples sont fournis pour vous aider à démarrer :

```
config/sites/
├── hotel_example.json       ← Hôtel avec PV, climatisation, horloge
├── hospital_example.json    ← Hôpital avec UPS, groupe électrogène
└── industry_example.json    ← Industrie avec variateurs, compresseurs
```

Pour ajouter un nouveau site, copiez l'exemple le plus proche et modifiez :

```bash
cp config/sites/hotel_example.json config/sites/mon_site.json
```

Puis éditez `mon_site.json` avec les informations de votre bâtiment.

---

## Structure du projet

```
volt-iq/
├── backend/
│   ├── api/            → API REST (FastAPI)
│   ├── collector/      → Collecte des données capteurs
│   ├── engine/         → Moteur de règles EMS
│   └── alerts/         → Système de notifications
├── frontend/           → Interface React
├── config/
│   └── sites/          → Profils de sites (JSON)
├── docs/               → Documentation
└── scripts/            → Outils d'installation
```

---

## Résolution des problèmes courants

### "python n'est pas reconnu"

Python n'est pas dans le PATH. Solutions :

- **Windows** : désinstallez Python et réinstallez en cochant "Add Python to PATH"
- **Mac/Linux** : essayez `python3` à la place de `python`

### "pip n'est pas reconnu"

```bash
python -m pip install -r backend/requirements.txt
```

### "Port 8000 déjà utilisé"

Un autre programme utilise ce port. Lancez l'API sur un autre port :

```bash
uvicorn backend.api.main:app --port 8001
```

### Le simulateur affiche des erreurs d'import

```bash
pip install -r backend/requirements.txt --upgrade
```

---

## Vérifier que tout fonctionne

Une fois l'API lancée, ouvrez votre navigateur et allez sur :

```
http://localhost:8000
```

Vous devez voir :

```json
{
  "name": "Volt-IQ",
  "version": "0.1.0",
  "status": "running"
}
```

Si c'est le cas, **Volt-IQ est correctement installé**.

---

## Prochaines étapes

- [Configurer votre premier site](configuration.md)
- [Connecter un vrai capteur Modbus](modbus.md)
- [Contribuer au projet](../CONTRIBUTING.md)

---

*Un problème ? Ouvrez une [issue sur GitHub](https://github.com/votre-compte/volt-iq/issues).*
