# Overview Of The Project
The Stock News Notifier is a Python script that provides users with a daily summary of a specified stock's performance along with relevant news headlines. The script uses the Alpha Vantage API to fetch daily stock data and the News API to retrieve news articles related to the specified company. It then sends an SMS notification using the Twilio API to a specified recipient, containing information about the stock's percentage change and a randomly selected news headline.

# Stock Performance:
The script leverages the Alpha Vantage API to retrieve daily stock data, specifically focusing on the closing prices of the stock for the current day and the day before. It calculates the percentage change in the stock price by comparing these two values. An emoji indicator, either 🔺 (upward arrow) or 🔻 (downward arrow), is added to visually represent whether the stock increased or decreased in value.

# Dynamic News Headlines: 
To keep the information engaging and varied, the script utilizes the News API to fetch news articles related to the specified company (in this case, Tesla Inc). It randomly selects one of the available news headlines to include in the SMS notification. This dynamic approach ensures that each time the script runs, users receive a different news headline, providing a broader perspective on the company's current events.

# SMS Notification: 
Upon gathering stock and news information, the script utilizes the Twilio API to send an SMS notification to a specified recipient. The SMS contains a concise summary of the stock's performance, including the percentage change and the dynamically chosen news headline. This feature allows users to receive timely updates on both the financial and news aspects of the specified stock.

# Error Handling: 
The script incorporates robust error handling mechanisms to gracefully handle exceptions that may occur during execution. It provides informative error messages, making it easier for users to troubleshoot issues. Whether it's a network problem, API key mismatch, or any other unexpected situation, the script aims to provide clear feedback on the problem encountered.

# Example Output:
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.

or

TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus...
