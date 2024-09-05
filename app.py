from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from helper import length_unit_conversion, temp_unit_conversion, weight_unit_conversion
from units import LENGTH_UNITS, TEMPERATURE_UNITS, WEIGHT_UNITS

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


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
    type_of: str = Form(...),
):
    converted_value = value
    if type_of == "temperature":
        converted_value = temp_unit_conversion(value, convertFrom, convertTo)
    elif type_of == "length":
        converted_value = length_unit_conversion(value, convertFrom, convertTo)
    elif type_of == "weight":
        converted_value = weight_unit_conversion(value, convertFrom, convertTo)
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "value": value,
            "converted_value": round(converted_value, 2),
            "convertFrom": convertFrom,
            "convertTo": convertTo,
            "href": "/" if type_of == "length" else type_of,
        },
    )
