from typing import List

from fastapi import APIRouter

from .todos import router as todos_router

# Add your APIRouters to this list
ALL_ROUTERS: List[APIRouter] = [todos_router]
