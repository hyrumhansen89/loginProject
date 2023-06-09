from _typeshed import Incomplete
from typing import Any

from braintree.credit_card import CreditCard as CreditCard
from braintree.error_result import ErrorResult as ErrorResult
from braintree.exceptions.not_found_error import NotFoundError as NotFoundError
from braintree.ids_search import IdsSearch as IdsSearch
from braintree.resource import Resource as Resource
from braintree.resource_collection import ResourceCollection as ResourceCollection
from braintree.successful_result import SuccessfulResult as SuccessfulResult

class CreditCardGateway:
    gateway: Any
    config: Any
    def __init__(self, gateway) -> None: ...
    def create(self, params: Incomplete | None = None): ...
    def delete(self, credit_card_token): ...
    def expired(self): ...
    def expiring_between(self, start_date, end_date): ...
    def find(self, credit_card_token): ...
    def forward(self, credit_card_token, receiving_merchant_id) -> None: ...
    def from_nonce(self, nonce): ...
    def update(self, credit_card_token, params: Incomplete | None = None): ...
