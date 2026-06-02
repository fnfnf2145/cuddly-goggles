import os

import requests

import pandas as pd


def download_weather(weather_filename, sy, ey):
    URL = f"https://api.taegon.kr/stations/146/?sy={sy}&ey={ey}&format=csv"

    if not os.path.exists(weather_filename):
        resp = requests.get(URL)
        with open(weather_filename, "w") as f:
            f.write(resp.text)

    else:
        print("이미 있습니다")
#
# def main():
#     sy=1980
#     ey=2024
#     weather_filename = f"weather_data_{sy}-{ey}.csv"
#     download_weather(weather_filename, sy, ey)
#
# if __name__ == '__main__':
#     main()


def main():
    filename = "weather_data_1980-2024.csv"
    download_weather(filename, 1980 , 2024)
    download_weather(filename_sw, 1980, 2024)

    df = pd.read_csv(filename, skipinitialspace=True)
    print(df.head())

    print(df[df["year"] == 2015]["rainfall"]. sum())
    print(df[df["year"] == 2022]["tavg"]. max())
    df["tdiff"] = df["tmax"] - df["tmin"]
    print(df[df["year"] == 2024]["tdiff"].sum())

    df_sw = pd.read_csv(filename_sw.csv, skiprows=ture)
    prec_jj = df[df["year"] == 2015]["rainfall"]. sum()
    prec_sw = df[df["year"] == 2015]["rainfall"]. sum()
if __name__ == "__main__":
    main()



