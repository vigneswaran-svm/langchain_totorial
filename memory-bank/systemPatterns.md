# System Patterns: LangChain Tutorial

## System Architecture
```
langchain_totorial/
├── .env                    # API keys (OpenAI)
├── tools/                  # Standalone tool scripts
│   ├── simple_openai_tool.py
│   ├── add_numbers_with_options_tool.py
│   ├── create_react_agent_tool.py
│   ├── simple_AI_math_tool.py
│   └── zero_shot_reasoning_tool.py
├── buil_agent/             # Jupyter notebooks for agents
│   ├── BuildInteractiveLLMAgentswithTools.ipynb
│   ├── LLM_powered_data_science_LCEL.ipynb
│   ├── math_agent.ipynb
│   └── wikipedia_tool.ipynb
└── venv/                   # Python virtual environment
```

## Key Technical Decisions
1. **Python as primary language** - Standard for LangChain ecosystem
2. **Virtual environment (venv)** - Isolated dependency management
3. **Jupyter notebooks for agents** - Interactive experimentation
4. **Standalone scripts for tools** - Focused, testable examples
5. **dotenv for secrets** - API key management via .env file

## Design Patterns in Use

### Tool Creation Patterns
1. **@tool Decorator Pattern** - Preferred for type-safe tools with auto-generated schemas
   ```python
   @tool
   def add_numbers(inputs: str) -> dict:
       """Docstring becomes tool description"""
       ...
   ```

2. **Tool Constructor Pattern** - Wraps existing functions
   ```python
   add_tool = Tool(
       name="AddTool",
       func=add_numbers,
       description="..."
   )
   ```

### Agent Patterns
1. **ReAct Agent** - Using `langgraph.prebuilt.create_react_agent`
   ```python
   agent_exec = create_react_agent(model=llm, tools=[tool1, tool2])
   msgs = agent_exec.invoke({"messages": [("human", "...")]})
   ```

2. **Zero-Shot Reasoning** - Tools that parse and process without prior examples

### Common Code Patterns
- `load_dotenv()` at script start for environment variables
- `ChatOpenAI(model="gpt-4o-mini")` as the default LLM
- Regex-based number extraction: `re.findall(r'\d+', inputs)`
- String-based tool inputs with parsing logic
- Dict return format: `{"result": value}`

## Component Relationships
- Tools are independent, reusable components
- Agents compose multiple tools together
- Notebooks import and orchestrate tools/agents
- All components share the same .env configuration
