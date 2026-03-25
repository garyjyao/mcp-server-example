# mcp-server-example

[![Build](https://github.com/jecklgamis/mcp-server-example/actions/workflows/build.yaml/badge.svg)](https://github.com/jecklgamis/mcp-server-example/actions/workflows/build.yaml)

A FastAPI MCP (Model Context Protocol) server built with [FastMCP](https://github.com/jlowin/fastmcp). Exposes math and performance testing tools over streamable-http transport.

## MCP Tools

### Math (`/math_mcp`)

| Tool        | Description                                    |
|-------------|------------------------------------------------|
| `add`       | Add two numbers                                |
| `subtract`  | Subtract b from a                              |
| `multiply`  | Multiply two numbers                           |
| `divide`    | Divide a by b                                  |
| `power`     | Raise base to the power of exponent            |
| `sqrt`      | Calculate the square root of a number          |
| `modulo`    | Calculate a mod b                              |
| `factorial` | Calculate the factorial of a non-negative integer |

### Perf (`/perf-mcp`)

| Tool             | Description                                         |
|------------------|-----------------------------------------------------|
| `run_perf_test`  | Run a load test against a URL with concurrent requests |

## Project Structure

```
server.py              — FastAPI app entry point with REST routes and MCP mount
math_mcp_server.py     — Math MCP server with tool definitions
perf_mcp_server.py     — Perf MCP server with load testing tool
math_mcp_client.py     — Interactive LangChain agent client (math)
perf_mcp_client.py     — Interactive LangChain agent client (perf)
llm_factory.py         — LLM provider factory (ollama, openai, gemini)
requirements.txt       — Python dependencies
Dockerfile             — Container image definition
Makefile               — Build and run shortcuts
deployment/            — Helm chart for Kubernetes deployment
```

## Getting Started

### Requirements

* Python 3.13+

### Run Locally

```bash
pip install -r requirements.txt
python server.py
```

The server starts on `http://localhost:8080` with:
- Root endpoint at `/` listing available endpoints
- Math MCP endpoint at `/math_mcp` (streamable-http transport)
- Perf MCP endpoint at `/perf-mcp` (streamable-http transport)
- REST API endpoints at `/add`, `/subtract`, `/multiply`, `/divide`, `/power`, `/sqrt`, `/modulo`, `/factorial`, `/run_perf_test`
- API docs at `/docs`

### Run Client

The client uses a LangChain agent to interact with the MCP server via an interactive REPL. Configure the LLM provider via the `LLM_PROVIDER` env var and the server URL via `MCP_SERVER_URL`.

| Env Var          | Description              | Default                   |
|------------------|--------------------------|---------------------------|
| `LLM_PROVIDER`  | LLM provider to use      | `ollama`                  |
| `MCP_SERVER_URL` | MCP server base URL      | `http://localhost:8080`   |

Supported LLM providers:

| Provider | Model              |
|----------|--------------------|
| `ollama` | `llama3.1`         |
| `openai` | `gpt-4.1`          |
| `gemini` | `gemini-2.5-flash` |

```bash
python math_mcp_client.py
```

```bash
python perf_mcp_client.py
```

```bash
LLM_PROVIDER=openai python math_mcp_client.py
```

### Run with Docker

```bash
docker build -t mcp-server-example .
docker run -p 8080:8080 mcp-server-example
```

### Deploy with Helm

```bash
cd deployment/k8s/helm
helm install mcp-server-example ./mcp-server-example
```

### Upgrade with Helm

```bash
cd deployment/k8s/helm
make upgrade
```

## Makefile Targets

| Target              | Description                        |
|---------------------|------------------------------------|
| `install-deps`      | Install Python dependencies        |
| `image`             | Build Docker image                 |
| `run`               | Run Docker container               |
| `run-shell`         | Start a shell in a new container   |
| `exec-shell`        | Exec into a running container      |
| `check`             | Run tests with pytest              |
| `clean`             | Remove generated files             |
| `up`                | Build and run (`check` + `image` + `run`) |

## CI/CD

The GitHub Actions [workflow](.github/workflows/build.yaml) runs on pushes to `main` and on pull requests. It builds the project with Python 3.13 and pushes a Docker image to Docker Hub on non-PR events.
