
import requests

url='http://127.0.0.1:5000/predict'
test_case={"Young, healthy, non-smoker":{
  "age": 25,
  "sex": "female",
  "bmi": 22,
  "children": 0,
  "smoker": "no",
  "region": "northwest"
},"Middle age, non-smoker":
{
  "age": 40,
  "sex": "male",
  "bmi": 27,
  "children": 2,
  "smoker": "no",
  "region": "southwest"
},"Smoker with average BMI":
{
  "age": 35,
  "sex": "female",
  "bmi": 26,
  "children": 1,
  "smoker": "yes",
  "region": "southeast"
},"High BMI + smoker":

{
  "age": 50,
  "sex": "male",
  "bmi": 35,
  "children": 3,
  "smoker": "yes",
  "region": "northeast"
},"Older non-smoker":
{
  "age": 60,
  "sex": "female",
  "bmi": 28,
  "children": 1,
  "smoker": "no",
  "region": "northwest"
}}


for case_name,data in test_case.items():
    response=requests.post(url,json=data)
    print(f"{case_name}-> {response.json()}")
