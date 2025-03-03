# FastAPI DICOM Service

FastAPI service for storing and retrieving DICOM metadata.

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

