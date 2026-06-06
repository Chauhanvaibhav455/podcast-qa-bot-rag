# 🎙️ Podcast Q&A Bot - Sportomic AI Lab Assignment

## Overview

Podcast Q&A Bot is an AI-powered Retrieval-Augmented Generation (RAG) system that answers questions from the Elon Musk × Nikhil Kamath podcast and returns the most relevant timestamp discussed in the video.

The system extracts YouTube subtitles, converts them into searchable embeddings, stores them in a FAISS vector database, retrieves relevant transcript sections, and generates contextual answers using Google's Gemini 2.5 Flash model.

---

## Problem Statement

Build an intelligent podcast assistant capable of:

* Understanding podcast content
* Answering user questions
* Returning relevant timestamps
* Providing source transcript context

Example:

Question:
What does Elon think about AI?

Answer:
Elon believes AI will significantly improve productivity and transform multiple industries, while emphasizing the importance of safety and regulation.

Timestamp:
01:14:52

---

## Features

* Transcript extraction from YouTube
* Automatic subtitle processing
* Semantic search using vector embeddings
* FAISS vector database
* Gemini-powered answer generation
* Timestamp retrieval
* Interactive Streamlit UI

---

## Tech Stack

### AI & NLP

* Sentence Transformers
* Gemini 2.5 Flash
* FAISS Vector Database

### Backend

* Python

### Frontend

* Streamlit

### Data Processing

* yt-dlp
* VTT Subtitle Processing

---

## Project Workflow

1. Extract subtitles from YouTube using yt-dlp
2. Clean VTT transcript data
3. Generate embeddings using Sentence Transformers
4. Store embeddings in FAISS
5. Accept user query
6. Perform semantic similarity search
7. Retrieve relevant transcript chunks
8. Generate answer using Gemini
9. Return answer with timestamp

---

## Folder Structure

project/

├── app.py

├── ingest.py

├── clean_vtt.py

├── transcript.txt

├── podcast.index

├── chunks.pkl

├── requirements.txt

└── README.md

---

## Sample Questions

* What does Elon think about AI?
* How should AI be regulated?
* What advice does Elon give entrepreneurs?
* What is the future of AI?
* Where would Elon invest?

---

## Limitations

* Auto-generated subtitles may contain transcription errors.
* Retrieval quality depends on chunk size.
* Some answers may require larger context windows.
* Timestamp accuracy depends on subtitle alignment.
* Semantic retrieval may occasionally return adjacent topics.

---

## Future Improvements

* Clickable YouTube timestamp links
* Conversation memory
* Multi-podcast support
* Confidence scoring
* Speaker identification
* Advanced reranking

---

## Author

Vaibhav Chauhan

Sportomic AI Lab Internship Assignment
