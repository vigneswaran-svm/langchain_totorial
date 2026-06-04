# Active Context: LangChain Tutorial

## Current Work Focus
- Setting up Memory Bank infrastructure for project continuity
- Exploring LangChain tools and agent patterns
- Building math operation tools (add, subtract, multiply, divide)
- Creating ReAct agents with LangGraph

## Recent Changes
- Established Memory Bank with all core documentation files
- Created `.clinerules` configuration for project standards
- Project contains working tool implementations and agent notebooks

## Next Steps
- Continue expanding tool library with new capabilities
- Explore more complex agent patterns beyond basic math
- Add error handling and input validation to existing tools
- Consider adding structured output parsing
- Explore multi-agent workflows with LangGraph

## Active Decisions and Considerations
- Using GPT-4o-mini as the default model (cost-effective for learning)
- String-based inputs for tools (simple but limited type safety)
- Regex for number extraction (works for digits, not word-numbers like "four")
- Notebooks for complex workflows, scripts for individual tools

## Important Patterns and Preferences
- All tools follow the pattern: string input → processing → dict output
- `load_dotenv()` is always called at the top of each file
- Tools include comprehensive docstrings with examples
- Test invocations are included at the bottom of tool scripts

## Learnings and Project Insights
- The `@tool` decorator auto-generates `args_schema` from type hints
- `Tool` constructor is simpler but less type-safe
- `create_react_agent` from langgraph handles tool routing automatically
- Number extraction via regex misses word-form numbers (e.g., "four")
