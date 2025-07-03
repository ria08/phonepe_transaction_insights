import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from fetch_analysis import fetch_query_to_df
import queries as q

# Streamlit page setup
st.set_page_config(layout="wide")
st.title("PhonePe Pulse Dashboard")

# ---------------- Load Data ----------------
df_tx = fetch_query_to_df(q.transaction_by_state_quarter)
df_users = fetch_query_to_df(q.users_by_device_brand)
df_app_opens = fetch_query_to_df(q.app_opens_by_state)
df_category = fetch_query_to_df(q.transaction_by_category)
df_insurance = fetch_query_to_df(q.insurance_summary_by_state)
df_top_districts = fetch_query_to_df(q.top_districts_by_transaction)
df_top_app = fetch_query_to_df(q.top_districts_by_app_opens)
df_user_growth = fetch_query_to_df(q.yearly_user_growth)




# ---------------- Sidebar Filters ---------------

st.sidebar.header("🔍 Filters")

states = sorted(df_tx['States'].unique())
years = sorted(df_tx['Years'].unique())
quarters = sorted(df_tx['Quarter'].unique())
brands = sorted(df_users['Brands'].unique())

selected_states = st.sidebar.multiselect("Select State(s):", states, default=states)
selected_years = st.sidebar.multiselect("Select Year(s):", years, default=years)
selected_quarters = st.sidebar.multiselect("Select Quarter(s):", quarters, default=quarters)
selected_brands = st.sidebar.multiselect("Select Brand(s):", brands, default=brands)

# ---------------- Filtered Data ----------------

filtered_df_tx = df_tx[
    (df_tx['States'].isin(selected_states)) &
    (df_tx['Years'].isin(selected_years)) &
    (df_tx['Quarter'].isin(selected_quarters))
]

filtered_users = df_users[df_users['Brands'].isin(selected_brands)]

filtered_app = df_app_opens[df_app_opens['States'].isin(selected_states)]


filtered_category = df_category[
    (df_category['Years'].isin(selected_years)) &
    (df_category['Quarter'].isin(selected_quarters))
]

filtered_insurance = df_insurance[df_insurance['States'].isin(selected_states)]

filtered_top_districts = df_top_districts[df_top_districts['States'].isin(selected_states)]

filtered_top_app = df_top_app[df_top_app['States'].isin(selected_states)]

filtered_growth = df_user_growth[
    (df_user_growth['States'].isin(selected_states)) &
    (df_user_growth['Years'].isin(selected_years))
]

# ---------------- KPIs (Interactive) ----------------

col1, col2, col3 = st.columns(3)
col1.metric("Total Transaction Amount", f"₹{filtered_df_tx['Total_Amount'].sum():,.0f}")
col2.metric("Total Users (Selected Brands)", f"{filtered_users['Total_Users'].sum():,.0f}")
col3.metric("Quarters Selected", f"{filtered_df_tx['Quarter'].nunique()}")

st.markdown("---")

# ---------------- Chart 1: Transaction by State and Quarter ----------------

st.subheader("Transaction Amount by State and Quarter")
fig1, ax1 = plt.subplots(figsize=(14, 6))
sns.barplot(data=filtered_df_tx, x="States", y="Total_Amount", hue="Quarter", ax=ax1)
plt.xticks(rotation=90)
st.pyplot(fig1)

# ---------------- Chart 2: Users by Device Brand ----------------

st.subheader(" Users by Device Brand")
fig2, ax2 = plt.subplots(figsize=(12, 5))
sns.barplot(data=filtered_users, x="Brands", y="Total_Users", ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# ---------------- Chart 3: App Opens vs Registered Users ----------------

st.subheader("App Opens vs Registered Users")
fig3, ax3 = plt.subplots(figsize=(12, 6))
sns.scatterplot(data=filtered_app, x="RegisteredUsers", y="AppOpens", hue="States", s=100, ax=ax3)
plt.title("App Opens vs Registered Users by State")
plt.legend(title="States", bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig3)

# ---------------- Chart 4: Transaction Amount by Category Over Time ----------------

st.subheader("Transaction Amount by Category Over Time")
fig4, ax4 = plt.subplots(figsize=(14, 6))
sns.lineplot(data=filtered_category, x="Years", y="Total_Amount", hue="Transaction_type", marker="o", ax=ax4)
plt.title("Total Transaction Amount by Category Over Time")
plt.xlabel("Year")
plt.ylabel("Transaction Amount")
st.pyplot(fig4)

# ---------------- Chart 5: Total Insurance Value by State ----------------

st.subheader("Total Insurance Value")
fig5, ax5 = plt.subplots(figsize=(14, 6))
sns.barplot(data=filtered_insurance, x="States", y="Total_Value", color="skyblue", ax=ax5)
plt.xticks(rotation=90)
plt.title("States by Insurance Value")
st.pyplot(fig5)

# ---------------- Chart 6: District-wise Transaction Volume ----------------


st.subheader("Transaction Volume by District")
st.dataframe(
    filtered_top_districts
    .sort_values(by="Total_Amount", ascending=False)
    .reset_index(drop=True)
    .style.format({"Total_Amount": "₹{:.0f}"})
)


# ---------------- Chart 7: App Opens by District ----------------


st.subheader("App Opens by District")
st.dataframe(
    filtered_top_app
    .sort_values(by="Total_AppOpens", ascending=False)
    .reset_index(drop=True)
)


# ---------------- Chart 8: User Growth Over the Years ----------------



st.subheader("User Growth Over the Years by State")
st.dataframe(filtered_growth.sort_values(by=["Years", "Total_Users"], ascending=[True, False]).reset_index(drop=True))