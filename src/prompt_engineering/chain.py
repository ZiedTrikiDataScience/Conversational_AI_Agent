from src.prompt_engineering.templates import get_system_prompt, get_user_prompt
from src.llm.openrouter_client import generate_with_openrouter
from src.llm.llamaindex_client import generate_with_llamaindex
from src.llm.langgraph_client import generate_with_langgraph
from src.utils.cache import disk_cache

@disk_cache
async def run_conversational_chain(question: str, model: str="openrouter") -> str:
    system = get_system_prompt()
    user_p = get_user_prompt(question)
    prompt = f"{system}\n\n{user_p}"
    if model == "llamaindex":
        return await generate_with_llamaindex(prompt)
    
    elif model == "langgraph":
        return await generate_with_langgraph(prompt)
    
    else:
        return await generate_with_openrouter(prompt)
