"""Exact business logic: Python calculates; AI only explains."""
from decimal import Decimal

PRICES = {"yam": Decimal("8.00"), "rice": Decimal("15.00"),
          "plantain": Decimal("5.00"), "tomatoes": Decimal("40.00")}


def quote(product: str, quantity: int) -> dict:
    product = product.strip().lower()
    if product not in PRICES:
        raise ValueError("Choose a product from the price board.")
    if type(quantity) is not int or not 1 <= quantity <= 100:
        raise ValueError("Quantity must be a whole number from 1 to 100.")
    price = PRICES[product]
    return {"product": product, "quantity": quantity, "currency": "GHS",
            "unit_price": str(price), "total": str(price * quantity)}


def receipt(item: dict) -> str:
    return (f"{item['quantity']} x {item['product']} @ GHS {item['unit_price']} "
            f"= GHS {item['total']}")
