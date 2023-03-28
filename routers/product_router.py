from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status

from auth.oauth2 import ITokenData, get_current_user
from db_actions.product_actions import ProductActions
from schemas.iproduct import IProduct, IProductQueryParams, IProductUpdate
from schemas.iquery_params import SortOrder, SortProductBy

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
async def create_product(product: IProduct,
                         current_user: ITokenData = Depends(get_current_user)):
    try:
        return ProductActions.create_product(product, current_user.user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "message": f"product not created: {e}"
            }
        )


@router.put("/{product_id}")
async def update_product(product_id: int, product: IProductUpdate,
                         current_user: ITokenData = Depends(get_current_user)):
    try:
        return ProductActions.update_product(product_id, product, current_user.user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": f"product not updated: {e}"
            }
        )


@router.delete("/{product_id}")
async def delete_product(product_id: int,
                         current_user: ITokenData = Depends(get_current_user)):
    try:
        return ProductActions.delete_product(product_id, current_user.user_id)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "not deleted"
            }
        )


@router.get("/{product_id}")
async def get_product_by_id(product_id: int,
                            current_user: ITokenData = Depends(get_current_user)):
    try:
        return ProductActions.get_product_by_id(product_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": f"{e}"
            }
        )


@router.get("/")
async def get_products(
    name: str = Query(None, title="name_filter", description=""),
    limit: int = Query(100, title="limit", description=""),
    sort_by: List[SortProductBy] | None = Query(
        None, title="order by", description=""),
    skip: int = Query(0, title="skip", description=""),
    order: SortOrder | None = Query("asc", title="order",
                                    description="Either `asc` for ascending or `desc` for descending"),
    expired: bool | None = Query(
        None, title="expired", description="Either `true` for ascending or `false` for descending"),
    current_user: ITokenData = Depends(get_current_user)
):
    params = IProductQueryParams(
        name=name,
        skip=skip,
        limit=limit,
        order=order,
        sort_by=sort_by,
        expired=expired,
    )
    return ProductActions.get_products(params)
