from enum import Enum

class AppMessages(str, Enum):
    WELCOME = "Hello All"
    HEALTHY = "API is healthy and running."
    ERROR_GENERIC = "An unexpected error occurred. Please try again."
    NOT_FOUND = "Resource not found."
    INVALID_INPUT = "Invalid input provided."