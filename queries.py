# -----------------------------
# Business Case 1: Decoding Transaction Dynamics on PhonePe

# PhonePe, a leading digital payments platform, has recently identified significant variations in transaction behavior across states, quarters, and payment categories. 
 # While some regions and transaction types demonstrate consistent growth, others show stagnation or decline. 
# The leadership team seeks a deeper understanding of these patterns to drive targeted business strategies.

# -----------------------------

transaction_by_state_quarter = """
SELECT 
    States,
    Years,
    Quarter,
    SUM(Transaction_amount) AS Total_Amount
FROM 
    aggregated_transaction
GROUP BY 
    States, Years, Quarter
ORDER BY 
    Years, Quarter, Total_Amount DESC;



"""

transaction_by_category = """
SELECT Transaction_type, Years, Quarter,
       SUM(Transaction_count) AS Total_Transactions,
       SUM(Transaction_amount) AS Total_Amount
FROM aggregated_transaction
GROUP BY Transaction_type, Years, Quarter
ORDER BY Years, Quarter;
"""

# -----------------------------
# Business Case 2: Device Dominance and User Engagement Analysis

# PhonePe aims to enhance user engagement and improve app performance by understanding user preferences across different device brands. 
# The data reveals the number of registered users and app opens, segmented by device brands, regions, and time periods. 
# However, trends in device usage vary significantly across regions, and some devices are disproportionately underutilized despite high registration numbers.

# -----------------------------

users_by_device_brand = """
SELECT Brands, SUM(Transaction_count) AS Total_Users
FROM aggregated_user
GROUP BY Brands
ORDER BY Total_Users DESC;
"""

app_opens_by_state = """
SELECT a.States, SUM(a.Transaction_count) AS RegisteredUsers, 
       SUM(b.AppOpens) AS AppOpens
FROM aggregated_user a
JOIN map_user b ON a.States = b.States AND a.Years = b.Years AND a.Quarter = b.Quarter
GROUP BY a.States
ORDER BY AppOpens DESC
;
"""

# -----------------------------
# Business Case 3: Insurance Penetration and Growth Potential Analysis

# PhonePe has ventured into the insurance domain, providing users with options to secure various policies. 
# With increasing transactions in this segment, the company seeks to analyze its growth trajectory and identify untapped opportunities for insurance adoption at the state level. 
# This data will help prioritize regions for marketing efforts and partnerships with insurers.

# -----------------------------

insurance_summary_by_state = """
SELECT States, SUM(Total_count) AS Policies_Sold,
       SUM(Total_amount) AS Total_Value
FROM aggregated_insurance
GROUP BY States
ORDER BY Total_Value DESC;
"""

insurance_per_user = """
SELECT ai.States, 
       SUM(ai.Total_count) / NULLIF(SUM(mu.RegisteredUser), 0) AS PoliciesPerUser
FROM aggregated_insurance ai
JOIN map_user mu ON ai.States = mu.States AND ai.Years = mu.Years AND ai.Quarter = mu.Quarter
GROUP BY ai.States
ORDER BY PoliciesPerUser DESC;
"""

# -----------------------------
# Business Case 4: Transaction Analysis for Market Expansion

# PhonePe operates in a highly competitive market, and understanding transaction dynamics at the state level is crucial for strategic decision-making.
# With a growing number of transactions across different regions, the company seeks to analyze its transaction data to identify trends, opportunities, and potential areas for expansion.

# -----------------------------

top_districts_by_transaction = """
SELECT District, States, SUM(Transaction_amount) AS Total_Amount
FROM map_map
GROUP BY District, States
ORDER BY Total_Amount DESC
;
"""

low_performing_states = """
SELECT States, SUM(Transaction_amount) AS Total_Amount
FROM aggregated_transaction
GROUP BY States
ORDER BY Total_Amount ASC
;
"""

# -----------------------------
# Business Case 5: User Engagement and Growth Strategy

# PhonePe seeks to enhance its market position by analyzing user engagement across different states and districts. 
# With a significant number of registered users and app opens, understanding user behavior can provide valuable insights for strategic decision-making and growth opportunities.

# -----------------------------

yearly_user_growth = """
SELECT States, Years, SUM(Transaction_count) AS Total_Users
FROM aggregated_user
GROUP BY States, Years
ORDER BY Years;
"""

top_districts_by_app_opens = """
SELECT Districts, States, SUM(AppOpens) AS Total_AppOpens
FROM map_user
GROUP BY Districts, States
ORDER BY Total_AppOpens DESC;
"""
