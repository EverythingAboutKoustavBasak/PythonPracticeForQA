"""
__init__.py is a special file that marks a directory as a Python package. 
It is executed when the package is imported and can be used to initialize the package, 
expose selected classes or functions, and simplify imports.

Now anywhere in your project you simply write(Inside this project, you can write:):
from exceptions import MissingAPIKey
instead of
from exceptions.custom_exceptions import MissingAPIKey

how can another project import it?
Ans -
Turn your project into an installable package.(ex - ai_test_case_generator/)
Then install it: pip install .
Now any project can do: from ai_test_case_generator.exceptions import MissingAPIKey
This is how libraries like requests, pydantic, and pytest work.

"""



from .custom_exceptions import (
    MissingAPIKey,
    EmptyUserStory,
    InvalidAIResponse,
    APICallFailed,
)

