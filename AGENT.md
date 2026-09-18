# AGENTS.md

## Project Name

Agent Lab Playground

## Project Purpose

This repository is a small playground project for testing how AI agents work in a real software project.

The goal is not to build a large product. The goal is to observe how agents can:

- Read project context
- Review code
- Run tests
- Find bugs
- Suggest fixes
- Generate feedback
- Save reports
- Help with local deployment

## Project Description

This project is a simple FastAPI Todo API.

Current API features:

- Health check endpoint
- Create task endpoint
- List tasks endpoint
- Basic automated tests with pytest

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pytest
- HTTPX
- Uvicorn
- GitHub
- VS Code
- Windows PowerShell

## Repository Structure

```text
agent-lab-playground/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── service.py
├── tests/
│   └── test_api.py
├── scripts/
│   └── run_checks.ps1
├── reports/
│   └── agent-runs/
├── agent_specs/
├── AGENTS.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Important Files

### app/main.py

Contains the FastAPI application and API endpoints.

### app/service.py

Contains the business logic for managing tasks.

### tests/test_api.py

Contains automated API tests.

### scripts/run_checks.ps1

Runs the basic local checks for the project.

### reports/agent-runs/

Stores agent review reports, test summaries, and feedback logs.

## API Endpoints

### GET /health

Checks whether the API is running.

Expected response:

```json
{
  "status": "ok"
}
```

### GET /tasks

Returns the list of tasks.

Expected response:

```json
[]
```

or:

```json
[
  {
    "id": 1,
    "title": "Review project with agent",
    "completed": false
  }
]
```

### POST /tasks

Creates a new task.

Example request:

```json
{
  "title": "Review project with agent"
}
```

Expected response:

```json
{
  "id": 1,
  "title": "Review project with agent",
  "completed": false
}
```

## Standard Commands

### Activate virtual environment

PowerShell:

```powershell
.venv\Scripts\Activate
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.venv\Scripts\Activate
```

### Install dependencies

```powershell
pip install -r requirements.txt
```

### Run tests

```powershell
pytest -v
```

### Run local API

```powershell
uvicorn app.main:app --reload
```

### Open API docs

```text
http://127.0.0.1:8000/docs
```

### Run local project checks

```powershell
.\scripts\run_checks.ps1
```

## Agent Roles

This project may use multiple agents. Each agent has a clear responsibility.

### reviewer-agent

Purpose:

- Review code quality
- Find possible bugs
- Check naming and readability
- Check missing edge cases
- Suggest improvements

Output:

- Review summary
- Issues found
- Suggested fixes
- Risk level

### tester-agent

Purpose:

- Run test commands
- Read test results
- Identify failing tests
- Explain test failures clearly

Output:

- Test command used
- Passed tests
- Failed tests
- Error explanation
- Suggested next step

### fixer-agent

Purpose:

- Suggest small code fixes
- Modify code only when explicitly allowed
- Keep changes small and focused

Output:

- Files changed
- Reason for change
- Tests to run after change

### feedback-agent

Purpose:

- Summarize all agent results
- Write beginner-friendly feedback
- Save review result into reports/agent-runs/

Output:

- What was checked
- What passed
- What failed
- What should be improved next

### deploy-agent

Purpose:

- Run local deployment only
- Check whether the API starts successfully
- Check health endpoint

Rules:

- Do not deploy to production
- Do not use cloud deployment unless explicitly approved
- Local testing only

## Agent Rules

All agents must follow these rules:

1. Read this file before analyzing the project.
2. Prefer reviewing changed files or git diff instead of reading the entire repository.
3. Do not make large changes without approval.
4. Always run tests after code changes.
5. Explain errors in simple language.
6. Save review reports inside reports/agent-runs/.
7. Do not delete files unless explicitly instructed.
8. Do not deploy to production.
9. Do not expose secrets, API keys, tokens, or credentials.
10. Keep feedback clear and actionable.

## Review Priorities

When reviewing this project, focus on:

1. Correctness
2. Test coverage
3. Simple code structure
4. Clear API behavior
5. Error handling
6. Beginner-friendly maintainability
7. Security basics
8. Deployment readiness

## What Agents Should Check

Agents should check:

- Does the API run?
- Do tests pass?
- Are endpoints clear?
- Are function names understandable?
- Are there missing tests?
- Are errors handled clearly?
- Is the project easy to run locally?
- Are reports saved properly?
- Is the README or documentation outdated?

## What Agents Should Not Do

Agents should not:

- Rewrite the whole project
- Add unnecessary frameworks
- Add complex architecture too early
- Deploy to cloud without approval
- Modify unrelated files
- Hide errors
- Skip tests after changes

## Expected Review Report Format

Each review report should use this structure:

```md
# Agent Review Report

## Run Information

- Date:
- Agent:
- Model:
- Task:
- Files reviewed:

## Commands Run

```text
command here
```

## Summary

Short summary of what was checked.

## Passed

- Item 1
- Item 2

## Issues Found

### Issue 1

Severity: Low / Medium / High

Description:

Suggested fix:

## Missing Tests

- Test suggestion 1
- Test suggestion 2

## Next Actions

1. Action 1
2. Action 2
3. Action 3

## Token Usage

- Prompt tokens:
- Completion tokens:
- Total tokens:
- Estimated cost:
```

## Token Tracking Goal

One purpose of this project is to observe token usage.

When possible, agents should record:

- Model name
- Prompt size
- Completion size
- Total tokens
- Estimated cost
- Files included in context

If exact token usage is not available, agents should clearly say:

```text
Exact token usage is not available in this environment.
```

## Beginner Explanation Rule

The user is learning how agents work.

When explaining results, agents should avoid overly complex language.

Good explanation style:

```text
The test failed because the API returned a different value than the test expected.
```

Avoid unclear explanation style:

```text
The assertion failed due to response schema inconsistency in the endpoint contract.
```

## Current Project Stage

Stage:

```text
Learning and experimentation
```

Current goal:

```text
Build a small project where agents can review, test, generate feedback, and help improve code step by step.
```