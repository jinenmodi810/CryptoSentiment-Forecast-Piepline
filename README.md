#  Crypto Sentiment & Forecast Pipeline

**Author:** Jinen Modi (A20549644)  
**Project:** CS554 Final Project – IIT

---

## Project Overview

This project integrates **sentiment analysis** and **time-series forecasting** to predict cryptocurrency market trends, with a focus on Bitcoin (BTC). It gathers real-time sentiment from multiple news sources and combines it with historical price data to generate actionable trading signals (BUY/HOLD) through a fully automated pipeline and dashboard.

---

## Problem Statement

Traditional crypto forecasting models focus mainly on historical prices and technical indicators, ignoring **real-time sentiment.** This gap limits the ability to respond to sudden market-moving news events. The goal here is to build a system that blends **natural language sentiment analysis** with **price forecasting models** to enhance prediction accuracy and responsiveness.

---

##  Features

- **Multi-source News Scraping:**  
  - Reddit (Pushshift API)  
  - CoinTelegraph (web scraping)  
  - CryptoSlate (API)

- **Sentiment Analysis:**  
  - VADER sentiment scoring  
  - Aggregated daily metrics: news count, % positive, % negative, avg. compound

- **Forecasting Models:**  
  - SARIMA: Seasonal ARIMA as statistical baseline  
  - LSTM: Deep learning model using price + sentiment

- **Evaluation Metrics:**  
  - RMSE, MAPE, Directional Accuracy

- **Live Dashboard:**  
  - Streamlit app for real-time visualization of sentiment trends, forecasts, and trading signals

---

## Key Results

| Model  | RMSE (USD) | MAPE (%) | Directional Accuracy (%) |
|--------|------------|----------|--------------------------|
| SARIMA | 1250.37    | 1.50     | 57                       |
| LSTM   | 5528.98    | 10.46    | 86                       |

 **Conclusion:** Sentiment-based LSTM significantly improves trend prediction despite higher RMSE, making it better suited for real-world trading.


<img width="1512" alt="Screenshot 2025-05-05 at 10 39 25 PM" src="https://github.com/user-attachments/assets/870f14cc-784f-461e-ab50-c4f429eff6a8" />
<img width="1123" alt="image" src="https://github.com/user-attachments/assets/c88f8dca-f8f7-4296-adf6-e3fb64c022d0" />
<img width="1065" alt="image" src="https://github.com/user-attachments/assets/d4936a3a-896b-4086-89e4-51135c3e9199" />
<img width="1109" alt="image" src="https://github.com/user-attachments/assets/d8fcdb34-2e55-493f-8963-e0b34378dd7f" />
<img width="1142" alt="image" src="https://github.com/user-attachments/assets/9f203336-2c89-48a9-9dde-ef861933de11" />
<img width="1111" alt="image" src="https://github.com/user-attachments/assets/ef97c5ff-13f6-4f17-8783-3832733a1b7e" />
<img width="1136" alt="image" src="https://github.com/user-attachments/assets/3755a595-39b7-42bf-998f-666a45e82779" />




---

## How to Run

** Clone the Repository:**

```bash
git clone https://github.com/YOUR_USERNAME/crypto-sentiment-forecast.git
cd crypto-sentiment-forecast
streamlit run Frontend.py

