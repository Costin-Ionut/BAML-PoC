"""POST /collector: runs ExtractTicket and reports token usage via a Collector.
-> extract_with_usage: returns the ticket plus input/output token counts.
"""

from typing import Annotated

from baml_py import Collector
from fastapi import APIRouter, Body

from baml_client import b

router = APIRouter()


@router.post("/collector")
async def extract_with_usage(text: Annotated[str, Body(embed=True)]) -> dict:
    collector = Collector(name="poc")
    ticket = await b.ExtractTicket(text, baml_options={"collector": collector})
    usage = collector.usage
    return {
        "ticket": ticket,
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
    }
