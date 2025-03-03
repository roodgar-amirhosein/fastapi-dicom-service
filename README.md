# DICOM Metadata API

A FastAPI-based service for storing and retrieving DICOM file metadata.

## Features

- Upload single or multiple DICOM files
- Extract metadata (PatientID, StudyInstanceUID, SeriesInstanceUID, Modality)
- Store metadata in SQLite database
- Query metadata with multiple filter options
- RESTful API endpoints

## Tech Stack

- FastAPI
- SQLAlchemy
- Alembic (migrations)
- SQLite
- pydicom

## Installation

```bash
# Clone the repository
git clone [your-repo-url]

# Install dependencies
poetry install

# Run migrations
alembic upgrade head

# Start the server
uvicorn main_app.main:app --reload
```

