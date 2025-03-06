import logging
from fastapi import FastAPI, Request

app = FastAPI()

###
# Event Logger
###
def create_logger(file=None):
    json_fmt = '{"timestamp":"%(asctime)s","log_level":"%(levelname)s","module":"%(module)s","event":%(message)s}'
    if file:
        log_handler = logging.FileHandler(file)
    else:
        log_handler = logging.StreamHandler()
    basic_json_fmt = logging.Formatter(
        fmt=json_fmt,
        datefmt="%Y-%m-%dT%H:%M:%S"
    )
    log_handler.setFormatter(basic_json_fmt)

    logger = logging.getLogger("webapp")
    logger.setLevel(logging.INFO)
    logger.addHandler(log_handler)

    return logger

ctr_file = "/app/logs/web-app.event.log"
logger = create_logger(ctr_file)

###
# Routers
###
@app.get("/")
async def root():
    return { "up": "webapp-2" }

@app.get("/broken", status_code=403)
async def broken(request: Request):
    headers = request.headers
    logger.info("Request headers:")
    for key, value in headers.items():
        logger.info(f"Header: {key} -> {value}")
    return {"error": "Not Good"}
