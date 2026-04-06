import os
import google.generativeai as genai

API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)  # still valid



def generate_test_script(description):
    prompt = f"""
    You are a QA automation engineer.
    Generate a Playwright Python test script for:
    {description}

    Requirements:
    - Use pytest
    - Use Playwright sync API
    - Include assertions
    - Follow good structure
    - Keep code clean and readable
    """
def generate_with_gemini(prompt: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text
        else:
            return "⚠️ Empty response from Gemini"

    except Exception as e:
        print("❌ Gemini Error:", e)
        return None


    def extract_text(response):
        return "".join(
            block.text for block in response.content
            if block.type == "text"
        )

    return extract_text(response)

if __name__ == "__main__":
    scenario = "Test login functionality for https://www.saucedemo.com with valid credentials"

    test_code = generate_test_script(scenario)

    # Save generated test
    with open("test_generated.py", "w") as f:
        f.write(test_code)

    print("✅ Test case generated and saved to test_generated.py")