def calculate_delivery_cost(city: str, weight_kg: float) -> float:
    """Розраховує доставку лише з потрібних примітивних даних."""
    return (50.0 if city == "Ivano-Frankivsk" else 80.0 if city == "Kyiv" else 110.0) + (weight_kg * 12.0)


def process_standard_invoice(
    amount: float,
    city: str,
    weight_kg: float,
    tax_rate: float = 0.20,
) -> dict:
    """Звичайний рахунок з явно переданою ставкою податку."""
    delivery = calculate_delivery_cost(city, weight_kg)
    total = (amount * (1 + tax_rate)) + delivery
    return {"status": "PROCESSED", "total": round(total, 2)}


def process_tax_exempt_invoice(amount: float, city: str, weight_kg: float) -> dict:
    """Рахунок без податку; глобальний стан не змінюється."""
    total = amount + calculate_delivery_cost(city, weight_kg)
    return {"status": "TAX_EXEMPT", "total": round(total, 2)}
