# Django + Scrapy Project

## Overview

This project integrates Django with Scrapy to build a web scraping solution that extracts product data and stores it in a Django application. The Django application provides an API for inserting scraped data, and Scrapy is used to scrape and send data to this API.

## Features

- **Django Application**: Provides an API endpoint for inserting scraped product data.
- **Scrapy Spider**: Scrapes product data from a website and sends it to the Django API.
- **Data Storage**: Stores product data and SKUs in a Django-managed database.

## Installation

### Prerequisites

- Python 3.7+
- Django 4.1+
- Scrapy 2.11+
- A database (e.g., PostgreSQL) configured for Django

### Setting Up the Environment

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure Django Settings**

    - Update `settings.py` with your database configuration and any other necessary settings.

6. **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

7. **Create a Superuser**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run Django Server**

    ```bash
    python manage.py runserver
    ```

9. **Configure Scrapy Settings**

    - Update the Scrapy spider settings if necessary.

## Usage

### Running the Spider

To run the Scrapy spider and start scraping:

```bash
scrapy crawl men