# FastAPI DICOM Metadata Service

A FastAPI-based service for storing and retrieving DICOM file metadata in a SQLite database.

## Features

- Upload single or multiple DICOM files simultaneously
- Extract essential DICOM metadata:
  - Patient ID
  - Study Instance UID
  - Series Instance UID
  - Modality
- Store metadata in SQLite database
- Query metadata with filters
- RESTful API endpoints with Swagger documentation

## Tech Stack

- FastAPI
- SQLAlchemy
- Alembic (migrations)
- SQLite
- pydicom
- Poetry
- Python 3.10+

## Installation & Setup

1. **Prerequisites**
   ```bash
   # Install Python 3.10 or higher
   python --version  # Should be 3.10+

   # Install Poetry
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone and Navigate**
   ```bash
   git clone https://github.com/roodgar-amirhosein/fastapi-dicom-service.git
   cd fastapi-dicom-service
   ```

3. **Install Dependencies**
   ```bash
   # Install project dependencies
   poetry install
   
   # Activate virtual environment
   poetry shell
   ```

4. **Database Setup**
   ```bash
   # Initialize Alembic migrations
   alembic init migrations
   
   # Run migrations to create database schema
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```

5. **Start the Server**
   ```bash
   uvicorn main_app.main:app --reload
   ```

## API Usage

The service will be running at `http://localhost:8000`

### API Documentation
- Swagger UI: `http://localhost:8000/docs`

### Endpoints

1. **Upload DICOM Files**
   ```bash
   POST /
   # Upload single or multiple DICOM files
   # Form data key: document_files
   ```

2. **Query Metadata**
   ```bash
   GET /
   # Query parameters:
   # - id: Integer
   # - patient_id: String
   # - study_instance_uid: String
   # - series_instance_uid: String
   # - modality: String
   ```

## Troubleshooting

If you encounter database errors, try deleting the `dicom.db` file and rerunning migrations





