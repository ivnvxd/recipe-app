# recipe-app

A REST API for managing recipes built with Python, Django, and Django REST Framework.

## Overview

This Recipe App API is a practical implementation of an advanced course on building a Backend REST API using *Python*, *Django*, *Django REST Framework*, *Docker*, *GitHub Actions*, *Postgres*, and *Test Driven Development* (TDD). The application focuses on creating a robust API for a recipe application, emphasizing best practices and TDD.

### Features

- **User Authentication:** Securely manage user sessions.
- **CRUD Operations:** Create, read, update, and delete recipes.
- **Image Uploads:** Ability to upload and view images associated with recipes.
- **Advanced Filtering:** Search and filter recipes based on various criteria.
- **Test Driven Development:** Developed using TDD principles for robust and reliable code.

### Technologies

- **Python & Django:** For building the core application.
- **Django REST Framework:** For creating RESTful APIs.
- **Docker & Docker-Compose:** For containerization and orchestration.
- **Nginx:** As a reverse proxy for the Django application.
- **GitHub Actions:** For continuous integration and deployment.
- **Postgres:** As the database backend.

<!-- ## Demo

A live demo of the application is available at [AWS](http://ec2-3-70-235-141.eu-central-1.compute.amazonaws.com/api/docs/). -->

## Installation & Usage

1. Clone the Repository

```sh
git clone https://github.com/ivnvxd/recipe-app.git
```

2. Change into the project directory

```sh
cd recipe-app
```

3.  Build and run the Docker containers

```sh
docker-compose up --build
```

### Usage

Once the application is running, you can use the provided API endpoints to manage recipes, users, and more.

Swagger documentation is available at [http://0.0.0.0:8000/api/docs/](http://0.0.0.0:8000/api/docs/).

## Testing

To run the tests:

```sh
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test && flake8"
```

---

:octocat: This is the training project of the ["Build a Backend REST API with Python & Django - Advanced"](https://www.udemy.com/course/django-python-advanced/) course available on [Udemy](https://www.udemy.com)

> GitHub [@ivnvxd](https://github.com/ivnvxd) &nbsp;&middot;&nbsp;
> LinkedIn [@Andrey Ivanov](https://www.linkedin.com/in/abivanov/)
