"""POST /client-registry: overrides the LLM client at runtime (here: temperature).
-> extract_with_runtime_client: builds a ClientRegistry client and runs ExtractTicket with it.
"""

from typing import Annotated

from baml_py import ClientRegistry
from fastapi import APIRouter, Body

import config
from baml_client import b
from baml_client.types import Ticket

router = APIRouter()


@router.post("/client-registry")
async def extract_with_runtime_client(
    text: Annotated[str, Body()],
    temperature: Annotated[float, Body()],
) -> Ticket:
    cr = ClientRegistry()
    cr.add_llm_client(
        name="Runtime",
        provider="openai-generic",
        options={
            "base_url": config.HOST,
            "api_key": config.API_KEY,
            "model": config.MODEL,
            "temperature": temperature,
        },
    )
    cr.set_primary("Runtime")
    return await b.ExtractTicket(text, baml_options={"client_registry": cr})
