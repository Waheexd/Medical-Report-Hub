import base64
import os
from rag.llm import get_vision_llm
from langchain_core.messages import HumanMessage

def extract_text_from_image(image_path: str) -> str:
    """
    Extract text from an image using Groq's Vision model.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at {image_path}")

    # 1. Encode image to base64
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    # 2. Initialize Vision model
    vision_llm = get_vision_llm()

    # 3. Create prompt for OCR-like transcription
    prompt = """
    Transcribe all text from this medical laboratory report image exactly as it appears. 
    Maintain the tabular structure where possible so that test names, values, units, and reference ranges are clearly linked.
    Do not add any preamble or summary. Just the transcribed text.
    """

    # 4. Invoke model with image
    message = HumanMessage(
        content=[
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                },
            },
        ]
    )

    response = vision_llm.invoke([message])
    
    return response.content
