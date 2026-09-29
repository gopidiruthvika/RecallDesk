from hindsight_memory import (
    remember_customer,
    recall_customer,
    close_hindsight
)
from llm import generate_response


# -------------------------------
# CUSTOMER INFORMATION
# -------------------------------

customer_id = "CUST001"

customer_information = """
The customer uses an Android phone.
They previously had UPI payment failures.
Clearing the app cache temporarily solved the problem.
The customer prefers concise troubleshooting instructions.
"""

# Save this information to Hindsight
print("🧠 Saving customer information to Hindsight...")

remember_customer(
    customer_id,
    customer_information
)

print("✅ Customer memory saved!")


# -------------------------------
# NEW CUSTOMER QUESTION
# -------------------------------

question = "My UPI payment is failing again. What should I do?"

print("\n👤 Customer:")
print(question)


# -------------------------------
# RECALL CUSTOMER MEMORY
# -------------------------------

print("\n🔍 Searching customer history...")

memories = recall_customer(
    customer_id,
    question
)

print("\n🧠 Relevant memories:")

for memory in memories:
    print("-", memory)


# -------------------------------
# GENERATE PERSONALIZED RESPONSE
# -------------------------------

memory_text = "\n".join(memories)

prompt = f"""
You are helping customer {customer_id}.

Customer's current question:
{question}

Relevant information from the customer's previous interactions:
{memory_text}

Use the customer's history when it is relevant.

Give a concise, helpful troubleshooting response.
Do not mention that you are using a memory system.
"""

print("\n🤖 RecallDesk:")

answer = generate_response(prompt)

print(answer)

close_hindsight()
