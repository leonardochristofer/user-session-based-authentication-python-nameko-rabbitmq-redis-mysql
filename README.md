# User Session Based Authentication
This service contains:
1. Register API (add user to database)
- `127.0.0.1:8000/register`
2. Login API (get user from database to create user session)
- `127.0.0.1:8000/login`
3. Testing API for user session validity (cannot call API if there are no cookie exist)
- `127.0.0.1:8000/combinations`
- `127.0.0.1:8000/permutations`
4. Logout API (delete session)
- `127.0.0.1:8000/logout`
## Prerequisite to running Gateway and Service
This service uses python, nameko, rabbitmq, redis, and mysql. I assume that you have everything installed on your local machine.
## Steps
1. Clone this repository.
2. Import .sql file from database folder into your local machine mysql database.
3. Open 2 terminals.
4. `nameko run user_access.service` or `make run-user` for running user access service.
5. `nameko run gateway.service` or `make run-gateway` for running gateway.
6. If you are using Postman to test an API, refer to postman folder to get sample request or import .json file into your Postman collection.