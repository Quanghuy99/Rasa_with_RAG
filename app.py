import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi import FastAPI, UploadFile, Form, File
import requests
import time

app = FastAPI()

numberrequest = 0
@app.post('/llm')
async def post(InputText: str = Form(None),
                IdRequest: str = Form(...),
                NameBot: str = Form(...),
                User: str = Form(...),
                Image: str = Form(None),
                Voice: UploadFile = File(None)):
    start_time = time.time()
    global numberrequest
    numberrequest = numberrequest + 1
    print("numberrequest", numberrequest)
    results = {
    "products" : [],
    "terms" : [],
    "content" : "",
    "status" : 200,
    "message": "",
    "time_processing":''
    }
    message_data = '''InputText:{},IdRequest:{},NameBot:{},User:{}'''.format(InputText,IdRequest,NameBot,User)
    
    # Ban len rasa
    print(message_data)
    r = requests.post('http://127.0.0.1:5005/webhooks/rest/webhook', json={"sender": "test", "message": message_data})
    
    # print('r:',r.json())
    results['content'] = r.json()[0]["text"]
    
    return results['content']

uvicorn.run(app, host="0.0.0.0", port=8002)