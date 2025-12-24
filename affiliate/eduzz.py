# affiliate/eduzz.py
class EduzzAdapter(AffiliateProvider):
platform = "eduzz"


def search_products(self, filters: Dict[str, Any]) -> List[AffiliateProduct]:
return []


def get_product(self, external_id: str) -> AffiliateProduct:
raise NotImplementedError


def generate_affiliate_link(self, external_id: str) -> str:
return f"https://eduzz.com/ref/{external_id}"


def validate_affiliation(self, external_id: str) -> bool:
return True


def normalize_product(self, raw_data: Dict[str, Any]) -> AffiliateProduct:
return AffiliateProduct()
