import streamlit as st 
import requests

api_url="http://127.0.0.1:8000/predict"

# Main title with emoji
st.title("🎭 Emotion Prediction App")

# Subtitle with description
st.subheader("Reveal hidden emotions in your text ✨")

# Separator
st.markdown("---")
st.markdown("Simply type or paste any text in the box below, "
    "and I'll instantly analyze the emotions for you!")


emotion=st.text_area("Enter your text here:")

if st.button("Predict Emotion"):

    # create a josn like in dic
    user_input = {"fellings": emotion}
    try:
        response=requests.post(api_url,json=user_input)
        if response.status_code == 200:
            result=response.json()
            predict=result["prediction"]
            if predict == "Sadness":
                st.success("😢💔 Sadness")
            elif predict =="Anger":
                st.success("😠 Anger")
            elif predict == "Fear":
                st.success("👻 Fear")
            else:
                st.success("😄 Joy")
        else:
            st.error(f"server returned status {response.status_code}")
    except Exception as e:
        st.error(f"Error connecting to the server: {e}")


# --- Sidebar ---
st.sidebar.header("ℹ️ Project Information")
st.sidebar.write("**Application:** Emotion Prediction App")
st.sidebar.write("**Developer:** Zaryab Ahmad")
st.sidebar.write("**Education:** BSIT Final Year")
st.sidebar.markdown("---")
st.sidebar.write("**Institution:** Emerson University, Multan")
st.sidebar.write("**Development Date:** October 2024")


st.markdown("---")
st.caption("Developed by Zaryab Ahmad | Emerson University Multan | © 2025")



# "Sadness" if pred == 0 else "Anger" if pred == 3 else "Fear" if pred ==4 else "Joy"