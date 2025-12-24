# affiliate/monetizze.py
class MonetizzeAdapter(AffiliateProvider):
platform = "monetizze"


def search_products(self, filters: Dict[str, Any]) -> List[AffiliateProduct]:
raise NotImplementedError


def get_product(self, external_id: str) -> AffiliateProduct:
raise NotImplementedError


def generate_affiliate_link(self, external_id: str) -> str:
raise NotImplementedError


def validate_affiliation(self, external_id: str) -> bool:
raise NotImplementedError


def normalize_product(self, raw_data: Dict[str, Any]) -> AffiliateProduct:
raise NotImplementedError
