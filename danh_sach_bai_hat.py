import requests
from bs4 import BeautifulSoup


def songInfo(response):
    soup = BeautifulSoup(response.content, "html.parser")

    # link tai/nghe
    link = soup.select('#pills-download > div > div.card-body > div > div.col-12.tab_download_music > ul > '
                       'li:nth-child(2) > a')[0]['href']

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

    song_dic = {
        "title": ten_bai_hat,
        "singer": ten_ca_si,
        "img_cover": anh_bia,
        "urlSong": link,
        "lyric": loi_bai_hat
    }

    return song_dic


def listSong():
    result = []
    # lay ra 10 bai hat
    for x in range(1, 21):
        url = 'https://chiasenhac.vn/nhac-hot/vietnam.html?playlist='
        response = requests.get(f'{url}' + str(x))
        # them link html
        result.append(songInfo(response))

    return result


# hien thi cac bai hat theo song_search
def searchSongByName(song_search):
    # lay ra 5 link html
    # links_html = [5]
    result = []
    response = requests.get(f'https://chiasenhac.vn/tim-kiem?q={song_search}')
    soup = BeautifulSoup(response.content, "html.parser")
    for i in range(1, 6):
        link_html = soup.select(f'#nav-all > ul > li:nth-child({i}) > .media-left.align-items-stretch.mr-2 > a')[0][
            'href']
        # them link html va tra ve inspect
        title = soup.select(f'#nav-all > ul > li:nth-child({i}) > .media-left.align-items-stretch.mr-2 > a')[0][
            'title']
        image = soup.select(f'#nav-all > ul > li:nth-child({i}) > .media-left.align-items-stretch.mr-2 > a > img')[0][
            'src']

        author = soup.select(f'#nav-all > ul > li:nth-child({i}) > .media-body.align-items-stretch.d-flex.flex-column'
                             f'.justify-content-between.p-0 > div > div')[0].get_text()

        song = {
            "link_html": link_html,
            "title": title,
            "image": image,
            "author": author
        }

        result.append(song)

    return result


print(searchSongByName("waiting"))
