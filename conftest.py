# conftest.py
from dotenv import load_dotenv
from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve().parent
ENV_PATH = ROOT_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)
print("WC_KEY =", os.environ.get("WC_KEY"))
print("ENV =", os.environ.get("ENV"))
