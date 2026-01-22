# API Test Example

A Python project for practicing automated REST API testing using `pytest`, `requests`, and `SQLAlchemy`.
This project was created during a training course on automated API testing with Pytest, focused on testing the API of a WooCommerce-based website.

It demonstrates:
- How to structure a Python test automation framework
- How to test real-world APIs (WooCommerce REST API)
- Usage of tools like pytest, requests, SQLAlchemy, and .env-based config
---

## Prerequisites

Before running the tests, make sure you have the following:

- A running WordPress site with the WooCommerce plugin installed and active.
- REST API access enabled and working (https://your-site.com/wp-json/wc/v3/).
- A pair of API credentials (consumer key and secret) generated for a user with proper permissions (usually via WooCommerce > Settings > Advanced > REST API).
---

Create a `.env` file in the root directory with the following structure:

```dotenv
WC_KEY=your_woocommerce_api_key
WC_SECRET=your_woocommerce_api_secret
ENV=test
DATABASE_URL=mysql+pymysql://user:password@host:port/dbname
```
Install Dependencies
```bash
pip install -r requirements.txt
```
Run the Tests
```bash
pytest
```

## API Documentation

For full reference of available endpoints and data formats, see the official WooCommerce API documentation:  
https://woocommerce.github.io/woocommerce-rest-api-docs/

## Related Course

This project was created while completing the Udemy course:

[API Testing with Python 3 & PyTest, Backend Automation 2026](https://www.udemy.com/course/backend-api-testing-with-python/)
> Learn to build a framework for API automation testing using Python, PyTest, SQL, reports, Docker, and more.
