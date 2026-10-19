import pandas as pd

df = pd.read_csv("k10forge.csv")

def get_financial_data(company, year):
    selected_data = df[
        (df["company"] == company) &
        (df["year"] == year)
    ]
    return selected_data

def get_year():
    while True:
        try:
            year = int(input("Which year? "))
            return year
        except ValueError:
            print("Invalid input. Please enter a numeric year.")

print("Welcome to the Financial Chatbot!")

user_query = input("What would you like to know? ")

if user_query == "What is the total revenue?":
    company = input("Which company? ").lower()
    year = get_year()
    selected_data = get_financial_data(company, year)
    if selected_data.empty:
        print("Sorry, no data found for this company and year.")
    else:
        revenue = selected_data["total revenue"].iloc[0]
        print("The total revenue of", company, "in", year, "was", revenue, "million USD.")
    


    

elif user_query == "What is the net income?":
    company = input("Which company? ").lower()
    year = get_year()

    selected_data = get_financial_data(company, year)
    if selected_data.empty:
        print("Sorry, no data found for this company and year.")
    else:
        net_income = selected_data["net income"].iloc[0]
        print("The net income of", company, "in", year, "was", net_income, "million USD.")

elif user_query == "How has revenue changed over the last year?":
    company = input("Which company? ").lower()
    year = get_year()

    current_data = get_financial_data(company, year)
    previous_data = get_financial_data(company, year - 1)   
    
    if current_data.empty or previous_data.empty:
        print("Sorry, revenue data is unavailable for these years.")
    else:
        current_revenue = current_data["total revenue"].iloc[0]
        previous_revenue = previous_data["total revenue"].iloc[0]

        if previous_revenue == 0:
            print("Cannot calculate growth because previous revenue is zero.")
        else:
            growth_rate = (current_revenue - previous_revenue) / previous_revenue * 100
            print("The revenue growth rate of", company, "in", year, "was", round(growth_rate, 2), "%")
    

elif user_query == "What is the net profit margin?":
    company = input("Which company? ").lower()
    year = get_year()

    selected_data = get_financial_data(company, year)

    if selected_data.empty:
        print("Sorry, no data found for this company and year.")
    else:
        revenue = selected_data["total revenue"].iloc[0]
        net_income = selected_data["net income"].iloc[0]

        if revenue == 0:
            print("Cannot calculate profit margin because revenue is zero.")
        else:
            profit_margin = net_income / revenue * 100
            print("The net profit margin of", company, "in", year, "was", round(profit_margin, 2), "%")

else:
    print("Sorry, I can only answer predefined financial questions.")
