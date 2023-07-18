# Insurance-Calculation-App
Implement a REST API service for calculating the cost of insurance depending on the type of cargo and the declared value (OS).
The fare must be loaded from a JSON file or must accept a JSON-like structure:
```
{
  "2020-06-01": [
    {
      "cargo_type": "Glass",
      "rate": 0.04,
      "freight_amount": 4000
    },
    {
      "cargo_type": "Hazardous",
      "rate": 0.10,
      "freight_amount": 9000
    },
    {
      "cargo_type": "Other",
      "rate": 0.05,
      "freight_amount": 3000
    }
  ]
}

```
 The service must calculate the cost of insurance for the request using the current rate. (Downloaded via API)
The service returns (declared value * rate) depending on the type of cargo and date specified in the request.
 The service must be deployed inside Docker.
Service must be developed via GIT (Readme file with deployment details)
Data must be stored in a database
Technologies that should be used in the implementation of the test task:
•	FastApi-framework
•	Tortoise ORM
•	Postgresql, Mysql, Sqlite - any to choose from
•	Docker
