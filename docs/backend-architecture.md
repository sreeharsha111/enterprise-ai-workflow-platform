# Backend Architecture

## Project Structure

```
backend/

└── app/

    ├── api/

    ├── services/

    ├── repositories/

    ├── models/

    ├── schemas/

    ├── db/

    ├── auth/

    ├── ai/

    ├── workflow/

    ├── core/

    └── main.py
```

---

# Folder Responsibilities

## api/

Contains all REST API endpoints.

Examples:

* Authentication APIs
* Project APIs
* Task APIs
* Workflow APIs

The API layer communicates with the Service layer.

---

## services/

Contains business logic.

Examples:

* ProjectService
* TaskService
* WorkflowService
* AIService

This layer coordinates multiple repositories and external services.

---

## repositories/

Responsible only for data access.

Examples:

* ProjectRepository
* TaskRepository
* UserRepository

This layer communicates with PostgreSQL.

---

## models/

Contains database models.

Each model represents one database table.

Examples:

* User
* Organization
* Project
* Task

---

## schemas/

Contains request and response models.

Examples:

* CreateProjectRequest
* UpdateTaskRequest
* LoginResponse

Schemas validate incoming data and define API responses.

---

## db/

Contains database configuration.

Responsibilities:

* Database connection
* Session management
* Migrations

---

## auth/

Contains authentication-related components.

Responsibilities:

* JWT generation
* Password hashing
* Token validation
* Authorization

---

## ai/

Contains AI-related functionality.

Future responsibilities:

* Prompt templates
* AI agents
* LLM integrations
* RAG
* Embedding generation

---

## workflow/

Contains workflow engine implementation.

Responsibilities:

* Workflow definitions
* Workflow execution
* Trigger handling
* Action execution

---

## core/

Contains application-wide configurations.

Examples:

* Environment variables
* Logging
* Security configuration
* Constants

---

## main.py

Application entry point.

Responsibilities:

* Initialize FastAPI
* Register routers
* Load configuration
* Start application

```
```
