from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from schemas.iproduct import IProductQueryParams

from schemas.iproduct_category import (
    IProductCategory,
    IProductCategoryQueryParams,
    IProductCategoryRefAdd,
    IProductCategoryUpdate,
    IProductCategoryRef,
)
from auth.oauth2 import ITokenData, get_current_user
from db_actions.product_category_actions import ProductCategoryActions
from schemas.iquery_params import SortOrder, SortProductBy, SortProductCategoryBy

router = APIRouter(tags=["Product Categories"], prefix="/product-categories")


@router.post("/")
async def create_product_category(
    category: IProductCategory, current_user: ITokenData = Depends(get_current_user)
):
    try:
        return ProductCategoryActions.create_category(category, current_user.user_id)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "category not created"},
        )


@router.put("/{category_id}")
async def update_product_category(
    category_id: int,
    category: IProductCategoryUpdate,
    current_user: ITokenData = Depends(get_current_user),
):
    try:
        return ProductCategoryActions.update_category(
            category_id, category, current_user.user_id
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "category not updated"},
        )


@router.delete("/{category_id}")
async def delete_category(
    category_id: int, current_user: ITokenData = Depends(get_current_user)
):
    try:
        return ProductCategoryActions.delete_category(category_id, current_user.user_id)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"message": "not deleted"}
        )


@router.get("/{category_id}")
async def get_category_by_id(
    category_id: int, current_user: ITokenData = Depends(get_current_user)
):
    try:
        return ProductCategoryActions.get_category_by_id(category_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"message": f"{e}"}
        )


@router.get("/")
async def get_categories(
    name: str = Query(None, title="username_filter", description=""),
    limit: int = Query(100, title="limit", description=""),
    sort_by: List[SortProductCategoryBy]
    | None = Query(None, title="order by", description=""),
    skip: int = Query(0, title="skip", description=""),
    order: SortOrder
    | None = Query(
        "asc",
        title="order",
        description="Either `asc` for ascending or `desc` for descending",
    ),
    current_user: ITokenData = Depends(get_current_user),
):
    params = IProductCategoryQueryParams(
        name=name,
        skip=skip,
        limit=limit,
        order=order,
        sort_by=sort_by,
    )
    return ProductCategoryActions.get_categories(params)


@router.post("/{category_id}")
async def add_product_to_category(
    category_id: int,
    product: IProductCategoryRefAdd,
    current_user: ITokenData = Depends(get_current_user),
):
    cat_prod_ref: IProductCategoryRef = IProductCategoryRef(
        category_id=category_id, product_id=product.product_id
    )
    try:
        return ProductCategoryActions.add_prod_category(
            cat_prod_ref, current_user.user_id
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"message": f"{e}"}
        )


@router.delete("/{category_id}/{product_id}")
async def remove_product_from_category(
    category_id: int,
    product_id: int,
    current_user: ITokenData = Depends(get_current_user),
):
    cat_prod_ref: IProductCategoryRef = IProductCategoryRef(
        category_id=category_id, product_id=product_id
    )
    try:
        return ProductCategoryActions.remove_prod_from_category(
            cat_prod_ref, current_user.user_id
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"message": f"{e}"}
        )


@router.get("/{category_id}/products")
async def get_category_products(
    category_id: int,
    name: str = Query(None, title="username_filter", description=""),
    limit: int = Query(100, title="limit", description=""),
    sort_by: List[SortProductBy] | None = Query(None, title="order by", description=""),
    skip: int = Query(0, title="skip", description=""),
    order: SortOrder
    | None = Query(
        "asc",
        title="order",
        description="Either `asc` for ascending or `desc` for descending",
    ),
    current_user: ITokenData = Depends(get_current_user),
):
    params = IProductQueryParams(
        name=name,
        skip=skip,
        limit=limit,
        order=order,
        sort_by=sort_by,
    )
    try:
        return ProductCategoryActions.get_category_items(
            category_id, current_user.user_id, params
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"message": f"{e}"}
        )
