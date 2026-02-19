# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to create a simple RESTful API using the FastAPI framework. Students will practice defining routes, handling requests and responses, and running a development server.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Create a new FastAPI application with a few basic endpoints. You should be able to start the server and see the automatic documentation.

#### Requirements
Completed program should:

- Install FastAPI and an ASGI server (e.g., `uvicorn`) using `pip`.
- Define a `FastAPI()` instance in a Python file (e.g. `starter-code.py`).
- Include at least two routes: one that returns a welcome message and another that echoes a path parameter.
- Run the application locally and verify that `http://127.0.0.1:8000/docs` shows the interactive API docs.

### 🛠️ Add CRUD Endpoints

#### Description
Extend the application with simple in-memory storage to support basic CRUD operations for an item (e.g. a dictionary of products).

#### Requirements
Completed program should:

- Define a Python data model using Pydantic (`BaseModel`).
- Implement endpoints to create, read, update, and delete items.
- Use appropriate HTTP methods (`POST`, `GET`, `PUT`, `DELETE`).
- Return JSON responses and use proper status codes (e.g. `201` on create).
- Test the endpoints using the interactive docs or curl commands.

### 🛠️ (Optional) Validation and Query Parameters

#### Description
Add input validation and support for query parameters to filter results.

#### Requirements
Completed program should:

- Validate request data automatically with Pydantic models.
- Accept a query parameter on the read endpoint to limit results (e.g. `?limit=5`).
- Return appropriate error messages for invalid input.
