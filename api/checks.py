"""POST /checks: runs ExtractOrder and returns the Order with its check results.
-> extract_order: endpoint; a failed @assert raises, a failed @check is just reported.
"""

from typing import Annotated

from fastapi import APIRouter, Body

from baml_client import b
from baml_client.types import Order

router = APIRouter()


@router.post("/checks")
async def extract_order(text: Annotated[str, Body(embed=True)]) -> Order:
    return await b.ExtractOrder(text)
