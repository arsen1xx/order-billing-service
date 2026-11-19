# Release v1.1.0 - Data Coupling & Updated Tariffs

Порівняно з версією v1.0.0.

## Added

- Додано спеціальний базовий тариф доставки `80.0` для міста `Kyiv`.
- Додано явний параметр `tax_rate` для `process_standard_invoice()` зі значенням за замовчуванням `0.20`.

## Changed

- Коефіцієнт вартості доставки за вагу збільшено з `12.0` до `15.0` за кілограм.
- Виконано перехід від Common, Stamp і Control Coupling до Data Coupling: функції отримують лише необхідні дані.
- Тариф доставки становить `50.0` для `Ivano-Frankivsk`, `80.0` для `Kyiv` та `110.0` для інших міст.

## Breaking Changes

- Змінено сигнатури функцій розрахунку: `calculate_delivery_cost(city, weight_kg)`, `process_standard_invoice(amount, city, weight_kg, tax_rate=0.20)` та `process_tax_exempt_invoice(amount, city, weight_kg)`.
- Видалено глобальну змінну `GLOBAL_TAX_RATE`.
- Видалено прапорець режиму `mode_flag`; стандартний і неоподатковуваний сценарії тепер викликаються окремими функціями.
- Код, що використовував старі сигнатури або `CustomerProfile` як аргумент розрахунку, потрібно адаптувати.
