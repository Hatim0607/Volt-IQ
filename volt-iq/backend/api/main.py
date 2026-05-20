"""
Volt-IQ — API principale (FastAPI)
Point d'entrée du backend.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Volt-IQ API",
    description="API de gestion intelligente de l'énergie",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"name": "Volt-IQ", "version": "0.1.0", "status": "running"}


@app.get("/sites")
def list_sites():
    """Liste tous les sites configurés."""
    return {"sites": []}  # À connecter à la config


@app.get("/sites/{site_id}/live")
def get_live_data(site_id: str):
    """Retourne les données temps réel d'un site."""
    return {"site_id": site_id, "data": {}}  # À connecter au collecteur


@app.get("/sites/{site_id}/history")
def get_history(site_id: str, period: str = "24h"):
    """Retourne l'historique d'un site."""
    return {"site_id": site_id, "period": period, "data": []}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
