**How to Use the RAG AI Teaching Assistant**

**Step 1** : Add Your Videos

Place all your video files inside the videos/ folder.

**Step 2** : Extract Audio

Run mp4tomp3 to convert videos into MP3 files.

**Step 3** : Generate Transcripts

Run mp3tojson to create JSON transcripts from the MP3 files.

**Step 4** : Create Embeddings

Use preprocessjson to generate embeddings and save them as a .joblib file.

**Step 5** : Query the Assistant

Load the .joblib file, create prompts based on user queries, and feed them to the LLM for context-aware responses.
