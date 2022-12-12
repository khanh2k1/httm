from fastapi import FastAPI
from danh_sach_bai_hat import danh_sach_bai_hat
app = FastAPI()


@app.get("/api/song")
def findAll():

    result = danh_sach_bai_hat()
    return result
