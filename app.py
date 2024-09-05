from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from units import LENGTH_UNITS, WEIGHT_UNITS, TEMPERATURE_UNITS

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def length_form(request: Request):
    return templates.TemplateResponse(
        "length_form.html", {"request": request, "units": LENGTH_UNITS}
    )


@app.get("/weight", response_class=HTMLResponse)
async def length_form(request: Request):
    return templates.TemplateResponse(
        "weight_form.html", {"request": request, "units": WEIGHT_UNITS}
    )


@app.get("/temperature", response_class=HTMLResponse)
async def length_form(request: Request):
    return templates.TemplateResponse(
        "temperature_form.html", {"request": request, "units": TEMPERATURE_UNITS}
    )


@app.post("/submit")
async def submit_form(
    request: Request,
    value: float = Form(...),
    convertFrom: str = Form(...),
    convertTo: str = Form(...),
):
    return {"value": value, "convertFrom": convertFrom, "convertTo": convertTo}
