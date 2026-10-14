"""POST /classify: classifies text into categories supplied in the request.
-> classify: adds the categories to the dynamic Category enum, then runs Classify.
"""

from typing import Annotated

from fastapi import APIRouter, Body

from baml_client import b
from baml_client.type_builder import TypeBuilder

router = APIRouter()


@router.post("/classify")
async def classify(
    text: Annotated[str, Body()],
    categories: Annotated[list[str], Body()],
) -> str:
    tb = TypeBuilder()
    for category in categories:
        tb.Category.add_value(category)
    return await b.Classify(text, baml_options={"tb": tb})
