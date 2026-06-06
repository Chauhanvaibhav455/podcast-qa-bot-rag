import streamlit as st
import faiss
import pickle
import os

from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import google.generativeai as genai

# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

llm = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Podcast Q&A Bot",
    page_icon="🎙️",
    layout="wide"
)

st.title("🎙️ Elon Musk Podcast Q&A Bot")
st.caption("Ask questions about Elon Musk × Nikhil Kamath Podcast and get answers with timestamps.")

# ----------------------------
# Load Models
# ----------------------------
@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_embedding_model()

# ----------------------------
# Load FAISS Index
# ----------------------------
index = faiss.read_index("podcast.index")

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# ----------------------------
# User Question
# ----------------------------
question = st.text_input(
    "Ask a question",
    placeholder="Example: How should AI be regulated?"
)

# ----------------------------
# Search + Answer
# ----------------------------
if question:

    with st.spinner("Searching podcast transcript..."):

        query_embedding = model.encode([question])

        D, I = index.search(query_embedding, 3)

        context = "\n\n".join(
            [chunks[idx] for idx in I[0]]
        )

        prompt = f"""
You are an AI assistant answering questions about a podcast.

Use ONLY the transcript provided below.

Transcript:
{context}

Question:
{question}

Return EXACTLY in this format:

Answer:
<clear concise answer>

Timestamp:
<most relevant timestamp>

Why this timestamp:
<one sentence explanation>
"""

        response = llm.generate_content(prompt)

    st.success("Answer generated successfully")

    st.subheader("📌 Answer")
    st.markdown(response.text)

    with st.expander("📄 View Transcript Context"):
        st.text_area(
            "",
            context,
            height=300
        )

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Built using FAISS + Sentence Transformers + Gemini")