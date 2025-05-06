# dashboard.py

import streamlit as st
from pathlib import Path
import pandas as pd
import altair as alt
from PIL import Image

# ─── PAGE CONFIG (must be first) ───────────────────────────────────────────────
st.set_page_config(
    page_title="📈 Crypto Sentiment & Forecast Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CUSTOM ALT AIR THEME ───────────────────────────────────────────────────────
def crypto_theme():
    return {
        "config": {
            "view": {"continuousWidth": 600, "continuousHeight": 300},
            "background": "#0E1117",
            "title": {"fontSize": 28, "font": "Helvetica", "color": "#FFFFFF"},
            "axis": {
                "labelColor": "#DDDDDD", "titleColor": "#FFFFFF",
                "gridColor": "#333333"
            },
            "legend": {
                "labelColor": "#FFFFFF", "titleColor": "#FFFFFF",
                "orient": "bottom", "direction": "horizontal"
            }
        },
        "mark": {"tooltip": {"fontSize": 14}}
    }

alt.themes.register("crypto_theme", crypto_theme)
alt.themes.enable("crypto_theme")

# ─── AUTO-DETECT “News Data Crypto” ─────────────────────────────────────────────
root = (
    Path.home()
    / "ImpData"
    / "Crypto Sentiment Prediction"
    / "crypto_sentiment_project"
    / "data"
)
candidates = [d for d in root.iterdir() if d.is_dir() and d.name.startswith("News Data Crypto")]
if not candidates:
    st.error(f"❌ Couldn’t find a 'News Data Crypto' folder under {root}")
    st.stop()
BASE = candidates[0]

# ─── DEFINE PATHS ───────────────────────────────────────────────────────────────
PATHS = {
    "merged_daily":    BASE / "merged_daily.csv",
    "live_signals":    BASE / "live_recommendations.csv",
    "walk_summary":    BASE / "walk_forward_summary.csv",
    "backtest_folder": BASE / "backtests",
}

# ─── FILE CHECKS ────────────────────────────────────────────────────────────────
st.sidebar.title("🔧 File Checks")
for name, p in PATHS.items():
    st.sidebar.write(f"{name}: `{p.name}` → {'✅' if p.exists() else '❌'}")

# ─── LOAD DATA ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    merged = pd.read_csv(PATHS["merged_daily"], parse_dates=["date"])  
    live   = pd.read_csv(PATHS["live_signals"], index_col="crypto_name") if PATHS["live_signals"].exists() else pd.DataFrame()
    perf   = pd.read_csv(PATHS["walk_summary"], index_col=0)       if PATHS["walk_summary"].exists() else pd.DataFrame()
    coins  = merged.crypto_name.unique().tolist()
    return merged, live, perf, coins

try:
    merged, live_signals, perf_summary, coins = load_data()
except FileNotFoundError as e:
    st.error(f"❌ Required data missing: {e}")
    st.stop()

# ─── NAVIGATION ─────────────────────────────────────────────────────────────────
st.sidebar.title("🔎 Navigation")
section = st.sidebar.radio("", [
    "Overview",
    "Sentiment Features",
    "Forecast Comparison",
    "Backtest Results",
    "Performance Metrics",
    "Live Signals",
    "Raw Data"
])

# ─── COMMON CONTROLS ────────────────────────────────────────────────────────────
if section != "Overview":
    coin = st.sidebar.selectbox("Select Coin", coins)
    date_min, date_max = merged.date.min().date(), merged.date.max().date()
    dr = st.sidebar.date_input(
        "Date range", value=(date_min, date_max), min_value=date_min, max_value=date_max
    )
    start_date, end_date = dr
    dfc = (
        merged[merged.crypto_name == coin]
        .set_index("date").loc[start_date:end_date]
        .sort_index()
    )

# ─── 1) Overview ───────────────────────────────────────────────────────────────
if section == "Overview":
    st.title("🚀 Crypto Sentiment & Forecast Pipeline")

    # 📝 A brief walk-through of the pipeline:
    st.markdown("""
    Welcome to the Crypto Sentiment & Forecast Dashboard! This application stitches together:

    1. **News Ingestion**  
       • Scrapes headlines from Reddit, CoinTelegraph, CryptoSlate, etc.  
       • Tags each headline with the relevant cryptocurrency.

    2. **Sentiment Analysis**  
       • Uses VADER (or another model) to compute a _compound_ sentiment score for each headline.  
       • Aggregates daily per-coin metrics:  
         - **news_count** (total headlines)  
         - **pct_positive / pct_negative** (share of strongly positive/negative)  
         - **avg_compound** (mean VADER score)

    3. **Historical Price Merge**  
       • Joins those daily sentiment features with historical price data  
       • Fills any “no-news” days with zeros so we always have a contiguous time series.

    4. **Forecasting Models**  
       • **SARIMA**: Seasonal ARMA with daily seasonality (7-day)  
       • **LSTM**: A simple deep-learning approach trained on the last 14 days  
       • Compares their one-day-ahead performance side-by-side.

    5. **Backtesting & Metrics**  
       • Walk-forward backtest to simulate real-time forecasting  
       • Records RMSE / MAPE / Directional Accuracy for each model  
       • Visualizes cumulative returns vs. buy-and-hold.

    6. **Live Signals**  
       • On any given day, shows today’s price, each model’s 24-h forecast,  
         and a BUY/HOLD recommendation based on which model “wins.”

    Use the sidebar on the left to step through each of these modules—from **Sentiment Features** all the way through **Live Signals** and **Raw Data**.
    """)

    # Finally—in case you want to still show your slides beneath:
    slide_dir = BASE.parent / "slides"
    for img_path in sorted(slide_dir.glob("slide*.png")):
        st.image(Image.open(img_path), use_column_width=True)


# ─── 2) Sentiment Features ─────────────────────────────────────────────────────
# in your "Sentiment Features" section, replace the single-chart block with:
# ─── 2) Sentiment Features ─────────────────────────────────────────────────────
# ─── 2) Sentiment Features ─────────────────────────────────────────────────────
# ─── 2) Sentiment Features ─────────────────────────────────────────────────────
# ─── 2) Sentiment Features ─────────────────────────────────────────────────────
# ─── 2) Sentiment Features ─────────────────────────────────────────────────────
# ─── 2) Sentiment Features ─────────────────────────────────────────────────────
# ─── 2) Sentiment Features ─────────────────────────────────────────────────────
# ─── 2) Sentiment Features ─────────────────────────────────────────────────────
# ─── 2) Sentiment Features ─────────────────────────────────────────────────────
elif section == "Sentiment Features":
    st.title(f"📰 News & Sentiment for {coin}")

    # 1) get your filtered DataFrame
    dfv = dfc.reset_index()  # should contain date + any of news_count, pct_*, avg_compound

    # 2) debug: show which columns are present
    st.write("Columns present:", dfv.columns.tolist())

    # 3) define all possible features + colours
    ALL_FEATS = {
        "news_count":   "#FF7043",
        "pct_positive": "#66BB6A",
        "pct_negative": "#EF5350",
        "avg_compound": "#29B6F6",
    }

    # 4) pick only the columns that actually exist
    features = [f for f in ALL_FEATS if f in dfv.columns]
    if not features:
        st.warning("⚠️ No sentiment features found in this slice.")
    else:
        # 5) build an Altair multilayer chart
        base = alt.Chart(dfv).encode(x=alt.X("date:T", title="Date"))
        layers = []
        for feat in features:
            layers.append(
                base.mark_line(strokeWidth=2, color=ALL_FEATS[feat]).encode(
                    y=alt.Y(f"{feat}:Q", title=None),
                    tooltip=[
                        alt.Tooltip("date:T",   title="Date"),
                        alt.Tooltip(f"{feat}:Q", title=feat)
                    ]
                )
            )

        chart = (
            alt.layer(*layers)
               .properties(
                   title=f"News & Sentiment Features for {coin}",
                   height=300
               )
               .interactive()
        )
        st.altair_chart(chart, use_container_width=True)



# ─── 3) Forecast Comparison ────────────────────────────────────────────────────
elif section == "Forecast Comparison":
    st.title(f"💹 {coin} Price & One-Day Forecasts")

    # reset_index so 'date' is a column
    dfv = dfc.reset_index()

    # define all possible series: (column_name) → (label,color,strokeDash)
    ALL_SERIES = {
        "price_usd":       ("Price",   "#00E676", []),
        "sarima_forecast": ("SARIMA",  "#FFAB00", [5,5]),
        "lstm_forecast":   ("LSTM",    "#29B6F6", [2,2]),
    }

    # pick out the keys that actually exist in this slice
    present = [k for k in ALL_SERIES if k in dfv.columns]

    if not present:
        st.warning("⚠️ No price or forecast columns found for this coin/date range.")
    else:
        # build a multilayer Altair chart
        base = alt.Chart(dfv).encode(x=alt.X("date:T", title="Date"))
        layers = []
        for col in present:
            label, color, dash = ALL_SERIES[col]
            layers.append(
                base.mark_line(strokeWidth=2, color=color, strokeDash=dash)
                    .encode(
                        y=alt.Y(f"{col}:Q", title="USD Price"),
                        tooltip=[
                            alt.Tooltip("date:T", title="Date"),
                            alt.Tooltip(f"{col}:Q", title=label, format=",.2f")
                        ]
                    )
            )

        chart = alt.layer(*layers).properties(
            height=400,
            width="container",
            title=f"{coin} Price & One-Day Forecasts"
        ).interactive()

        st.altair_chart(chart, use_container_width=True)

        # legend hack: Altair won't auto-legend layered charts,
        # so we manually add a markdown legend
        legend_items = "  ".join(
            f"<span style='color:{ALL_SERIES[c][1]};'>■</span> {ALL_SERIES[c][0]}"
            for c in present
        )
        st.markdown(f"**Series:** {legend_items}", unsafe_allow_html=True)

# ─── 4) Backtest Results ───────────────────────────────────────────────────────
# ─── 4) Backtest Results ───────────────────────────────────────────────────────
elif section == "Backtest Results":
    st.title(f"📈 Cumulative Returns for {coin}")

    # build path (coin names in your files have underscores)
    fname = f"{coin.replace(' ', '')}_cum_returns.csv"
    csv_fp = PATHS["backtest_folder"] / fname

    if not csv_fp.exists():
        st.error(f"❌ Backtest file not found: {csv_fp.name}")
    else:
        # load & melt
        bt = pd.read_csv(csv_fp, parse_dates=["date"])
        dfm = bt.melt("date", var_name="Strategy", value_name="Cumulative Return")

        # Altair chart
        chart = (
            alt.Chart(dfm, title=f"Cumulative Returns for {coin}")
               .mark_line(point=True, strokeWidth=2)
               .encode(
                   x=alt.X("date:T", title="Date"),
                   y=alt.Y("Cumulative Return:Q", title="Equity Curve"),
                   color=alt.Color(
                       "Strategy:N",
                       scale=alt.Scale(
                           domain=["Buy & Hold", "SARIMA", "LSTM"],
                           range=["#29B6F6", "#FFAB00", "#66BB6A"]
                       )
                   ),
                   tooltip=["date:T", "Strategy:N", "Cumulative Return:Q"]
               )
               .interactive()
        )
        st.altair_chart(chart, use_container_width=True)


# ─── 5) Performance Metrics ────────────────────────────────────────────────────
elif section == "Performance Metrics":
    st.title("📊 Walk-Forward Performance Summary")
    if perf_summary.empty:
        st.warning("⚠️ `walk_forward_summary.csv` not found. Run walk-forward script first.")
    else:
        # 1) Show the raw table
        st.subheader("Summary Table")
        st.dataframe(
            perf_summary.style.format({
                "RMSE": "{:.2f}",
                "MAPE": "{:.2%}",
                "DirAcc": "{:.0%}"
            }),
            use_container_width=True
        )

        # 2) Melt to long form for plotting
        dfm = (
            perf_summary
              .reset_index()
              .melt(
                  id_vars="strategy",
                  value_vars=["RMSE","MAPE","DirAcc"],
                  var_name="Metric",
                  value_name="Value"
              )
        )

        # 3) Create a facet-bar chart with independent x-scales
        chart = (
            alt.Chart(dfm)
               .mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3)
               .encode(
                   y=alt.Y("strategy:N", title=None, sort="-x"),
                   x=alt.X("Value:Q", title=None),
                   color=alt.Color("Metric:N", legend=None),
                   column=alt.Column("Metric:N", title=None)
               )
               .properties(height=200)
               .resolve_scale(x="independent")  # <-- each panel gets its own x-axis
        )

        st.subheader("Metric Comparison")
        st.altair_chart(chart, use_container_width=True)


# ─── 6) Live Signals ────────────────────────────────────────────────────────────
elif section == "Live Signals":
    st.title("🚦 Live BUY/HOLD Recommendations")
    if live_signals.empty:
        st.warning("⚠️ `live_recommendations.csv` not found. Run live-signal script first.")
    else:
        st.table(live_signals.loc[[coin]])

# ─── 7) Raw Data Explorer ──────────────────────────────────────────────────────
elif section == "Raw Data":
    st.title("🗃️ Raw Merged Data")
    st.write("Filtered for your selection:")
    st.dataframe(dfc.reset_index(), use_container_width=True)
    st.write("Full merged dataset:")
    st.dataframe(merged, use_container_width=True)

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "🔍 Use the sidebar to navigate: **Overview**, **Sentiment Features**, **Forecast Comparison**, **Backtest Results**, **Performance Metrics**, **Live Signals**, **Raw Data**."
)

