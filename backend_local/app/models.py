# app/models.py

from pydantic import BaseModel
from typing import List, Optional

class Attraction(BaseModel):
    id: str
    name: str
    description: Optional[str]
    lat: float
    lon: float
    tags: List[str]
    images: List[str] = []       # 小程序里展示卡片和详情页需要至少一张封面图
    address: Optional[str] = None # 详情页要显示的地址
    pros: List[str] = []
    cons: List[str] = []
    source_posts: List[str] = []


class Post(BaseModel):
    post_id: str
    attraction_id: str
    content: str
    url: Optional[str]
    tags: List[str]
    likes: int
    sentiment: float

class RecommendRequest(BaseModel):
    destination: str
    days: int
    preferences: List[str]

class ItineraryRequest(BaseModel):
    selected_ids: List[str]
    days: int
    preferences: List[str]