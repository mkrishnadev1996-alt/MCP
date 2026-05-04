# mcp-check

A reference implementation and testbed for integrating Model Context Protocol (MCP) servers with LangChain and Google Gemini.

## Architecture Overview

This project demonstrates two primary patterns for implementing MCP clients using LangChain:

### 1. The Adapter Pattern (`main.py`)
Uses the `MultiServerMCPClient` from `langchain_mcp_adapters`. This approach is ideal for orchestrating multiple MCP servers across different transports (e.g., Stdio and HTTP) through a unified interface.

### 2. The Direct Session Pattern (`langchain_mcp_client.py`)
Uses `ClientSession` and `stdio_client` from the base `mcp` library. This provides low-level, direct communication with a specific MCP server, offering more control over the session lifecycle.

## Project Structure

- **Clients**:
  - `main.py`: Implementation of the Multi-server Adapter pattern.
  - `langchain_mcp_client.py`: Implementation of the Direct Session pattern.
- **Servers**:
  - `servers/math_server.py`: A computational tool provider using Stdio transport.
  - `servers/weather_server.py`: A weather data provider using HTTP transport.

## Setup & Usage

### Prerequisites
- Python 3.13+
- A Google Gemini API Key

### Installation
Install the dependencies using `uv` or `pip`:
```bash
pip install .
```

### Environment Variables
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_api_key_here
GOOGLE_MODEL=gemini-3-flash-preview
```

### Running the Examples

#### Running the Multi-Server Client
This client connects to both the math server (Stdio) and the weather server (HTTP).
```bash
python main.py
```
*Note: Ensure the weather server is running (see Server Configuration).*

#### Running the Direct Session Client
This client interacts exclusively with the math server.
```bash
python langchain_mcp_client.py
```

## Server Configuration

### Math Server
The math server is invoked directly by the clients via Python stdio.

### Weather Server
The weather server must be started independently to provide the HTTP endpoint:
```bash
python servers/weather_server.py
```
By default, it listens on `http://localhost:8000/mcp`.
