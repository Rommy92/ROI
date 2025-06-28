import streamlit as st
import pandas as pd

# ------------------ CONFIG --------------------
st.set_page_config(page_title="Options & Shares Profit Calculator", layout="centered")
st.title("💹 Calls-Only Options & Shares Profit Table")
st.caption("Enter your inputs and instantly see projected profits at multiple target returns.")

# ------------------ OPTIONS CALCULATOR --------------------
st.header("📈 Long Call Options Profit Table")

col1, col2 = st.columns(2)
with col1:
    option_cost = st.number_input("Option Premium per Share ($)", min_value=0.01, step=0.1, value=1.0)
with col2:
    contracts = st.number_input("Number of Contracts", min_value=1, step=1, value=1)

share_multiplier = 100  # 1 contract = 100 shares
total_cost = option_cost * share_multiplier * contracts

# Calculate profits at various sell returns
returns = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
rows = []

for r in returns:
    sell_price = option_cost * (1 + r / 100)
    total_sell = sell_price * share_multiplier * contracts
    profit = total_sell - total_cost
    rows.append({
        "Target Return": f"+{r}%",
        "Sell Price per Share": f"${sell_price:.2f}",
        "Total Sell Value": f"${total_sell:.2f}",
        "Profit": f"${profit:.2f}"
    })

df_options = pd.DataFrame(rows)
st.subheader("📊 Call Option Sale Profit Table")
st.dataframe(df_options, use_container_width=True)

# ------------------ SHARES CALCULATOR --------------------
st.header("📉 Shares Profit Table")

col3, col4 = st.columns(2)
with col3:
    share_price = st.number_input("Buy Price per Share ($)", min_value=0.01, step=0.1, value=100.0)
with col4:
    num_shares = st.number_input("Number of Shares", min_value=1, step=1, value=100)

total_share_cost = share_price * num_shares

rows_shares = []
for r in returns:
    sell_price = share_price * (1 + r / 100)
    total_sell = sell_price * num_shares
    profit = total_sell - total_share_cost
    rows_shares.append({
        "Target Return": f"+{r}%",
        "Sell Price": f"${sell_price:.2f}",
        "Total Sell Value": f"${total_sell:.2f}",
        "Profit": f"${profit:.2f}"
    })

df_shares = pd.DataFrame(rows_shares)
st.subheader("📊 Share Sale Profit Table")
st.dataframe(df_shares, use_container_width=True)

# ------------------ FOOTER --------------------
st.markdown("---")
st.markdown("🧠 **Tip:** This tool assumes you're selling into profit (no Greeks, break-even, or expiry logic — just ROI snapshots).")
