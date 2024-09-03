from fastapi import APIRouter, Request, Form
from typing import Dict, Any

from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from yt_summarizer import summarize, download_as_text, delete_files_in_directory
import os
from pathlib import Path


app = APIRouter()
templates = Jinja2Templates(directory="templates/html")


@app.get('/home', response_class=HTMLResponse)
def main(request: Request):
    
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/bg_process') 
def bg_process(request: Request, yt_url: str = Form(...)):
    # t1 = threading.Thread(target=summarize,  args=(yt_url, request))
    # t1.start()
    data = summarize(yt_url)
    download_as_text(data['actual_text'], data['summarized_text'][0]['summary_text'])
    
    remove_wav = str(Path.cwd() / 'ytaudio.wav')
    remove_mp4 = str(Path.cwd() / 'ytaudio.mp4')
    os.remove(remove_wav)
    os.remove(remove_mp4)
    delete_files_in_directory(str(Path.cwd() / 'content'))
    return templates.TemplateResponse('summarizer.html', 
                                      {'request': request, 'act_text': data['actual_text'], 'summarized': data['summarized_text']})

