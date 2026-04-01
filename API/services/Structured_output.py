from pydantic import BaseModel, Field

class PaperOutput(BaseModel):
    Abstract: str = Field(description="full blown Summary of the paper with Research Paper Name")
    Method: str = Field(description="Methodology used")
    Math: str = Field(description="Mathematical equations or concepts with Research Paper Name")
    Experiments: str = Field(description="Datasets and experimental setup")
    Results: str = Field(description="Evaluation results")
    Youtube: str = Field(description="YouTube search query for the paper NOT YOUTUBE LINKS JUST SEARCH QUERY ")