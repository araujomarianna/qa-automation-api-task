# qa-automation-api-task
In this repo you can find an API QA Automation test task in python with pytest.
## Setup
`pip install -r requirements.txt`
## Task
Write 5-10 automated tests in python of highest priority for api endpoint, which returns list of restaurants in Austria:
https://www.mjam.net/api/v3/restaurants/search/

Endpoint is implemented following this documentation:

1. Only method GET is allowed.
2. Authorization is done through token in Authorization header.
3. Mandatory parameter for request is address.

Example of using the endpoint:

curl -X GET -H 'Authorization:Token 0d6fcd84b74e2d81606e8daf5b1575c7c3fcfb40' https://www.mjam.net/api/v3/restaurants/search/?address=Liezen

## How to run
`pytest`  
At the end of execution a HTML report is generated