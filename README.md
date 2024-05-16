# HomeLabPi
A Sandbox run on a cluster of Raspberry Pis!
This project aims to create an integrated system that records and transcribes audio from a Discord channel, stores the transcriptions, and allows users to query the transcriptions using an AI/LLM backend. The system is designed to be lightweight and run efficiently on a Raspberry Pi cluster. Here’s a breakdown of each service and the technologies used:

1. Discord Bot(aka front end): Python, discord.py
Functionality: The bot joins a Discord voice channel, records audio from the channel, saves the audio files, and interacts with users to handle commands and queries.
Key Tasks:
Recording audio from Discord channels.
Saving audio files to the local filesystem.
Handling user commands for transcriptions and queries.
2. Transcription Service: Vosk (Python)
Functionality: Converts recorded audio files into text transcriptions.
Key Tasks:
Receiving audio files from the Discord bot.
Using Vosk to transcribe the audio files into text.
Storing the transcriptions in the SQLite database.
3. Storage
Technology: Local Filesystem
Functionality: Stores the audio files recorded by the Discord bot.
Key Tasks:
Persistently storing audio files on the local filesystem for transcription.
4. Database: SQLite
Functionality: Stores transcriptions and user queries.
Key Tasks:
Storing text transcriptions of audio files.
Storing user queries and corresponding AI-generated responses.
Providing efficient retrieval of transcriptions and query responses.
5. Backend AI/LLM Service: Python, Flask (or another web framework), possibly DistilBERT as a LLM
Functionality: Processes user queries, retrieves relevant transcriptions from the database, and generates responses using a language model.
Key Tasks:
Handling HTTP requests for user queries.
Interacting with the SQLite database to fetch transcriptions.
Using an AI/LLM model (like LLaMA or GPT) to generate responses based on transcriptions.
Sending responses back to the Discord bot or frontend interface.

Data Flow and Interaction
Recording:
The Discord bot records audio from the voice channel and saves it to the local filesystem.
Transcription:
The Transcription Service retrieves audio files from the local filesystem.
Vosk transcribes the audio into text.
The transcription is stored in the SQLite database.
User Queries:
Users can interact with the Discord bot to query the stored transcriptions.
The Backend AI/LLM Service processes the query, retrieves relevant transcriptions from SQLite, and generates a response.
The response is sent back to the user via the Discord bot.
Summary
This project integrates several components to provide a seamless experience for recording, transcribing, and querying audio from a Discord channel. Each component is designed to be lightweight and efficient, suitable for running on a Raspberry Pi 5 cluster. The technologies used include Python, discord.py, Vosk, SQLite, and a Flask-based AI/LLM backend service. This setup ensures robust functionality while maintaining simplicity and efficiency, making it ideal for small-scale deployments and learning environments.