# OpenMindAI 🧠🤖 <!-- omit from toc -->

---

**PROJECT:** **OpenMindAI**  
**VERSION:** _**`AXYS`**_  
**DESCRIPTION:** Automated Teachable Chatbot AI for Intelligent Conversation  
**UPDATED:** 10-28-2023

---

## Contents <!-- omit from toc -->

- [Introduction](#introduction)
- [💾 Dependencies](#-dependencies)
  - [🤖🎓 AutoGen](#-autogen)
  - [🤖💬 OpenAI](#-openai)
  - [💾👨‍💻 SQLite](#-sqlite)
  - [🔁💬 SentenceTransformers](#-sentencetransformers)
- [🧩🐍 Modules](#-modules)
  - [Root Directory](#root-directory)
    - [🐍 `/main.py`](#-mainpy)
  - [📁 `/agents` Subfolder](#-agents-subfolder)
    - [🐍 `/agents/agent_manager.py`](#-agentsagent_managerpy)
    - [🐍 `/agents/conversable_agent.py`](#-agentsconversable_agentpy)
    - [🐍 `/agents/teachable_agent.py`](#-agentsteachable_agentpy)
    - [🐍 `/agents/text_analyzer_agent.py`](#-agentstext_analyzer_agentpy)
  - [📁 `/db` Subfolder](#-db-subfolder)
    - [🐍 `/db/database.py`](#-dbdatabasepy)
    - [`/db/app.db`](#dbappdb)
  - [📁 `/logs` Subfolder](#-logs-subfolder)
    - [`/logs/app.log`](#logsapplog)
    - [📁 `/ops` Subfolder](#-ops-subfolder)
  - [🐍 `/ops/chat_manager.py`](#-opschat_managerpy)
  - [🐍 `/ops/config.py`](#-opsconfigpy)
- [🧩 Structure](#-structure)
  - [📁🌳 Directory Tree Diagram](#-directory-tree-diagram)
- [📝 Changelog](#-changelog)
  - [10-29-2023: Updates](#10-29-2023-updates)
  - [10-28-2023: Updates](#10-28-2023-updates)
    - [Dev Session 5](#dev-session-5)
    - [Dev Session 4](#dev-session-4)
    - [Dev Session 3](#dev-session-3)
    - [Dev Session 2](#dev-session-2)
    - [Dev Session 1](#dev-session-1)
  - [10-27-2023: Updates](#10-27-2023-updates)
    - [10-27-2023: Created](#10-27-2023-created)
    - [10-27-2023: Added](#10-27-2023-added)
    - [10-27-2023: Modified](#10-27-2023-modified)
    - [10-27-2023: Fixed](#10-27-2023-fixed)

---

## Introduction

**OpenMindAI 🧠🤖 (`AXYS`)** is an advanced, teachable artificial intelligence (AI) designed to simulate intelligent and contextual conversations with users. Built upon GPT-4 architecture, it is capable of understanding natural language queries, providing coherent and contextually relevant responses, and learning from user feedback. The chatbot leverages advanced natural language processing techniques, utilizing GPT-4 based models for conversation and a Sentence Transformer model for semantic search in an SQLite database.

The project is modular, consisting of separate components for database operations, logging, configuration, and chat management. This modular approach makes the codebase scalable, maintainable, and easy to understand.

---

## 💾 Dependencies

- 🤖🎓 AutoGen SDK
- 🤖💬 OpenAI API
- 💾👨‍💻 SQLite database
- 🔁💬 SentenceTransformers

---

### 🤖🎓 AutoGen

AXYS leverages the **AutoGen SDK** for agent abilities, classes, utilities, etc.

---

### 🤖💬 OpenAI

AXYS relies on the **OpenAI API**, especially to utilize the `gpt-3.5-turbo`, `gpt-3.5-turbo-16k`, and `gpt-4` language model (LLMs).

---

### 💾👨‍💻 SQLite

AXYS uses a **SQLite database**. The database is located at `/db/axys.db` and database operations are managed by the `db/database.py` file.

---

### 🔁💬 SentenceTransformers

AXYS uses the **`SentenceTransformers` tool** for database embeddings.

---

## 🧩🐍 Modules

**OpenMindAI (`AXYS`)** is initiated by the `main.py` file in the root directory, but the project's code is split into several Python modules. A brief description of each module is provided below.

### Root Directory

#### 🐍 `/main.py`

The main application file that initializes and runs the chatbot.

---

### 📁 `/agents` Subfolder

#### 🐍 `/agents/agent_manager.py`

Centralized file that manages the `ConversableAgent`, `TeachableAgent`, and `TextAnalyzerAgent` classes which handle chat functionalities and learning capabilities. These classes are now organized into separate modules under the `/agents` subfolder for better modularity and ease of maintenance.

---

#### 🐍 `/agents/conversable_agent.py`

Contains the AutoGen `ConversableAgent` class which handles basic chat functionalities.

---

#### 🐍 `/agents/teachable_agent.py`

Contains the AutoGen `TeachableAgent` class which extends the functionalities of `ConversableAgent` with learning capabilities.

---

#### 🐍 `/agents/text_analyzer_agent.py`

Contains the AutoGen `TextAnalyzerAgent` class which provides text analysis functionalities.

---

### 📁 `/db` Subfolder

#### 🐍 `/db/database.py`

Handles database operations, including memo storage and retrieval.

---

#### `/db/app.db`

The SQLite database file where memos are stored.

---

### 📁 `/logs` Subfolder

#### `/logs/app.log`

The log file where debug and info statements are saved.

---

#### 📁 `/ops` Subfolder

The `/ops` directory contains these core files:

- `chat_manager.py`
- `config.py`

It only contains configuration files with private API keys, including an `.env` file and a specific `OAI_CONFIG_LIST.json` file.

---

### 🐍 `/ops/chat_manager.py`

Manages the chat functionalities specifically for a `TeachableAgent`.

---

### 🐍 `/ops/config.py`

Handles configuration and logging settings. Pulls API keys and LLM config settings from `/ops/OAI_CONFIG_LIST.json`. As a backup, it can pull API keys using environment variables using an `.env` file in the same folder.

---

## 🧩 Structure

### 📁🌳 Directory Tree Diagram

The following diagram represents the current project directory structure.

```txt
Root
├── main.py
├── README.md
├── agents
│   ├── agent_manager.py
│   ├── conversable_agent.py
│   ├── teachable_agent.py
│   └── text_analyzer_agent.py
├── db
│   ├── database.py
│   └── app.db
├── docs
│   ├── _archive
|   │   └── {old project files}
│   ├── autogen
|   │   └── {AutoGen documentation files}
│   ├── chatgpt_custom_instructions.yml
│   └── prompts.md
├── logs
│   └── app.log
└── ops
    ├── .env
    ├── chat_manager.py
    ├── config.py
    └── OAI_CONFIG_LIST.json
```

---

## 📝 Changelog

_The following is a record of changes, updates improvements, bug fixes, etc._

---

### 10-29-2023: Updates

- Renamed `/agent` subfolder to **`/agents`**
- Renamed `agent.py` to **`agent_manager.py`**

### 10-28-2023: Updates

#### Dev Session 5

**ChatGPT-4:** "These updates integrate the various agent modules into a single, unified AI personality and streamline the user interaction process through the `ChatManager`."

**`main.py` Updates:**

- Replaced individual agent initializations with `AgentManager` class.
- Used `AgentManager` for initializing `ChatManager`.

**`agent/agent.py` Updates:**

- Added `AgentManager` class to manage `ConversableAgent`, `TeachableAgent`, and `TextAnalyzerAgent`.

**`ops/chat_manager.py` Updates:**

- Updated constructor to take an `AgentManager` object instead of a `TeachableAgent`.
- Added `handle_user_input()` method to process user input through all three agent modules.

#### Dev Session 4

- Modified `teachable_agent.py` to correct indentation and import the logger and config settings appropriately.
- Updated `conversable_agent.py` to correct the import statement and added logger and config imports.
- Added logger and config imports to `text_analyzer_agent.py`.
- Verified that `agent.py` is correctly managing all agent classes.
- Updated the `ChatManager` class in `/ops/chat_manager.py` to include methods for managing the interaction between the `ConversableAgent`, `TeachableAgent`, and `TextAnalyzerAgent`.
- Added a `handle_user_input` method to the `ChatManager` class to centralize processing of user input through the different agents.
- Modified the `ChatManager` constructor to accept an `AgentManager` instance instead of just a `TeachableAgent`.
- Updated the `start_chat` method in `ChatManager` to initiate a terminal-based chat loop.

#### Dev Session 3

**Files Updated:**

- `/agent/teachable_agent.py`
- `/ops/config.py`

**Updates to `teachable_agent.py`:**

- Added `start_chat` method: Introduced a method to integrate the `TeachableAgent` with the `ChatManager` for initiating a chat session.

**Updates to `chat_manager.py`:**

- `start_chat` method: Modified to initialize and update the `chat_history` of the `TeachableAgent` during the chat session.

**Update summary:**

- The updates primarily focus on ensuring seamless integration between the `TeachableAgent` and the `ChatManager`. Specifically, a new method `start_chat` was added to the `TeachableAgent` class to initiate a chat session via the `ChatManager`. Additionally, the `ChatManager`'s `start_chat` method was updated to manage the chat history of the `TeachableAgent`.

#### Dev Session 2

- Aligned `ConversableAgent`, `TeachableAgent`, and `TextAnalyzerAgent` classes with AutoGen documentation for better compliance and leveraging SDK functionalities.
- Moved `ConversableAgent`, `TeachableAgent`, and `TextAnalyzerAgent` classes to separate modules under the `/agent` subfolder for better modularity and ease of maintenance.
- Created a centralized `/agent/agent.py` file to manage the three agent class modules.
- Various bug fixes and optimizations.

#### Dev Session 1

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

### 10-27-2023: Updates

#### 10-27-2023: Created

- Created first version of OpenMindAI code (**_v.`AXYS`_**).
- Created `axys.py` file as the main entry point for the application.
- Introduced `ConversableAgent` and `TeachableAgent` classes to `axys.py`.

#### 10-27-2023: Added

- Added `database.py` for SQLite database operations, including a `MemoStore` class for memory storage and retrieval.
- Created `config.py` for configuration and logging setup.
- Implemented a chat manager module (`chat_manager.py`) to handle chat functionalities.

#### 10-27-2023: Modified

- Enhanced error handling across modules.
- Improved logging by adopting the DEBUG level and adding timestamps.

#### 10-27-2023: Fixed

- Resolved path issues for the SQLite database in `database.py`.
- Corrected error messages for better debugging.

---

> ⚠️ **END OF README FILE.** ⚠️

---
