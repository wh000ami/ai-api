from fastapi import FastAPI
from pydantic.json_schema import Examples
from loguru import logger

from app.model import MessageParams
from app.service import get_text_generation

app = FastAPI()


@app.get("/health")
async def healths_check():
    result = {"status": "health"}
    return result


@app.post("/generate")
async def generate_text(message_params: MessageParams):
    try:
        result = get_text_generation(message=message_params.message, model=message_params.model)
        return result
    except Exception as error:
        logger.error(repr(error))
