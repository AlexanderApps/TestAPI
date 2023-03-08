from enum import Enum
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status

from auth.oauth2 import get_current_user
from models.transaction import Transaction
from schemas.iquery_params import SortOrder, SortTransactionBy
from schemas.itransaction import ITransaction, ITransactionQueryParams
from db_actions.transaction_actions import TransactionActions

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)



class OrderBy(Enum):
    date_created = Transaction.date_created
    transaction_id = Transaction.transaction_id


@router.get("/")
async def get_transactions(
    name: str = Query(None, title="name_filter", description=""),
    limit: int = Query(100, title="limit", description=""),
    sort_by: Optional[List[SortTransactionBy]] = Query(None, title="order by", description=""),
    skip: int = Query(0, title="skip", description=""),
    order: SortOrder = Query("asc", title="order",
                       description="Either `asc` for ascending or `desc` for descending"),
    current_user=Depends(get_current_user)
):
    params = ITransactionQueryParams(
        name=name,
        skip=skip,
        limit=limit,
        order=order,
        sort_by=sort_by,
    )
    return TransactionActions.get_transactions(params)


@router.post("/")
async def create_transaction(transaction: ITransaction, current_user=Depends(get_current_user)):
    try:
        return TransactionActions.create_transaction(transaction)
    except Exception as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail={
                            "message": f"{e}"})


@router.get("/{transaction_id}")
async def get_transaction_by_id(transaction_id: int, current_user=Depends(get_current_user)):
    try:
        return TransactionActions.get_transaction_by_id2(transaction_id)
    except Exception as e:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail={
                            "message": f"{e}"})
