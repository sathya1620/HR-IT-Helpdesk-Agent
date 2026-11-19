
import streamlit as st

st.set_page_config(
    page_title="AI Helpdesk Agent",
    page_icon="🎧"
)

st.title("🎧 AI Helpdesk Agent")
st.write("Welcome! How can I help you today?")

# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Customer question
user_question = st.chat_input("Ask your question here...")

# Helpdesk responses
responses = {
    "password": "To reset your password, click Forgot Password on the login page and follow the instructions.",
    "order": "To track your order, please visit the My Orders section of your account.",
    "refund": "For a refund, please share your order details with our support team.",
    "account": "You can update your account details from the Profile Settings section.",
    "contact": "You can contact our support team through the Help and Support section.",
    "payment": "Please check your payment method and transaction status. If the issue continues, contact our support team.",
    "delivery": "You can check your estimated delivery date in the My Orders section.",
    "cancel": "To cancel your order, visit My Orders and select the Cancel Order option if available.",
    "email": "You can update your email address from your Profile Settings.",
    "login": "Please check your username and password. If you still cannot log in, try resetting your password.",
    "support": "For further assistance, please contact our support team at support@example.com."
}

# Generate response
if user_question:
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    question = user_question.lower()

    response = "Sorry, I couldn't find an answer. Please contact our support team."

    for keyword, answer in responses.items():
        if keyword in question:
            response = answer
            break

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.rerun()


