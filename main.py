import os
import json
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT,
    database=DB_NAME
)
cursor = conn.cursor()


def load_aggregated_transaction(path):
    skipped = []

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    quarter = file.replace(".json", "")
                    file_path = os.path.join(year_path, file)

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)

                        txs = data.get("data", {}).get("transactionData", [])
                        for tx in txs:
                            tx_type = tx.get("name")
                            instrument = tx.get("paymentInstruments", [{}])[0]
                            count = instrument.get("count")
                            amount = instrument.get("amount")

                            if None in (tx_type, count, amount):
                                skipped.append(f"{file_path} → {tx}")
                                continue

                            cursor.execute("""
                                INSERT INTO aggregated_transaction
                                (States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """, (state, year, quarter, tx_type, count, amount))

                    except Exception as e:
                        print(f"Error in {file_path}: {e}")

    conn.commit()
    if skipped:
        with open("missing_aggregated_transaction_log.txt", "w", encoding="utf-8") as f:
            for row in skipped:
                f.write(row + "\n")
        print(f"Skipped: {len(skipped)} rows → missing_aggregated_transaction_log.txt")
    print("Aggregated transaction data loaded.")



def load_aggregated_user(path):
    skipped = []

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    quarter = file.replace(".json", "")
                    file_path = os.path.join(year_path, file)

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)

                        brands = data.get("data", {}).get("usersByDevice", [])
                        for brand in brands:
                            name = brand.get("brand")
                            count = brand.get("count")
                            percentage = brand.get("percentage")

                            if None in (name, count, percentage):
                                skipped.append(f"{file_path} → {brand}")
                                continue

                            cursor.execute("""
                                INSERT INTO aggregated_user
                                (States, Years, Quarter, Brands, Transaction_count, Percentage)
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """, (state, year, quarter, name, count, percentage))

                    except Exception as e:
                        print(f"Error in {file_path}: {e}")

    conn.commit()
    if skipped:
        with open("missing_aggregated_user_log.txt", "w", encoding="utf-8") as f:
            for row in skipped:
                f.write(row + "\n")
        print(f" Skipped: {len(skipped)} rows → missing_aggregated_user_log.txt")
    print("Aggregated user data loaded.")



def load_aggregated_insurance(path):
    skipped = []

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    quarter = file.replace(".json", "")
                    file_path = os.path.join(year_path, file)

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)

                        txs = data.get("data", {}).get("transactionData", [])
                        for tx in txs:
                            insurance_type = tx.get("name")
                            instrument = tx.get("paymentInstruments", [{}])[0]
                            count = instrument.get("count")
                            amount = instrument.get("amount")

                            if None in (insurance_type, count, amount):
                                skipped.append(f"{file_path} → {tx}")
                                continue

                            cursor.execute("""
                                INSERT INTO aggregated_insurance
                                (States, Years, Quarter, Insurance_type, Total_count, Total_amount)
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """, (state, year, quarter, insurance_type, count, amount))

                    except Exception as e:
                        print(f"Error in {file_path}: {e}")

    conn.commit()
    if skipped:
        with open("missing_aggregated_insurance_log.txt", "w", encoding="utf-8") as f:
            for row in skipped:
                f.write(row + "\n")
        print(f"Skipped: {len(skipped)} rows → missing_aggregated_insurance_log.txt")
    print("Aggregated insurance data loaded.")


def load_map_user(path):
    skipped = []

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    quarter = file.replace(".json", "")
                    file_path = os.path.join(year_path, file)

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)

                        hover_data = data.get("data", {}).get("hoverData", {})

                        for district, values in hover_data.items():
                            reg = values.get("registeredUsers")
                            opens = values.get("appOpens")

                            if None in (district, reg, opens):
                                skipped.append(f"{file_path} → {district}")
                                continue

                            cursor.execute("""
                                INSERT INTO map_user
                                (States, Years, Quarter, Districts, RegisteredUser, AppOpens)
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """, (state, year, quarter, district, reg, opens))

                    except Exception as e:
                        print(f"Error in {file_path}: {e}")

    conn.commit()
    if skipped:
        with open("missing_map_user_log.txt", "w", encoding="utf-8") as f:
            for row in skipped:
                f.write(row + "\n")
        print(f"Skipped: {len(skipped)} rows → missing_map_user_log.txt")
    print("Map user data loaded.")



def load_map_map(path):
    skipped = []

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    quarter = file.replace(".json", "")
                    file_path = os.path.join(year_path, file)

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)

                        districts = data.get("data", {}).get("hoverDataList", [])
                        for d in districts:
                            district = d.get("name")
                            metric = d.get("metric", [{}])[0]
                            count = metric.get("count")
                            amount = metric.get("amount")

                            if None in (district, count, amount):
                                skipped.append(f"{file_path} → {d}")
                                continue

                            cursor.execute("""
                                INSERT INTO map_map
                                (States, Years, Quarter, District, Transaction_count, Transaction_amount)
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """, (state, year, quarter, district, count, amount))

                    except Exception as e:
                        print(f"Error in {file_path}: {e}")

    conn.commit()
    if skipped:
        with open("missing_map_map_log.txt", "w", encoding="utf-8") as f:
            for row in skipped:
                f.write(row + "\n")
        print(f"Skipped: {len(skipped)} → missing_map_map_log.txt")
    print("Map map (transaction) data loaded.")



def load_map_insurance(path):
    skipped = []

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    quarter = file.replace(".json", "")
                    file_path = os.path.join(year_path, file)

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)

                        districts = data.get("data", {}).get("hoverDataList", [])
                        for d in districts:
                            district = d.get("name")
                            metric = d.get("metric", [{}])[0]
                            count = metric.get("count")
                            amount = metric.get("amount")
                            category = d.get("insuranceCategory", "Unknown")

                            if None in (district, count, amount):
                                skipped.append(f"{file_path} → {d}")
                                continue

                            cursor.execute("""
                                INSERT INTO map_insurance
                                (States, Districts, Years, Quarter, Insurance_Category, Transaction_count, Transaction_amount)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """, (state, district, year, quarter, category, count, amount))

                    except Exception as e:
                        print(f"Error in {file_path}: {e}")

    conn.commit()
    if skipped:
        with open("missing_map_insurance_log.txt", "w", encoding="utf-8") as f:
            for row in skipped:
                f.write(row + "\n")
        print(f"Skipped: {len(skipped)} → missing_map_insurance_log.txt")
    print("Map insurance data loaded.")



def load_top_user(path):
    skipped = []

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    try:
                        quarter = int(file.strip(".json"))
                        file_path = os.path.join(year_path, file)

                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)

                        pincodes = data.get("data", {}).get("pincodes", [])
                        for i in pincodes:
                            name = i.get("name")
                            reg = i.get("registeredUsers")

                            if None in (name, reg):
                                skipped.append(f"{file_path} → {i}")
                                continue

                            # State name formatting
                            clean_state = state.replace("-", " ").title()
                            if clean_state.lower() == "Andaman & Nicobar Islands":
                                clean_state = "Andaman and Nicobar"
                            elif "dadra" in clean_state.lower():
                                clean_state = "Dadra and Nagar Haveli and Daman Diu"

                            cursor.execute("""
                                INSERT INTO top_user
                                (States, Years, Quarter, Pincodes, RegisteredUser)
                                VALUES (%s, %s, %s, %s, %s)
                            """, (clean_state, year, quarter, name, reg))

                    except Exception as e:
                        print(f"Error in {file_path}: {e}")

    conn.commit()
    if skipped:
        with open("missing_top_user_log.txt", "w", encoding="utf-8") as f:
            for row in skipped:
                f.write(row + "\n")
        print(f"Skipped: {len(skipped)} → missing_top_user_log.txt")
    print("Top user data loaded.")



def load_top_map(path):
    skipped = []

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    quarter = int(file.strip(".json"))
                    file_path = os.path.join(year_path, file)

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = json.load(f)

                        pincodes = data.get("data", {}).get("pincodes", [])
                        for i in pincodes:
                            pincode = i.get("entityName")
                            count = i.get("metric", {}).get("count", 0)
                            amount = i.get("metric", {}).get("amount", 0)

                            if None in (pincode, count, amount):
                                skipped.append(f"{file_path} → {i}")
                                continue

                            # State cleanup
                            clean_state = state.replace("-", " ").title()
                            if clean_state.lower() == "Andaman & Nicobar Islands":
                                clean_state = "Andaman and Nicobar"
                            elif "dadra" in clean_state.lower():
                                clean_state = "Dadra and Nagar Haveli and Daman Diu"

                            cursor.execute("""
                                INSERT INTO top_map
                                (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """, (clean_state, year, quarter, pincode, count, amount))

                    except Exception as e:
                        print(f"Error in {file_path}: {e}")

    conn.commit()

    if skipped:
        with open("missing_top_map_log.txt", "w", encoding="utf-8") as f:
            for row in skipped:
                f.write(row + "\n")
        print(f" Skipped {len(skipped)} rows → missing_top_map_log.txt")

    print("Top transaction data (top_map) loaded.")




def load_top_insurance(path):
    skipped = []

    for state in os.listdir(path):
        state_path = os.path.join(path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    quarter = int(file.strip(".json"))
                    file_path = os.path.join(year_path, file)

                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            file_contents = f.read()

                        if not file_contents:
                            print(f"⚠️ Warning: {file_path} is empty.")
                            continue

                        data = json.loads(file_contents)
                        pincodes = data.get("data", {}).get("pincodes", [])

                        for i in pincodes:
                            pincode = i.get("entityName")
                            metric = i.get("metric", {})
                            count = metric.get("count", 0)
                            amount = metric.get("amount", 0)

                            if None in (pincode, count, amount):
                                skipped.append(f"{file_path} → {i}")
                                continue

                            # Clean state formatting
                            clean_state = state.replace("-", " ").title()
                            if clean_state.lower() == "Andaman & Nicobar Islands":
                                clean_state = "Andaman and Nicobar"
                            elif "dadra" in clean_state.lower():
                                clean_state = "Dadra and Nagar Haveli and Daman Diu"

                            cursor.execute("""
                                INSERT INTO top_insurance
                                (States, Years, Quarter, Pincodes, Insurance_Category, Transaction_count, Transaction_amount)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """, (clean_state, year, quarter, pincode, "TOTAL", count, amount))

                    except json.JSONDecodeError as je:
                        print(f"JSON Decode Error in {file_path}: {je}")
                    except Exception as e:
                        print(f"Error in {file_path}: {e}")

    conn.commit()

    if skipped:
        with open("missing_top_insurance_log.txt", "w", encoding="utf-8") as f:
            for row in skipped:
                f.write(row + "\n")
        print(f"Skipped {len(skipped)} rows → missing_top_insurance_log.txt")

    print("Top insurance data loaded.")











if __name__ == "__main__":
    print("Starting data load...")

    load_aggregated_transaction("pulse/data/aggregated/transaction/country/india/state")
    load_aggregated_user("pulse/data/aggregated/user/country/india/state")
    load_aggregated_insurance("pulse/data/aggregated/insurance/country/india/state")
    load_map_user("pulse/data/map/user/hover/country/india/state")
    load_map_map("pulse/data/map/transaction/hover/country/india/state")
    load_map_insurance("pulse/data/map/insurance/hover/country/india/state")
    load_top_user("pulse/data/top/user/country/india/state")
    load_top_map("pulse/data/top/transaction/country/india/state")
    load_top_insurance("pulse/data/top/insurance/country/india/state")

    print("Data load complete!")

    cursor.close()
    conn.close()

