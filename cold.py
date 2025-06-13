import streamlit as st
import smtplib
from email.message import EmailMessage
from gemini_helper import my_google_llm

st.set_page_config(page_title="Cold Email Sender with Gemini", layout="centered")

# -----------------------------------
# 🧠 Sidebar: Gemini Q&A
# -----------------------------------
with st.sidebar:
    st.title("🤖 Ask Gemini")
    st.markdown("Need help writing your email? Ask Gemini here!")

    question = st.text_input("Ask a Question to Gemini")
    if st.button("Ask Gemini"):
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Gemini is thinking..."):
                answer = my_google_llm(question)
            st.success("Gemini's Answer:")
            st.write(answer)

# -----------------------------------
# 📧 Main Interface: Email Sender
# -----------------------------------
st.title("📧 Cold Email Sender to HR with Resume")

st.write("Fill in the details below to send a cold email to an HR with your resume.")

# User Inputs
sender_email = st.text_input("Your Gmail Address")
sender_password = st.text_input("Your Gmail App Password", type="password")
receiver_email = st.text_input("HR's Email Address")

subject = st.text_input("Email Subject", "Application for Internship Opportunity")
message = st.text_area("Email Message",
                       """Dear [HR's Name],
                       
                       I hope this email finds you well. I am writing to express my interest in an opportunity at your organization.
                       
                       Please find my resume attached. I would be grateful for the opportunity to connect further.
                       
                       Best regards,  
                       [Your Name]  
                       [LinkedIn/GitHub link]
                       """, height=250)

# Resume Upload
resume_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

# Send Email
if st.button("Send Email"):
    if not all([sender_email, sender_password, receiver_email, subject, message]):
        st.warning("⚠️ Please fill in all the fields.")
    elif not resume_file:
        st.warning("⚠️ Please upload your resume.")
    else:
        try:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg.set_content(message)

            # Attach resume
            msg.add_attachment(resume_file.read(), maintype='application', subtype='pdf', filename=resume_file.name)

            # Send via Gmail SMTP
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(sender_email, sender_password)
                smtp.send_message(msg)

            st.success("✅ Email sent successfully with resume!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
