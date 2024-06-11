from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from sqlalchemy.orm import Session
from database import sessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
import requests
import models


# Initialize FastAPI applicatioker
app = FastAPI()


# Load municipalities data
url = "http://municipalities-api:8000/municipalities"
try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP request errors
    data = response.json()  # Parse the JSON response
    print("Municipality data loaded successfully.")
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")


# CORS settings
origins = ["http://localhost:80", "http://localhost"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create database tables
models.base.metadata.create_all(bind=engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# Pydantic models
class report_model(BaseModel):
    title: str
    report: str
    author: str
    municipality: str
    year: str


# Utility function
def get_closest_year(year: int, available_years: List[int]) -> str:
    closest_year = min(available_years, key=lambda x: abs(x - year))
    return str(closest_year)


@app.get("/")
async def root():
    return {"message": "API is up and running"}


@app.get("/reports")
async def get_reports(db: db_dependency):
    result = db.query(models.Reports).all()
    if not result:
        raise HTTPException(status_code=404, detail="Reports not found")
    return result


@app.get("/reports/{report_id}")
async def get_report_by_id(report_id: int, db: db_dependency):
    result = db.query(models.Reports).filter(models.Reports.id == report_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Report not found")
    return result


@app.post("/reports")
async def create_report(report: report_model, db: db_dependency):
    try:
        response = requests.get(
            f"https://api-dados-abertos.tce.ce.gov.br/municipios?nome_municipio={report.municipality}"
        )
        response.raise_for_status()  # Check for HTTP request errors
        municipality_code_data = response.json()  # Parse the JSON response
        try:
            response_budget_data = requests.get(
                f"https://api-dados-abertos.tce.ce.gov.br/dados_orcamentos?codigo_municipio={municipality_code_data['data'][0]['codigo_municipio']}&exercicio_orcamento={report.year}00"
            )
            budget_data = response_budget_data.json()
            budget_key = str(budget_data["data"][0]["valor_total_fixado_orcamento"])
        except requests.exceptions.HTTPError as err:
            print(f"Something went wrong: {err}")
            raise HTTPException(status_code=404, detail="Budget data not found")
        except Exception as err:
            print(f"Something went wrong: {err}")
            raise HTTPException(status_code=404, detail="Budget data not found")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    for item in data:
        if item["Municipality_name"].lower() == report.municipality.lower():
            population_key = f"Total population {get_closest_year(int(report.year), [1991, 2000, 2010, 2014, 2017])}"
            poverty_key = f"Extreme poverty percentage {get_closest_year(int(report.year), [1991, 2000, 2010])}"
            idhm_key = f"IDHM {get_closest_year(int(report.year), [1991, 2000, 2010])}"

            db_report = models.Reports(
                title=report.title,
                report=report.report,
                author=report.author,
                municipality=item["Municipality_name"],
                year=report.year,
                population=f"{item[population_key]} ({get_closest_year(int(report.year), [1991, 2000, 2010, 2014, 2017])})",
                extreme_poverty_percentage=f"{item[poverty_key]} ({get_closest_year(int(report.year), [1991, 2000, 2010])})",
                idhm=f"{item[idhm_key]} ({get_closest_year(int(report.year), [1991, 2000, 2010])})",
                budget=f"{budget_key} ({report.year})",
            )
            db.add(db_report)
            db.commit()
            db.refresh(db_report)
            return db_report
    raise HTTPException(status_code=404, detail="Municipality not found")


@app.put("/reports/{report_id}")
async def update_report(report_id: int, report: report_model, db: db_dependency):
    db.query(models.Reports).filter(models.Reports.id == report_id).update(
        report.model_dump()
    )
    db.commit()
    updated_report = (
        db.query(models.Reports).filter(models.Reports.id == report_id).first()
    )
    if not updated_report:
        raise HTTPException(status_code=404, detail="Report not found")
    return updated_report


@app.delete("/reports/{report_id}")
async def delete_report(report_id: int, db: db_dependency):
    report_to_be_deleted = (
        db.query(models.Reports).filter(models.Reports.id == report_id).first()
    )
    if not report_to_be_deleted:
        raise HTTPException(status_code=404, detail="Report not found")
    db.delete(report_to_be_deleted)
    db.commit()
    return {"message": "Report deleted successfully"}
