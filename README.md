### User Session Based Authentication
This service contains:
1. Register API (add user to database)
- `127.0.0.1:8000/register`
Sample JSON input
{
    "userAccount": "Hello",
    "userPassword": "World"
}
2. Login API (get user from database to create user session)
- `127.0.0.1:8000/login`
Sample JSON input
{
    "userAccount": "Hello",
    "userPassword": "World"
}
3. Testing API for user session validity (cannot call API if there are no cookie exist)
- `127.0.0.1:8000/combinations`
Sample JSON input
{
    "input": "Hello",
    "size": 3
}
- `127.0.0.1:8000/permutations`
Sample JSON input
{
    "input": "Hello"
}
4. Logout API (delete session)
- `127.0.0.1:8000/logout`
```

```
### Prerequisite to running Gateway and Service
This service uses python, nameko, rabbitmq, redis, and mysql. I assume that you have everything installed on your local machine.
```

```
### Steps
1. Clone this repository.
2. Import .sql file into your local machine mysql database and refer to `user_access` table for login API or create your own user using register API.
3. Open 2 terminals.
4. `nameko run gateway_service` for running gateway.
5. `nameko run user_access_service` for running user access service.
6. With testing tools (usually Postman), Hit API on `127.0.0.1:8000/combinations` or `127.0.0.1:8000/permutations` using JSON as request body to test user session validity.
