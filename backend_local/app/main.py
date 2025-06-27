# app/main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from typing import List, Optional
import pathlib

from .models import Attraction, RecommendRequest, ItineraryRequest
from .services import recommend, detail, build_itinerary

app = FastAPI(title="Local Travel Prototype")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# 挂载 static 目录
static_path = pathlib.Path(__file__).parent.parent / "static"

# 原有的 /attractions 接口...
@app.get("/attractions", response_model=List[Attraction])
def api_recommend(
    destination: Optional[str]    = Query(None, description="目的地关键词"),
    days: int                     = Query(1, gt=0, description="行程天数"),
    preferences: List[str]        = Query([], description="偏好标签列表")
):
    req = RecommendRequest(destination=destination or "", days=days, preferences=preferences)
    return recommend(req)

@app.get("/attractions/{id}", response_model=Attraction)
def api_detail(id: str):
    return detail(id)

@app.post("/itinerary", response_model=List[dict])
def api_itinerary(req: ItineraryRequest):
    return build_itinerary(req)

@app.get("/", include_in_schema=False)
def health_check():
    return {"status":"ok", "message":"Travel API is running"}
