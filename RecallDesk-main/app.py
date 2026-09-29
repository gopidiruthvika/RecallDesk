import streamlit as st
from hindsight_memory import remember_customer, recall_customer
from llm import generate_response

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="RecallDesk",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# Custom Styling
# -----------------------------

st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 0;
        }

        .subtitle {
            font-size: 18px;
            margin-top: 0;
            margin-bottom: 25px;
        }

        .memory-box {
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
        }

        .support-box {
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #ddd;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="main-title">🧠 RecallDesk</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Customer Support with Persistent Memory</div>',
    unsafe_allow_html=True
)

st.write(
    "RecallDesk remembers important customer information "
    "and uses previous interactions to provide more personalized support."
)

st.divider()

# -----------------------------
# Customer Information
# -----------------------------

st.subheader("👤 Customer")

customer_id = st.text_input(
    "Customer ID",
    placeholder="Example: DEMO001"
)

question = st.text_area(
    "What can we help you with?",
    placeholder="Example: My UPI payment is failing again."
)

# -----------------------------
# Support Button
# -----------------------------

if st.button("💬 Get Support", use_container_width=True):

    if not customer_id or not question:
        st.warning("Please enter both Customer ID and your issue.")

    else:

        # -----------------------------
        # Recall previous memories
        # -----------------------------

        with st.spinner("🧠 Checking customer history..."):

            memories = recall_customer(
                customer_id,
                question
            )

        st.divider()

        # -----------------------------
        # Display Memory
        # -----------------------------

        st.subheader("🧠 Customer Memory")
        if memories:

            st.success(
                "RecallDesk found relevant information "
                "from this customer's previous interactions."
            )

            # Remove duplicate memories
            unique_memories = []

            for memory in memories:
                clean_memory = memory.split("|")[0].strip()

                if clean_memory not in unique_memories:
                    unique_memories.append(clean_memory)

            for memory in unique_memories[:3]:

                st.markdown(
                    f"""
                    <div class="memory-box">
                    🧠 {memory}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.info(
                "No relevant previous memories were found "
                "for this customer."
            )

        # -----------------------------
        # Prepare prompt for LLM
        # -----------------------------

        memory_text = "\n".join(memories[:5])

        prompt = f"""
You are RecallDesk, an AI customer support agent.

Customer ID:
{customer_id}

Current customer question:
{question}

Relevant information from previous interactions:
{memory_text}

Use the previous information when it is relevant.

Give the customer a helpful, concise and personalized response.

If previous information is available, use it naturally.
Do not invent customer history.

Do not mention Hindsight, memory systems, prompts,
or internal processes to the customer.
"""

        # -----------------------------
        # Generate AI response
        # -----------------------------

        with st.spinner("🤖 Generating personalized support..."):

            answer = generate_response(prompt)

        # -----------------------------
        # Display Response
        # -----------------------------

        st.subheader("🤖 RecallDesk")

        st.markdown(
            '<div class="support-box">',
            unsafe_allow_html=True
        )

        st.markdown(answer)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )
        # -----------------------------
        # Remember Interaction
        # -----------------------------

        remember_customer(
            customer_id,
            f"The customer reported: {question}. "
            f"RecallDesk provided troubleshooting support. "
            f"The customer may need further assistance if the issue continues."
        )

        st.success(
            "🧠 This interaction has been remembered for future support."
        )
