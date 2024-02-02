from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

PyObjectId = Annotated[str, BeforeValidator(str)]


# https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/
# https://www.mongodb.com/developer/languages/python/farm-stack-fastapi-react-mongodb/?_ga=2.74919130.950231897.1706874852-1770370946.1706874852

class Wine(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    region: str

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Macketo wine",
                "region": "Bordo",
            }
        }
    )



