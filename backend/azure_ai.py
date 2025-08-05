import requests
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

# Azure Computer Vision
AZURE_CV_ENDPOINT = os.getenv("AZURE_CV_ENDPOINT")
AZURE_CV_KEY = os.getenv("AZURE_CV_KEY")

# Azure OpenAI
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")  # e.g. "gpt-4"

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)

def analyze_image_with_azure(image_path: str):
    url = f"{AZURE_CV_ENDPOINT}/computervision/imageanalysis:analyze?features=objects&api-version=2023-10-01"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_CV_KEY,
        "Content-Type": "application/octet-stream"
    }

    with open(image_path, "rb") as image_file:
        response = requests.post(url, headers=headers, data=image_file.read())

    response.raise_for_status()
    return response.json()


def generate_detailed_report(detected_objects: list) -> str:
    if not detected_objects:
        return "No visible damage was detected in the image."

    object_descriptions = []
    for obj in detected_objects:
        tags = obj.get("tags", [])
        if tags:
            object_descriptions.append(tags[0].get("name", "unknown object"))

    prompt = f"""
You are a certified automotive damage assessment specialist.

Based on the following detected objects on a damaged vehicle:
{', '.join(object_descriptions)}

Write a detailed and professional damage report that:
- Describes each damage area
- Explains how it might affect the vehicle's function or appearance
- Provides an estimated repair cost per item
- Calculates the total estimated repair cost
"""

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800,
    )

    return response.choices[0].message.content.strip()
