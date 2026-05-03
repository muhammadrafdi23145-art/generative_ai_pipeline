# ==================================================
# Generative AI: Automated Text Analysis & Summarization
# ==================================================

import os
from google import genai
from IPython.display import Markdown, display

# 1. Initialize API Client
# PRO TIP: Set your API key in your environment variables instead of hardcoding it.
# Example: export GEMINI_API_KEY="your_api_key_here"
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API Key not found. Please set the GEMINI_API_KEY environment variable.")

client = genai.Client(api_key=api_key)

def summarize_article(file_path):
    """Reads an article and summarizes it using Generative AI."""
    print("\n--- Task 1: Article Summarization ---")
    
    with open(file_path, "r", encoding="utf-8") as f:
        article_text = f.read()

    prompt = f"""
    Summarize the following article into clear and concise bullet points.
    Requirements:
    - Write in formal English.
    - Use bullet point format.
    - Keep the summary under 500 words.
    Article:
    {article_text}
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    print("Summarization Complete! Here is the result:\n")
    print(response.text)
    return response.text

def analyze_customer_feedback(file_path):
    """Reads customer feedback and acts as a data analyst to extract insights."""
    print("\n--- Task 2: Customer Feedback Analysis ---")
    
    with open(file_path, "r", encoding="utf-8") as f:
        feedback = f.read()

    prompt_feedback = f"""
    You are a professional data analyst specializing in customer feedback interpretation.

    Analyze the following customer feedback about a newly released perfume product and provide the following:
    1. Perform a sentiment analysis (positive, negative, or neutral) with a brief justification.
    2. Summarize the key strengths and weaknesses of the product based on customer opinions.
    3. Provide at least 55 actionable recommendations to improve the product and customer satisfaction.

    Customer Feedback Data:
    {feedback}
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt_feedback
    )
    
    print("Analysis Complete! Here is the detailed report:\n")
    print(response.text)
    return response.text

if __name__ == "__main__":
    # Define file paths (Ensure these files exist in your directory)
    article_path = "Artikel.txt"
    feedback_path = "no2.txt"
    
    # Execute AI Pipelines
    try:
        summary_result = summarize_article(article_path)
        analysis_result = analyze_customer_feedback(feedback_path)
        
        # Note: If running in Jupyter Notebook/Colab, you can use display(Markdown(result))
        
    except FileNotFoundError as e:
        print(f"Error: {e}. Please make sure the text files are in the correct directory.")
