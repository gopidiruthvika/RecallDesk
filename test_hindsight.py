import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

# Load the API key from .env
load_dotenv()

api_key = os.getenv("HINDSIGHT_API_KEY")
base_url = os.getenv("HINDSIGHT_BASE_URL")

if not api_key:
    print("ERROR: Hindsight API key not found in .env")
    exit()

# Connect to Hindsight Cloud
client = Hindsight(
    api_key=api_key,
    base_url=base_url
)

# Use the exact bank ID you created in Hindsight Cloud
bank_id = "recall-desk"

try:
    # 1. RETAIN: Store a customer memory
    print("Saving customer memory...")

    client.retain(
        bank_id=bank_id,
        content=(
            "Customer CUST001 previously experienced UPI "
            "payment failures on an Android phone. "
            "Clearing the app cache temporarily resolved "
            "the issue. The customer prefers concise "
            "troubleshooting instructions."
        )
    )

    print("Memory saved!")

    # 2. RECALL: Retrieve the customer's history
    print("\nSearching for the customer's previous issue...")

    result = client.recall(
        bank_id=bank_id,
        query="What issue did customer CUST001 have before, "
              "and what solution helped?"
    )

    if result.results:
        print("\nMemories found:")

        for memory in result.results:
            print("-", memory.text)
    else:
        print("No memories found yet.")

except Exception as e:
    print("\nSomething went wrong:")
    print(e)

finally:
    client.close()