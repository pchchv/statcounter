<div align="center">

# Microservice for statistics counters

</div>

## Running the application

```
docker-compose up --build
```

### Running the application without Docker

```
uvicorn main:app
```

## HTTP Methods

```
"GET" / — Checking the server connection

    example: 
        "GET" :8000/
```

```
"GET" /stat — Get statistics for a given period
    options:
        fromDate — YYYY-MM-DD
        toDate — YYYY-MM-DD

    example: 
        "GET" :8000/stat?fromDate=2022-02-23,toDate=2022-03-11
```

```
"POST" /json —  Saves statistics. Need JSON body

    example: 
        "POST" :8000/json
```

```json
{
    "date": "2022-03-21",
    "views": 37,
    "clicks": 4,
    "cost": 9.99
}
```

```
"POST" / — Saves statistics. without JSON.
    options:
        date — Date of event. YYYY-MM-DD
        views — Number of views
        clicks — Number of clicks
        cost — Cost of clicks (in rubles accurate to a penny)

    example: 
        "POST" :8000/?date=2022-03-21,views=37,clicks=4,cost=9.99
```

```
"DELETE" / —  Deletes all statistics.

    example: 
        "DELETE" :8000/delete
```
