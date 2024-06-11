# FastAPI Municipality Reports API

Introduction
This FastAPI application provides endpoints to manage reports related to municipalities in Brazil's State of Ceará. It interacts with an external API that provides data about Ceará municipalities. Note that this application relies on the availability of the Ceará municipalities API, and it may not work properly if the API is down.

The Ceará municipalities API used by this application is available in the same GitHub repositories, providing seamless integration with this FastAPI application.

This FastAPI application also provides endpoints to manage reports related to municipalities in Brazil's State of Ceará. It uses SQLAlchemy for database interactions and integrates with external APIs for data enrichment.


## Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Checks if the API is running.

### 2. Get All Reports
- **URL**: `/reports`
- **Method**: `GET`
- **Description**: Retrieves all reports from the database.

### 3. Get Report by ID
- **URL**: `/reports/{report_id}`
- **Method**: `GET`
- **Description**: Retrieves a report by its ID.
- **Parameters**:
  - `report_id` (int): The ID of the report.
- **Response**:
  - The report data if found.
  - `"Report not found"` if the report is not found.

### 4. Create a Report
- **URL**: `/reports`
- **Method**: `POST`
- **Description**: Creates a new report.
- **Request Body**:
  - `title` (str): The title of the report.
  - `report` (str): The content of the report.
  - `author` (str): The author of the report.
  - `municipality` (str): The name of the municipality.
  - `year` (str): The year of the report.
- **Response**:
  - The created report data.
  - `"Municipality not found"` if the municipality is not found.

### 5. Update a Report
- **URL**: `/reports/{report_id}`
- **Method**: `PUT`
- **Description**: Updates an existing report.
- **Parameters**:
  - `report_id` (int): The ID of the report.
- **Request Body**:
  - `title` (str): The title of the report.
  - `report` (str): The content of the report.
  - `author` (str): The author of the report.
  - `municipality` (str): The name of the municipality.
  - `year` (str): The year of the report.
- **Response**:
  - The updated report data.
  - `"Report not found"` if the report is not found.

### 6. Delete a Report
- **URL**: `/reports/{report_id}`
- **Method**: `DELETE`
- **Description**: Deletes a report by its ID.
- **Parameters**:
  - `report_id` (int): The ID of the report.
- **Response**:
  - `"Report deleted successfully"` if the report is deleted.
  - `"Report not found"` if the report is not found.

## Running the Application

## Using Docker
## 1. Clone the Repository:
- git clone https://your-repo-url
- cd your-repo-directory

## 2. Ensure Docker is Installed:
- Make sure you have Docker installed on your machine. You can download and install it from the Docker website.

## 3. Build the Docker Image:
- docker build -t my-fastapi-app .

## 4. Run the Docker Container:
- docker run -d -p 5000:5000 my-fastapi-app

## 5. Access the Endpoints:
- Once the application is running, access the endpoints by visiting http://localhost:5000/ in your web browser or using a tool like cURL or Postman.

