"""
Professional Streamlit Website UI for SmartShop AI
--------------------------------------------------
A website-style interface for the Intelligent E-Commerce Recommendation System.

Important:
- This UI reads product data from mocks/mock_functions.py using PRODUCT_CATALOG.
- It uses the existing mock recommendation functions:
  cf_recommend, cb_recommend, kb_recommend, evaluate
- The recommendation logic is not rewritten; this file focuses on UI and website experience.
"""

from __future__ import annotations

import hashlib
import os
from typing import Any

import pandas as pd
import streamlit as st

from mocks.mock_functions import (
    PRODUCT_CATALOG,
    cf_recommend,
    cb_recommend,
    kb_recommend,
    evaluate,
)


# ============================================================
# App Constants
# ============================================================

APP_TITLE = "RecomXpert"
APP_SUBTITLE = "AI-Powered Product Discovery Platform"
COURSE_LABEL = "AIE425 · Intelligent Recommender System"

APPROACH_OPTIONS = {
    "Collaborative Filtering": "cf",
    "Content-Based Recommendation": "content",
    "Knowledge-Based Recommendation": "knowledge",
}

CF_METHOD_LABELS = {
    "User-Based CF": "user_based",
    "Item-Based CF": "item_based",
    "SVD Matrix Factorization": "svd",
    "ALS Matrix Factorization": "als",
}

CONTENT_METHOD_LABELS = {
    "TF-IDF Similarity": "tfidf",
    "Feature-Based Similarity": "feature_based",
}

KNOWLEDGE_METHOD_LABELS = {
    "Constraint Matching": "constraint_matching",
}


# ============================================================
# Page Config
# ============================================================

st.set_page_config(
    page_title="RecomXpert",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# Data Helpers
# ============================================================

def stable_number(text: str, modulo: int, offset: int = 0) -> int:
    """Return a deterministic number for mock UI-only values."""
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return int(digest[:8], 16) % modulo + offset


def image_for_category(category: str, product_id: str) -> str:
    """Return stable direct image URLs for each category.

    Important:
    source.unsplash.com sometimes fails in Streamlit because it redirects.
    These are direct images.unsplash.com URLs, so they display more reliably.
    """
    image_pool = {
        "Smartphone": [
            "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=900&auto=format&fit=crop&q=80",
        ],
        "Headphones": [
            "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1484704849700-f032a568e944?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=900&auto=format&fit=crop&q=80",
        ],
        "Laptop": [
            "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=900&auto=format&fit=crop&q=80",
        ],
        "Tablet": [
            "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1586864387967-d02ef85d93e8?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1561154464-82e9adf32764?w=900&auto=format&fit=crop&q=80",
        ],
        "Smartwatch": [
            "https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=900&auto=format&fit=crop&q=80",
        ],
        "Speaker": [
            "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1542193810-9007c21cd37e?w=900&auto=format&fit=crop&q=80",
        ],
        "Accessory": [
            "https://images.unsplash.com/photo-1527814050087-3793815479db?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1580894908361-967195033215?w=900&auto=format&fit=crop&q=80",
        ],
        "Camera": [
            "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1495121553079-4c61bcce1894?w=900&auto=format&fit=crop&q=80",
        ],
        "Gaming": [
            "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1605901309584-818e25960a8f?w=900&auto=format&fit=crop&q=80",
        ],
        "Smart Home": [
            "https://images.unsplash.com/photo-1558002038-1055907df827?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1558089687-f282ffcbc126?w=900&auto=format&fit=crop&q=80",
            "https://images.unsplash.com/photo-1518444065439-e933c06ce9cd?w=900&auto=format&fit=crop&q=80",
        ],
    }

    fallback = [
        "https://images.unsplash.com/photo-1498049794561-7780e7231661?w=900&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=900&auto=format&fit=crop&q=80",
        "https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=900&auto=format&fit=crop&q=80",
    ]

    images = image_pool.get(category, fallback)
    index = stable_number(product_id + category, len(images), 0)
    return images[index]


@st.cache_data
def load_products() -> pd.DataFrame:
    """Load products from PRODUCT_CATALOG and enrich them for website UI."""
    df = pd.DataFrame(PRODUCT_CATALOG).copy()

    # Keep compatibility with older catalog names if needed.
    if "title" not in df.columns and "name" in df.columns:
        df["title"] = df["name"]

    df["price"] = df["price"].astype(float)
    df["battery_hrs"] = df["battery_hrs"].fillna(0).astype(int)

    # UI-only fields derived deterministically.
    df["rating"] = df["product_id"].apply(lambda pid: round(4.1 + stable_number(pid, 9) / 10, 1))
    df["rating"] = df["rating"].clip(upper=4.9)
    df["stock"] = df["product_id"].apply(lambda pid: stable_number(pid + "stock", 44, 6))
    df["reviews"] = df["product_id"].apply(lambda pid: stable_number(pid + "reviews", 1800, 85))
    df["discount"] = df["product_id"].apply(lambda pid: stable_number(pid + "discount", 22, 0))
    df["image"] = df.apply(lambda row: image_for_category(row["category"], row["product_id"]), axis=1)

    df["description"] = df.apply(
        lambda row: (
            f"{row['title']} by {row['brand']} is a {row['category'].lower()} product designed "
            f"for customers looking for reliable performance, strong value, and modern features."
        ),
        axis=1,
    )

    df["sale_price"] = df.apply(
        lambda row: row["price"] * (1 - row["discount"] / 100) if row["discount"] > 0 else row["price"],
        axis=1,
    )

    return df


def recommendation_to_df(recommendations: list[dict[str, Any]], products: pd.DataFrame) -> pd.DataFrame:
    """Merge recommendation results with UI product fields."""
    rec_df = pd.DataFrame(recommendations)
    if rec_df.empty:
        return rec_df

    ui_cols = [
        "product_id",
        "battery_hrs",
        "rating",
        "stock",
        "reviews",
        "discount",
        "image",
        "description",
        "sale_price",
    ]
    return rec_df.merge(products[ui_cols], on="product_id", how="left")


@st.cache_data
def load_popularity_data() -> pd.DataFrame:
    """Load real/semi-real popularity interaction data from CSV.

    Expected path:
        data/popularity_products.csv

    This is intentionally separated from the mock recommendation catalog so
    the extra Popularity-Based approach can use real interaction columns while
    the three required approaches remain unchanged.
    """
    csv_path = os.path.join("data", "popularity_products.csv")

    if not os.path.exists(csv_path):
        st.error(
            "Missing file: data/popularity_products.csv. "
            "Please place popularity_products.csv inside the data folder."
        )
        return pd.DataFrame()

    df = pd.read_csv(csv_path)
    required_cols = {
        "product_id",
        "title",
        "brand",
        "category",
        "price",
        "avg_rating",
        "reviews_count",
        "views",
        "cart_adds",
        "purchases",
        "last_30_days_sales",
        "last_7_days_sales",
        "return_rate",
        "stock",
        "discount_percent",
        "launch_date",
    }

    missing = required_cols - set(df.columns)
    if missing:
        st.error(f"Popularity CSV is missing columns: {sorted(missing)}")
        return pd.DataFrame()

    numeric_cols = [
        "price",
        "avg_rating",
        "reviews_count",
        "views",
        "cart_adds",
        "purchases",
        "last_30_days_sales",
        "last_7_days_sales",
        "return_rate",
        "stock",
        "discount_percent",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df["image"] = df.apply(lambda row: image_for_category(row["category"], row["product_id"]), axis=1)
    df["description"] = df.apply(
        lambda row: (
            f"{row['title']} by {row['brand']} is trending in {row['category']} based on "
            f"{int(row['views'])} views, {int(row['purchases'])} purchases, and "
            f"{int(row['reviews_count'])} reviews."
        ),
        axis=1,
    )
    df["rating"] = df["avg_rating"]
    df["reviews"] = df["reviews_count"]
    df["discount"] = df["discount_percent"]
    df["sale_price"] = df.apply(
        lambda row: float(row["price"]) * (1 - float(row["discount_percent"]) / 100),
        axis=1,
    )

    return df


def normalize_series(series: pd.Series) -> pd.Series:
    """Normalize a numeric series to 0..1 safely."""
    series = pd.to_numeric(series, errors="coerce").fillna(0)
    min_value = series.min()
    max_value = series.max()
    if max_value == min_value:
        return pd.Series([0.0] * len(series), index=series.index)
    return (series - min_value) / (max_value - min_value)


def compute_popularity_score(df: pd.DataFrame) -> pd.DataFrame:
    """Compute a weighted popularity score using interaction signals."""
    df = df.copy()

    df["views_norm"] = normalize_series(df["views"])
    df["purchases_norm"] = normalize_series(df["purchases"])
    df["reviews_norm"] = normalize_series(df["reviews_count"])
    df["rating_norm"] = normalize_series(df["avg_rating"])
    df["cart_norm"] = normalize_series(df["cart_adds"])
    df["trend_norm"] = normalize_series(df["last_7_days_sales"])
    df["return_norm"] = normalize_series(df["return_rate"])

    df["popularity_score"] = (
        0.28 * df["purchases_norm"]
        + 0.22 * df["views_norm"]
        + 0.18 * df["reviews_norm"]
        + 0.15 * df["rating_norm"]
        + 0.10 * df["cart_norm"]
        + 0.10 * df["trend_norm"]
        - 0.05 * df["return_norm"]
    )

    df["popularity_score"] = (df["popularity_score"] * 100).round(2)
    return df.sort_values("popularity_score", ascending=False)


def popularity_recommend(df: pd.DataFrame, method: str, top_n: int = 8) -> pd.DataFrame:
    """Return popularity-based recommendations using different simple methods."""
    if df.empty:
        return df

    if method == "Most Purchased":
        result = df.sort_values("purchases", ascending=False)

    elif method == "Most Viewed":
        result = df.sort_values("views", ascending=False)

    elif method == "Best Rated":
        result = df.sort_values(["avg_rating", "reviews_count"], ascending=False)

    elif method == "Trending This Week":
        result = df.sort_values(["last_7_days_sales", "last_30_days_sales"], ascending=False)

    else:
        result = compute_popularity_score(df)

    return result.head(top_n).copy()


def get_popularity_reason(row: pd.Series, method: str) -> str:
    """Generate a clear explanation for popularity-based recommendations."""
    if method == "Most Purchased":
        return (
            f"Recommended because it has one of the highest purchase counts "
            f"with {int(row['purchases'])} purchases."
        )

    if method == "Most Viewed":
        return (
            f"Recommended because customers viewed it frequently "
            f"with {int(row['views'])} total views."
        )

    if method == "Best Rated":
        return (
            f"Recommended because it has a strong average rating of "
            f"{float(row['avg_rating']):.2f}/5 based on {int(row['reviews_count'])} reviews."
        )

    if method == "Trending This Week":
        return (
            f"Recommended because it is trending recently with "
            f"{int(row['last_7_days_sales'])} sales in the last 7 days."
        )

    return (
        "Recommended using a weighted popularity score combining purchases, views, "
        "ratings, reviews, cart additions, recent sales, and return rate."
    )


# ============================================================
# Session State
# ============================================================

def initialize_session_state(products: pd.DataFrame) -> None:
    defaults = {
        "page": "Home",
        "user_id": "U1001",
        "product_id": str(products.iloc[0]["product_id"]),
        "approach_label": "Collaborative Filtering",
        "method_label": "User-Based CF",
        "top_n": 8,
        "max_price": float(min(1200, products["price"].max())),
        "preferred_brand": "Any",
        "preferred_category": "Any",
        "min_battery_hrs": 0,
        "selected_product_details": str(products.iloc[0]["product_id"]),
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def get_method_options(approach_label: str) -> list[str]:
    approach_key = APPROACH_OPTIONS[approach_label]
    if approach_key == "cf":
        return list(CF_METHOD_LABELS.keys())
    if approach_key == "content":
        return list(CONTENT_METHOD_LABELS.keys())
    return list(KNOWLEDGE_METHOD_LABELS.keys())


def build_constraints() -> dict:
    constraints = {
        "max_price": float(st.session_state.max_price),
        "min_battery_hrs": int(st.session_state.min_battery_hrs),
    }
    if st.session_state.preferred_brand != "Any":
        constraints["brand"] = st.session_state.preferred_brand
    if st.session_state.preferred_category != "Any":
        constraints["category"] = st.session_state.preferred_category
    return constraints


def get_recommendations(products: pd.DataFrame) -> pd.DataFrame:
    approach_key = APPROACH_OPTIONS[st.session_state.approach_label]
    top_n = int(st.session_state.top_n)

    if approach_key == "cf":
        method = CF_METHOD_LABELS[st.session_state.method_label]
        recs = cf_recommend(st.session_state.user_id, method, top_n=top_n)
        return recommendation_to_df(recs, products)

    if approach_key == "content":
        method = CONTENT_METHOD_LABELS[st.session_state.method_label]
        recs = cb_recommend(st.session_state.product_id, method, top_n=top_n)
        return recommendation_to_df(recs, products)

    recs = kb_recommend(build_constraints(), top_n=top_n)
    return recommendation_to_df(recs, products)


# ============================================================
# CSS Styling
# ============================================================

def inject_css() -> None:
    st.markdown(
        """
        <style>
        :root {
            --navy: #0F172A;
            --blue: #2563EB;
            --sky: #38BDF8;
            --orange: #F97316;
            --muted: #64748B;
            --card: #FFFFFF;
            --line: #E2E8F0;
            --bg: #F8FAFC;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.12), transparent 30%),
                radial-gradient(circle at top right, rgba(249, 115, 22, 0.10), transparent 30%),
                linear-gradient(135deg, #F8FAFC 0%, #EEF2FF 45%, #FFFFFF 100%);
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0F172A 0%, #111827 100%);
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        [data-testid="stSidebar"] * {
            color: #F8FAFC !important;
        }

        div[data-testid="stRadio"] label {
            padding: 8px 10px;
            border-radius: 12px;
        }

        .top-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 18px;
            padding: 12px 4px;
        }

        .brand {
            font-weight: 950;
            font-size: 24px;
            color: #0F172A;
            letter-spacing: -0.5px;
        }

        .brand span {
            color: #2563EB;
        }

        .course-pill {
            background: white;
            color: #334155;
            border: 1px solid #E2E8F0;
            border-radius: 999px;
            padding: 8px 14px;
            font-weight: 800;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
        }

        .hero {
            position: relative;
            overflow: hidden;
            padding: 42px 42px;
            border-radius: 34px;
            background:
                linear-gradient(135deg, rgba(15, 23, 42, 0.96) 0%, rgba(30, 58, 138, 0.94) 58%, rgba(37, 99, 235, 0.92) 100%),
                url('https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=1400');
            background-size: cover;
            background-position: center;
            color: white;
            box-shadow: 0 24px 60px rgba(15, 23, 42, 0.25);
            margin-bottom: 22px;
        }

        .hero h1 {
            font-size: 54px;
            margin: 0 0 10px 0;
            letter-spacing: -1.5px;
            line-height: 1.02;
        }

        .hero p {
            font-size: 18px;
            opacity: 0.93;
            max-width: 830px;
            line-height: 1.65;
        }

        .hero-actions {
            display: flex;
            gap: 12px;
            margin-top: 24px;
            flex-wrap: wrap;
        }

        .hero-button {
            display: inline-block;
            background: #FFFFFF;
            color: #0F172A;
            padding: 12px 18px;
            border-radius: 999px;
            font-weight: 900;
            box-shadow: 0 10px 30px rgba(0,0,0,0.18);
        }

        .hero-button.secondary {
            background: rgba(255,255,255,0.12);
            color: #FFFFFF;
            border: 1px solid rgba(255,255,255,0.35);
        }

        .section-title {
            color: #0F172A;
            font-size: 30px;
            font-weight: 950;
            margin-top: 14px;
            margin-bottom: 6px;
            letter-spacing: -0.7px;
        }

        .section-subtitle {
            color: #64748B;
            font-size: 15px;
            margin-bottom: 18px;
        }

        .stat-card, .feature-card, .product-card, .recommend-card, .method-card {
            background: rgba(255,255,255,0.92);
            border: 1px solid #E2E8F0;
            border-radius: 24px;
            box-shadow: 0 12px 34px rgba(15, 23, 42, 0.08);
        }

        .stat-card {
            padding: 20px;
            min-height: 112px;
        }

        .stat-label {
            font-size: 12px;
            color: #64748B;
            font-weight: 850;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }

        .stat-value {
            font-size: 30px;
            color: #0F172A;
            font-weight: 950;
            margin-top: 6px;
        }

        .feature-card {
            padding: 20px;
            min-height: 162px;
        }

        .feature-icon {
            font-size: 30px;
            margin-bottom: 8px;
        }

        .feature-title {
            color: #0F172A;
            font-size: 18px;
            font-weight: 950;
            margin-bottom: 6px;
        }

        .feature-text {
            color: #64748B;
            font-size: 14px;
            line-height: 1.55;
        }

        .product-card {
            overflow: hidden;
            min-height: 510px;
            transition: all 0.22s ease;
            margin-bottom: 18px;
        }

        .product-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 22px 50px rgba(15, 23, 42, 0.15);
        }

        .product-img {
            width: 100%;
            height: 205px;
            object-fit: cover;
            display: block;
        }

        .product-body {
            padding: 16px 16px 18px 16px;
        }

        .product-title {
            color: #0F172A;
            font-size: 18px;
            font-weight: 950;
            line-height: 1.25;
            margin: 12px 0 8px 0;
            min-height: 46px;
        }

        .product-desc {
            color: #64748B;
            font-size: 13.5px;
            line-height: 1.45;
            min-height: 58px;
        }

        .badge {
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 900;
            margin-right: 5px;
            margin-bottom: 5px;
        }

        .badge-blue {
            background: #DBEAFE;
            color: #1D4ED8;
        }

        .badge-orange {
            background: #FFEDD5;
            color: #C2410C;
        }

        .badge-green {
            background: #DCFCE7;
            color: #15803D;
        }

        .badge-purple {
            background: #F3E8FF;
            color: #7E22CE;
        }

        .price {
            font-size: 23px;
            font-weight: 950;
            color: #0F172A;
            margin-top: 10px;
        }

        .old-price {
            color: #94A3B8;
            text-decoration: line-through;
            font-size: 13px;
            margin-left: 6px;
            font-weight: 700;
        }

        .muted {
            color: #64748B;
            font-size: 14px;
        }

        .recommend-card {
            border-left: 7px solid #2563EB;
            padding: 18px 20px;
            margin-bottom: 14px;
        }

        .recommend-title {
            color: #0F172A;
            font-size: 21px;
            font-weight: 950;
            margin-bottom: 8px;
        }

        .reason-box {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 12px 14px;
            margin-top: 12px;
            color: #334155;
            font-size: 14px;
            line-height: 1.5;
        }

        .method-card {
            padding: 18px;
            min-height: 128px;
            border-top: 5px solid #2563EB;
        }

        .footer {
            text-align: center;
            color: #64748B;
            padding: 28px;
            margin-top: 30px;
        }

        .warning-note {
            background: #FFF7ED;
            color: #9A3412;
            border: 1px solid #FED7AA;
            border-radius: 18px;
            padding: 14px 16px;
            font-weight: 700;
        }


        .product-card .reason-box {
            min-height: 95px;
        }

        .product-card .stProgress {
            margin-top: 6px;
        }


        .details-image-card {
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: 28px;
            padding: 14px;
            box-shadow: 0 14px 38px rgba(15, 23, 42, 0.09);
        }

        .details-img {
            width: 100%;
            height: 430px;
            object-fit: cover;
            border-radius: 22px;
            display: block;
        }

        .details-main-card {
            background: rgba(255,255,255,0.94);
            border: 1px solid #E2E8F0;
            border-radius: 28px;
            padding: 26px;
            box-shadow: 0 14px 38px rgba(15, 23, 42, 0.08);
            min-height: 430px;
        }

        .details-title {
            color: #0F172A;
            font-size: 34px;
            line-height: 1.1;
            margin: 18px 0 14px 0;
            letter-spacing: -0.8px;
        }

        .details-desc {
            color: #475569;
            font-size: 15.5px;
            line-height: 1.7;
            margin-bottom: 22px;
        }

        .details-spec-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 12px;
            margin-top: 18px;
        }

        .details-spec {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 13px;
            color: #334155;
            font-size: 14px;
        }

        .buy-box {
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: 28px;
            padding: 24px;
            box-shadow: 0 14px 38px rgba(15, 23, 42, 0.10);
            min-height: 430px;
        }

        .buy-label {
            color: #64748B;
            font-size: 13px;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }

        .buy-price {
            color: #0F172A;
            font-size: 34px;
            font-weight: 950;
            margin: 6px 0;
        }

        .old-price-details {
            color: #94A3B8;
            text-decoration: line-through;
            font-weight: 800;
            margin-bottom: 4px;
        }

        .save-line {
            color: #15803D;
            background: #DCFCE7;
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 900;
            margin: 6px 0 14px 0;
        }

        .buy-info {
            color: #334155;
            font-size: 14px;
            margin: 10px 0;
        }

        .fake-button-primary {
            background: #2563EB;
            color: white;
            border-radius: 999px;
            padding: 12px 14px;
            text-align: center;
            font-weight: 950;
            margin-top: 22px;
            box-shadow: 0 10px 24px rgba(37, 99, 235, 0.25);
        }

        .fake-button-secondary {
            background: #F8FAFC;
            color: #0F172A;
            border: 1px solid #CBD5E1;
            border-radius: 999px;
            padding: 12px 14px;
            text-align: center;
            font-weight: 950;
            margin-top: 10px;
        }

        .stButton > button {
            border-radius: 999px;
            font-weight: 850;
            border: 1px solid #CBD5E1;
        }
        
        /* ===== RecomXpert Premium Website Upgrade ===== */
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(14, 165, 233, 0.12), transparent 28%),
                radial-gradient(circle at top right, rgba(124, 58, 237, 0.10), transparent 30%),
                linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 42%, #FFFFFF 100%) !important;
        }

        .brand {
            font-size: 28px;
        }

        .brand span {
            background: linear-gradient(90deg, #2563EB, #7C3AED, #F97316);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .course-pill {
            background: rgba(255,255,255,0.86);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(148,163,184,0.28);
        }

        .hero {
            display: grid;
            grid-template-columns: minmax(0, 1.45fr) minmax(320px, 0.55fr);
            gap: 28px;
            align-items: center;
            padding: 54px 50px;
            border-radius: 38px;
            min-height: 430px;
            background:
                radial-gradient(circle at 15% 20%, rgba(56,189,248,0.30), transparent 25%),
                radial-gradient(circle at 85% 25%, rgba(249,115,22,0.24), transparent 22%),
                linear-gradient(135deg, #020617 0%, #0F172A 48%, #1D4ED8 100%);
        }

        .hero h1 {
            max-width: 780px;
            font-size: 58px;
            line-height: 0.98;
        }

        .hero p {
            max-width: 760px;
            font-size: 18.5px;
        }

        .eyebrow {
            display: inline-block;
            padding: 8px 13px;
            border-radius: 999px;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.22);
            color: #BAE6FD;
            font-weight: 900;
            font-size: 12px;
            letter-spacing: 0.9px;
            text-transform: uppercase;
            margin-bottom: 18px;
        }

        .trust-row {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 22px;
        }

        .trust-row span {
            padding: 8px 11px;
            border-radius: 999px;
            background: rgba(255,255,255,0.10);
            border: 1px solid rgba(255,255,255,0.16);
            font-size: 13px;
            font-weight: 850;
            color: #E0F2FE;
        }

        .hero-glass-card {
            background: rgba(255,255,255,0.13);
            border: 1px solid rgba(255,255,255,0.24);
            box-shadow: 0 24px 70px rgba(0,0,0,0.22);
            backdrop-filter: blur(18px);
            border-radius: 30px;
            padding: 28px;
            color: white;
        }

        .glass-label {
            color: #BAE6FD;
            font-size: 12px;
            font-weight: 950;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .glass-product {
            font-size: 24px;
            font-weight: 950;
            line-height: 1.15;
            margin: 18px 0 10px 0;
        }

        .glass-score {
            font-size: 38px;
            font-weight: 950;
            color: #FDBA74;
        }

        .glass-line {
            height: 8px;
            border-radius: 999px;
            background: linear-gradient(90deg, #38BDF8, #2563EB, #F97316);
            margin: 18px 0;
        }

        .glass-small {
            color: rgba(255,255,255,0.80);
            font-size: 13.5px;
            line-height: 1.6;
        }

        .hero-button {
            background: linear-gradient(90deg, #FFFFFF, #E0F2FE);
            color: #020617;
            padding: 13px 20px;
        }

        .hero-button.secondary {
            background: rgba(255,255,255,0.10);
            color: white;
        }

        .stat-card {
            background: rgba(255,255,255,0.86);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(148,163,184,0.26);
            position: relative;
            overflow: hidden;
        }

        .stat-card::after {
            content: "";
            position: absolute;
            right: -25px;
            top: -25px;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, rgba(37,99,235,0.16), rgba(249,115,22,0.12));
            border-radius: 999px;
        }

        .premium-feature {
            position: relative;
            overflow: hidden;
            border-top: 5px solid transparent;
            background:
                linear-gradient(white, white) padding-box,
                linear-gradient(90deg, #2563EB, #7C3AED, #F97316) border-box;
        }

        .premium-feature::before {
            content: "";
            position: absolute;
            inset: auto -50px -55px auto;
            width: 130px;
            height: 130px;
            border-radius: 999px;
            background: rgba(37,99,235,0.08);
        }

        .product-card {
            border: 1px solid rgba(148,163,184,0.30);
            background: rgba(255,255,255,0.94);
        }

        .product-img {
            background: #E2E8F0;
        }

        .section-title {
            font-size: 34px;
        }

        [data-testid="stSidebar"] {
            background:
                radial-gradient(circle at top left, rgba(37,99,235,0.25), transparent 28%),
                linear-gradient(180deg, #020617 0%, #0F172A 100%) !important;
        }

        .sidebar-brand-card {
            padding: 18px;
            border-radius: 24px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.12);
            margin-bottom: 16px;
        }

        .sidebar-mini {
            font-size: 12px;
            opacity: 0.82;
            line-height: 1.5;
        }

        .website-strip {
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: 14px;
            margin: 22px 0;
        }

        .strip-item {
            background: rgba(255,255,255,0.86);
            border: 1px solid #E2E8F0;
            border-radius: 20px;
            padding: 16px;
            color: #334155;
            box-shadow: 0 10px 28px rgba(15,23,42,0.06);
            font-weight: 850;
            text-align: center;
        }

        @media (max-width: 900px) {
            .hero {
                grid-template-columns: 1fr;
                padding: 34px 26px;
            }
            .hero h1 {
                font-size: 40px;
            }
            .website-strip {
                grid-template-columns: 1fr 1fr;
            }
        }

        
        .popularity-hero {
            background:
                radial-gradient(circle at 10% 20%, rgba(249,115,22,0.25), transparent 25%),
                linear-gradient(135deg, #111827 0%, #1E1B4B 58%, #7C2D12 100%);
            border-radius: 32px;
            padding: 34px;
            color: white;
            box-shadow: 0 22px 54px rgba(15,23,42,0.22);
            margin-bottom: 22px;
        }

        .popularity-hero h1 {
            margin: 0;
            font-size: 42px;
            letter-spacing: -1px;
        }

        .popularity-hero p {
            color: rgba(255,255,255,0.82);
            max-width: 850px;
            font-size: 16px;
            line-height: 1.6;
        }

        .pop-rank {
            width: 42px;
            height: 42px;
            border-radius: 14px;
            background: linear-gradient(135deg, #2563EB, #7C3AED);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 950;
            margin-bottom: 10px;
        }

        .pop-signal-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 8px;
            margin-top: 12px;
        }

        .pop-signal {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 8px;
            color: #334155;
            font-size: 12px;
            font-weight: 800;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# UI Components
# ============================================================

def render_top_nav() -> None:
    st.markdown(
        f"""
        <div class="top-nav">
            <div class="brand">Recom<span>Xpert</span></div>
            <div class="course-pill">{COURSE_LABEL}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero">
            <div class="hero-content">
                <div class="eyebrow">AI-Powered E-Commerce Recommendation Platform</div>
                <h1>Discover the right product before you even search for it.</h1>
                <p>
                    RecomXpert is a premium e-commerce recommendation experience that combines personalized
                    product discovery, explainable AI, and side-by-side model comparison in one clean interface.
                </p>
                <div class="hero-actions">
                    <span class="hero-button">Start Exploring</span>
                    <span class="hero-button secondary">View AI Recommendations</span>
                </div>
                <div class="trust-row">
                    <span>✓ Multi-Approach AI</span>
                    <span>✓ Explainable Results</span>
                    <span>✓ Evaluation Dashboard</span>
                </div>
            </div>
            <div class="hero-glass-card">
                <div class="glass-label">Top AI Match</div>
                <div class="glass-product">Sony WH-1000XM5</div>
                <div class="glass-score">4.91 / 5.00</div>
                <div class="glass-line"></div>
                <div class="glass-small">Recommended because similar users preferred premium noise-canceling headphones.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stats(products: pd.DataFrame) -> None:
    stats = [
        ("Products", len(products)),
        ("Categories", products["category"].nunique()),
        ("Brands", products["brand"].nunique()),
        ("Avg Rating", f"{products['rating'].mean():.2f} ⭐"),
    ]

    cols = st.columns(4)
    for col, (label, value) in zip(cols, stats):
        with col:
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-label">{label}</div>
                    <div class="stat-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_feature_cards() -> None:
    features = [
        (
            "👥",
            "Behavior Intelligence",
            "Collaborative Filtering identifies patterns between users and recommends products based on similar behavior.",
        ),
        (
            "🧬",
            "Product Similarity Engine",
            "Content-Based Recommendation studies product attributes to suggest items close to what the user already likes.",
        ),
        (
            "🎯",
            "Preference Match",
            "Knowledge-Based Recommendation respects explicit needs such as budget, brand, category, and battery life.",
        ),
        (
            "🔥",
            "Popularity Signals",
            "An extra approach using real interaction-style data such as views, purchases, ratings, and recent sales.",
        ),
    ]

    cols = st.columns(4)
    for col, (icon, title, text) in zip(cols, features):
        with col:
            st.markdown(
                f"""
                <div class="feature-card premium-feature">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-text">{text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def format_price(price: float) -> str:
    return f"${price:,.2f}"


def product_card(row: pd.Series) -> None:
    old_price = ""
    if int(row.get("discount", 0)) > 0:
        old_price = f'<span class="old-price">{format_price(float(row["price"]))}</span>'

    final_price = float(row.get("sale_price", row["price"]))

    battery_badge = ""
    if int(row.get("battery_hrs", 0)) > 0:
        battery_badge = f'<span class="badge badge-purple">🔋 {int(row["battery_hrs"])}h</span>'

    discount_badge = ""
    if int(row.get("discount", 0)) > 0:
        discount_badge = f'<span class="badge badge-green">{int(row["discount"])}% OFF</span>'

    st.markdown(
        f"""
        <div class="product-card">
            <img src="{row['image']}" class="product-img">
            <div class="product-body">
                <span class="badge badge-blue">{row['category']}</span>
                <span class="badge badge-orange">{row['brand']}</span>
                {battery_badge}
                {discount_badge}
                <div class="product-title">{row['title']}</div>
                <div class="product-desc">{row['description']}</div>
                <div class="price">{format_price(final_price)} {old_price}</div>
                <p class="muted">⭐ {row['rating']} · {int(row['reviews'])} reviews · {int(row['stock'])} in stock</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_products_page(products: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">Explore the Product Universe</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">A premium catalog experience with filtering, sorting, ratings, discounts, and stock indicators.</div>',
        unsafe_allow_html=True,
    )

    search_col, sort_col = st.columns([2, 1])
    with search_col:
        search = st.text_input(
            "Search",
            placeholder="Search by product name, brand, category, or product ID...",
            label_visibility="collapsed",
        )
    with sort_col:
        sort_by = st.selectbox(
            "Sort",
            ["Recommended", "Price: Low to High", "Price: High to Low", "Highest Rating", "Most Reviews"],
        )

    f1, f2, f3, f4 = st.columns(4)
    with f1:
        category_filter = st.selectbox("Category", ["All"] + sorted(products["category"].unique().tolist()))
    with f2:
        brand_options = ["All"] + sorted(products["brand"].unique().tolist())
        brand_filter = st.selectbox("Brand", brand_options)
    with f3:
        max_price = st.slider(
            "Max Price",
            min_value=float(products["price"].min()),
            max_value=float(products["price"].max()),
            value=float(products["price"].max()),
        )
    with f4:
        min_rating = st.slider("Minimum Rating", 4.0, 5.0, 4.0, 0.1)

    filtered = products.copy()

    if search:
        s = search.lower()
        filtered = filtered[
            filtered["title"].str.lower().str.contains(s)
            | filtered["brand"].str.lower().str.contains(s)
            | filtered["category"].str.lower().str.contains(s)
            | filtered["product_id"].str.lower().str.contains(s)
        ]

    if category_filter != "All":
        filtered = filtered[filtered["category"] == category_filter]

    if brand_filter != "All":
        filtered = filtered[filtered["brand"] == brand_filter]

    filtered = filtered[(filtered["price"] <= max_price) & (filtered["rating"] >= min_rating)]

    if sort_by == "Price: Low to High":
        filtered = filtered.sort_values("sale_price", ascending=True)
    elif sort_by == "Price: High to Low":
        filtered = filtered.sort_values("sale_price", ascending=False)
    elif sort_by == "Highest Rating":
        filtered = filtered.sort_values(["rating", "reviews"], ascending=False)
    elif sort_by == "Most Reviews":
        filtered = filtered.sort_values("reviews", ascending=False)

    st.caption(f"Showing {len(filtered)} product(s) from {len(products)} total products.")

    if filtered.empty:
        st.warning("No products match your filters.")
        return

    cols = st.columns(4)
    for i, (_, row) in enumerate(filtered.iterrows()):
        with cols[i % 4]:
            product_card(row)


def render_product_details(products: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">Product Details</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">A realistic product page with image, price, specs, availability, and related products.</div>',
        unsafe_allow_html=True,
    )

    selected = st.selectbox(
        "Choose product",
        products["product_id"].tolist(),
        key="selected_product_details",
        format_func=lambda pid: f"{pid} · {products.loc[products['product_id'] == pid, 'title'].iloc[0]}",
    )

    row = products[products["product_id"] == selected].iloc[0]
    final_price = float(row.get("sale_price", row["price"]))
    has_discount = int(row.get("discount", 0)) > 0
    battery_text = f"{int(row['battery_hrs'])} hours" if int(row["battery_hrs"]) > 0 else "Not applicable"
    stock_status = "In Stock" if int(row["stock"]) > 0 else "Out of Stock"

    left, center, right = st.columns([1.05, 1.35, 0.9])

    with left:
        st.markdown(
            f"""
            <div class="details-image-card">
                <img src="{row['image']}" class="details-img">
            </div>
            """,
            unsafe_allow_html=True,
        )

    with center:
        st.markdown(
            f"""
            <div class="details-main-card">
                <span class="badge badge-blue">{row['category']}</span>
                <span class="badge badge-orange">{row['brand']}</span>
                <span class="badge badge-green">⭐ {row['rating']} Rating</span>

                <h1 class="details-title">{row['title']}</h1>
                <p class="details-desc">{row['description']}</p>

                <div class="details-spec-grid">
                    <div class="details-spec"><b>Product ID</b><br>{row['product_id']}</div>
                    <div class="details-spec"><b>Brand</b><br>{row['brand']}</div>
                    <div class="details-spec"><b>Category</b><br>{row['category']}</div>
                    <div class="details-spec"><b>Battery</b><br>{battery_text}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### Why this page matters for recommendations")
        st.markdown(
            """
            <div class="reason-box">
            This selected product can be used as a reference item for <b>Content-Based Recommendation</b>.
            The system can compare category, brand, price, and product characteristics to recommend similar items.
            For <b>Knowledge-Based Recommendation</b>, the same product attributes help explain user constraints like budget,
            brand preference, category preference, and battery requirement.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        old_price_line = ""
        if has_discount:
            old_price_line = f'<div class="old-price-details">{format_price(float(row["price"]))}</div>'

        st.markdown(
            f"""
            <div class="buy-box">
                <div class="buy-label">Current Price</div>
                <div class="buy-price">{format_price(final_price)}</div>
                {old_price_line}
                <div class="save-line">{int(row['discount'])}% discount applied</div>

                <hr>

                <div class="buy-info"><b>Status:</b> {stock_status}</div>
                <div class="buy-info"><b>Stock:</b> {int(row['stock'])} units</div>
                <div class="buy-info"><b>Reviews:</b> {int(row['reviews'])}</div>
                <div class="buy-info"><b>Delivery:</b> 2–4 business days</div>

                <div class="fake-button-primary">Add to Cart</div>
                <div class="fake-button-secondary">Add to Wishlist</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown('<div class="section-title">Related Products</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Products from the same category, useful for explaining Content-Based recommendations.</div>',
        unsafe_allow_html=True,
    )

    related = products[
        (products["category"] == row["category"]) & (products["product_id"] != row["product_id"])
    ].sort_values(["rating", "reviews"], ascending=False).head(4)

    if related.empty:
        st.info("No related products found for this category.")
        return

    cols = st.columns(4)
    for col, (_, related_row) in zip(cols, related.iterrows()):
        with col:
            product_card(related_row)


def render_method_selector(products: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">AI Recommendations</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Choose the approach, method, and user/product inputs to generate explainable recommendations.</div>',
        unsafe_allow_html=True,
    )

    top_col_1, top_col_2, top_col_3 = st.columns(3)
    with top_col_1:
        st.text_input("User ID", key="user_id")
    with top_col_2:
        st.selectbox(
            "Reference Product",
            products["product_id"].tolist(),
            key="product_id",
            format_func=lambda pid: f"{pid} · {products.loc[products['product_id'] == pid, 'title'].iloc[0][:42]}",
        )
    with top_col_3:
        st.slider("Number of Recommendations", min_value=3, max_value=12, key="top_n")

    approach_col, method_col = st.columns(2)
    with approach_col:
        previous_approach = st.session_state.approach_label
        st.selectbox("Approach", options=list(APPROACH_OPTIONS.keys()), key="approach_label")
    with method_col:
        method_options = get_method_options(st.session_state.approach_label)
        if previous_approach != st.session_state.approach_label or st.session_state.method_label not in method_options:
            st.session_state.method_label = method_options[0]
        st.selectbox("Method", options=method_options, key="method_label")

    st.markdown("#### Knowledge-Based Constraints")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.number_input(
            "Maximum Price ($)",
            min_value=float(products["price"].min()),
            max_value=float(products["price"].max()),
            step=50.0,
            key="max_price",
        )
    with c2:
        st.selectbox("Preferred Brand", options=["Any"] + sorted(products["brand"].unique().tolist()), key="preferred_brand")
    with c3:
        st.selectbox("Preferred Category", options=["Any"] + sorted(products["category"].unique().tolist()), key="preferred_category")
    with c4:
        st.slider(
            "Minimum Battery Hours",
            min_value=0,
            max_value=max(1, int(products["battery_hrs"].max())),
            key="min_battery_hrs",
        )


def render_recommendation_card(row: pd.Series, rank: int) -> None:
    """Render one recommended product as a website product card."""
    score = float(row["score"])
    score_percent = min(max(score / 5.0, 0.0), 1.0)
    battery = f"{int(row['battery_hrs'])}h" if int(row.get("battery_hrs", 0)) > 0 else "N/A"

    winner_badge = ""
    if rank == 1:
        winner_badge = '<span class="badge badge-green">🏆 Top Match</span>'
    elif score >= 4.6:
        winner_badge = '<span class="badge badge-green">⭐ Strong Match</span>'

    st.markdown(
        f"""
        <div class="product-card">
            <img src="{row['image']}" class="product-img">
            <div class="product-body">
                <span class="badge badge-blue">#{rank}</span>
                <span class="badge badge-orange">{row['brand']}</span>
                <span class="badge badge-purple">🔋 {battery}</span>
                {winner_badge}

                <div class="product-title">{row['title']}</div>
                <div class="product-desc">{row.get('description', '')}</div>

                <div class="price">{format_price(float(row['price']))}</div>
                <p class="muted">⭐ {row.get('rating', 4.5)} · Product ID: {row['product_id']}</p>

                <div class="reason-box">
                    <b>Why recommended?</b><br>
                    💡 {row['reason']}
                </div>

                <p class="muted" style="margin-top:10px;">
                    Recommendation Score: <b>{score:.2f}/5.00</b>
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(score_percent)


def render_recommendations_page(products: pd.DataFrame) -> None:
    render_method_selector(products)
    recs = get_recommendations(products)

    if recs.empty:
        st.warning("No recommendations were returned for the selected inputs.")
        return

    st.markdown("### Recommended Products")
    st.caption("Products are shown as e-commerce cards with explanation, score, brand, category, and battery information.")

    summary_col_1, summary_col_2, summary_col_3 = st.columns(3)
    with summary_col_1:
        st.metric("Returned Products", len(recs))
    with summary_col_2:
        st.metric("Average Score", f"{recs['score'].mean():.2f}/5")
    with summary_col_3:
        st.metric("Top Score", f"{recs['score'].max():.2f}/5")

    st.write("")

    cols = st.columns(3)
    for i, (_, row) in enumerate(recs.iterrows()):
        with cols[i % 3]:
            render_recommendation_card(row, i + 1)


def render_comparison_page(products: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">Approach Comparison</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Compare the three recommendation approaches side by side using the same catalog context.</div>',
        unsafe_allow_html=True,
    )

    selected_product = st.selectbox(
        "Reference Product",
        products["product_id"].tolist(),
        key="comparison_ref_product",
        format_func=lambda pid: f"{pid} · {products.loc[products['product_id'] == pid, 'title'].iloc[0]}",
    )

    comparison_top_n = 4
    cf_items = recommendation_to_df(cf_recommend(st.session_state.user_id, "svd", top_n=comparison_top_n), products)
    content_items = recommendation_to_df(cb_recommend(selected_product, "tfidf", top_n=comparison_top_n), products)
    knowledge_items = recommendation_to_df(kb_recommend(build_constraints(), top_n=comparison_top_n), products)

    columns_data = [
        ("Collaborative Filtering", "Uses similar users and rating behavior.", cf_items),
        ("Content-Based", "Uses similarity to the selected reference product.", content_items),
        ("Knowledge-Based", "Uses selected constraints such as price, brand, category, and battery.", knowledge_items),
    ]

    cols = st.columns(3)
    for col, (title, desc, items) in zip(cols, columns_data):
        with col:
            st.markdown(
                f"""
                <div class="method-card">
                    <div class="feature-title">{title}</div>
                    <div class="feature-text">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")
            for rank, (_, row) in enumerate(items.iterrows(), start=1):
                st.markdown(
                    f"""
                    <div class="recommend-card">
                        <b>#{rank} · {row['title']}</b><br>
                        <span class="muted">{row['brand']} · {row['category']}</span><br>
                        <b>{format_price(float(row['price']))}</b><br>
                        <span class="muted">Score: {float(row['score']):.2f}/5</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


def render_evaluation_page(products: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">Evaluation Dashboard</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Mock evaluation dashboard prepared for presentation. Replace mock values later with real model results.</div>',
        unsafe_allow_html=True,
    )

    actual = [4.8, 4.5, 4.2, 4.0, 3.8, 3.6]
    predicted = [item["score"] for item in cf_recommend(st.session_state.user_id, "svd", top_n=6)]

    metrics = {
        "MAE": evaluate(actual, predicted, "mae"),
        "RMSE": evaluate(actual, predicted, "rmse"),
        "Precision@K": evaluate(actual, predicted, "precision_at_k"),
        "Coverage": evaluate(actual, predicted, "coverage"),
    }

    cols = st.columns(4)
    for col, (label, value) in zip(cols, metrics.items()):
        with col:
            st.metric(label, value)

    chart_df = pd.DataFrame({"Metric": list(metrics.keys()), "Value": list(metrics.values())}).set_index("Metric")
    st.bar_chart(chart_df)

    st.markdown("### Method Comparison Example")
    methods = ["user_based", "item_based", "svd", "als"]
    rows = []
    for method in methods:
        recs = cf_recommend(st.session_state.user_id, method, top_n=6)
        scores = [item["score"] for item in recs]
        rows.append(
            {
                "CF Method": method,
                "Average Score": round(sum(scores) / len(scores), 3),
                "Precision@K": evaluate(actual, scores, "precision_at_k"),
                "Coverage": evaluate(actual, scores, "coverage"),
            }
        )

    st.dataframe(pd.DataFrame(rows), use_container_width=True)

    st.markdown(
        """
        <div class="warning-note">
        Presentation note: these metrics are mock values for UI demonstration. In the final academic version,
        connect this section to the real evaluation module to answer: which method performs best, under what conditions, and why.
        </div>
        """,
        unsafe_allow_html=True,
    )




def render_popularity_card(row: pd.Series, rank: int, method: str) -> None:
    """Render one popularity recommendation as a premium product card."""
    score_text = ""
    if "popularity_score" in row and pd.notna(row["popularity_score"]):
        score_text = f'<span class="badge badge-green">Score {float(row["popularity_score"]):.2f}</span>'

    discount_badge = ""
    if int(row.get("discount_percent", 0)) > 0:
        discount_badge = f'<span class="badge badge-green">{int(row["discount_percent"])}% OFF</span>'

    html_parts = [
        '<div class="product-card">',
        f'<img src="{row["image"]}" class="product-img">',
        '<div class="product-body">',
        f'<div class="pop-rank">#{rank}</div>',
        f'<span class="badge badge-blue">{row["category"]}</span>',
        f'<span class="badge badge-orange">{row["brand"]}</span>',
        discount_badge,
        score_text,
        f'<div class="product-title">{row["title"]}</div>',
        f'<div class="product-desc">{row["description"]}</div>',
        f'<div class="price">{format_price(float(row["sale_price"]))}</div>',
        f'<p class="muted">⭐ {float(row["avg_rating"]):.2f} · {int(row["reviews_count"])} reviews</p>',
        '<div class="pop-signal-grid">',
        f'<div class="pop-signal">👀 {int(row["views"])} views</div>',
        f'<div class="pop-signal">🛒 {int(row["purchases"])} purchases</div>',
        f'<div class="pop-signal">➕ {int(row["cart_adds"])} cart adds</div>',
        f'<div class="pop-signal">🔥 {int(row["last_7_days_sales"])} weekly sales</div>',
        '</div>',
        '<div class="reason-box">',
        f'<b>Why popular?</b><br>💡 {get_popularity_reason(row, method)}',
        '</div>',
        '</div>',
        '</div>',
    ]

    st.markdown("".join(html_parts), unsafe_allow_html=True)

def render_popularity_page() -> None:
    """Render the extra Popularity-Based Recommendation page."""
    st.markdown(
        """
        <div class="popularity-hero">
            <h1>🔥 Popularity-Based Recommendations</h1>
            <p>
                Extra feature beyond the required three approaches. This page uses a separate CSV dataset
                with real interaction-style signals such as views, purchases, cart additions, reviews,
                recent sales, discounts, stock, and return rate.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    df = load_popularity_data()
    if df.empty:
        return

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Popularity Products", len(df))
    with c2:
        st.metric("Total Views", f"{int(df['views'].sum()):,}")
    with c3:
        st.metric("Total Purchases", f"{int(df['purchases'].sum()):,}")
    with c4:
        st.metric("Avg Rating", f"{df['avg_rating'].mean():.2f} ⭐")

    st.write("")

    filters_col, method_col, top_col = st.columns([1.2, 1.2, 0.8])
    with filters_col:
        selected_category = st.selectbox(
            "Category Filter",
            ["All"] + sorted(df["category"].unique().tolist()),
            key="popularity_category",
        )
    with method_col:
        method = st.selectbox(
            "Popularity Method",
            [
                "Weighted Popularity Score",
                "Trending This Week",
                "Most Purchased",
                "Most Viewed",
                "Best Rated",
            ],
            key="popularity_method",
        )
    with top_col:
        top_n = st.slider("Top Products", 4, 12, 8, key="popularity_top_n")

    filtered = df.copy()
    if selected_category != "All":
        filtered = filtered[filtered["category"] == selected_category]

    results = popularity_recommend(filtered, method, top_n)

    if results.empty:
        st.warning("No popularity results match the selected filters.")
        return

    if method == "Weighted Popularity Score":
        chart_df = compute_popularity_score(filtered).head(10)[["title", "popularity_score"]].set_index("title")
        st.markdown("### Top Popularity Scores")
        st.bar_chart(chart_df)

    st.markdown("### Popular Products")
    st.caption("This section is independent from CF, Content-Based, and Knowledge-Based mock functions.")

    cols = st.columns(4)
    for i, (_, row) in enumerate(results.iterrows()):
        with cols[i % 4]:
            render_popularity_card(row, i + 1, method)

    st.markdown("### Method Explanation")
    st.markdown(
        """
        <div class="reason-box">
        <b>Popularity-Based Recommendation</b> is a simple but powerful baseline used in many e-commerce systems.
        It does not require user history, so it works well for new visitors and cold-start cases.
        The implemented methods include: Most Purchased, Most Viewed, Best Rated, Trending This Week,
        and Weighted Popularity Score.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_home_page(products: pd.DataFrame) -> None:
    render_hero()
    render_stats(products)
    st.write("")
    st.markdown('<div class="section-title">Recommendation Approaches</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">The website demonstrates all mandatory project approaches with explanations and comparison.</div>',
        unsafe_allow_html=True,
    )
    render_feature_cards()

    st.markdown(
        """
        <div class="website-strip">
            <div class="strip-item">⚡ Fast product discovery</div>
            <div class="strip-item">🧠 Explainable AI reasons</div>
            <div class="strip-item">📊 Model evaluation ready</div>
            <div class="strip-item">🛍️ Website-like catalog</div>
            <div class="strip-item">🔥 Extra popularity approach</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown('<div class="section-title">Featured Products</div>', unsafe_allow_html=True)
    featured = products.sort_values(["rating", "reviews"], ascending=False).head(4)
    cols = st.columns(4)
    for col, (_, row) in zip(cols, featured.iterrows()):
        with col:
            product_card(row)


# ============================================================
# Sidebar and Main
# ============================================================

def render_sidebar(products: pd.DataFrame) -> str:
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand-card">
                <h2 style="margin:0;">✨ RecomXpert</h2>
                <div class="sidebar-mini">
                    Premium AI product discovery platform for intelligent e-commerce recommendations.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        page = st.radio(
            "Navigation",
            [
                "Home",
                "Products",
                "Product Details",
                "Recommendations",
                "Popularity",
                "Comparison",
                "Evaluation",
            ],
            key="page",
        )

        st.divider()
        st.markdown("### Catalog Summary")
        st.write(f"**Products:** {len(products)}")
        st.write(f"**Categories:** {products['category'].nunique()}")
        st.write(f"**Brands:** {products['brand'].nunique()}")

        st.divider()
        st.markdown("### Project Requirements")
        st.write("✅ Collaborative Filtering")
        st.write("✅ Content-Based")
        st.write("✅ Knowledge-Based")
        st.write("🔥 Extra: Popularity-Based")
        st.write("✅ Explanations")
        st.write("✅ Evaluation")
        st.write("✅ Comparison")

        st.divider()
        st.caption("Required approaches use mocks/mock_functions.py. Popularity uses data/popularity_products.csv")

    return page


def main() -> None:
    inject_css()
    products = load_products()
    initialize_session_state(products)

    page = render_sidebar(products)
    render_top_nav()

    if page == "Home":
        render_home_page(products)
    elif page == "Products":
        render_products_page(products)
    elif page == "Product Details":
        render_product_details(products)
    elif page == "Recommendations":
        render_recommendations_page(products)
    elif page == "Popularity":
        render_popularity_page()
    elif page == "Comparison":
        render_comparison_page(products)
    elif page == "Evaluation":
        render_evaluation_page(products)

    st.markdown(
        """
        <div class="footer">
            AIE425 Intelligent Recommender System · RecomXpert · AI-Powered Product Discovery Platform
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
