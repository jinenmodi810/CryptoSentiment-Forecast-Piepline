#  Crypto Sentiment & Forecast Pipeline

**Author:** Jinen Modi (A20549644)  
**Project:** CS554 Final Project – IIT

---

## 📄 Project Overview

This project integrates **sentiment analysis** and **time-series forecasting** to predict cryptocurrency market trends, with a focus on Bitcoin (BTC). It gathers real-time sentiment from multiple news sources and combines it with historical price data to generate actionable trading signals (BUY/HOLD) through a fully automated pipeline and dashboard.

---

## 🔍 Problem Statement

Traditional crypto forecasting models focus mainly on historical prices and technical indicators, ignoring **real-time sentiment.** This gap limits the ability to respond to sudden market-moving news events. The goal here is to build a system that blends **natural language sentiment analysis** with **price forecasting models** to enhance prediction accuracy and responsiveness.

---

## 🛠️ Features

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

## 📈 Key Results

| Model  | RMSE (USD) | MAPE (%) | Directional Accuracy (%) |
|--------|------------|----------|--------------------------|
| SARIMA | 1250.37    | 1.50     | 57                       |
| LSTM   | 5528.98    | 10.46    | 86                       |

✅ **Conclusion:** Sentiment-based LSTM significantly improves trend prediction despite higher RMSE, making it better suited for real-world trading.

---

## 🚀 How to Run

1️⃣ **Clone the Repository:**

```bash
git clone https://github.com/YOUR_USERNAME/crypto-sentiment-forecast.git
cd crypto-sentiment-forecast
