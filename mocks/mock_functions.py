"""Mock recommendation and evaluation functions for the Streamlit UI.

Expanded mock dataset version.
These functions intentionally do not implement real machine learning. They
return realistic, deterministic sample data that follows the agreed project
schema so other members can later replace these imports with real functions.

Dataset size: 80 products across multiple e-commerce categories.
"""

from __future__ import annotations

import hashlib
import math
import random
from typing import Any


PRODUCT_CATALOG: list[dict[str, Any]] = [
    {
        "product_id": "P1001",
        "title": "Sony WH-1000XM5 Wireless Noise-Canceling Headphones",
        "brand": "Sony",
        "category": "Headphones",
        "price": 399.99,
        "battery_hrs": 30,
    },
    {
        "product_id": "P1002",
        "title": "Apple AirPods Pro 2nd Generation",
        "brand": "Apple",
        "category": "Headphones",
        "price": 249.0,
        "battery_hrs": 24,
    },
    {
        "product_id": "P1008",
        "title": "Bose QuietComfort Ultra Headphones",
        "brand": "Bose",
        "category": "Headphones",
        "price": 429.0,
        "battery_hrs": 24,
    },
    {
        "product_id": "P1022",
        "title": "Beats Studio Pro Wireless Headphones",
        "brand": "Beats",
        "category": "Headphones",
        "price": 349.99,
        "battery_hrs": 40,
    },
    {
        "product_id": "P1025",
        "title": "Anker Soundcore Space Q45 Headphones",
        "brand": "Anker",
        "category": "Headphones",
        "price": 149.99,
        "battery_hrs": 50,
    },
    {
        "product_id": "P1026",
        "title": "JBL Tune 770NC Wireless Headphones",
        "brand": "JBL",
        "category": "Headphones",
        "price": 129.95,
        "battery_hrs": 70,
    },
    {
        "product_id": "P1027",
        "title": "Sennheiser Momentum 4 Wireless Headphones",
        "brand": "Sennheiser",
        "category": "Headphones",
        "price": 379.95,
        "battery_hrs": 60,
    },
    {
        "product_id": "P1028",
        "title": "Sony WF-1000XM5 True Wireless Earbuds",
        "brand": "Sony",
        "category": "Headphones",
        "price": 299.99,
        "battery_hrs": 24,
    },
    {
        "product_id": "P1029",
        "title": "Samsung Galaxy Buds2 Pro",
        "brand": "Samsung",
        "category": "Headphones",
        "price": 229.99,
        "battery_hrs": 29,
    },
    {
        "product_id": "P1030",
        "title": "Bose QuietComfort Earbuds II",
        "brand": "Bose",
        "category": "Headphones",
        "price": 279.0,
        "battery_hrs": 24,
    },
    {
        "product_id": "P1003",
        "title": "Samsung Galaxy S24 256GB Smartphone",
        "brand": "Samsung",
        "category": "Smartphone",
        "price": 859.99,
        "battery_hrs": 28,
    },
    {
        "product_id": "P1004",
        "title": "Apple iPhone 15 128GB Smartphone",
        "brand": "Apple",
        "category": "Smartphone",
        "price": 799.0,
        "battery_hrs": 20,
    },
    {
        "product_id": "P1023",
        "title": "OnePlus 12 512GB Smartphone",
        "brand": "OnePlus",
        "category": "Smartphone",
        "price": 799.99,
        "battery_hrs": 26,
    },
    {
        "product_id": "P1024",
        "title": "Google Pixel 8 Pro Smartphone",
        "brand": "Google",
        "category": "Smartphone",
        "price": 899.0,
        "battery_hrs": 24,
    },
    {
        "product_id": "P1031",
        "title": "Samsung Galaxy A55 5G Smartphone",
        "brand": "Samsung",
        "category": "Smartphone",
        "price": 449.99,
        "battery_hrs": 32,
    },
    {
        "product_id": "P1032",
        "title": "Xiaomi Redmi Note 13 Pro Smartphone",
        "brand": "Xiaomi",
        "category": "Smartphone",
        "price": 329.99,
        "battery_hrs": 34,
    },
    {
        "product_id": "P1033",
        "title": "Nothing Phone 2a Smartphone",
        "brand": "Nothing",
        "category": "Smartphone",
        "price": 349.0,
        "battery_hrs": 30,
    },
    {
        "product_id": "P1034",
        "title": "Motorola Edge 50 Pro Smartphone",
        "brand": "Motorola",
        "category": "Smartphone",
        "price": 599.99,
        "battery_hrs": 31,
    },
    {
        "product_id": "P1035",
        "title": "Apple iPhone 15 Pro 256GB Smartphone",
        "brand": "Apple",
        "category": "Smartphone",
        "price": 1099.0,
        "battery_hrs": 23,
    },
    {
        "product_id": "P1036",
        "title": "Google Pixel 8a Smartphone",
        "brand": "Google",
        "category": "Smartphone",
        "price": 499.0,
        "battery_hrs": 25,
    },
    {
        "product_id": "P1005",
        "title": "Dell XPS 13 Plus Ultrabook",
        "brand": "Dell",
        "category": "Laptop",
        "price": 1249.99,
        "battery_hrs": 13,
    },
    {
        "product_id": "P1006",
        "title": "HP Spectre x360 14 Convertible Laptop",
        "brand": "HP",
        "category": "Laptop",
        "price": 1199.99,
        "battery_hrs": 15,
    },
    {
        "product_id": "P1007",
        "title": "Lenovo ThinkPad X1 Carbon Gen 12",
        "brand": "Lenovo",
        "category": "Laptop",
        "price": 1499.0,
        "battery_hrs": 16,
    },
    {
        "product_id": "P1020",
        "title": "Microsoft Surface Laptop 5",
        "brand": "Microsoft",
        "category": "Laptop",
        "price": 999.99,
        "battery_hrs": 17,
    },
    {
        "product_id": "P1037",
        "title": "Apple MacBook Air M3 13-Inch",
        "brand": "Apple",
        "category": "Laptop",
        "price": 1099.0,
        "battery_hrs": 18,
    },
    {
        "product_id": "P1038",
        "title": "ASUS Zenbook 14 OLED Laptop",
        "brand": "ASUS",
        "category": "Laptop",
        "price": 899.99,
        "battery_hrs": 14,
    },
    {
        "product_id": "P1039",
        "title": "Acer Swift Go 14 Laptop",
        "brand": "Acer",
        "category": "Laptop",
        "price": 749.99,
        "battery_hrs": 12,
    },
    {
        "product_id": "P1040",
        "title": "Lenovo Legion 5 Gaming Laptop",
        "brand": "Lenovo",
        "category": "Laptop",
        "price": 1299.0,
        "battery_hrs": 8,
    },
    {
        "product_id": "P1041",
        "title": "HP Victus 16 Gaming Laptop",
        "brand": "HP",
        "category": "Laptop",
        "price": 999.99,
        "battery_hrs": 7,
    },
    {
        "product_id": "P1042",
        "title": "Dell Inspiron 15 Student Laptop",
        "brand": "Dell",
        "category": "Laptop",
        "price": 649.99,
        "battery_hrs": 10,
    },
    {
        "product_id": "P1043",
        "title": "ASUS ROG Zephyrus G14 Gaming Laptop",
        "brand": "ASUS",
        "category": "Laptop",
        "price": 1599.99,
        "battery_hrs": 10,
    },
    {
        "product_id": "P1044",
        "title": "MSI Modern 15 Business Laptop",
        "brand": "MSI",
        "category": "Laptop",
        "price": 699.99,
        "battery_hrs": 11,
    },
    {
        "product_id": "P1009",
        "title": "Samsung Galaxy Tab S9 11-Inch Tablet",
        "brand": "Samsung",
        "category": "Tablet",
        "price": 699.99,
        "battery_hrs": 15,
    },
    {
        "product_id": "P1010",
        "title": "Apple iPad Air 10.9-Inch Tablet",
        "brand": "Apple",
        "category": "Tablet",
        "price": 599.0,
        "battery_hrs": 10,
    },
    {
        "product_id": "P1021",
        "title": "Amazon Kindle Paperwhite Signature Edition",
        "brand": "Amazon",
        "category": "Tablet",
        "price": 189.99,
        "battery_hrs": 240,
    },
    {
        "product_id": "P1045",
        "title": "Apple iPad Pro 11-Inch M4 Tablet",
        "brand": "Apple",
        "category": "Tablet",
        "price": 999.0,
        "battery_hrs": 10,
    },
    {
        "product_id": "P1046",
        "title": "Lenovo Tab P12 Tablet",
        "brand": "Lenovo",
        "category": "Tablet",
        "price": 349.99,
        "battery_hrs": 12,
    },
    {
        "product_id": "P1047",
        "title": "Xiaomi Pad 6 Tablet",
        "brand": "Xiaomi",
        "category": "Tablet",
        "price": 399.99,
        "battery_hrs": 13,
    },
    {
        "product_id": "P1048",
        "title": "Microsoft Surface Pro 9 Tablet",
        "brand": "Microsoft",
        "category": "Tablet",
        "price": 1099.99,
        "battery_hrs": 10,
    },
    {
        "product_id": "P1049",
        "title": "Samsung Galaxy Tab A9 Plus Tablet",
        "brand": "Samsung",
        "category": "Tablet",
        "price": 249.99,
        "battery_hrs": 13,
    },
    {
        "product_id": "P1011",
        "title": "Garmin Venu 3 Fitness Smartwatch",
        "brand": "Garmin",
        "category": "Smartwatch",
        "price": 449.99,
        "battery_hrs": 336,
    },
    {
        "product_id": "P1012",
        "title": "Apple Watch Series 9 GPS",
        "brand": "Apple",
        "category": "Smartwatch",
        "price": 399.0,
        "battery_hrs": 18,
    },
    {
        "product_id": "P1019",
        "title": "Samsung Galaxy Watch 6 Classic",
        "brand": "Samsung",
        "category": "Smartwatch",
        "price": 399.99,
        "battery_hrs": 40,
    },
    {
        "product_id": "P1050",
        "title": "Fitbit Versa 4 Fitness Smartwatch",
        "brand": "Fitbit",
        "category": "Smartwatch",
        "price": 199.95,
        "battery_hrs": 144,
    },
    {
        "product_id": "P1051",
        "title": "Garmin Forerunner 265 Running Watch",
        "brand": "Garmin",
        "category": "Smartwatch",
        "price": 449.99,
        "battery_hrs": 312,
    },
    {
        "product_id": "P1052",
        "title": "Huawei Watch GT 4 Smartwatch",
        "brand": "Huawei",
        "category": "Smartwatch",
        "price": 249.99,
        "battery_hrs": 336,
    },
    {
        "product_id": "P1053",
        "title": "Amazfit GTR 4 Smartwatch",
        "brand": "Amazfit",
        "category": "Smartwatch",
        "price": 199.99,
        "battery_hrs": 336,
    },
    {
        "product_id": "P1054",
        "title": "Apple Watch SE 2nd Generation",
        "brand": "Apple",
        "category": "Smartwatch",
        "price": 249.0,
        "battery_hrs": 18,
    },
    {
        "product_id": "P1013",
        "title": "JBL Charge 5 Portable Bluetooth Speaker",
        "brand": "JBL",
        "category": "Speaker",
        "price": 179.95,
        "battery_hrs": 20,
    },
    {
        "product_id": "P1014",
        "title": "Sonos Roam 2 Smart Portable Speaker",
        "brand": "Sonos",
        "category": "Speaker",
        "price": 179.0,
        "battery_hrs": 10,
    },
    {
        "product_id": "P1018",
        "title": "Sony SRS-XG300 Portable Party Speaker",
        "brand": "Sony",
        "category": "Speaker",
        "price": 349.99,
        "battery_hrs": 25,
    },
    {
        "product_id": "P1055",
        "title": "Bose SoundLink Flex Bluetooth Speaker",
        "brand": "Bose",
        "category": "Speaker",
        "price": 149.0,
        "battery_hrs": 12,
    },
    {
        "product_id": "P1056",
        "title": "Anker Soundcore Motion X600 Speaker",
        "brand": "Anker",
        "category": "Speaker",
        "price": 199.99,
        "battery_hrs": 12,
    },
    {
        "product_id": "P1057",
        "title": "Marshall Emberton II Portable Speaker",
        "brand": "Marshall",
        "category": "Speaker",
        "price": 169.99,
        "battery_hrs": 30,
    },
    {
        "product_id": "P1058",
        "title": "JBL Flip 6 Bluetooth Speaker",
        "brand": "JBL",
        "category": "Speaker",
        "price": 129.95,
        "battery_hrs": 12,
    },
    {
        "product_id": "P1059",
        "title": "Ultimate Ears BOOM 3 Speaker",
        "brand": "Ultimate Ears",
        "category": "Speaker",
        "price": 149.99,
        "battery_hrs": 15,
    },
    {
        "product_id": "P1015",
        "title": "Logitech MX Master 3S Wireless Mouse",
        "brand": "Logitech",
        "category": "Accessory",
        "price": 99.99,
        "battery_hrs": 70,
    },
    {
        "product_id": "P1016",
        "title": "Logitech MX Keys S Wireless Keyboard",
        "brand": "Logitech",
        "category": "Accessory",
        "price": 109.99,
        "battery_hrs": 240,
    },
    {
        "product_id": "P1017",
        "title": "Anker 737 Power Bank 24,000mAh",
        "brand": "Anker",
        "category": "Accessory",
        "price": 159.99,
        "battery_hrs": 80,
    },
    {
        "product_id": "P1060",
        "title": "Samsung 45W USB-C Fast Charger",
        "brand": "Samsung",
        "category": "Accessory",
        "price": 49.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1061",
        "title": "Apple MagSafe Charger",
        "brand": "Apple",
        "category": "Accessory",
        "price": 39.0,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1062",
        "title": "SanDisk Extreme Portable SSD 1TB",
        "brand": "SanDisk",
        "category": "Accessory",
        "price": 109.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1063",
        "title": "Kingston DataTraveler USB-C Flash Drive 256GB",
        "brand": "Kingston",
        "category": "Accessory",
        "price": 39.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1064",
        "title": "Logitech C920 HD Pro Webcam",
        "brand": "Logitech",
        "category": "Accessory",
        "price": 79.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1065",
        "title": "Razer DeathAdder V3 Gaming Mouse",
        "brand": "Razer",
        "category": "Accessory",
        "price": 69.99,
        "battery_hrs": 90,
    },
    {
        "product_id": "P1066",
        "title": "Keychron K2 Wireless Mechanical Keyboard",
        "brand": "Keychron",
        "category": "Accessory",
        "price": 89.99,
        "battery_hrs": 240,
    },
    {
        "product_id": "P1067",
        "title": "Canon EOS R50 Mirrorless Camera",
        "brand": "Canon",
        "category": "Camera",
        "price": 679.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1068",
        "title": "Sony ZV-E10 Creator Camera",
        "brand": "Sony",
        "category": "Camera",
        "price": 699.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1069",
        "title": "GoPro HERO12 Black Action Camera",
        "brand": "GoPro",
        "category": "Camera",
        "price": 399.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1070",
        "title": "DJI Osmo Pocket 3 Creator Camera",
        "brand": "DJI",
        "category": "Camera",
        "price": 519.99,
        "battery_hrs": 2,
    },
    {
        "product_id": "P1071",
        "title": "Sony PlayStation 5 Slim Console",
        "brand": "Sony",
        "category": "Gaming",
        "price": 499.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1072",
        "title": "Microsoft Xbox Series X Console",
        "brand": "Microsoft",
        "category": "Gaming",
        "price": 499.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1073",
        "title": "Nintendo Switch OLED Console",
        "brand": "Nintendo",
        "category": "Gaming",
        "price": 349.99,
        "battery_hrs": 6,
    },
    {
        "product_id": "P1074",
        "title": "Sony DualSense Wireless Controller",
        "brand": "Sony",
        "category": "Gaming",
        "price": 69.99,
        "battery_hrs": 12,
    },
    {
        "product_id": "P1075",
        "title": "Razer BlackShark V2 Gaming Headset",
        "brand": "Razer",
        "category": "Gaming",
        "price": 99.99,
        "battery_hrs": 24,
    },
    {
        "product_id": "P1076",
        "title": "Amazon Echo Dot 5th Gen Smart Speaker",
        "brand": "Amazon",
        "category": "Smart Home",
        "price": 49.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1077",
        "title": "Google Nest Hub 2nd Gen",
        "brand": "Google",
        "category": "Smart Home",
        "price": 99.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1078",
        "title": "Philips Hue Smart Bulb Starter Kit",
        "brand": "Philips",
        "category": "Smart Home",
        "price": 129.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1079",
        "title": "TP-Link Tapo Smart Plug Mini",
        "brand": "TP-Link",
        "category": "Smart Home",
        "price": 19.99,
        "battery_hrs": 0,
    },
    {
        "product_id": "P1080",
        "title": "Ring Video Doorbell Wired",
        "brand": "Ring",
        "category": "Smart Home",
        "price": 64.99,
        "battery_hrs": 0,
    },
]


CF_METHOD_OFFSETS = {
    "user_based": 0.13,
    "item_based": 0.04,
    "svd": 0.20,
    "als": 0.10,
}

CONTENT_METHOD_OFFSETS = {
    "tfidf": 0.12,
    "feature_based": 0.22,
}


def _stable_seed(*parts: object) -> int:
    """Create a deterministic seed from arbitrary inputs for repeatable mocks."""
    seed_text = "|".join(str(part) for part in parts)
    digest = hashlib.sha256(seed_text.encode("utf-8")).hexdigest()
    return int(digest[:12], 16)


def _score_product(base_score: float, product: dict[str, Any], offset: float, index: int) -> float:
    """Generate a realistic score between 0.0 and 5.0 for one product."""
    brand_signal = (sum(ord(char) for char in product["brand"]) % 9) / 100
    price_penalty = min(float(product["price"]) / 5000, 0.25)
    category_bonus = 0.08 if product["category"] in {"Headphones", "Laptop", "Smartphone", "Gaming"} else 0.02
    rank_variation = max(0.0, 0.28 - index * 0.025)
    score = base_score + offset + brand_signal + category_bonus + rank_variation - price_penalty
    return round(min(max(score, 3.25), 4.95), 2)


def _format_product(product: dict[str, Any], score: float, reason: str) -> dict:
    """Return one product using the exact shared recommendation schema."""
    return {
        "product_id": str(product["product_id"]),
        "title": str(product["title"]),
        "brand": str(product["brand"]),
        "category": str(product["category"]),
        "price": float(product["price"]),
        "score": float(score),
        "reason": reason,
    }


def _sample_products(seed: int, top_n: int) -> list[dict[str, Any]]:
    """Return a deterministic shuffled sample from the mock product catalog."""
    rng = random.Random(seed)
    products = PRODUCT_CATALOG.copy()
    rng.shuffle(products)
    return products[: max(1, min(top_n, len(products)))]


def cf_recommend(user_id: str, method: str, top_n: int = 10) -> list[dict]:
    """Mock collaborative filtering recommendations."""
    if method not in CF_METHOD_OFFSETS:
        raise ValueError("method must be one of: 'user_based', 'item_based', 'svd', 'als'")

    seed = _stable_seed("cf", user_id, method)
    products = _sample_products(seed, top_n)
    base_score = 4.12 + (seed % 17) / 100
    reason = "Because users similar to you also rated this highly"

    recommendations = [
        _format_product(
            product,
            _score_product(base_score, product, CF_METHOD_OFFSETS[method], index),
            reason,
        )
        for index, product in enumerate(products)
    ]
    return sorted(recommendations, key=lambda item: item["score"], reverse=True)


def cb_recommend(product_id: str, method: str, top_n: int = 10) -> list[dict]:
    """Mock content-based recommendations."""
    if method not in CONTENT_METHOD_OFFSETS:
        raise ValueError("method must be one of: 'tfidf', 'feature_based'")

    reference_product = next(
        (product for product in PRODUCT_CATALOG if product["product_id"] == product_id),
        PRODUCT_CATALOG[0],
    )
    candidates = [product for product in PRODUCT_CATALOG if product["product_id"] != reference_product["product_id"]]

    def similarity_key(product: dict[str, Any]) -> tuple[int, int, float]:
        same_category = int(product["category"] == reference_product["category"])
        same_brand = int(product["brand"] == reference_product["brand"])
        price_distance = abs(float(product["price"]) - float(reference_product["price"]))
        return same_category, same_brand, -price_distance

    ranked = sorted(candidates, key=similarity_key, reverse=True)
    seed = _stable_seed("cb", product_id, method)
    top_pool = ranked[: max(top_n * 3, top_n)]
    rng = random.Random(seed)
    rng.shuffle(top_pool)
    products = sorted(top_pool[:top_n], key=similarity_key, reverse=True)
    base_score = 4.05 + (seed % 13) / 100
    reason = "Matches the category and brand of products you viewed"

    recommendations = [
        _format_product(
            product,
            _score_product(base_score, product, CONTENT_METHOD_OFFSETS[method], index),
            reason,
        )
        for index, product in enumerate(products)
    ]
    return sorted(recommendations, key=lambda item: item["score"], reverse=True)


def kb_recommend(constraints: dict, top_n: int = 10) -> list[dict]:
    """Mock knowledge-based recommendations."""
    max_price = float(constraints.get("max_price", 2000))
    preferred_brand = constraints.get("brand")
    preferred_category = constraints.get("category")
    min_battery_hrs = int(constraints.get("min_battery_hrs", 0))

    filtered_products = []
    for product in PRODUCT_CATALOG:
        if float(product["price"]) > max_price:
            continue
        if preferred_brand and product["brand"] != preferred_brand:
            continue
        if preferred_category and product["category"] != preferred_category:
            continue
        if int(product["battery_hrs"]) < min_battery_hrs:
            continue
        filtered_products.append(product)

    if len(filtered_products) < top_n:
        backup_products = [product for product in PRODUCT_CATALOG if product not in filtered_products]
        backup_products = sorted(
            backup_products,
            key=lambda product: (
                float(product["price"]) <= max_price,
                int(product["battery_hrs"]) >= min_battery_hrs,
                -abs(float(product["price"]) - max_price),
            ),
            reverse=True,
        )
        filtered_products.extend(backup_products)

    def constraint_score(product: dict[str, Any]) -> tuple[float, float]:
        price_fit = max(0.0, 1.0 - abs(float(product["price"]) - max_price) / max(max_price, 1.0))
        battery_fit = min(int(product["battery_hrs"]) / max(min_battery_hrs, 1), 2.0)
        brand_fit = 1.0 if preferred_brand and product["brand"] == preferred_brand else 0.0
        category_fit = 1.0 if preferred_category and product["category"] == preferred_category else 0.0
        total = price_fit + battery_fit + brand_fit + category_fit
        return total, -float(product["price"])

    ranked_products = sorted(filtered_products, key=constraint_score, reverse=True)[:top_n]
    reason = "Matches your budget and specified constraints"

    recommendations = []
    for index, product in enumerate(ranked_products):
        score = 3.75 + min(constraint_score(product)[0] * 0.28, 1.05) - index * 0.03
        recommendations.append(_format_product(product, round(min(max(score, 3.35), 4.92), 2), reason))

    return sorted(recommendations, key=lambda item: item["score"], reverse=True)


def evaluate(actual: list, predicted: list, metric: str) -> float:
    """Mock evaluation metric function."""
    if metric not in {"mae", "rmse", "precision_at_k", "coverage"}:
        raise ValueError("metric must be one of: 'mae', 'rmse', 'precision_at_k', or 'coverage'")

    actual_values = [float(value) for value in actual] or [4.0]
    predicted_values = [
        float(item.get("score", 0.0)) if isinstance(item, dict) else float(item)
        for item in predicted
    ] or [4.0]
    pairs = list(zip(actual_values, predicted_values))

    if metric == "mae":
        return round(sum(abs(actual - pred) for actual, pred in pairs) / len(pairs), 3)

    if metric == "rmse":
        mse = sum((actual - pred) ** 2 for actual, pred in pairs) / len(pairs)
        return round(math.sqrt(mse), 3)

    if metric == "precision_at_k":
        relevant_predictions = sum(1 for pred in predicted_values if pred >= 4.0)
        return round(relevant_predictions / len(predicted_values), 3)

    unique_recommendations = len({round(pred, 2) for pred in predicted_values})
    return round(min(1.0, 0.55 + unique_recommendations / 20), 3)
