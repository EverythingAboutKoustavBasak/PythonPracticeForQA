"""
prompts
      │
      ▼
Execute __init__.py
      │
      ▼
Import SYSTEM_PROMPT
Import build_prompt


Without __init__.py
-------------------------
from prompts.system_prompt import SYSTEM_PROMPT
from prompts.prompt_builder import build_prompt

With __init__.py
------------------------
from prompts import SYSTEM_PROMPT, build_prompt


"""


from .system_prompt import SYSTEM_PROMPT
from .prompt_builder import build_user_prompt