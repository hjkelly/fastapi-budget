from datetime import date

from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    amount: float


class BudgetInput(BaseModel):
    start: date
    end: date
    incomes: List[Item]
    expenses: List[Item]


class BudgetOutput(BudgetInput):
    id: str
