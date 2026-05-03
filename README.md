# Generative AI: Text Analysis & Prompt Engineering

**Large Language Models (LLMs) | Prompt Engineering | Sentiment Analysis**

## Project Overview
This project demonstrates the practical application of **Generative AI** in solving real-world business problems. By leveraging the **Google Gemini API**, I built an automated pipeline capable of digesting large amounts of unstructured text to generate structured, actionable business intelligence.

## Key Tasks Performed
1. **Automated Article Summarization:**
   - **Goal:** Summarize lengthy economic articles regarding Indonesia's e-commerce landscape.
   - **Technique:** Utilized constraint-based prompting to enforce formal English, bullet-point formatting, and strict word count limits.
   
2. **Customer Feedback & Sentiment Analysis:**
   - **Goal:** Analyze mixed customer reviews for a newly launched perfume product ("Aetheria").
   - **Technique:** Implemented role-playing prompts (acting as a Data Analyst) to extract sentiment justifications, product strengths/weaknesses, and generate over 55 highly specific, actionable business recommendations.

## Tech Stack
* **Language:** Python
* **Generative AI:** Google Gemini API (`gemini-3-flash-preview`, `gemini-2.5-flash`, `gemini-2.0-flash`, `gemini-1.5-pro`)
* **Environment:** Visual Studio Code, Jupyter Notebook / Google Colab
* **Techniques:** Prompt Engineering, Constraint Modeling, Role-prompting.

## How to Run
1. Clone this repository.
2. Install the required Google GenAI SDK:
   ```bash
   pip install -r requirements.txt
3. Set your Gemini API key as an environment variable:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
5. Run the script:
   ```bash
   python generative_ai_pipeline.py

## Repository Structure
`generative_ai_pipeline.py`: Main python script containing the AI logic.
`Artikel-1.txt`: Raw text data for the summarization task.
`Artikel-2.txt`: Raw customer feedback data for the sentiment analysis task.
`requirements.txt`: Project dependencies.

## Result
1. Result on Task 1: Article Summarization

2. Result on Task 2: Customer Feedback
