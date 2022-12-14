from fastapi import FastAPI
from danh_sach_bai_hat import searchSongByName, listSong
app = FastAPI()


@app.get("/api/song")
def findAll():

    result = listSong()
    return result


@app.get("/api/song/{song_name}")
async def findSong(song_name: str):
    result = searchSongByName(song_name)
    return result


