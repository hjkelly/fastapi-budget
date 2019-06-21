from datetime import date
from typing import List

from fastapi import APIRouter
from google.cloud import firestore

from app.viewmodels.budget import BudgetInput, BudgetOutput, Item

router = APIRouter()
db = firestore.Client()
collection = db.collection("budget")


@router.get("/budgets/?")
async def list() -> List[BudgetOutput]:
    results: List[BudgetOutput] = []
    for doc in collection.stream():
        results.append(to_output_model(doc))
    return results


@router.post("/budgets/?")
async def create(budget: BudgetInput) -> BudgetOutput:
    doc_ref = collection.document()
    doc_ref.set(get_db_dict(budget))
    return to_output_model(doc_ref.get())


@router.get("/budgets/{budget_id}/?")
async def retrieve(budget_id: str) -> BudgetOutput:
    doc_ref = collection.document(budget_id)
    return to_output_model(doc_ref.get())


@router.put("/budgets/{budget_id}/?")
async def replace(budget_id: str, budget: BudgetInput):
    doc_ref = collection.document(budget_id)
    doc_ref.set(get_db_dict(budget))
    return to_output_model(doc_ref.get())


def get_db_dict(budget: BudgetInput) -> dict:
    data = budget.dict()
    data["start"] = data["start"].isoformat()
    data["end"] = data["end"].isoformat()
    return data


def to_output_model(document) -> BudgetOutput:
    return BudgetOutput(id=document.id, **document.to_dict())
