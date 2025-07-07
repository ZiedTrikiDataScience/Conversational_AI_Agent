import yaml

def load_templates(path="config/prompt_templates.yaml") -> dict:
    return yaml.safe_load(open(path, "r"))

_templates = load_templates()

def get_system_prompt() -> str:
    return _templates["system"]["welcome"]

def get_user_prompt(question: str) -> str:
    return _templates["user"]["question"].replace("{{ question }}", question)
