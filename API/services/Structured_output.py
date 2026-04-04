from pydantic import BaseModel, Field

class PaperOutput(BaseModel):
    Name: str = Field(description="Include the Research Paper Name")
    Abstract: str = Field(description="full blown Summary of the Research Paper Name")
    Method: str = Field(description="Methodology used in the research paper")
    Math: str = Field(description="Mathematical equations or concepts with Research Paper Name")
    Experiments: str = Field(description="Datasets and experimental setup")
    Results: str = Field(description="Evaluation results")
    Youtube: str = Field(description="Just a SHORT searchable YOUTUBE query STRICTLY NOT A LINK ")