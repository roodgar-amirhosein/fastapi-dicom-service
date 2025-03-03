from pydantic import BaseModel

class DicomMetadataBase(BaseModel):
    patient_id: str
    study_instance_uid: str
    series_instance_uid: str
    modality: str

class DicomMetadataCreate(DicomMetadataBase):
    pass

class DicomMetadata(DicomMetadataBase):
    id: int

    class Config:
        from_attributes = True  # Updated from orm_mode for newer Pydantic versions 