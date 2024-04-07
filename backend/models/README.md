# Models

This folder contains Pydantic data models that define the shape of data used in the application.

## Usage

1. Create a new Pydantic data model file in this folder for each distinct data structure used in your application.
2. Use a meaningful naming convention for your models. For example, use PascalCase and suffix the name with "_model.py"
    Example: `Usermodel`, `ProductModel`
3. Define the attributes and types for each model using Pydantic's BaseModel class.
4. Ensure that the data models accurately represent the structure of the data being used in your application.

## Example
```python
from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    email: str
    age: int
```