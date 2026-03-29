# Simple Date MCP Example

This is a very small MCP example for learning.

It contains:

- `date_server.py`: the MCP server
- `date_client.py`: the client that starts the server, lists the tools, and calls the date tool

The server exposes one tool:

- `get_today_date()`: returns today's date in `YYYY-MM-DD` format

## How It Works

1. You run the client.
2. The client starts the server.
3. The client connects to the server using `stdio`.
4. The client asks the server which tools are available.
5. The client calls the `get_today_date` tool.
6. The result is printed in the terminal.

## How To Run

Run this from the project root:

```bash
uv run date_mcp/date_client.py
```

You should see:

- the available tool name
- today's date printed in the terminal

## Which File Is The Main One?

The main file to run is:

`date_mcp/date_client.py`

That is the file that drives the whole example.

## Optional

If you run only the server:

```bash
uv run date_mcp/date_server.py
```

it will start and wait for a client connection. By itself, it does not do much, because the client is the part that asks for tools and calls them.
