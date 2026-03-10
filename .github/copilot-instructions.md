# Copilot Instructions for data-eng-projects

## Project Overview

This is a data engineering platform repository with the following structure:

- **data_platform/**: Core data platform libraries and utilities
- **orchestration/kestra/**: Workflow definitions and orchestration using Kestra
- **projects/**: Individual project implementations (each may be a self-contained data pipeline)
- **docker/**: Docker containerization and environment setup
- **compose.yml**: Docker Compose configuration for local development and services

## Environment & Setup

### Development Environment
- The project uses Docker and Docker Compose for consistent environments
- Python development environment is configured via Conda (see `docker/environment.yml`)
- Development container configuration: `temp.devcontainer/devcontainer.json`

### Environment Variables
- Copy `.env.example` to `.env` for local development
- The `.env` file is git-ignored and should not be committed

### Local Development Setup
```bash
# Start services
docker compose up -d

# Stop services
docker compose down
```

## Architecture

### Multi-Project Structure
This repository follows a **monorepo pattern** where:
1. **Shared utilities** live in `data_platform/` for reuse across projects
2. **Workflow orchestration** is centralized in `orchestration/kestra/`
3. **Project-specific code** is isolated in `projects/`

Each project directory should be mostly independent, importing from `data_platform/` as needed.

### Kestra Workflows
Kestra is used for workflow orchestration. Workflow definitions go in `orchestration/kestra/`. Key conventions:
- Workflows define data pipelines, transformations, and dependencies
- Keep workflows DRY by reusing common tasks
- Use parameterized flows for different environments (dev, staging, prod)

## Build, Test & Lint

As of now, no formal CI/CD pipeline exists. When setting up:

- **Testing**: Use pytest for Python tests. Place tests in a `tests/` subdirectory alongside source code
- **Linting**: Consider using `black` for formatting and `pylint`/`flake8` for linting
- **Environment Management**: Dependencies should be specified in `docker/environment.yml` (Conda) or `requirements.txt` (pip)

## Code Conventions

### Python Style
- Follow PEP 8 conventions
- Use type hints where practical
- Docstrings for modules, classes, and public functions

### Project Organization
```
projects/my_project/
├── src/                    # Source code
│   ├── __init__.py
│   ├── extractors/         # Data extraction
│   ├── transformers/       # Data transformation
│   └── loaders/            # Data loading
├── tests/                  # Project tests
├── config.yaml             # Project configuration
└── README.md               # Project documentation
```

### Data Platform Modules
Modules in `data_platform/` should be:
- Well-documented (docstrings for all public APIs)
- Tested with unit tests
- Generic enough to be reused across projects

### Kestra Workflows
- Use meaningful flow names (e.g., `project-name-daily-sync`)
- Document flow parameters and outputs
- Use task naming that reflects the operation (extract, transform, load)
- Keep individual tasks focused on a single responsibility

## Git Conventions

- Commit messages should be descriptive and reference the problem they solve
- Use feature branches for new work
- Include Copilot authorship in commit messages:
  ```
  git commit -m "Your message..."
  ```

## Key Files & Directories

| Path | Purpose |
|------|---------|
| `compose.yml` | Docker Compose service definitions |
| `docker/environment.yml` | Conda environment for Python dependencies |
| `docker/init.sh` | Initialization script for Docker container |
| `temp.devcontainer/` | VS Code dev container configuration |
| `orchestration/kestra/` | Kestra workflow definitions |
| `data_platform/` | Shared data engineering libraries |
| `projects/` | Project-specific implementations |

## Important Notes

- This is a **multi-project monorepo**, so changes to `data_platform/` may affect multiple projects
- Always update `.env.example` when adding new environment variables
- Docker setup files should be updated when adding new dependencies or services
