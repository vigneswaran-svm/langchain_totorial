# Tech Context: LangChain Tutorial

## Technologies Used

### Core Framework
- **LangChain** - Framework for building LLM-powered applications
- **LangGraph** - Graph-based agent orchestration (prebuilt ReAct agents)
- **langchain_openai** - OpenAI integration for LangChain

### Language & Runtime
- **Python 3** - Primary programming language
- **Jupyter Notebooks** - Interactive development environment
- **venv** - Python virtual environment for dependency isolation

### AI/LLM
- **OpenAI GPT-4o-mini** - Default language model
- **ChatOpenAI** - LangChain wrapper for OpenAI chat models

### Utilities
- **python-dotenv** - Environment variable management from .env files
- **re (regex)** - Number extraction and text parsing

## Development Setup
1. Python virtual environment in `venv/`
2. API keys stored in `.env` file (OPENAI_API_KEY)
3. Run scripts directly: `python tools/simple_openai_tool.py`
4. Run notebooks via Jupyter/VS Code

## Technical Constraints
- Requires valid OpenAI API key in .env
- Internet connection needed for API calls
- Python 3.8+ required for LangChain compatibility
- Some tools depend on others (e.g., create_react_agent_tool imports from zero_shot_reasoning_tool)

## Dependencies
Key packages (installed in venv):
- `langchain`
- `langchain-openai`
- `langgraph`
- `python-dotenv`
- `openai`
- `jupyter`

## Tool Usage Patterns
- Scripts in `tools/` are self-contained and can be run independently
- Notebooks in `buil_agent/` are for interactive exploration
- All files use `load_dotenv()` to load API keys
- Tools use string inputs and return dict outputs
