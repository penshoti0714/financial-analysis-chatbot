
# Financial Chatbot - Test Results

## Test Environment

- Language: Python 3
- Libraries: pandas
- Interface: Command-line
- Dataset: k10forge.csv

## Functional Tests

| Test | Query | Company | Year | Expected Result |
|---|---|---|---|---|
| 1 | Total Revenue | Microsoft | 2025 | 281724 million USD |
| 2 | Net Income | Apple | 2025 | 112010 million USD |
| 3 | Revenue Growth | Tesla | 2024 | 0.95% |
| 4 | Net Profit Margin | Apple | 2025 | 26.92% |

## Error Handling Tests

| Test | Input | Expected Behavior |
|---|---|---|
| 5 | Google, 2025 | Display no data found |
| 6 | Tesla, 2023 (Revenue Growth) | Display data unavailable |
| 7 | Invalid year: hello | Request a valid numeric year |
| 8 | Unsupported question: hello | Display unsupported query message |


## Test Status

All 8 test cases passed.

- Functional tests: 4/4 PASS
- Error handling tests: 4/4 PASS
- No unexpected exceptions occurred during testing.

## Conclusion

The chatbot successfully responds to four predefined financial queries using historical financial data.

It also handles unsupported questions, invalid year inputs, and unavailable financial records without crashing.

The prototype meets its intended functionality as a simple rule-based financial chatbot.
