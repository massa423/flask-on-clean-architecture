from app.config import config

template = {
    "swagger": "2.0",
    "info": {
        "title": "My API",
        "description": "API for my data",
        "contact": {
            "responsibleOrganization": "ME",
            "responsibleDeveloper": "Me",
            "email": "me@example.com",
            "url": "example.com",
        },
        "termsOfService": "https://example.com/terms",
        "version": "1.0.0",
    },
    "host": config().SWAGGER_HOST,
    "basePath": "/api/",
    "schemes": ["http"],
    "operationId": "getmyData",
}
