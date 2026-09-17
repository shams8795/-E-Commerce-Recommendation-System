<h1 align="center">RecomXpert</h1>

<h3 align="center">E-Commerce Product Discovery & Popularity Recommendation Platform</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=flat-square&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-Numerical_Computing-013243?style=flat-square&logo=numpy&logoColor=white">
</p>

<p align="center">
An interactive e-commerce application for product discovery, popularity analysis, recommendation exploration, and product analytics.
</p>

---

# Overview

RecomXpert is an interactive e-commerce application developed using Python and Streamlit.

The platform provides a structured environment for browsing products, viewing detailed product information, exploring recommendation interfaces, analyzing product popularity, comparing recommendation approaches, and viewing recommendation evaluation metrics.

The application includes:

- 80 products
- 10 product categories
- 40 brands
- 48 products in the popularity dataset
- 16 dataset attributes
- An interactive Streamlit interface

---

# Main Features

RecomXpert provides several features for exploring and analyzing e-commerce products.

Product Catalog  
Browse and explore a collection of 80 products from different categories and brands.

Product Discovery  
Filter and explore products according to category, brand, price, rating, and selected preferences.

Product Details  
View detailed information about individual products, including price, rating, availability, discounts, and other product characteristics.

Recommendation Interface  
Explore different recommendation approaches through the application interface.

Popularity Analysis  
Discover popular and trending products using product interaction data.

Comparison  
Compare different recommendation approaches from the application.

Evaluation  
View recommendation evaluation metrics through a dedicated evaluation page.

---

# Product Catalog

The application contains 80 products distributed across 10 product categories:

- Smartphones
- Laptops
- Tablets
- Headphones
- Smartwatches
- Speakers
- Accessories
- Cameras
- Gaming
- Smart Home

Each product contains information such as:

- Product ID
- Product name
- Brand
- Category
- Price
- Battery information

The interface also displays additional information including:

- Ratings
- Stock availability
- Reviews
- Discounts
- Product images
- Sale prices

---

# Product Discovery

Users can browse and filter products through an interactive Streamlit interface.

Products can be explored according to:

- Category
- Brand
- Price
- Rating
- Product preferences

These options make it easier to navigate the available catalog and focus on products that match selected criteria.

---

# Product Details

The Product Details page provides a dedicated view for individual products.

The page can display:

- Product image
- Brand
- Category
- Price
- Discount
- Rating
- Stock availability
- Battery information
- Product description
- Related product information

---

# Popularity-Based Recommendation

RecomXpert includes a data-driven popularity recommendation system based on a dedicated CSV dataset.

The application provides several ways to identify popular products:

### Most Purchased

Ranks products according to the number of completed purchases.

### Most Viewed

Identifies products receiving the highest number of views.

### Best Rated

Highlights products based on customer ratings.

### Trending This Week

Uses recent weekly sales activity to identify currently trending products.

### Weighted Popularity Score

Combines several interaction signals to calculate an overall popularity score.

The weighted score uses:

- Purchases: 28%
- Views: 22%
- Reviews: 18%
- Average Rating: 15%
- Cart Adds: 10%
- Recent Weekly Sales: 10%
- Return Rate: -5%

All numeric signals are normalized before calculating the final popularity score.

---

# Popularity Dataset

The popularity dataset contains 48 products and 16 attributes.

The available attributes are:

- `product_id` — Unique product identifier
- `title` — Product name
- `brand` — Product brand
- `category` — Product category
- `price` — Product price
- `avg_rating` — Average customer rating
- `reviews_count` — Number of customer reviews
- `views` — Product views
- `cart_adds` — Number of cart additions
- `purchases` — Completed purchases
- `last_30_days_sales` — Sales during the previous 30 days
- `last_7_days_sales` — Recent weekly sales
- `return_rate` — Product return rate
- `stock` — Available stock
- `discount_percent` — Product discount percentage
- `launch_date` — Product launch date

---

# Application Pages

### Home

Provides an overview of the platform and its main functionality.

### Products

Displays the product catalog and product filtering options.

### Product Details

Displays detailed information about individual products.

### Recommendations

Provides an interface for exploring recommendation approaches.

### Popularity

Displays popular and trending products based on interaction data.

### Comparison

Provides a side-by-side comparison of recommendation approaches.

### Evaluation

Displays recommendation evaluation metrics.

---

# Tech Stack

The project is developed using:

### Python

Used for the core application logic and data processing.

### Streamlit

Used to build the interactive web application interface.

### Pandas

Used for loading, processing, and analyzing product data.

### NumPy

Used for numerical operations.

### CSV

Used to store product interaction and popularity data.

---

# Project Structure

```text
E-Commerce-Recommendation-System/
│
├── app.py
│
├── data/
│   └── popularity_products.csv
│
├── evaluation/
│   └── __init__.py
│
├── models/
│   └── __init__.py
│
├── mocks/
│   ├── __init__.py
│   └── mock_functions.py
│
└── requirements.txt
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/shams8795/-E-Commerce-Recommendation-System.git
```

## 2. Open the Project Folder

```bash
cd ./-E-Commerce-Recommendation-System
```

## 3. Install the Required Libraries

```bash
pip install -r requirements.txt
```

## 4. Run the Application

```bash
streamlit run app.py
```

The Streamlit application will automatically open in the browser.

---

# Project Context
ل



The project demonstrates an interactive e-commerce application focused on:

- Product discovery
- Product analytics
- Popularity analysis
- Recommendation exploration
- Recommendation comparison
- Evaluation metrics

---

<h2 align="center">RecomXpert</h2>

<p align="center">
E-Commerce Product Discovery and Popularity Analysis Platform
</p>

<p align="center">
Python • Streamlit • Pandas • NumPy
</p>
