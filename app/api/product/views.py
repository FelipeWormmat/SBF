from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.api.product.schemas import PaymentMethodSchema, ShowPaymentMethodSchema
from app.repositories.product_repository import Product
from app.models.models import PaymentMethods
from app.services.auth_service import only_admin

router = APIRouter(dependencies=[Depends(only_admin)])


@router.get('/', response_model=List[ShowPaymentMethodSchema])
def index(repository: Product = Depends()):
    return repository.get_all()