# 🎙️ Podcast Q&A Bot

AI-powered Retrieval-Augmented Generation (RAG) system that answers questions from podcast transcripts and returns relevant timestamps using semantic vector search and Google's Gemini 2.5 Flash.

## 🚀 Overview

Podcast Q&A Bot enables users to interact with long-form podcast content through natural language queries. Instead of manually searching through hours of audio, users can ask questions and instantly receive contextual answers along with the most relevant timestamp.

The system extracts YouTube subtitles, converts transcript chunks into vector embeddings, stores them in a FAISS vector database, retrieves semantically relevant content, and uses Gemini 2.5 Flash to generate grounded responses.

---

## 🏗️ System Architecture

![Architecture](assets/architecture_modern.png)

---

## 📱 Application Demo

![Application](assets/app_screenshot.png)

---

## ✨ Features

* Semantic search using FAISS
* Retrieval-Augmented Generation (RAG)
* Sentence Transformer embeddings
* Gemini 2.5 Flash integration
* Timestamp-aware question answering
* Transcript-based answer grounding
* Interactive Streamlit interface

---

## 🛠️ Tech Stack

| Component             | Technology            |
| --------------------- | --------------------- |
| Programming Language  | Python 3.14           |
| Frontend              | Streamlit             |
| Embeddings            | Sentence Transformers |
| Vector Database       | FAISS                 |
| LLM                   | Gemini 2.5 Flash      |
| Transcript Extraction | yt-dlp                |
| Storage               | Pickle                |

---

## 🔄 Workflow

1. Extract subtitles from YouTube using yt-dlp
2. Clean and preprocess transcript data
3. Generate embeddings using Sentence Transformers
4. Store embeddings in FAISS
5. Accept user query
6. Perform semantic retrieval
7. Retrieve relevant transcript chunks
8. Generate answer using Gemini
9. Return answer with timestamp

---

## 📂 Project Structure

```text
podcast-qa-bot-rag/

├── app.py
├── ingest.py
├── clean_vtt.py
├── transcript.txt
├── podcast.index
├── chunks.pkl
├── requirements.txt
├── README.md

├── assets/
│   ├── architecture_modern.png
│   └── app_screenshot.png

└── docs/
    └── project_report.pdf
```

---

## 💬 Sample Questions

* What does Elon think about AI?
* How should AI be regulated?
* What advice does Elon give entrepreneurs?
* What is the future of AI?
* Where would Elon invest?

---

## ⚠️ Limitations

* Auto-generated subtitles may contain transcription errors.
* Retrieval quality depends on transcript chunking.
* Some questions require larger context windows.
* Timestamp accuracy depends on subtitle alignment.
* Semantic retrieval may occasionally retrieve adjacent topics.

---

## 🔮 Future Improvements

* Multi-podcast support
* Clickable YouTube timestamp links
* Speaker identification
* Confidence scoring
* Conversation memory
* Hybrid retrieval (Keyword + Semantic)
* Cloud deployment

---

## 📄 Documentation

Project Report:

```text
docs/project_report.pdf
```

---

## 👨‍💻 Author

**Vaibhav Chauhan**

Sportomic AI Lab Internship Assignment

