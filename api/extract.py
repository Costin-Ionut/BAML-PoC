"""POST /extract: basic structured extraction.
-> extract: runs ExtractTicket and returns the Ticket.
"""

from typing import Annotated

from fastapi import APIRouter, Body

from baml_client import b
from baml_client.types import Ticket

router = APIRouter()


@router.post("/extract")
async def extract(text: Annotated[str, Body(embed=True)]) -> Ticket:
    return await b.ExtractTicket(text)
