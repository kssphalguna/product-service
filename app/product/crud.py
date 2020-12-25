from uuid import uuid4

from sqlalchemy.orm import Session

from app.product.models import Product


def add_product(db_session: Session, product_data):
    product = Product(**product_data)
    db_session.add(product)
    db_session.commit()
    return product


def get_product_by_id(db_session: Session, external_id):
    product = db_session.query(Product).filter_by(id=external_id).first()
    return product


def get_all(db_session: Session):
    return db_session.query(Product).all()
#
#
# def update(db_session: Session, product_to_update: Product, product_data: dict):
#     for each in product_data:
#         setattr(product_to_update, each, product_data[each])
#     db_session.commit()
#     return product_to_update


def delete(db_session: Session, product_to_delete: Product):
    db_session.delete(product_to_delete)
    db_session.commit()
