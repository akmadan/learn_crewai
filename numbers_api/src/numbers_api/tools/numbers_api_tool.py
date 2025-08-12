from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests

class NumbersAPIToolInput(BaseModel):
    """Input schema for NumbersAPITool."""
    number: int = Field(..., description="The number to get a fact about.")
    type: str = Field(
        default="trivia",
        description="The type of fact to retrieve. Options are 'trivia', 'math', 'date', or 'year'."
    )

class NumbersAPITool(BaseTool):
    name: str = "This is a Numbers API tool"
    description: str = (
        "It takes a number and returns a fact about it based on the type of number (e.g., trivia, math, date, or year)."
    )
    args_schema: Type[BaseModel] = NumbersAPIToolInput

    def _run(self, number: int, type: str) -> str:
        # Implementation goes here
        url = f"http://numbersapi.com/{number}/{type}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            return f"Error fetching data from Numbers API: {str(e)}"
        
