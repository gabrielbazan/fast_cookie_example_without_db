from fastapi import APIRouter
from settings import settings

router = APIRouter(prefix=settings.todos_route, tags=[settings.todos_tag])
