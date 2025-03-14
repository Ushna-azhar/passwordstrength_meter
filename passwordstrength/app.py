import streamlit as st
import re

def check_password_strength(password):
    score = 0
    criteria = {
        "Length (8+ characters)": len(password) >= 8,
        "Upper & Lowercase Letters": bool(re.search(r"[a-z]", password) and re.search(r"[A-Z]", password)),
        "Numbers": bool(re.search(r"\d", password)),
        "Special Characters": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }
    
    score = sum(criteria.values())
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength = strength_levels[score]
    
    return strength, criteria

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")
    
    # Apply background color using Markdown and CSS
    st.markdown(
        """
        <style>
            body {
                background-color: #000000;
                color: #FFFFFF;
            }
            .stApp {
                background-color: #000000;
            }
            h1, h2, h3, h4, h5, h6, p, div, span, label {
                color: #FFFFFF !important;
            }
            .stTextInput > div > div > input {
                background-color: #222222;
                color: #FFFFFF;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🔐 Password Strength Meter")
    st.markdown("Enter a password to check its strength.")
    
    password = st.text_input("Enter Password", type="password")
    
    if password:
        strength, criteria = check_password_strength(password)
        
        st.subheader(f"Password Strength: {strength}")
        
        for criterion, met in criteria.items():
            st.write(f"{'✅' if met else '❌'} {criterion}")
        
        st.progress(sum(criteria.values()) / len(criteria))
    
if __name__ == "__main__":
    main()
