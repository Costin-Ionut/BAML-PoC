"""POST /tools: tool selection.
-> pick_tool: runs PickTool and returns GetWeather or SendEmail.
"""

from typing import Annotated

from fastapi import APIRouter, Body

from baml_client import b
from baml_client.types import GetWeather, SendEmail

router = APIRouter()


@router.post("/tools")
async def pick_tool(request: Annotated[str, Body(embed=True)]) -> GetWeather | SendEmail:
    return await b.PickTool(request)
