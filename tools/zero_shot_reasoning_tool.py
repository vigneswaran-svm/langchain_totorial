from langchain.agents import initialize_agent

from langchain.tools import tool
from langchain.tools import Tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import Dict, Union
import re
from simple_openai_tool import add_tool
from add_numbers_with_options_tool import add_numbers_with_options

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini")

agent = initialize_agent(
    [add_tool], 
    llm, 
    agent="zero-shot-react-description", 
    verbose=True, 
    handle_parsing_errors=True)

@tool
def sum_numbers_with_complex_output(inputs: str) -> Dict[str, Union[float, str]]:
    """
    Extracts and sums all integers and decimal numbers from the input string.

    Parameters:
    - inputs (str): A string that may contain numeric values.

    Returns:
    - dict: A dictionary with the key "result". If numbers are found, the value is their sum (float). 
            If no numbers are found or an error occurs, the value is a corresponding message (str).

    Example Input:
    "Add 10, 20.5, and -3."

    Example Output:
    {"result": 27.5}
    """
    matches = re.findall(r'-?\d+(?:\.\d+)?', inputs)
    if not matches:
        return {"result": "No numbers found in input."}
    try:
        numbers = [float(num) for num in matches]
        total = sum(numbers)
        return {"result": total}
    except Exception as e:
        return {"result": f"Error during summation: {str(e)}"}

@tool
def sum_numbers_from_text(inputs: str) -> float:
    """
    Adds a list of numbers provided in the input string.
    
    Args:
        text: A string containing numbers that should be extracted and summed.
        
    Returns:
        The sum of all numbers found in the input.
    """
    # Use regular expressions to extract all numbers from the input
    numbers = [int(num) for num in re.findall(r'\d+', inputs)]
    result = sum(numbers)
    return result

#response = agent.run("In 2023, the US GDP was approximately $27.72 trillion, while Canada's was around $2.14 trillion and Mexico's was about $1.79 trillion what is the total.")

#agent.invoke({"input": "Add 10, 20, two and 30"})

agent_2 = initialize_agent(
    [add_numbers_with_options], 
    llm, 
    agent="structured-chat-zero-shot-react-description", 
    verbose=True, 
    handle_parsing_errors=True)

response = agent_2.invoke({
    "input": "Add -10, -20, and -30 using absolute values."
     })
print(response)




llm_ai = ChatOpenAI(model="gpt-4.1-nano")

agent_3 = initialize_agent(
    [sum_numbers_with_complex_output], 
    llm_ai, 
    agent="openai-functions", 
    verbose=True, 
    handle_parsing_errors=True)
response = agent_3.invoke({"input": "Add 10, 20 and 30"})
print(response)

agent_openai = initialize_agent(
    [add_numbers_with_options],
    llm_ai,
    agent="openai-functions",
    verbose=True
)

response = agent_openai.invoke({
    "input": "Add -10, -20, and -30 using absolute values."
})
print(response)