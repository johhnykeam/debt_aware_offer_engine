# Debt-Aware Financial Recommendation Engine

## Overview

The **Debt-Aware Financial Recommendation Engine** is a machine learning–driven system that generates responsible credit and offer recommendations based on user repayment behavior, debt exposure, and risk signals.

The project is inspired by mobile lending and overdraft products such as **Fuliza** and **Okoa Jahazi**, where the challenge is balancing:

* User access to short-term credit
* Revenue and retention for the lender
* Default risk and over-indebtedness

This project demonstrates how data-driven decision systems can be designed to promote **financial inclusion while managing risk**.

---

## Problem Statement

Traditional digital lending systems often rely on simple heuristics or rigid rules, which can:

* Overextend high-risk users
* Penalize recovering users
* Fail to adapt to changing repayment behavior

This project explores how **machine learning and behavioral features** can be used to:

* Estimate repayment likelihood
* Adjust credit recommendations dynamically
* Encourage sustainable borrowing behavior

---

## Approach

The system models each user using historical and behavioral features, including:

* Repayment history
* Debt-to-income proxies
* Usage frequency
* Previous defaults or late payments

Using these signals, the engine:

1. Estimates repayment risk
2. Scores users by financial behavior
3. Generates personalized offer recommendations
4. Applies risk-aware constraints to avoid overexposure

The focus is not only prediction accuracy, but **decision quality under risk**.

---

## Data

This project uses **synthetic user data** generated to simulate real-world mobile lending behavior.

The dataset includes:

* User demographic proxies
* Transaction and repayment patterns
* Debt levels and limits
* Outcome labels (repayment / default)

Synthetic data is used to:

* Avoid privacy issues
* Enable controlled experimentation
* Simulate edge cases common in fintech systems

---

## Modeling

While model complexity is intentionally kept interpretable, the pipeline includes:

* Feature engineering on repayment behavior
* Risk scoring using statistical and ML-based methods
* Rule-based constraints layered on model outputs

The emphasis is on **explainability and deployability**, rather than black-box optimization.

---

## Example Output

For a given user, the engine can recommend:

* Whether to offer credit
* An adjusted credit limit
* Risk flags or cooldown periods

Example decision:

* User Risk Score: Moderate
* Recommended Limit: Reduced
* Action: Offer with safeguards

---

## Project Structure

```
├── data_generator.py       # Synthetic data creation
├── synthetic_users.csv     # Generated dataset
├── src/                    # Core logic (planned refactor)
├── notebooks/              # Exploratory analysis (planned)
├── README.md
```

---

## How to Run

```bash
git clone https://github.com/johnnykeam/debt_aware_offer_engine.git
cd debt_aware_offer_engine
python data_generator.py
```

---

## Limitations

* Uses synthetic data rather than live production data
* Simplified behavioral assumptions
* No real-time deployment layer yet

---

## Future Improvements

* Integrate real transaction streams (Kafka / streaming)
* Train calibrated probabilistic risk models
* Add fairness and bias evaluation
* Expose recommendations via a FastAPI service
* Add dashboards for monitoring portfolio risk

---

## Why This Project Matters

This project reflects real challenges faced in **fintech and digital credit systems**, especially in emerging markets.

It demonstrates:

* Applied statistics in decision-making
* Responsible AI thinking
* Practical ML system design beyond toy problems

---

## Author

**John Kimani**
Machine Learning Engineer | Big Data Analyst
LinkedIn: [https://www.linkedin.com/in/n-john-kimani-283a81274](https://www.linkedin.com/in/n-john-kimani-283a81274)
