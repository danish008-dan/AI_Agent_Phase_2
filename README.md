# Multilingual AI Agent (Groq Powered)

A fast, memory-enabled multilingual AI assistant built using the Groq API.  
This AI automatically responds in the same language as the user (English, Hindi, or Hinglish) and maintains conversation memory for contextual understanding.

---

## Project Overview

This module is part of Phase Two of the AI system architecture.

It contains:

1. AI Response Engine – Handles communication with Groq LLM.
2. System Prompt Configuration – Controls AI personality and multilingual behavior.

The system is designed to:
- Maintain conversation memory
- Follow strict language rules
- Generate fast and contextual responses
- Provide clean and structured AI outputs

---

## File 1: AI Response Engine

### File Purpose

This file connects your application to the Groq LLM API and generates responses using:

- System Prompt
- Conversation Memory
- Model Configuration

---

### Core Function

generate_ai_response(user_message)

#### What It Does:

1. Stores the user message in memory
2. Adds system prompt
3. Loads conversation history
4. Sends everything to Groq API
5. Receives AI response
6. Saves AI response to memory
7. Returns the response

---

### How It Works (Step-by-Step)

#### 1. Import Dependencies

- groq → For interacting with Groq LLM
- settings → Loads API key and model configuration
- system_prompt → Defines AI behavior rules
- conversation_memory → Handles chat history

#### 2. Initialize Groq Client

client = Groq(api_key=GROQ_API_KEY)

Creates authenticated connection to Groq servers.

---

#### 3. Memory Handling

Before sending the request:
add_to_memory("user", user_message)

After receiving response:
add_to_memory("assistant", response)

This ensures contextual conversation.

---

#### 4. API Call

client.chat.completions.create(...)

Parameters used:

- model → LLM model name
- messages → System + memory + user
- temperature → Creativity level
- max_tokens → Response length limit
- top_p → Sampling control

---

#### 5. Error Handling

If anything fails, the system safely returns:

"Sorry, something went wrong while generating response."

---

## File 2: Multilingual System Prompt

### File Purpose

Defines AI behavior and response rules.

---

### System Prompt Content

The AI is instructed to:

1. Respond in the same language used by the user.
2. If the user speaks English → respond in English.
3. If the user speaks Hindi → respond in Hindi.
4. If the user mixes Hindi and English → respond in Hinglish.
5. Keep responses clear and helpful.
6. Be concise but informative.

---

### Why This Is Important

Without system prompts:
- AI may change language unexpectedly
- Tone may be inconsistent
- Responses may become verbose or unfocused

This prompt ensures:
- Speed
- Consistency
- Multilingual intelligence
- Clear instructions

---

## Project Architecture (Phase Two)

phase_two/
│
├── config/
│   └── settings.py
│
├── brain/
│   └── system_prompt.py
│
├── memory/
│   └── conversation_memory.py
│
└── ai_engine.py

---

## Installation Guide

### 1. Install Dependencies

pip install groq

---

### 2. Add Your API Key

Inside settings.py:

GROQ_API_KEY = "your_api_key_here"

---

### 3. Example Usage

response = generate_ai_response("Hello AI")
print(response)

---

## Features

- Fast Groq inference
- Context-aware responses
- Conversation memory
- Multilingual intelligence
- Configurable temperature and tokens
- Clean modular architecture
- Error handling

---

## Why This Architecture Is Good

- Separation of concerns
- Scalable structure
- Modular design
- Easy integration with UI
- Centralized AI behavior control

---

## Future Improvements

- Persistent database memory (MongoDB / PostgreSQL)
- User-based memory profiles
- Streaming responses
- Voice input/output integration
- Emotion detection
- Personality switching modes
- Token usage tracking
- Logging and monitoring system

---

## Use Case Examples

- Personal AI assistant
- Multilingual chatbot
- Website chatbot
- Desktop assistant
- Customer support bot
- Voice AI system

---

## License

This project is for educational and development purposes.
