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
- MCP endpoint at `/mcp` (streamable-http transport)
- REST API endpoints at `/add`, `/subtract`, `/multiply`, `/divide`, `/power`, `/sqrt`, `/modulo`, `/factorial`
- API docs at `/docs`

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
