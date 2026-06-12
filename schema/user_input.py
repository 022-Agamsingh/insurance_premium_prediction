
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities , tier_2_cities 
class UserInput(BaseModel):
    age: Annotated[int,Field(...,gt=0,lt=120,description="Age of the person")]
    weight:Annotated[float,Field(...,gt=0,description="weight of the person in kg")]
    height:Annotated[float,Field(...,gt=0,description="height of the person in meters")]
    income_lpa: Annotated[float,Field(...,gt=0,description="Annual income in lakhs")]
    smoker: Annotated[bool,Field(...,description="Whether the person is a smoker")]
    city: Annotated[str,Field(...,description="City of residence")]
    occupation: Annotated[Literal['retired','freelancer','student','government_job','private_job'],Field(...,description="Occupation")]
    
    @field_validator('city')
    def validate_city(cls, v: str)->str:
        v=v.strip().title()
        return v



    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    # @computed_field
    # @property
    # def smoker_binary(self)->int:
    #     return 1 if self.smoker else 0
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi>30:
            return "high"
        elif self.bmi >25:
            return "medium"
        else:
            return "low"
        

    @computed_field
    @property
    def age_group(self)->str:
        if self.age<25:
            return "young"
        elif self.age<45:
            return "adult"
        elif self.age<60:
            return "middle-aged"
        else:
            return "senior"
        
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3