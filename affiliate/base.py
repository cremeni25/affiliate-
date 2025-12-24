# affiliate/base.py
from abc import ABC, abstractmethod
from typing import List, Dict, Any


class AffiliateProduct(dict):
"""Estrutura normalizada de produto afiliado."""
pass


class AffiliateProvider(ABC):
platform: str


@abstractmethod
def search_products(self, filters: Dict[str, Any]) -> List[AffiliateProduct]:
pass


@abstractmethod
def get_product(self, external_id: str) -> AffiliateProduct:
pass


@abstractmethod
def generate_affiliate_link(self, external_id: str) -> str:
pass


@abstractmethod
def validate_affiliation(self, external_id: str) -> bool:
pass


@abstractmethod
def normalize_product(self, raw_data: Dict[str, Any]) -> AffiliateProduct:
pass
