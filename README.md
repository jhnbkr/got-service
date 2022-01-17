# Game of Thrones Service

[API Documentation](https://documenter.getpostman.com/view/6815172/UVXkoFco)

[https://got-service.herokuapp.com/api/character/](https://got-service.herokuapp.com/api/character/)

[https://got-service.herokuapp.com/api/house/](https://got-service.herokuapp.com/api/house/)

Data provided by [https://github.com/joakimskoog/AnApiOfIceAndFire](https://github.com/joakimskoog/AnApiOfIceAndFire).

## Development

#### Setup

- [ ] [Create Environment](#create-environment)
- [ ] [Docker Services (Optional)](#docker-services-optional)
- [ ] [Configure Environment](#configure-environment)
- [ ] [Update Database](#update-database)
- [ ] [Run Application](#run-application)

#### Create Environment

Create Python virtual environment and install dependencies

```
python -m venv venv
source venv/bin/activate
make install
```

#### Docker Services (Optional)

Optionally you can run necessary services with Docker; db (postgres), cache (redis), and broker (rabbitmq).

```
docker compose -f develop/docker-compose.yml up
```

*WARNING*: The provided Docker compose configuration is intended for local development only.

```
DATABASE_URL=postgres://postgres:postgres@localhost:5432/postgres
REDIS_URL=redis://localhost:6379
```

#### Configure Environment

Create `.env` file in the project root and configure.

```
cp .env.template .env
```

#### Update Database

Sync database with project.

```
python manage.py migrate
python manage.py loaddata initial_data
```

#### Run Application

Run development server

```
source venv/bin/activate
make run
```

Run web server

```
source venv/bin/activate
make web
```
