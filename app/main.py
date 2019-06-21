from fastapi import FastAPI

from app.budgets.routers import router as budget_router

app = FastAPI()

app.include_router(budget_router, tags=["budgets"])
