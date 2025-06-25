import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analysis App", layout="centered")

st.title("🧠 Sentiment Analysis")
st.write("यह ऐप किसी टेक्स्ट की भावना (Positive / Negative / Neutral) का विश्लेषण करता है।")

# टेक्स्ट इनपुट
text = st.text_area("कृपया अपना टेक्स्ट लिखें:", height=150)

if st.button("भाव विश्लेषण करें"):
    if text.strip() == "":
        st.warning("कृपया कुछ टेक्स्ट दर्ज करें।")
    else:
        try:
            # हिंदी को अंग्रेजी में अनुवाद करें
            blob = TextBlob(text)
            translated_text = blob.translate(to='en')

            sentiment = translated_text.sentiment
            polarity = sentiment.polarity

            st.write("**अनुवादित टेक्स्ट:**", translated_text)
            st.write("**Polarity Score:**", polarity)

            if polarity > 0:
                st.success("🎉 भावना: Positive")
            elif polarity < 0:
                st.error("☹️ भावना: Negative")
            else:
                st.info("😐 भावना: Neutral")

        except Exception as e:
            st.error(f"त्रुटि: {e}")
