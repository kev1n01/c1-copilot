from fastapi import FastAPI

app = FastAPI()

# endpoint to save data to db
@app.post("/save-data")
def save_data_to_db():
    #load controller documents

    #split data into chunks
    
    #convert data into embeddings

    #store embeddings in db
    return {"save"}

# endpoint to retrieve data from db
@app.post("/retrieval")
def retrieve_data_from_db():
    #get question to user

    #get retrieve data to db

    #build the prompt

    #ask the LLM

    #get answer from LLM
    return {"response"}

# endpoint to convert text to speech
@app.post("/text-to-speech")
def text_to_speech():
    return {"speech AUD"}