from fastapi import FastAPI
import requests
from danh_sach_bai_hat import searchSongByName, listSong, songInfo

app = FastAPI()


@app.get("/api/songs")
def findAll():

    result = listSong()
    return result


@app.get("/api/song_link/{url_html:path}")
async def findSong(url_html: str):

    response = requests.get(url_html)
    result = songInfo(response)
    return result


@app.get("/api/songSearch/{song_name}")
async def findSong(song_name: str):
    result = searchSongByName(song_name)
    return result


@app.get("/api/song/listen/{song_name}")
def listenSong(song_name: str):
    result = listenSong(song_name)
    return result


