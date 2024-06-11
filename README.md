# FastAPI Project with Two APIs

This repository contains two FastAPI applications:

1. **Reports API**: Manages reports data.
2. **Municipalities API**: Provides municipality data from a JSON file.

## Table of Contents

- [FastAPI Project with Two APIs](#fastapi-project-with-two-apis)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Running the Applications](#running-the-applications)
    - [With Docker](#with-docker)
    - [Without Docker](#without-docker)
      - [Running the Municipalities API](#running-the-municipalities-api)
      - [Running the Reports API](#running-the-reports-api)
  - [API Endpoints](#api-endpoints)
    - [Reports API](#reports-api)
    - [Municipalities API](#municipalities-api)
  - [Contributing](#contributing)
  - [License](#license)

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized setup)
- PostgreSQL (for Reports API database)

### Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Configure the database (for Reports API):

    Update the `database.py` file with your PostgreSQL connection details.

## Running the Applications

### With Docker

1. Ensure Docker is installed and running on your machine.
2. Build and run the Docker containers:

    ```sh
    docker-compose up --build
    ```

This will start both APIs on the following addresses:

- Reports API: `http://localhost:5000`

- Municipalities API: `http://localhost:8000`

### Without Docker

#### Running the Municipalities API

1. Navigate to the `municipalities_api` directory:

    ```sh
    cd municipalities_api
    ```

2. Start the application:

    ```sh
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```

#### Running the Reports API

1. Navigate to the `reports_api` directory:

    ```sh
    cd reports_api
    ```

2. Start the application:

    ```sh
    uvicorn main:app --reload --host 0.0.0.0 --port 5000
    ```

Ensure that the Municipalities API is running before starting the Reports API since it depends on it for initial data loading.

## API Endpoints

### Reports API

- **GET /**: Check if the API is running.
- **GET /reports**: Retrieve all reports.
- **GET /reports/{report_id}**: Retrieve a report by its ID.
- **POST /reports**: Create a new report.
- **PUT /reports/{report_id}**: Update an existing report by its ID.
- **DELETE /reports/{report_id}**: Delete a report by its ID.

### Municipalities API

- **GET /**: Check if the API is running.
- **GET /municipalities**: Retrieve all municipalities.
- **GET /municipality/{item_name}**: Retrieve a municipality by its name.
- **GET /municipality/population/{population}**: Retrieve municipalities with a population greater than the specified value (2017).
- **GET /municipality/startswith/{char}**: Retrieve municipalities starting with a specific character.
- **GET /municipality/population/{population}/year/{year}**: Retrieve municipalities with a population greater than the specified value for a given year.
- **GET /municipality/idhm_higher_than/{idhm}**: Retrieve municipalities with IDHM greater than the specified value.
- **GET /municipality/idhm_lower_than/{idhm}**: Retrieve municipalities with IDHM lower than the specified value.
- **GET /municipality/population/{population}/idhm/{idhm}**: Retrieve municipalities with a population greater than the specified value and IDHM greater than the specified value (2017).
- **GET /municipality/population/{population}/idhm/{idhm}/year/{year}**: Retrieve municipalities with a population greater than the specified value, IDHM greater than the specified value, for a given year.

## Contributing

Feel free to contribute by opening a pull request or an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Text partially generated bi A.I.