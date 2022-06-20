from fastapi import APIRouter
from serialization.base_models import PaginatedListField
from serialization.todo_models import TodoPaginatedList
from settings import ROOT_ROUTE, settings

router = APIRouter(prefix=settings.todos_route, tags=[settings.todos_tag])


@router.get(ROOT_ROUTE, response_model=TodoPaginatedList)
def list_todos(
    limit: int = settings.default_limit,
    offset: int = settings.default_offset,
):
    # TODO: ... work your galactic magic here ...
    results = [
        {
            "id": 1,
            "name": "Feed the cat",
        }
    ]

    return {
        PaginatedListField.TOTAL_COUNT: 1,
        PaginatedListField.COUNT: len(results),
        PaginatedListField.LIMIT: limit,
        PaginatedListField.OFFSET: offset,
        PaginatedListField.RESULTS: results,
    }
