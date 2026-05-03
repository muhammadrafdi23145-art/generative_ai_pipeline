# ==============================================================================
# Generative AI Task: Text Summarization & Customer Feedback Analysis
# Designed for Jupyter Notebook / Google Colab (.ipynb)
# ==============================================================================

import os
import time
import getpass
from google import genai
from IPython.display import Markdown, display

# ------------------------------------------------------------------------------
# 1. SETUP API KEY (Secure input for Jupyter/Colab)
# ------------------------------------------------------------------------------
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API Key is required to run the model.")

client = genai.Client(api_key=API_KEY)

# ------------------------------------------------------------------------------
# 2. CONFIGURATION (MODELS & RETRY SYSTEM)
# ------------------------------------------------------------------------------
MODELS = [
    "gemini-3-flash-preview"
    "gemini-2.5-flash",
    "gemini-2.0-flash",        
    "gemini-1.5-pro"
]

MAX_RETRY = 3
RETRY_DELAY = 10  # seconds

def generate_with_fallback(prompt):
    """Generates AI content with an automatic fallback and retry mechanism."""
    for model in MODELS:
        for attempt in range(MAX_RETRY):
            try:
                print(f"[*] Attempting generation with model: {model} (Attempt {attempt+1}/{MAX_RETRY})...")
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                if response and response.text:
                    print(f"[+] Success using {model}!\n")
                    return response.text
            except Exception as e:
                print(f"[-] Error with {model}: {e}")
                if "429" in str(e) or "quota" in str(e).lower():
                    print(f"[!] Rate limit hit. Waiting for {RETRY_DELAY} seconds before retrying...")
                    time.sleep(RETRY_DELAY)
                else:
                    break # Move to the next model if it's not a quota issue
    raise RuntimeError("All models failed to generate a response. Please check your API key and network.")

# ------------------------------------------------------------------------------
# 3. TASK 1: ARTICLE SUMMARIZATION
# ------------------------------------------------------------------------------
def run_task_1_summarization(file_path):
    display(Markdown("## Task 1: Article Summarization"))
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            article_text = f.read()
    except FileNotFoundError:
        print(f"[!] File '{file_path}' not found. Please ensure the file is uploaded.")
        return

    # PROMPT ENGINEERING: Setting strict constraints (Bullet points, <500 words, Formal English)
    prompt = f"""
    Please summarize the following article based on these strict requirements:
    1. The summary MUST be formatted as bullet points.
    2. The total length MUST NOT exceed 500 words.
    3. The summary MUST be written in English.
    4. You MUST use a highly formal, professional, and academic tone.

    Article Text to Summarize:
    \"\"\"
    {article_text}
    \"\"\"
    """
    
    result = generate_with_fallback(prompt)
    if result:
        display(Markdown(result))

# ------------------------------------------------------------------------------
# 4. TASK 2: CUSTOMER FEEDBACK ANALYSIS
# ------------------------------------------------------------------------------
def run_task_2_feedback_analysis(file_path):
    display(Markdown("## Task 2: Customer Feedback Analysis (Perfume Product)"))
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            feedback_text = f.read()
    except FileNotFoundError:
        print(f"[!] File '{file_path}' not found. Please ensure the file is uploaded.")
        return

    # PROMPT ENGINEERING: Contextualizing the data and forcing a minimum of 55 recommendations
    prompt = f"""
    You are a Senior Data Analyst and Product Strategist. 
    Context: The following data is a collection of customer feedback regarding a newly released perfume product.

    Analyze the feedback and generate a comprehensive report with the following specific sections:
    
    1. Sentiment Analysis: Provide a detailed sentiment analysis (Positive, Negative, Neutral distribution) based on the customer feedback.
    2. Product Strengths & Weaknesses: Summarize the core strengths and critical weaknesses of the perfume.
    3. 55 Actionable Recommendations: You MUST provide a numbered list of AT LEAST 55 distinct, actionable recommendations for product improvement, marketing, packaging, and customer service. Do not stop until you reach 55 points.

    Customer Feedback Data:
    \"\"\"
    {feedback_text}
    \"\"\"
    """
    
    result = generate_with_fallback(prompt)
    if result:
        display(Markdown(result))

# ------------------------------------------------------------------------------
# 5. MAIN EXECUTION BLOCK
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    ARTICLE_FILE_PATH = "Article.txt" 
    FEEDBACK_FILE_PATH = "Customer Feedback.txt"
    
    print("\n" + "="*50)
    print("STARTING AI GENERATIVE PIPELINE")
    print("="*50 + "\n")
    
    run_task_1_summarization(ARTICLE_FILE_PATH)
    
    print("\n" + "-"*50 + "\n")
    
    run_task_2_feedback_analysis(FEEDBACK_FILE_PATH)
    
    print("\n" + "="*50)
    print("PIPELINE EXECUTION COMPLETED")
    print("="*50)
