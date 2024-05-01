from fastapi import FastAPI
import config


app = FastAPI(title = config.APP_NAME)