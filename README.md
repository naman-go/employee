# Employee Management

Sample project for github action

### Folder Structure
<details>
  <summary>Click to expand</summary>

```
.
├── Dockerfile
├── README.md
├── TODO.md
├── dapr.yaml
├── employee_management
│   ├── __init__.py
│   ├── app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── config.py
│   │   ├── controllers
│   │   │   ├── __init__.py
│   │   │   └── employee.py
│   │   ├── db_interface
│   │   │   ├── __init__.py
│   │   │   └── employee.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── employee.py
│   │   ├── serializers
│   │   │   ├── __init__.py
│   │   │   └── employee.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── employee.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── responses.py
│   │       ├── errors.py
│   │       ├── config.py
│   │       ├── pagination.py
│   │       └── logger.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── local.yml
├── manage.py
├── pyproject.toml
├── requirements.txt
└── setup.cfg
```
</details>

### Features
* RESTful APIs
* Standard Error message
* Standard Response format
* Unit Tests
* Pre-commit hooks
* OpenAPI schema / Swagger
* Custom Pagination -- Limit Offset Count
* Continuous Integration - GitHub Actions
* Logger


### Endpoints
* GET `/api/v1.0/employees`
* POST `/api/v1.0/employees`
* GET `/api/v1.0/employees/:id`
* PUT `/api/v1.0/employees/:id`
* DELETE `/api/v1.0/employees/:id`

# Getting Started

## Non-Docker Setup:

<details>
<summary>Click to Expand</summary>

#### Create virtual environment and install dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

#### Migrations
Copy the sample env file and make changes as per the environment
```
cp .env.sample .env
```

Make changes models.py to suit the needs of your app

Generate migration files using the following command
```
python3 manage.py makemigrations
```

Run the migration
```
python3 manage.py migrate
```

#### Setting Up Your Users

To create a **superuser account**, use this command:

```
python3 manage.py createsuperuser
```

#### Run Server
```
python3 manage.py runserver 8000
```
#### Running tests with Pytest

```
python3 manage.py test employee_management.app.tests.employee
```

</details>

## Docker Setup:
<details>
<summary>Click to Expand</summary>

1. Copy the .env file
```
cp .env.sample .env
```

2. Start the docker containers
```
docker-compose -f local.yml up --build
```

3. Shell into django's container
```
docker exec -it neo_employee_management bash
```
> Note: If the name "neo_employee_management" doesn't match, run `docker ps` and get the name of the django container

4. Make migrations
```
python3 manage.py makemigrations
```

5. Run migrations
```
python3 manage.py migrate
```

6. [Optional] Run tests
```
python3 manage.py test employee_management.app.tests.employee
```

7. [Optional] Create superuser for admin access
```
python3 manage.py createsuperuser
```

</details>

### Pre-Commit Hooks [Important]
Install pre-commit hook using the following command. After this, pre-commit hooks will be executed everytime you commit the code.
> if you are following the Docker setup, please install pre-commit package locally outside docker using `pip3 install pre-commit`

Install pre-commit hooks using the following command
```
pre-commit install
```

Incase, you want to manually trigger the pre-commit hooks
```
pre-commit run --all-files
```
#### [Optional] Type checks

Running type checks with mypy:
```
mypy employee_management/app
```


#### [Optional] Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```commandline

coverage run -m pytest
coverage html
open htmlcov/index.html
```

## DAPR [Optional]
#### Installation

```
brew install dapr/tap/dapr-cli
dapr init
```
#### Standalone Mode
```
dapr run --app-id employee_app --app-port 8000 --dapr-http-port 3500 python3 manage.py runserver 8000

```
Make a request:
```commandline
curl http://localhost:3500/v1.0/invoke/employee_app/method/api/v1.0/employees/
```

#### Kubernetes

* Build Docker Image
```
docker build . -t neo_employee_management:latest
```

* Run docker-compose
```
 docker-compose -f local.yml up --build
```
[This section is under construction]

## API References

#### Sample response format
```
{
    "response": {
        "data": {
            "employees": []
        },
    },
    "status": "success",
    "message": "Response was successful",
}
```

#### Sample Paginated Response
```json
{
    "response": {
        "data": {},
        "pagination": {
            "count": 2,
            "next": "http://localhost:8000/api/v1.0/employees/?limit=1&offset=1",
            "previous": null,
        },
    },
    "status": "success",
    "message": null,
}
```


#### Sample Error response
we are using `drf-standardized-errors` plugin for error response.

* **type** can be `client_error`, `server_error` or `validation_error`
```json
{
    "status": "error",
    "type": "client_error",
    "errors": [
        {
            "code": "not_found",
            "detail": "Not found.",
            "attr": null
        }
    ]
}

```


####  Notes of naming stuff:
* Name Mold : [adjective]_[noun]_[measurement]
  * Example: Suppose you are storing maximum number of order per month. What is the variable name?
    * max_order_length

    [Learn More](https://www.youtube.com/watch?v=z7w2lKG8zWM&t=325s)



#### custom error message

* For validation error:

```
raise ValidationError(serializer.errors)
```

* For custom client error:

```
raise ClientAPIExceptionHandler(
        detail=ErrorMessages.ENTITY_NOT_FOUND,
        code=status.HTTP_400_BAD_REQUEST,
    )

```

* For server side error:

```
raise ServerAPIExceptionHandler(
        detail=ErrorMessages.ENTITY_NOT_FOUND,
        code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
```


##### using logger 
```
from employee_management.app.utils.logger import logging

logging.info("This is info log message")
logging.error("This is info log message")

```

#### Swagger Documentation

* Swagger documentation is available at `/api/schema/swagger-ui/` endpoint
* Redoc documentation is available at `/api/schema/redoc/` endpoint
* OpenAPI schema is available at `/api/schema/openapi.json` endpoint
