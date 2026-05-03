# ==================================================
# Generative AI: Automated Text Analysis & Summarization
# ==================================================

import os
import time
from google import genai
from IPython.display import Markdown, display

# ==================================================
# 1. SETUP API KEY
# ==================================================

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API Key not found. Please set GEMINI_API_KEY environment variable.")

client = genai.Client(api_key=API_KEY)

# ==================================================
# 2. CONFIG (MODEL + RETRY SYSTEM)
# ==================================================

MODELS = [
    "gemini-3-flash-preview",  # Main priority
    "gemini-2.0-flash"         # Fallback model
]

MAX_RETRY = 3
RETRY_DELAY = 30  # seconds

# ==================================================
# 3. GENERATE WITH FALLBACK + RETRY
# ==================================================

def generate_with_fallback(prompt):
    for model in MODELS:
        for attempt in range(MAX_RETRY):
            try:
                print(f"Trying model: {model} (Attempt {attempt+1})")
                
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                
                if response and response.text:
                    print(f"Success using {model}")
                    return response.text
            
            except Exception as e:
                print(f"Error: {e}")
                
                if "429" in str(e):
                    print(f"Quota limit reached, waiting {RETRY_DELAY} seconds...")
                    time.sleep(RETRY_DELAY)
                else:
                    break
                    
    raise RuntimeError("All models failed to generate a response.")

# ==================================================
# 4. SUMMARIZE FUNCTION
# ==================================================

def summarize_article(file_path):
    print("\n--- Task 1: Article Summarization ---")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            article_text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    # Prevent token overload
    article_text = article_text[:5000]

    prompt = f"""
Summarize the following article into clear and concise bullet points.

Requirements:
- Formal English
- Bullet points
- Max 300 words

Article:
{article_text}
"""
    try:
        result = generate_with_fallback(prompt)
        display(Markdown(result))
        return result
    except Exception as e:
        print(f"Summarization failed: {e}")
        return None

# ==================================================
# 5. ANALYZE FUNCTION
# ==================================================

def analyze_customer_feedback(file_path):
    print("\n--- Task 2: Customer Feedback Analysis ---")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            feedback = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    # Prevent token overload
    feedback = feedback[:5000]

    prompt = f"""
You are a professional data analyst.

Analyze the feedback and provide:
1. Sentiment analysis + reasoning
2. Key strengths
3. Key weaknesses
4. 10 actionable recommendations

Feedback:
{feedback}
"""
    try:
        result = generate_with_fallback(prompt)
        display(Markdown(result))
        return result
    except Exception as e:
        print(f"Analysis failed: {e}")
        return None

# ==================================================
# 6. MAIN EXECUTION
# ==================================================

if __name__ == "__main__":
    # Ensure these paths point to your actual text files
    article_path = "Artikel-1.txt"
    feedback_path = "Artikel-2.txt"

    print("Starting AI Pipeline...\n")

    summary_result = summarize_article(article_path)
    analysis_result = analyze_customer_feedback(feedback_path)

    print("\nPipeline execution completed.")
