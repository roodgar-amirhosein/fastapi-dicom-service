from fastapi import FastAPI, UploadFile, File, Depends, Query, HTTPException
from sqlalchemy.orm import Session
import pydicom
from typing import Optional, List
from io import BytesIO
from . import models, schemas, database

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=database.engine)

@app.post("/", response_model=List[schemas.DicomMetadata])
async def upload_dicom(
    document_files: List[UploadFile] = File(...),
    db: Session = Depends(database.get_db)
):
    if not document_files:
        raise HTTPException(status_code=400, detail="No files provided")
        
    metadata_list = []
    errors = []
    
    for document_file in document_files:
        try:
            contents = await document_file.read()
            ds = pydicom.dcmread(BytesIO(contents))
            
            
            metadata = models.DicomMetadata(
                patient_id=ds.PatientID,
                study_instance_uid=ds.StudyInstanceUID,
                series_instance_uid=ds.SeriesInstanceUID,
                modality=ds.Modality
            )
            
            db.add(metadata)
            metadata_list.append(metadata)
            
        except Exception as e:
            errors.append(f"Error processing {document_file.filename}: {str(e)}")
    
    if metadata_list:
        db.commit()
        for metadata in metadata_list:
            db.refresh(metadata)
    
    if errors:
        raise HTTPException(status_code=400, detail={"processed": len(metadata_list), "errors": errors})
    
    return metadata_list

@app.get("/", response_model=List[schemas.DicomMetadata])
def get_metadata(
    id: Optional[int] = Query(None),
    patient_id: Optional[str] = Query(None),
    study_instance_uid: Optional[str] = Query(None),
    series_instance_uid: Optional[str] = Query(None),
    modality: Optional[str] = Query(None),
    db: Session = Depends(database.get_db)
):
    query = db.query(models.DicomMetadata)
    
    if id:
        query = query.filter(models.DicomMetadata.id == id)
    if patient_id:
        query = query.filter(models.DicomMetadata.patient_id == patient_id)
    if study_instance_uid:
        query = query.filter(models.DicomMetadata.study_instance_uid == study_instance_uid)
    if series_instance_uid:
        query = query.filter(models.DicomMetadata.series_instance_uid == series_instance_uid)
    if modality:
        query = query.filter(models.DicomMetadata.modality == modality)
    
    return query.all() 