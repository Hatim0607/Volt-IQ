"""
Volt-IQ — Simulateur de capteurs
Génère des données réalistes sans matériel réel.
Idéal pour développer et tester le dashboard.
"""

import math
import random
import time
from datetime import datetime


def solar_production(hour: float, capacity_kwp: float = 5.0) -> float:
    """Simule la production PV selon l'heure de la journée."""
    if hour < 6 or hour > 19:
        return 0.0
    peak = math.sin((hour - 6) * math.pi / 13) * capacity_kwp
    noise = random.uniform(-0.2, 0.2)
    return max(0.0, round(peak + noise, 2))


def building_consumption(hour: float, site_type: str = "hotel") -> float:
    """Simule la consommation selon le type de bâtiment et l'heure."""
    base = {
        "hotel":    [1.5, 1.2, 1.0, 1.0, 1.1, 1.3, 2.0, 3.5, 4.0, 3.8,
                     3.5, 3.2, 3.0, 3.2, 3.5, 3.8, 4.2, 5.0, 5.5, 5.0,
                     4.5, 3.5, 2.5, 2.0],
        "hospital": [3.0, 2.8, 2.8, 2.9, 3.0, 3.5, 4.5, 5.5, 6.0, 6.2,
                     6.0, 5.8, 5.5, 5.8, 6.0, 6.2, 6.5, 6.8, 6.5, 6.0,
                     5.5, 5.0, 4.0, 3.5],
        "industry": [1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 5.0, 8.0, 9.0, 9.5,
                     9.0, 8.5, 7.0, 8.5, 9.0, 9.5, 9.0, 8.0, 5.0, 3.0,
                     2.0, 1.5, 1.2, 1.0],
    }
    h = int(hour) % 24
    profile = base.get(site_type, base["hotel"])
    noise = random.uniform(-0.15, 0.15)
    return max(0.0, round(profile[h] + noise, 2))


def read_sensors(site_config: dict) -> dict:
    """Retourne une lecture simulée pour tous les capteurs du site."""
    now = datetime.now()
    hour = now.hour + now.minute / 60

    site_type = site_config.get("type", "hotel")
    pv_device = next((d for d in site_config["devices"] if d["type"] == "solar_pv"), None)
    capacity = pv_device.get("capacity_kwp", 5.0) if pv_device else 5.0

    pv_kw = solar_production(hour, capacity)
    conso_kw = building_consumption(hour, site_type)
    grid_kw = max(0.0, round(conso_kw - pv_kw, 2))
    injection_kw = max(0.0, round(pv_kw - conso_kw, 2))

    return {
        "timestamp": now.isoformat(),
        "site_id": site_config["site_id"],
        "pv_production_kw": pv_kw,
        "consumption_kw": conso_kw,
        "grid_import_kw": grid_kw,
        "grid_export_kw": injection_kw,
        "self_consumption_pct": round((pv_kw / conso_kw * 100) if conso_kw > 0 else 0, 1),
        "devices": {
            d["id"]: {
                "status": "online",
                "value": round(random.uniform(0.8, 1.0) * pv_kw, 2) if d["type"] == "solar_pv" else None
            }
            for d in site_config["devices"]
        }
    }


if __name__ == "__main__":
    # Test rapide — affiche des données toutes les 2 secondes
    import json
    demo_site = {
        "site_id": "demo",
        "type": "hotel",
        "devices": [{"id": "pv_01", "type": "solar_pv", "capacity_kwp": 10}]
    }
    print("Volt-IQ — Simulateur démarré. Ctrl+C pour arrêter.\n")
    while True:
        data = read_sensors(demo_site)
        print(json.dumps(data, indent=2))
        time.sleep(2)
