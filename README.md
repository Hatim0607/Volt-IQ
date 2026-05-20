# ⚡ Volt-IQ

**Plateforme open source de gestion intelligente de l'énergie pour bâtiments**

Volt-IQ permet de surveiller, analyser et optimiser la consommation électrique de tout type de bâtiment (hôtel, hôpital, industrie, tertiaire) à partir de capteurs réels (panneaux PV, variateurs de vitesse, compteurs, horloges).

---

## Fonctionnalités

- 📊 **Dashboard temps réel** — production PV, consommation, surplus réseau
- 🏢 **Multi-sites** — gérez plusieurs bâtiments depuis une seule interface
- 🔌 **Multi-protocoles** — Modbus RTU/TCP, MQTT, Sunspec, M-Bus
- ⚙️ **Profils configurables** — chaque site déclaré via un fichier JSON
- 🔔 **Alertes** — email/SMS en cas de dépassement ou de panne
- 📈 **Historique** — courbes sur 24h, 7 jours, 1 mois
- 🧠 **Moteur de règles EMS** — délestage, priorités, optimisation tarifaire

---

## Stack technique

| Couche | Technologie |
|--------|------------|
| Collecte | Python + pymodbus / paho-mqtt |
| Stockage | InfluxDB (time-series) |
| API | FastAPI (Python) |
| Frontend | React + Chart.js |
| Alertes | SMTP / API SMS |

---

## Démarrage rapide

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-compte/volt-iq.git
cd volt-iq

# 2. Lancer l'environnement de développement
./scripts/setup.sh

# 3. Démarrer avec Docker
docker-compose up

# 4. Ouvrir le dashboard
# http://localhost:3000
```

---

## Structure du projet

```
volt-iq/
├── backend/
│   ├── api/          # API REST (FastAPI)
│   ├── collector/    # Collecte des données capteurs
│   ├── engine/       # Moteur de règles EMS
│   └── alerts/       # Système de notifications
├── frontend/         # Interface React
├── config/
│   └── sites/        # Profils de sites (JSON)
├── docs/             # Documentation
└── scripts/          # Outils d'installation
```

---

## Contribuer

Les contributions sont les bienvenues ! Lisez [CONTRIBUTING.md](CONTRIBUTING.md) pour commencer.

---

## Licence

MIT — libre d'utilisation, de modification et de distribution.

---

*Projet initié au Maroc 🇲🇦 — conçu pour fonctionner partout.*
