import os

import requests

# def main():
#     url = "https://www.jbnu.ac.kr/web/unvrslife/campuslife/cafeteria/dataAjax.do?type=day"
#
#     resp = requests.get(url)
#     resp.encoding = "UTF-8"
#     print(resp.text)

def main():
    year = 2022
    URL = "https://api.taegon.kr/stations/146/?sy=2022&ey=2022&format=csv"

    filename = f"weather_{year}.csv"

    if not os.path.exists(filename):
        resp = requests.get(URL)
        with open(filename, "w") as f:
            f.write(resp.text)

    else:
        print("이미 있습니다")

if __name__ == '__main__':
    main()
