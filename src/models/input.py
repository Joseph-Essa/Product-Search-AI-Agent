from pydantic import BaseModel, Field
from typing import List

class InputModel(BaseModel):
    product_name: str = Field(..., example="coffee machine for the office")
    websites_list: List[str] = Field(
        ..., 
        example=["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"]
    )
    country_name: str = Field(..., example="Egypt")
    no_keywords: int = Field(..., example=10)
    language: str = Field(..., example="English")
    score_th: float = Field(..., example=0.10)
    top_recommendations_no: int = Field(..., example=10)
