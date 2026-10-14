"""App entrypoint: mounts every feature router on one FastAPI app, served by Granian.
-> app: FastAPI app, one router (and Swagger tag) per feature module in api/.
"""

from fastapi import FastAPI
from granian import Granian
from granian.constants import Interfaces

import config
from api import checks, client_registry, collector, dynamic_types, extract, stream, tools

app = FastAPI(title="BAML PoC")

for feature in (
    extract,
    stream,
    dynamic_types,
    client_registry,
    collector,
    checks,
    tools,
):
    app.include_router(feature.router, tags=[feature.__name__.removeprefix("api.")])

if __name__ == "__main__":
    Granian("main:app", interface=Interfaces.ASGI, port=config.PORT).serve()
