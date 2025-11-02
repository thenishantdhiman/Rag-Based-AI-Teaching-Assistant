import whisper
import json
import os

model = whisper.load_model("large-v2")

audios = os.listdir("audios")

for audio in audios:
    result = model.transcribe(audio = f"audios/{audio}", 
                              language="hi",
                              task="translate",
                              word_timestamps=False)
        
    chunks = []
    for segment in result["segments"]:
        chunks.append({ "start": segment["start"], "end": segment["end"], "text": segment["text"]})
        
    chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

    filename = os.path.splitext(audio)[0]
    
    with open(f"jsons/{filename}.json", "w") as f:
            json.dump(chunks_with_metadata,f)