# OpenMindAI <!-- omit from toc -->

**VERSION:** _**`AXYS`**_  
**DESCRIPTION:** Automated Teachable Chatbot AI for Intelligent Conversation  
**UPDATED:** 10-28-2023

---

## Table of Contents <!-- omit from toc -->

- [Introduction](#introduction)
- [Dependencies](#dependencies)
  - [AutoGen](#autogen)
  - [OpenAI](#openai)
  - [SQLite](#sqlite)
  - [SentenceTransformers](#sentencetransformers)
- [Modules](#modules)
  - [`/main.py`](#mainpy)
  - [`/agent/agent.py`](#agentagentpy)
  - [`/db/database.py`](#dbdatabasepy)
  - [`/db/app.db`](#dbappdb)
  - [`/logs/app.log`](#logsapplog)
  - [`/ops/chat_manager.py`](#opschat_managerpy)
  - [`/ops/config.py`](#opsconfigpy)
- [Structure](#structure)
  - [Directory Structure](#directory-structure)
- [Changelog](#changelog)
  - [10-28-2023](#10-28-2023)
    - [Updated](#updated)
  - [10-27-2023](#10-27-2023)
    - [Created](#created)
    - [Added](#added)
    - [Modified](#modified)
    - [Fixed](#fixed)

---

## Introduction

AgentChat AXYS is an advanced, teachable artificial intelligence (AI) designed to simulate intelligent and contextual conversations with users. Built upon GPT-4 architecture, it is capable of understanding natural language queries, providing coherent and contextually relevant responses, and learning from user feedback. The chatbot leverages advanced natural language processing techniques, utilizing GPT-4 based models for conversation and a Sentence Transformer model for semantic search in an SQLite database.

The project is modular, consisting of separate components for database operations, logging, configuration, and chat management. This modular approach makes the codebase scalable, maintainable, and easy to understand.

---

## Dependencies

- AutoGen SDK
- OpenAI API
- SQLite database
- SentenceTransformers

---

### AutoGen

AXYS leverages the **AutoGen SDK** for agent abilities, classes, utilities, etc.

---

### OpenAI

AXYS relies on the **OpenAI API**, especially to utilize the `gpt-3.5-turbo`, `gpt-3.5-turbo-16k`, and `gpt-4` language model (LLMs).

---

### SQLite

AXYS uses a **SQLite database**. The database is located at `/db/axys.db` and database operations are managed by the `db/database.py` file.

---

### SentenceTransformers

AXYS uses the **`SentenceTransformers` tool** for database embeddings.

---

## Modules

### `/main.py`

The main application file that initializes and runs the chatbot.

---

### `/agent/agent.py`

Contains the `ConversableAgent` and `TeachableAgent` classes, which handle the chat functionalities and learning capabilities.

---

### `/db/database.py`

Handles database operations, including memo storage and retrieval.

---

### `/db/app.db`

The SQLite database file where memos are stored.

---

### `/logs/app.log`

The log file where debug and info statements are saved.

---

### `/ops/chat_manager.py`

Manages the chat functionalities specifically for a `TeachableAgent`.

---

### `/ops/config.py`

Handles configuration and logging settings. Pulls API keys and LLM config settings from `/ops/OAI_CONFIG_LIST.json`.

---

## Structure

### Directory Structure

```txt
Root
├── main.py
├── README.md
├── agent
│   └── agent.py
├── db
│   ├── database.py
│   └── app.db
├── docs
│   ├── _archive
|   │   └── {old project files}
│   ├── autogen
|   │   └── {AutoGen documentation files}
│   └── chatgpt_custom_instructions.yml
├── logs
│   └── app.log
└── ops
    ├── .env
    ├── chat_manager.py
    ├── config.py
    └── OAI_CONFIG_LIST.json
```

---

## Changelog

_The following is a record of changes, updates improvements, bug fixes, etc._

---

### 10-28-2023

#### Updated

- Moved `ConversableAgent` and `TeachableAgent` classes from `/axys.py` to new `/agent.py` module.
- Introduced `/chat_manager.py` to manage chat functionalities for `TeachableAgent`.
- Updated logging to follow project guidelines.
- Various bug fixes and optimizations.
- Modules renamed & reorganized:
  - `/axys.py` renamed to `/main.py`
  - `/db/axys.db` renamed to `/db/app.db`
  - `/logs/axys.log` renamed to `/logs/app.log`
  - `/chat_manager.py` file moved to `/ops` folder: `/ops/chat_manager.py`
  - `/agent.py` file moved to new `/agent` folder: `/agent/agent.py`
- Updated files so imports reflect new locations

---

### 10-27-2023

#### Created

- Created first version of TeachableAI (AXYS) code.
- Created `axys.py` file as the main entry point for the application.
- Introduced `ConversableAgent` and `TeachableAgent` classes to `axys.py`.

#### Added

- Added `database.py` for SQLite database operations, including a `MemoStore` class for memory storage and retrieval.
- Created `config.py` for configuration and logging setup.
- Implemented a chat manager module (`chat_manager.py`) to handle chat functionalities.

#### Modified

- Enhanced error handling across modules.
- Improved logging by adopting the DEBUG level and adding timestamps.

#### Fixed

- Resolved path issues for the SQLite database in `database.py`.
- Corrected error messages for better debugging.

---
