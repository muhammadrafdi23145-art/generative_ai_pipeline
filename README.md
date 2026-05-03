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

==================================================
STARTING AI GENERATIVE PIPELINE
==================================================

Task 1: Article Summarization
[*] Attempting generation with model: gemini-2.5-flash (Attempt 1/3)...
[+] Success using gemini-2.5-flash!

The Indonesian digital economy, predominantly driven by e-commerce, functions as a primary catalyst for national growth, projected to achieve USD 77 billion in 2022 and nearing USD 130 billion by 2025. Despite this rapid expansion, the sector presents a complex "dual impact," characterized by significant economic growth alongside emerging challenges in equitable distribution and human resource preparedness.

Positive Contributions of E-commerce:

Market Access Enhancement: It significantly benefits Micro, Small, and Medium Enterprises (MSMEs) by eliminating geographical barriers, thereby extending their reach to national and global consumer bases.
Stimulation of Domestic Consumption: The convenience of transactions, intensive promotions, and diverse product offerings directly contribute to increased purchasing power and domestic consumption, vital components of the Gross Domestic Product (GDP).
Novel Employment Generation: The burgeoning e-commerce ecosystem necessitates new professional roles, encompassing logistics couriers, content creators, data analysts, and prompt engineers, which are distinct from traditional commerce.
Operational Cost Optimization: Businesses achieve greater efficiency in marketing and distribution costs by reducing reliance on expensive physical retail locations, enabling a focus on product quality and digital strategies.
Challenges and Exacerbated Disparities:

Infrastructure Disparity: A pronounced imbalance in e-commerce growth exists between urban centers (e.g., Java-Bali) and outer regions, primarily due to uneven internet infrastructure and high logistical expenses, which impede MSME participation in remote areas.
Critical Digital Talent Deficit: Indonesia faces a substantial shortage of approximately 600,000 new digital talents annually. The current supply of graduates possessing requisite hard skills (e.g., data analysis, cybersecurity, prompt engineering) is insufficient to meet demand, thereby hindering innovation.
Regulatory and Security Concerns: The escalating volume of online transactions correlates with an increased prevalence of cybercrime and data privacy issues. This necessitates proactive governmental and regulatory measures to establish a robust legal framework that simultaneously fosters innovation.
Shifting Consumer Behavior: The perpetual availability of online shopping and promotional events (e.g., flash sales) fosters excessive consumptive behaviors, potentially leading to impulsive purchasing and instability in household finances.
Conclusion and Path Forward:

While e-commerce undeniably serves as a pivotal engine for economic growth and a transformative force in business operations, its long-term sustainability and inclusivity are contingent upon the nation's capacity to mitigate the digital divide.
Addressing these challenges requires accelerated infrastructure equalization, a significant investment in bridging the digital talent gap through educational reforms, and comprehensive training initiatives.
Without targeted interventions, the benefits of e-commerce risk being concentrated in already advanced regions, thereby marginalizing less prepared communities.

--------------------------------------------------

Task 2: Customer Feedback Analysis (Perfume Product)
[*] Attempting generation with model: gemini-2.5-flash (Attempt 1/3)...
[+] Success using gemini-2.5-flash!

Comprehensive Report: Aetheria Perfume Customer Feedback Analysis
Date: October 26, 2023 Product: Aetheria Perfume Data Source: 50 customer feedback statements

1. Sentiment Analysis
A detailed analysis of the 50 customer feedback statements reveals a mixed but leaning negative sentiment towards the newly released Aetheria perfume. While there are clear strengths and positive experiences, a significant portion of the feedback highlights areas needing immediate attention.

Positive Sentiment: 18 statements (36%)

Customers praised the unique woody/citrus aroma, its professional and elegant character, soft vanilla notes, and expensive-smelling sandalwood/amber.
Strong longevity and appropriate sillage were noted by some, making it a "signature scent."
The bottle's aesthetic (minimalist, premium, golden liquid) and sturdy cap received high marks.
Value for money was highlighted by those experiencing good longevity.
Positive experiences with delivery speed, safe packaging, and friendly, helpful customer service were also noted.
The brand's cruelty-free aspect and philosophy resonated positively.
Negative Sentiment: 25 statements (50%)

The most prominent negative feedback centered on aroma (too sweet, generic, weak base, strong initial spray, causes headaches, smells cheap, turns sour in tropical climates, not suitable for unisex claim, disappears with sweat).
Inconsistent longevity was a critical issue, with many reporting very poor performance (as short as 2 hours).
Packaging issues included fragile bottles, heavy/impractical design, cheap-looking sticker labels, and faulty atomizers.
Pricing was deemed too high for poor longevity and expensive refills.
Significant operational and customer service complaints included slow claim processes, unresponsiveness, website errors, and frequent stockouts.
Allergic reactions and inconsistency between tester and full bottle scents were serious concerns.
Marketing efforts were criticized for unattractive discounts and lack of free samples.
Neutral Sentiment: 7 statements (14%)

These statements expressed general indifference ("lumayan," "standar"), expressed desire for options (travel size, small size first), or noted discrepancies between hype and reality without strong negative emotion.
Conclusion on Sentiment: The high proportion of negative feedback (50%) indicates that Aetheria is facing significant challenges, particularly around product consistency (aroma, longevity), packaging durability, and overall customer experience (e-commerce, service, stock). While some aspects are highly appreciated, these positive points are overshadowed by critical pain points that affect a large segment of the customer base.

2. Product Strengths & Weaknesses
Core Strengths:

Aroma Diversity & Appeal: Certain scent profiles (unique woody/citrus, professional, elegant, soft vanilla, luxurious sandalwood/amber) are highly praised, fitting for various occasions like office wear, first dates, or even as a comforting bedtime scent. The "cruelty-free" aspect is a strong selling point for an ethical consumer base.
Longevity (Inconsistent but Strong for Some): A subset of users experiences exceptional longevity, praising its staying power throughout the day, indicating the potential for a high-performing product.
Packaging Aesthetics: The bottle design is widely appreciated for its beauty, minimalism, premium feel, sturdy cap, and the appealing golden hue of the liquid. The inclusion of a bonus pouch was also a positive touch.
Customer Service Excellence (Specific Touchpoints): Aspects like fast and secure delivery, friendly admin support (especially for scent recommendations), and easy return processes for damaged goods are noted as stellar experiences.
Brand Identity: The brand's philosophy resonates deeply with some customers, adding to its appeal beyond the scent itself.
Critical Weaknesses:

Inconsistent Product Performance: This is the most glaring weakness, manifesting in:
Longevity: Wildly varying reports from "gila" (amazing) to "cuma 2 jam" (only 2 hours). This inconsistency is a major detractor from perceived value and reliability.
Aroma Profile: Contradictory feedback on sweetness, uniqueness, sillage, and suitability for various climates/occasions (too sweet for hot weather, turns sour in tropics, generic, weak base, too strong initial spray, causes headaches, smells cheap, inconsistent between tester and full bottle, not truly unisex).
Safety: The serious issue of allergic reactions for some users.
Packaging Durability & Practicality: The bottle, while aesthetically pleasing, is criticized for being too heavy/large for portability, easily breakable, and having a cheap-looking sticker label. Atomizer malfunctions are also reported.
Value Perception: High price for poor longevity, and expensive refills, lead to customers feeling it's not "worth the price."
Operational & E-commerce Issues: Frequent stockouts, slow customer service responses for claims, and website errors during checkout significantly detract from the overall customer experience and brand reliability.
Marketing Effectiveness: Discounts are considered unattractive, and the absence of free samples, even for large purchases, leads to disappointment. Some feel the product doesn't live up to influencer hype.
3. 55 Actionable Recommendations
Here are 55 distinct, actionable recommendations for product improvement, marketing, packaging, and customer service:

Product Improvement - Aroma & Performance:

Formulation Review: Conduct an immediate, in-depth audit of the perfume's formulation to identify and rectify causes of inconsistent longevity across batches and skin types.
Scent Consistency QC: Implement stringent quality control protocols to ensure absolute consistency in aroma profile between tester bottles and full-sized retail products.
Climate-Specific Testing: Research and test the perfume's performance in various climates, especially tropical and humid conditions, to understand and mitigate issues like the scent turning "sour."
Aroma Rebalancing (Sweetness): Develop a variant or adjust the current formulation to reduce excessive sweetness, making it more appealing for those sensitive to sweet notes, especially in warm weather.
Base Note Enhancement: Strengthen and refine the base notes (e.g., patchouli, musk) to provide a more memorable, long-lasting, and distinctive dry-down.
Unisex Profile Adjustment: Re-evaluate the "unisex" claim by enhancing musk or woody notes and reducing overwhelming floral elements to cater to a broader audience.
Sillage Optimization: Aim for consistent, moderate sillage that is noticeable without being overpowering, addressing feedback of both too weak and too strong projection.
Allergen Transparency & Alternatives: Clearly list all ingredients and potential allergens. Explore developing a hypoallergenic version or offering a patch test kit.
Initial Spray Softening: Adjust the atomization or concentration to prevent an overly "piercing" initial scent, ensuring a smoother opening.
Headache Inducer Identification: Work with fragrance experts to identify and reformulate any components that may be causing headaches for sensitive individuals.
Sweat Resistance Study: Investigate and integrate ingredients that can improve the perfume's longevity and scent integrity when exposed to sweat or active lifestyles.
Formal Occasion Variant: Develop a new, more intense or complex variant specifically designed to be "wow-factor" worthy for formal events.
Product Improvement - Options & Safety:

Travel Size Introduction: Launch a travel-sized (e.g., 10ml/15ml) version for portability and as an affordable trial option.
Refill Pricing Strategy: Re-evaluate and reduce the price of refills to offer a clear cost advantage, incentivizing eco-conscious and loyal customers.
Cruelty-Free Certification Promotion: Prominently feature "cruelty-free" certifications and ethics in all product descriptions and marketing materials.
Packaging Improvements:

Engraved Labeling: Replace the sticker label with engraved or direct-print labeling on the bottle for a significantly more premium and durable finish.
Bottle Durability Enhancement: Explore alternative, more durable glass materials or protective coatings to prevent easy breakage.
Atomizer Quality Check: Implement rigorous quality checks for atomizers from suppliers, ensuring consistent, fine, and non-jamming sprays.
Weight & Size Optimization: While maintaining aesthetic appeal, explore ways to reduce bottle weight and size without compromising the premium feel, addressing portability concerns.
Outer Packaging Upgrade: Offer an optional premium outer box for gifting or special editions, allowing for a more luxurious unboxing experience.
Emphasize Existing Strengths: Actively promote the minimalist design, sturdy cap, and beautiful golden liquid color in product visuals and descriptions.
Marketing & Sales Strategies:

Targeted Scent Descriptions: Provide highly detailed scent profiles including suitability for climates, occasions (e.g., "best for cooler evenings," "daytime professional"), and skin types.
Scent Discovery Kits: Create mini-sample kits for purchase, allowing customers to explore multiple scents before committing to a full bottle.
Bundling & Tiered Discounts: Introduce attractive bundle deals (e.g., full size + travel size, perfume + complementary product) and tiered discounts for repeat customers.
Free Sample Program: Implement a consistent free sample program, especially for larger orders or first-time buyers, to encourage trials and positive sentiment.
Diverse Influencer Outreach: Collaborate with a broader range of influencers with varying styles and demographics to provide authentic reviews and manage "hype" expectations.
Testimonial-Driven Campaigns: Feature compelling customer testimonials and "signature scent" stories prominently in marketing.
Value Communication: Clearly articulate the value proposition, linking the price to unique aroma, premium ingredients, and strong longevity (when consistent).
Engagement Quizzes: Develop an interactive online quiz to help customers find their ideal perfume based on their preferences, lifestyle, and personality.
Brand Storytelling: Create engaging content (blogs, videos) detailing the brand's philosophy, inspiration, and commitment to quality.
Loyalty Program: Launch a customer loyalty program with exclusive benefits like early access to new products, birthday discounts, and special offers.
Community Building: Foster an online community where fragrance enthusiasts can share experiences and recommendations.
Refill Program Promotion: Actively market the refill options as an eco-friendly and cost-effective choice.
Seasonal Campaigns: Develop campaigns for specific seasons or holidays, recommending scents suitable for those times.
Cross-Promotional Partnerships: Collaborate with complementary luxury brands (e.g., fashion, skincare) for joint marketing efforts.
Visual Merchandising Guidance: If selling in physical stores, provide guidelines for displaying the beautiful bottle design effectively.
Podcast/Audio Content: Explore creating podcast episodes discussing fragrance notes, history, and usage tips.
User-Generated Content Campaigns: Encourage customers to share their Aetheria moments on social media using a specific hashtag.
Scent "Layering" Guides: Offer advice on how to layer Aetheria with other scents or body products for a personalized experience.
Subscription Box Partnerships: Consider partnerships with luxury beauty subscription boxes to reach a wider audience for trial.
Customer Service & Operations:

Streamlined Claim Process: Overhaul the claims process for damaged goods to ensure rapid response times, clear communication, and swift resolution.
Enhanced CS Responsiveness: Increase customer service staffing and training to significantly reduce email response times and improve overall communication quality.
Website UX Audit: Conduct regular, thorough audits of the e-commerce website to proactively identify and fix checkout errors and other technical glitches.
Robust Inventory Management: Implement an advanced inventory management system to minimize "out of stock" occurrences and provide real-time stock information.
Proactive Stock Communication: Develop a clear communication strategy for anticipated stockouts and replenishment dates, informing customers well in advance.
Personalized Scent Consultation: Train customer service agents to offer expert, personalized scent recommendations based on customer preferences and feedback.
Shipping Carrier Review: Periodically review and optimize partnerships with shipping carriers to ensure consistent, fast, and safe delivery.
Comprehensive FAQ Section: Create an exhaustive FAQ section on the website covering common queries about longevity, ingredients, usage, and returns.
Feedback Loop System: Establish a direct and documented feedback loop from customer service to product development and marketing teams for continuous improvement.
Allergy Protocol: Develop a clear protocol for handling allergy reports, including immediate follow-up and potential product recall if a pattern emerges.
Post-Purchase Follow-up: Implement a system for follow-up emails after purchase, asking for feedback and offering assistance.
Live Chat Support: Introduce a live chat feature on the website for immediate customer support and quicker query resolution.
Returns/Exchange Policy Review: Ensure the returns and exchange policy is customer-friendly and clearly communicated.
CS Training on Product Knowledge: Provide comprehensive training to CS teams on all product details, including scent notes, longevity expectations, and best use cases.
Emergency Contact for Serious Issues: Establish a dedicated, high-priority channel for urgent customer issues, such as severe allergic reactions or major product defects.
