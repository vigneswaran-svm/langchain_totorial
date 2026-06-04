# Product Context: LangChain Tutorial

## Why This Project Exists
This project serves as a personal learning repository for mastering LangChain and related AI agent frameworks. It provides a structured environment to experiment with different patterns for building AI-powered tools and agents.

## Problems It Solves
- Provides hands-on examples for understanding LangChain tool creation
- Demonstrates different approaches to building agents (ReAct, zero-shot)
- Shows how to integrate OpenAI models with custom tool logic
- Offers reusable patterns for math operations, Wikipedia lookups, and more

## How It Works
The project is organized into two main directories:
1. **tools/** - Standalone Python scripts demonstrating individual tool patterns
2. **buil_agent/** - Jupyter notebooks for interactive agent building and experimentation

### Key Workflows
- Tool creation using `@tool` decorator and `Tool` constructor
- ReAct agent creation using `langgraph.prebuilt.create_react_agent`
- LCEL chains for data science workflows
- Interactive notebook-based experimentation

## User Experience Goals
- Clear, well-documented code examples
- Progressive complexity (simple tools → full agents)
- Easy to run and modify for learning purposes
- Self-contained examples with minimal setup
