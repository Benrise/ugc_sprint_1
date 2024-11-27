import logging
import uvicorn
import datetime

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.config import settings
from core.logger import LOGGING

app = FastAPI(
    title=settings.project_name,
    docs_url='/ugc/api/v1/docs',
    openapi_url='/ugc/api/v1/docs.json',
    default_response_class=ORJSONResponse,
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
    }


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=settings.service_port,
        log_config=LOGGING,
        log_level=logging.DEBUG,
        reload=True,
    )
