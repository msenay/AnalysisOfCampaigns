# Meta Campaign Data Analysis API

This project provides a RESTful API for analyzing a dataset related to digital marketing campaigns. The API is built using Django and Django REST Framework, with Pandas used for data processing. The project is containerized using Docker and managed with Docker Compose, making it easy to set up and run the application.

### Features

Conversion Rate Calculation: Calculates the conversion rate for each customer, along with the highest and lowest conversion rates.
Status-Based Analysis: Analyzes the distribution of statuses (e.g., ENABLED, HIDDEN) across different types and categories.
Category and Type Performance: Provides total revenue and conversions grouped by category and type, highlighting the top-performing combination.
Filtered and Aggregated Data: Filters the data for type = 'CONVERSION' and provides aggregated average revenue and conversions per customer.


###Endpoints
```text
/api/conversion-rate/
GET: Returns the conversion rate for each customer, as well as the highest and lowest conversion rates.
/api/status-distribution/
GET: Provides a breakdown of total revenue, total conversions, and count of customers for each combination of status, type, and category.
/api/category-type-performance/
GET: Returns total revenue and conversions grouped by category and type, and highlights the top-performing combination.
/api/filtered-aggregation/
GET: Filters the data for type = 'CONVERSION' and returns average revenue and conversions per customer.
```

### Docker Setup

Prerequisites
* Docker
* Docker Compose

### Clone the Repository
```bash
git clone https://github.com/yourusername/meta-campaign-analysis-api.git](https://github.com/msenay/AnalysisOfCampaigns.git
```
```bash
cd marketing_analysis
```
### Running the Application
```bash
docker compose up --build
```
### Stop the Application
```bash
docker-compose down
```

### Running Tests

To run the test suite inside the Docker container, you can run:

```bash
cd marketing_analysis
docker-compose run api python manage.py test
```


### Project Structure

```text
meta-campaign-analysis-api/
│
├── analytics/
│   ├── migrations/        # Migration files
│   ├── __init__.py        # Package initialization
│   ├── admin.py           # Admin configurations
│   ├── apps.py            # App configuration
│   ├── models.py          # (Unused) Models for future needs
│   ├── tests.py           # Test cases for API
│   ├── urls.py            # API URLs
│   └── views.py           # API view functions
│
├── marketing_analysis/     # Main Django project folder
│   ├── __init__.py         # Package initialization
│   ├── asgi.py             # ASGI entry point
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing for project
│   └── wsgi.py             # WSGI entry point for deployment
│
├── .env                    # Environment variables
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Dockerfile for building the container
├── manage.py                # Django's command-line utility
└── requirements.txt         # Project dependencies

```
### Dataset

The dataset is sourced from a CSV file available online and loaded directly into memory for analysis using Pandas. The dataset URL can be updated in the views.py file if needed.

### Technologies Used

Django: Backend framework for handling API requests.

Django REST Framework: For building the API endpoints.

Pandas: For data analysis and manipulation.

Docker: Containerization of the application.

Docker Compose: To orchestrate the containerized services.

Python 3.8+
