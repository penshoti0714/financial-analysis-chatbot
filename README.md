
# Financial Chatbot Prototype

## Project Overview

This project is a rule-based financial chatbot developed as part of the BCG X GenAI Job Simulation on Forage.

The chatbot uses Python and pandas to retrieve and analyze financial data for Microsoft, Tesla, and Apple from 2023 to 2025.

It responds to predefined financial questions through a command-line interface.

## Features

The chatbot supports four types of financial queries:

1. Total Revenue
2. Net Income
3. Year-over-Year Revenue Growth
4. Net Profit Margin

Users can select a company and year to retrieve the corresponding financial information.

The chatbot also includes basic input validation and error handling for unavailable data.

## Installation & Usage

### Requirements

- Python 3
- pandas
- Financial dataset (`k10forge.csv`)

### How to Run

1. Place `chatbot.py` and `k10forge.csv` in the same folder.
2. Open a terminal in that folder.
3. Install pandas if it is not already installed:

   ```bash
   python -m pip install pandas
   ```

4. Run the chatbot:

   ```bash
   python chatbot.py
   ```

5. Enter one of the supported financial questions.
6. Provide the company name and year when prompted.

### Example Interaction

```text
Welcome to the Financial Chatbot!
What would you like to know? What is the total revenue?
Which company? Microsoft
Which year? 2025
The total revenue of microsoft in 2025 was 281724 million USD.
```

## Limitations

- The chatbot is rule-based and does not use a large language model (LLM) or natural language processing (NLP).
- It only recognizes four predefined questions with exact wording.
- Financial data is limited to Microsoft, Tesla, and Apple from 2023 to 2025.
- Year-over-year revenue growth can only be calculated for 2024 and 2025 because 2022 data is unavailable.
- The chatbot relies on a local CSV file and does not retrieve real-time financial information.
- The chatbot handles invalid year formats and missing financial records, but it does not support complex financial analysis or follow-up conversations.

## Data Sources

The financial dataset was independently compiled from publicly available financial reports published by Microsoft, Apple, and Tesla.

The dataset covers fiscal years 2023–2025 and includes financial metrics such as total revenue, net income, total assets, total liabilities, and operating cash flow.

The data was organized into a CSV file for analysis using Python and pandas.

**Note:** This project was developed for educational purposes as part of the BCG X GenAI Job Simulation on Forage. It is not affiliated with or endorsed by Microsoft, Apple, Tesla, or BCG X.