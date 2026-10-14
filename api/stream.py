"""POST /stream: streams partial Tickets as the LLM generates them.
-> stream: yields each partial ExtractTicket result.
"""

from collections.abc import AsyncIterable
from typing import Annotated

from fastapi import APIRouter, Body

from baml_client import b, stream_types

router = APIRouter()


@router.post("/stream")
async def stream(text: Annotated[str, Body(embed=True)]) -> AsyncIterable[stream_types.Ticket]:
    async for partial in b.stream.ExtractTicket(text):
        yield partial
