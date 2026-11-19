
import streamlit as st

st.set_page_config(
    page_title="HR/IT Helpdesk Agent",
    page_icon="🤖"
)

st.title("🤖 HR/IT Helpdesk Agent")
st.write("Welcome! I am your HR and IT support assistant.")
st.write("Ask me about leave, payroll, attendance, passwords or technical issues.")

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

# HR and IT responses
responses = {
    "leave balance": "Your sample leave balance is 12 days. Please contact HR to confirm your actual leave balance.",
    "apply leave": "To apply for leave, log in to your employee portal, open the Leave Management section, select your leave dates and submit your request for approval.",
    "leave": "For leave-related questions, please visit the Leave Management section of your employee portal or contact HR.",

    "payslip": "You can download your payslip from the Payroll section of your employee portal. Contact HR if you cannot access it.",
    "salary date": "Salary is generally processed according to your organization's payroll schedule. Please contact HR or Payroll for the exact payment date.",
    "salary": "For salary-related questions, including deductions and payment details, please contact your HR or Payroll department.",
    "payroll": "The Payroll department can help with salary payments, payslips and deductions.",

    "attendance": "You can check your attendance records in the employee portal. If any attendance entry is missing, contact HR.",
    "check in": "Please use your organization's attendance system to record your check-in time.",
    "missing attendance": "Please report missing attendance details to HR or your reporting manager for correction.",

    "password": "To reset your password, select 'Forgot Password' on the login page and follow the instructions.",
    "login": "Please check your username and password. If you still cannot log in, try resetting your password or contact IT support.",
    "email": "If you cannot access your official email, contact IT support for assistance.",

    "laptop": "Please restart your laptop and check the power and network connections. If the problem continues, contact IT support.",
    "software": "For software installation or access, please raise a request with your IT support team.",
    "vpn": "Please check your internet connection and VPN credentials. If the issue continues, contact IT support.",
    "internet": "Please check your Wi-Fi or network connection. If the issue continues, contact IT support.",

    "support": "For HR-related issues, contact your HR department. For technical issues, contact your IT support team.",
    "contact hr": "Please contact your organization's HR department for employee-related assistance.",
    "contact it": "Please contact your organization's IT support team for technical assistance."
}

# Get user question
user_question = st.chat_input("Ask your HR or IT question here...")

if user_question:
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    question = user_question.lower()

    response = (
        "Sorry, I couldn't find a suitable answer. "
        "Please contact your HR or IT support team for further assistance."
    )

    # Match the question with predefined keywords
    for keyword, answer in responses.items():
        if keyword in question:
            response = answer
            break

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.rerun()

st.caption(
    "Note: This is a demonstration application using predefined responses "
    "and sample information. It is not connected to actual employee records."
)

