from typing import List, Optional, Union
from fastapi import APIRouter, Depends, HTTPException, Query, status

from db_actions.user_actions import UserActions
from auth.oauth2 import ITokenData, get_current_user
from schemas.iquery_params import SortOrder, SortUserBy
from helper.query_descriptions import user_query_description
from schemas.iuser import IUser, IUserOut, IUserQueryParams, IUserUpdate

router = APIRouter(
    tags=["Users"],
    prefix="/users"
)


@router.post("/", response_model=IUserOut)
async def create_user(user: IUser,
                      current_user: ITokenData = Depends(get_current_user)):
    try:
        return UserActions.create_user(user, current_user.user_id)
    except Exception as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail={
                "message": f"user not created: {e}"
            })


@router.put("/{user_id}", response_model=IUserOut)
async def update_user(user_id: int, user: IUserUpdate,
                      current_user: ITokenData = Depends(get_current_user)):
    try:
        return UserActions.update_user(user_id, user, current_user.user_id)
    except Exception as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail={
                "message": f"info not updated: {e}"
            })


@router.delete("/{user_id}", response_model=IUserOut)
async def delete_user(user_id: int,
                      current_user: ITokenData = Depends(get_current_user)):
    try:
        return UserActions.delete_user(user_id, current_user.user_id)
    except:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail={
                "message": "user not deleted"
            })


@router.get("/", response_model=List[IUserOut])
async def get_users(
    name: str = Query(None, title="username_filter",
                      description=user_query_description["name"]),
    limit: int = Query(100, title="limit",
                       description=user_query_description["limit"]),
    sort_by: List[SortUserBy] | None = Query(
        None, title="order by", description=user_query_description["sort_by"]),
    skip: int = Query(
        0, title="skip", description=user_query_description["sort_by"]),
    order: SortOrder = Query("asc", title="order",
                             description=user_query_description["order"]),
    current_user: ITokenData = Depends(get_current_user)
):
    params = IUserQueryParams(
        name=name,
        skip=skip,
        limit=limit,
        order=order,
        sort_by=sort_by,
    )

    return UserActions.get_users(params)


@router.get("/{user_id}", response_model=IUserOut)
async def get_user_by_id(user_id: int,
                         current_user: ITokenData = Depends(get_current_user)):
    return UserActions.get_user_by_id(user_id)
