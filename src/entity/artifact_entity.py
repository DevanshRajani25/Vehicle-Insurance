# This file specify what output we need in our artifact(output) folder
from dataclasses import dataclass


# This will give following items in data ingestion folder in artifact folder 
@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str

# This will give following items in data validation folder in artifact folder 
@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    validation_report_file_path: str

# This will give following items in data Transformation folder in artifact folder 
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str

# This will give following items in Model Training folder in artifact folder 

@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float
    
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact