import os
import re
from dotenv import load_dotenv
from sarvamai import SarvamAI

def get_sarvam_client():
    """Get fresh Sarvam client with reloaded API key."""
    load_dotenv(override=True)  # Force reload from disk
    api_key = os.getenv("SARVAM_API_KEY")
    if not api_key:
        raise ValueError("SARVAM_API_KEY not found in .env")
    return SarvamAI(api_subscription_key=api_key)

SYSTEM_PROMPT = (
    "You are a helpful e-commerce customer support assistant. "
    "Answer with a single direct customer-facing response. "
    "Do not include analysis, internal reasoning, planning, or debugging notes. "
    "Do not show steps, drafts, or any text intended for developers. "
    "Return only the final answer text in one or two short sentences unless the user explicitly asks for more detail."
)

MODEL_NAME = "sarvam-105b"


