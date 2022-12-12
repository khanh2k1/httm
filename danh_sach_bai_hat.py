
import requests
from bs4 import BeautifulSoup


def danh_sach_bai_hat():
    danh_sach = []

    for x in range(1, 2):
        response = requests.get('https://chiasenhac.vn/nhac-hot/vietnam.html?playlist=' + str(x))
        soup = BeautifulSoup(response.content, "html.parser")

        # link tai/nghe
        link = soup.select('.card-body')[4].select('.download_status > li > a')[1]['href']

        # ten bai hat
        temp = soup.select('body > section > div.container > div > div.col-md-9 > '
                           'div.d-flex.justify-content-between.mb-3.box1.music-listen-title > h1')[0].get_text()
        arr1 = temp.split('-')
        ten_bai_hat = arr1[0].strip()

        # ten ca si
        ten_ca_si = arr1[1].strip()

        # anh_bia
        anh_bia = soup.select('#companion_cover > img')[0]['src']

        # loi_bai_hat
        loi_bai_hat = soup.select('#fulllyric')[0].get_text()

        # print(link)
        # print(ten_bai_hat)
        # print(ten_ca_si)
        # print(anh_bia)
        # print(loi_bai_hat)

        # convert to JSON string

        song_dic = {
            "link": link,
            "ten_ca_si": ten_ca_si,
            "ten_bai_hat": ten_bai_hat,
            "anh_bia": anh_bia,
            "loi_bai_hat": loi_bai_hat
        }

        # bai_hat = Bai_hat(ten_bai_hat, anh_bia, ten_ca_si, loi_bai_hat, link)
        # # default encoding to utf-8
        # jsonStr = json.dumps(bai_hat.__dict__, ensure_ascii=False).encode('utf-8')
        # string_utf = jsonStr.decode()
        # # indent=4, separators=(".", " = ")

        # json_object = json.dumps(song_dic, ensure_ascii=False).encode('utf-8')
        # string_utf = json_object.decode()
        danh_sach.append(song_dic)

    return danh_sach
