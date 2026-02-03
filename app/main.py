import logging
from fastapi import FastAPI

from app.config.logging_config import setup_logging
from app.middlewares.access_log import access_log_middleware
from app.api.logs import router as logs_router
from app.api.excel import router as excel_router
from app.api.word import router as word_router
from app.exceptions.handlers import global_exception_handler

setup_logging(logging.DEBUG)  # Pass DEBUG level

app = FastAPI(title="FastAPI MSOffice サンプル")

app.middleware("http")(access_log_middleware)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(logs_router)
app.include_router(excel_router)
app.include_router(word_router)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/test-error")
def test_error():
    raise ValueError("Intentional test error")
