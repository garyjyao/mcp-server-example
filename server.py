import uvicorn
from fastapi import FastAPI
from fastmcp import FastMCP

mcp = FastMCP("Math Server", instructions="A math utility server.")

app = FastAPI(
    title="MCP Math Server",
    description="A FastAPI MCP math server",
    version="1.0.0-rc.1",
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "app_name": "mcp-server-example",
        "message": "It works on my machine!",
        "endpoints": {
            "docs": "/docs",
            "mcp": "/mcp",
        },
    }


def _add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def _subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def _multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def _divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def _power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base**exponent


def _sqrt(a: float) -> float:
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return a**0.5


def _modulo(a: float, b: float) -> float:
    """Calculate a mod b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b


def _factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# MCP tools
mcp.tool()(_add)
mcp.tool()(_subtract)
mcp.tool()(_multiply)
mcp.tool()(_divide)
mcp.tool()(_power)
mcp.tool()(_sqrt)
mcp.tool()(_modulo)
mcp.tool()(_factorial)

# FastAPI routes
app.get("/add", tags=["math"])(_add)
app.get("/subtract", tags=["math"])(_subtract)
app.get("/multiply", tags=["math"])(_multiply)
app.get("/divide", tags=["math"])(_divide)
app.get("/power", tags=["math"])(_power)
app.get("/sqrt", tags=["math"])(_sqrt)
app.get("/modulo", tags=["math"])(_modulo)
app.get("/factorial", tags=["math"])(_factorial)

app.mount("/mcp", mcp.http_app())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
