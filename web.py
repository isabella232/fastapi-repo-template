# Service entry point
import uvicorn
from fastapi import FastAPI

from config import settings

app = FastAPI(
    debug=settings.debug,
    root_path=settings.root_path,
    #servers=[{'url': '/control-center/configs-service'}],
    redoc_url='/internal/redoc',
    docs_url='/internal/docs',
)

if __name__ == '__main__':
    uvicorn.run(
        'web:app',
        reload=settings.autoreload,
        host=settings.service_host,
        port=settings.service_port,
        log_level=settings.log_level.lower(),
    )
