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
* **Generative AI:** Google Gemini API (`gemini-2.0-flash`)
* **Environment:** Jupyter Notebook / Google Colab
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
--- Task 1: Article Summarization ---

    Economic Dominance: E-commerce serves as the primary engine for Indonesia's digital economy, with its valuation projected to reach approximately USD 130 billion by 2025.
    Market Inclusivity for MSMEs: Digital platforms eliminate geographical barriers, allowing Micro, Small, and Medium Enterprises (MSMEs) in remote areas to access national and international markets.
    Stimulation of Domestic Consumption: Enhanced accessibility and intensive digital promotions drive domestic demand, contributing significantly to the national Gross Domestic Product (GDP).
    Job Creation and Efficiency: The sector fosters modern employment opportunities—such as data analysts, content creators, and logistics personnel—while reducing operational costs by eliminating the need for physical storefronts.
    Infrastructure Disparities: A significant digital divide persists between urbanized regions (Java-Bali) and outer islands, hindered by uneven internet access and high logistics expenses.
    Digital Talent Deficit: Indonesia faces a critical shortage of specialized technical labor, requiring approximately 600,000 new digital talents annually to sustain innovation.
    Regulatory and Security Concerns: The surge in online transactions increases vulnerability to cybercrime, necessitating robust legal frameworks for consumer data protection.
    Consumer Behavior Risks: Constant accessibility and aggressive sales tactics may encourage impulsive purchasing habits, potentially impacting household financial stability.
    Strategic Imperative: To ensure inclusive growth, the government must prioritize infrastructure equity and educational reform to bridge the digital gap and prevent economic polarization.

--- Task 2: Customer Feedback Analysis ---

    1. Sentiment Analysis & Reasoning
    Overall Sentiment Distribution:
    Positive (42%): Customers praise the premium scent profiles (woody, amber, vanilla), aesthetic bottle design, and excellent customer service interactions.
    Neutral (28%): These customers find the product "okay" but lack a "wow" factor, or they offer constructive criticism regarding specific notes and gender-leaning scents.
    Negative (30%): Driven primarily by inconsistent longevity, packaging durability (fragile glass/faulty atomizers), and technical issues (website/CS response times).
    Reasoning: The brand sits in a "Polarized Premium" position. While the brand identity and olfactory compositions are perceived as high-end, the functional execution (product durability and performance consistency) fails to meet the expectations set by the price point and branding.
    2. Key Strengths
    Premium Olfactory Composition: High appreciation for specific notes like Sandalwood, Amber, and "luxury" Woody-Citrus blends that don't smell "generic."
    Visual Branding: The bottle design, golden liquid color, and brand philosophy (cruelty-free) resonate strongly with the target market.
    Effective CRM (Pre-Sales): The "Admin" is highly praised for being helpful and acting as a fragrance consultant, which builds initial trust.
    Niche Appeal: Success in specific use cases, such as "office/professional" wear and "first dates."
    3. Key Weaknesses
    Performance Inconsistency: Significant "Longevity Gap." Some report all-day wear, while others report it vanishing after 2 hours. This suggests batch inconsistency or formula stability issues.
    Packaging Ergonomics & Quality: Bottles are reported as too heavy/bulky for travel, atomizers are prone to jamming, and labels (stickers) cheapen the premium feel.
    Climate & Chemistry Sensitivity: The fragrance does not perform well in tropical heat or with sweat, sometimes turning "sour" or causing skin irritation/headaches for sensitive users.
    Logistics & Technical Friction: Website errors during checkout and slow response times for "post-purchase" issues (claims/returns) contrast sharply with the friendly pre-sales experience.
    4. 10 Actionable Recommendations
    - Standardize Quality Control (QC): Investigate the 2-hour longevity complaints versus the 8-hour praises. This indicates a potential issue with maceration time or ingredient concentration consistency between batches.
    - Launch a Travel Size (10ml): Address the "bulky/heavy bottle" complaints by offering a portable travel spray. This also serves as a lower-entry price point for new customers (addressing feedback #34 and #42).
    - Upgrade Labeling Technology: Replace stickers with screen printing or laser etching directly on the glass. For a premium-priced perfume, stickers are a significant "brand killer" (feedback #21).
    - Reformulate for Tropical Stability: Work with perfumers to ensure the "base notes" (dry down) remain stable in high humidity/sweat to prevent the "sour" smell reported in feedback #35 and #49.
    - Refine the "Opening" Notes: Soften the initial spray impact. Several users reported "headaches" or "piercing" scents initially; a smoother transition from top to heart notes is needed.
    - Fix Website UX/UI: Immediately resolve the checkout errors. Technical friction at the point of purchase is a direct cause of lost revenue (feedback #44).
    - Introduce a Discovery Set: Since customers are hesitant about the price vs. longevity, sell a "Discovery Kit" with 2ml samples. This reduces the risk for the customer and increases the conversion rate for full bottles.
    - Improve After-Sales Support: Align the "Claims/Returns" response speed with the "Pre-sales" admin speed. A slow response to broken items destroys brand loyalty (feedback #28).
    - Develop a "Refill" Strategy: Since customers complained about refill prices, introduce a "Bottle Return Program" or more competitively priced eco-refills to encourage repeat purchases.
    - Inclusion of Samples: Implement a policy to include 1-2 free samples of other scents with every full-bottle purchase to encourage cross-selling and mitigate the "no samples" disappointment (feedback #29).

