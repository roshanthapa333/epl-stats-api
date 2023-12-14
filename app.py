from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.route import router


origins = [
    "http://localhost:3000",
]


app = FastAPI(
    title="Premier League Scraper",
    description="Api to scrape premier league data and store in db."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
