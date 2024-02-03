## Stock_News_Notifier
# Overview
The Stock News Notifier is a Python script that provides users with a daily summary of a specified stock's performance along with relevant news headlines. The script uses the Alpha Vantage API to fetch daily stock data and the News API to retrieve news articles related to the specified company. It then sends an SMS notification using the Twilio API to a specified recipient, containing information about the stock's percentage change and a randomly selected news headline.

# Features
Stock Performance Overview: The script calculates the percentage change in the stock price from the previous day and includes an emoji indicator (🔺 or 🔻) based on whether the stock increased or decreased.

# Dynamic News Headlines: 
The script fetches news articles related to the specified company and randomly selects one to include in the SMS notification. This ensures a fresh and varied news headline with each execution.

# SMS Notification: 
The script uses Twilio to send an SMS notification to a specified recipient with the calculated stock performance and selected news headline.

# Error Handling: 
The script includes error handling to gracefully manage exceptions, providing informative messages in case of issues.
