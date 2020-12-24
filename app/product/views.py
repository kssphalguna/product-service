from typing import List
from uuid import uuid4

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.product.schemas import Product, ProductIn
from app.product import crud as product_crud
product_router = APIRouter()


@product_router.get(
    '',
    response_model=List[Product]
)
async def get_all_products(
        db_session: Session = Depends(get_db)
):
    return product_crud.get_all(db_session=db_session)


@product_router.post(
    '',
    response_model=Product
)
async def create_product(
        product_in: ProductIn,
        db_session: Session = Depends(get_db),
):
    product_data = product_in.dict()
    product_data['id'] = uuid4()
    return product_crud.add_product(
        db_session=db_session,
        product_data=product_data
    )


