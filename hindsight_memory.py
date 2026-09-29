import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    api_key=os.getenv("HINDSIGHT_API_KEY"),
    base_url=os.getenv("HINDSIGHT_BASE_URL")
)

BANK_ID = "recall-desk"


def remember_customer(customer_id, information):
    """
    Store customer information in Hindsight
    with a customer-specific tag.
    """
    content = f"Customer {customer_id}: {information}"

    client.retain(
        bank_id=BANK_ID,
        content=content,
        tags=[f"customer:{customer_id}"]
    )


def recall_customer(customer_id, question):
    """
    Retrieve memories only for this specific customer.
    """
    query = f"Customer {customer_id}: {question}"

    result = client.recall(
        bank_id=BANK_ID,
        query=query,
        tags=[f"customer:{customer_id}"],
        tags_match="all_strict"
    )

    memories = []

    if result.results:
        for memory in result.results:
            memories.append(memory.text)

    return memories
