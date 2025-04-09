# MCP Tools Project

## Overview

This project implements a suite of AI tools built on the Machine Communication Protocol (MCP) framework. Each tool leverages large language models through a client-server architecture to provide specialized functionality for search, mathematics, and news retrieval operations.

## Features

- **DuckDuckGo Search Engine**: Web search with content extraction capabilities
- **Mathematical Operations Engine**: Basic arithmetic with natural language processing
- **Tech News Aggregator**: Real-time technology news from reputable sources

## Requirements

- Python 3.8+
- UV package manager
- Groq API key

## Installation

### Setting up UV

If you don't have UV installed, install it first:

```bash
# Install UV using curl
curl -sSf https://install.ultraviolet.rs | sh

# Or with pip
pip install uv
```

### Installing Project Dependencies

Clone the repository and install dependencies using the existing pyproject.toml:

```bash
# Clone the repository
git clone https://github.com/rahulsamant37/mcp-tools.git
cd mcp-tools

# Create and activate a virtual environment
uv venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies from pyproject.toml
uv pip sync
```

If you need to install dependencies without an existing pyproject.toml:

```bash
# Install directly (will update pyproject.toml and uv.lock)
uv pip install mcp langchain-mcp-adapters langchain-groq langgraph httpx beautifulsoup4 python-dotenv
```

### Environment Configuration

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

## Usage Guide

Each tool can be tested independently by running its client script, which automatically launches the corresponding server component.

### DuckDuckGo Search Tool

```bash
python duckduckgo_client.py
```

This tool provides:
- Web search functionality via DuckDuckGo
- Content extraction from websites
- Rate-limited requests to prevent IP blocking
- Formatted search results optimized for LLM consumption

### Math Calculation Tool

```bash
python math_client.py
```

This tool enables:
- Basic arithmetic operations (addition, multiplication)
- Natural language processing of mathematical expressions
- Integration with ReAct agents for complex problem solving

### Tech News Retrieval Tool

```bash
python weather_client.py
```

This tool delivers:
- Latest articles from Ars Technica
- Content parsing and summarization
- Structured data output for LLM processing

## Technical Architecture

The project implements a microservices architecture using MCP:

### Server Layer
- Implements domain-specific functionality
- Exposes capabilities through standardized MCP interfaces
- Handles rate limiting and error management
- Processes raw data into LLM-friendly formats

### Client Layer
- Establishes connections to server components
- Creates LangChain-compatible tool interfaces
- Integrates with ReAct agents for reasoning
- Manages conversation context and state

### LLM Integration
- Leverages Groq's Qwen-2.5-32b model for reasoning
- Implements ReAct (Reasoning + Acting) methodology
- Supports asynchronous operations for improved performance

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Connection errors | Check that no other processes are using required ports |
| Authentication failures | Verify Groq API key in .env file |
| Rate limiting | Implement exponential backoff between requests |
| Timeout errors | Increase timeout values in httpx client configurations |
| Dependency issues | Run `uv pip list` to verify installations |
| UV sync errors | Check if pyproject.toml exists and is valid |

## Contributing

To extend this project with new tools:

1. Create a server file implementing your tool's functionality
2. Expose methods using the `@mcp.tool()` decorator
3. Develop a client file that establishes connections and loads tools
4. Integrate with the ReAct agent framework

## License

This project is licensed under the GNU License - see the LICENSE file for details.

## Acknowledgments

- [Machine Communication Protocol](https://github.com/llm-protocol/mcp) team
- [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) framework
- [Groq](https://groq.com/) for LLM API access