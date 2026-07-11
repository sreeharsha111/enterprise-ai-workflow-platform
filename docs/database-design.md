# Database Design

## Overview

The database is designed around Organizations.

Every Organization contains:

* Users
* Projects
* Tasks
* Workflows

---

# Roles

Purpose:

Defines permissions in the system.

Examples:

* Admin
* Manager
* User

Fields:

* id
* name
* description

---

# Users

Purpose:

Represents platform users.

Fields:

* id
* first_name
* last_name
* email
* password_hash
* role_id
* organization_id
* created_at
* updated_at

Relationships:

User belongs to one Organization.

User has one Role.

---

# Organizations

Purpose:

Represents a company or team using the platform.

Fields:

* id
* name
* owner_id
* created_at

Relationships:

Organization contains many Users.

Organization contains many Projects.

Organization contains many Workflows.

---

# Projects

Purpose:

Represents business initiatives.

Examples:

* AI Workflow Platform
* Client Portal
* Data Migration

Fields:

* id
* organization_id
* name
* description
* status
* created_by
* created_at

Relationships:

Project belongs to one Organization.

Project contains many Tasks.

---

# Tasks

Purpose:

Represents work items.

Examples:

* Build Login API
* Create Database Schema
* Deploy Application

Fields:

* id
* project_id
* title
* description
* status
* priority
* assigned_to
* due_date
* created_by
* created_at

Relationships:

Task belongs to one Project.

Task is assigned to one User.

---

# Workflows

Purpose:

Defines automation processes.

Example:

Task Created
→ Assign Reviewer
→ Notify Team

Fields:

* id
* organization_id
* name
* is_active
* created_by

Relationships:

Workflow belongs to one Organization.

Workflow contains multiple Workflow Nodes.

---

# Workflow Nodes

Purpose:

Represents individual workflow steps.

Node Types:

* Trigger
* Action
* Condition

Fields:

* id
* workflow_id
* node_type
* configuration
* position_x
* position_y

Relationships:

Node belongs to one Workflow.

---

# Future Tables

To be implemented later:

* Documents
* Embeddings
* Conversations
* AI Agent Executions
* MCP Tool Registrations
* Audit Logs


# Entity Relationships

## Roles -> Users

Relationship Type:
One-to-Many

roles.id -> users.role_id

One role can be assigned to many users.

---

## Organizations -> Users

Relationship Type:
One-to-Many

organizations.id -> users.organization_id

One organization can contain many users.

---

## Organizations -> Projects

Relationship Type:
One-to-Many

organizations.id -> projects.organization_id

One organization can contain many projects.

---

## Projects -> Tasks

Relationship Type:
One-to-Many

projects.id -> tasks.project_id

One project can contain many tasks.

---

## Users -> Tasks

Relationship Type:
One-to-Many

users.id -> tasks.assigned_to

One user can have multiple assigned tasks.

---

## Organizations -> Workflows

Relationship Type:
One-to-Many

organizations.id -> workflows.organization_id

One organization can contain many workflows.

---

## Workflows -> Workflow Nodes

Relationship Type:
One-to-Many

workflows.id -> workflow_nodes.workflow_id

One workflow can contain multiple workflow nodes.
