# Changelog — Volt-IQ

Toutes les modifications notables de ce projet sont documentées ici.

Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).
Versionnage basé sur [Semantic Versioning](https://semver.org/lang/fr/).

---

## [Non publié]

### En cours
- Connexion du simulateur à l'API FastAPI
- Premier dashboard React fonctionnel
- Intégration InfluxDB pour le stockage time-series

---

## [0.1.0] — 2026-05-20

### Ajouté
- Structure complète du projet (backend, frontend, config, docs, scripts)
- Simulateur de capteurs Python — génère des données réalistes selon l'heure et le type de site
- API FastAPI avec routes de base (`/`, `/sites`, `/sites/{id}/live`, `/sites/{id}/history`)
- Profils de sites configurables via fichiers JSON (`hotel_example.json`, `hospital_example.json`)
- Dashboard React — maquettes des 6 écrans principaux (Vue d'ensemble, Dashboard site, Historique, Équipements, Alertes, Paramètres)
- Logo Volt-IQ (SVG + PNG) — cercle bleu, éclair blanc, soleil vert
- Fichier `docker-compose.yml` — InfluxDB + API + Frontend
- Script d'installation `scripts/setup.sh`
- Documentation : `README.md`, `CONTRIBUTING.md`, `LICENSE` (MIT)
- Dépôt GitHub public avec 12 topics et description bilingue

---

## À venir

## [0.2.0] — prévu T3 2026

### Prévu
- Connexion réelle Modbus TCP/RTU via `pymodbus`
- Stockage des mesures dans InfluxDB
- Graphiques historiques 24h / 7j / 30j
- Système d'alertes par email

## [0.5.0] — prévu T4 2026

### Prévu
- Interface React complète et connectée à l'API
- Gestion multi-sites depuis le dashboard
- Profil de site industriel complet
- Premier site pilote réel

## [1.0.0] — prévu 2027

### Prévu
- Version stable et documentée
- Support Modbus RTU, TCP, MQTT, Sunspec, M-Bus
- Moteur de règles EMS (délestage, priorités, optimisation tarifaire)
- Rapports PDF mensuels
- Authentification utilisateurs avec rôles

---

## Convention de versionnage

| Version | Signification |
|---------|--------------|
| `0.x.x` | Phase prototype — instable, en développement actif |
| `1.0.0` | Première version stable — utilisable en production |
| `x.Y.x` | Nouvelle fonctionnalité ajoutée |
| `x.y.Z` | Correction de bug |

## Types de changements

- `Ajouté` — nouvelles fonctionnalités
- `Modifié` — changements dans les fonctionnalités existantes
- `Déprécié` — fonctionnalités qui seront supprimées
- `Supprimé` — fonctionnalités supprimées
- `Corrigé` — corrections de bugs
- `Sécurité` — corrections de failles de sécurité
