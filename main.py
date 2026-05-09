from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Mazda 3 Showcase")

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "plantillas")


@app.get("/")
def root(request: Request):
    return index(request)


@app.get("/index.html")
def index(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "title": "Mazda 3 | Especificaciones Oficiales",
            "active_page": "index",
            "footer_text": "2024 Mazda 3 Showcase | Proyecto Frontend Profesional",
        },
    )


@app.get("/plantillas/curiosos.html")
def curiosos(request: Request):
    return templates.TemplateResponse(
        request,
        "curiosos.html",
        {
            "title": "Datos Curiosos | El legado del Mazda 3",
            "active_page": "curiosos",
            "footer_text": "2026 Mazda 3 Showcase | Historia y Curiosidades",
        },
    )


@app.get("/plantillas/proceso.html")
def proceso(request: Request):
    return templates.TemplateResponse(
        request,
        "proceso.html",
        {
            "title": "Proceso de Creacion | El Arte de Mazda",
            "active_page": "proceso",
            "footer_text": "2026 Mazda 3 Showcase | Filosofia de Diseno",
        },
    )


@app.get("/plantillas/versiones.html")
def versiones(request: Request):
    return templates.TemplateResponse(
        request,
        "versiones.html",
        {
            "title": "Versiones Mazda 3 | Encuentra el tuyo",
            "active_page": "versiones",
            "footer_text": "2026 Mazda 3 Showcase | Versiones de Gama Alta",
        },
    )
