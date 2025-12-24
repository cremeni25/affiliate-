# affiliate/hotmart.py
import requests
from typing import List, Dict, Any


class HotmartAdapter(AffiliateProvider):
platform = "hotmart"


def __init__(self, api_key: str):
self.api_key = api_key
self.base_url = "https://api.hotmart.com"


def search_products(self, filters: Dict[str, Any]) -> List[AffiliateProduct]:
return []


def get_product(self, external_id: str) -> AffiliateProduct:
raise NotImplementedError


def generate_affiliate_link(self, external_id: str) -> str:
return f"https://go.hotmart.com/{external_id}"


def validate_affiliation(self, external_id: str) -> bool:
return True


def normalize_product(self, raw_data: Dict[str, Any]) -> AffiliateProduct:
return AffiliateProduct()
