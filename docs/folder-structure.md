# Backend Folder Structure

The backend is organized into logical layers.

Folders are introduced only when the project requires them.

---

## app/

Contains the application source code.

Everything related to the backend lives inside this folder.

---

## api/

Purpose:

Expose REST APIs.

Responsibilities:

* Receive requests
* Validate input
* Return responses

Never:

* Business logic
* SQL

---

## services/

Purpose:

Contains business logic.

Responsibilities:

* Validation
* Business rules
* Workflow orchestration

---

## repositories/

Purpose:

Communicate with the database.

Responsibilities:

* INSERT
* UPDATE
* DELETE
* SELECT

Never:

* Business decisions

---

## models/

Purpose:

Represent database tables.

Every model corresponds to a PostgreSQL table.

---

## schemas/

Purpose:

Define request and response objects.

Used for validation and API documentation.

---

## db/

Purpose:

Database configuration.

Responsibilities:

* Database connection
* Session management
* Migration support

---

## core/

Purpose:

Application-wide configuration.

Examples:

* Settings
* Logging
* Security
* Environment Variables

---

## tests/

Purpose:

Automated testing.

Contains:

* Unit Tests
* Integration Tests

```
```
