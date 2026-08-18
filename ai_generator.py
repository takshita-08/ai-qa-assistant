import os
from google import genai

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

# Create client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))



def generate_test_script(description):
    prompt = f"""
    You are a QA automation engineer.
    Generate Python Playwright pytest test. Code only, no text.
    Include imports, test_ function, assertions.
    Do not include ``` or markdown formatting.

    {description}
    """

    try:
        print("🚀 Starting request...")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        print("✅ Got response")

        return response.text.strip() if response.text else "⚠️ Empty response"

    except Exception as e:
        print("❌ Gemini Error:", e)
        return None


if __name__ == "__main__":
    scenario = "Test login functionality for https://www.saucedemo.com with invalid credentials"

    code = generate_test_script(scenario)

    if code:
        with open("test_generated_invalid.py", "w") as f:
            f.write(code)

        print("✅ Generated successfully")