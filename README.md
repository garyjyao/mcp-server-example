# mcp-server-example

[![Build](https://github.com/jecklgamis/mcp-server-example/actions/workflows/build.yaml/badge.svg)](https://github.com/jecklgamis/mcp-server-example/actions/workflows/build.yaml)

A FastAPI MCP (Model Context Protocol) math server built with [FastMCP](https://github.com/jlowin/fastmcp).

## Tools

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
- MCP endpoint at `/mcp` (streamable-http transport)
- REST API endpoints at `/add`, `/subtract`, `/multiply`, `/divide`, `/power`, `/sqrt`, `/modulo`, `/factorial`
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
python client.py
```

```bash
LLM_PROVIDER=openai python client.py
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
