import os

from dotenv import load_dotenv
from pathlib import Path
from promptflow.tracing import trace
from promptflow.core import Prompty

BASE_DIR = Path(__file__).absolute().parent


@trace
def chat(question: str = "What's the capital of France?") -> str:
    """Flow entry function."""

    if (
        "LOCAL_MODEL" not in os.environ
        or "LOCAL_API_KEY" not in os.environ
        or "LOCAL_BASE_URL" not in os.environ
    ):
        load_dotenv()

    prompty = Prompty.load(source=BASE_DIR / "chat.prompty")
    # trigger a llm call with the prompty obj
    output = prompty(question=question)
    return output
