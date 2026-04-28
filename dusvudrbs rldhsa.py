def main():
    weather_filename = "weather(146)_2022-2022.csv"
    tavgs = read_tavgs(weather_filename)

    print(f"욘평균기온은{sum(tavgs)/len(tavgs)}")

    rainfalls = read






def read_rainfall(weather_filename):
    rainfalls = []
    with open(weather_filename, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            rainfalls.append(float(tokens[4]))  # 강수량 위치 (예: 4번 인덱스)
    return rainfalls


def main():
    weather_filename = "weather(146)_2022-2022.csv"

    tavgs = read_tavgs(weather_filename)
    print(f"연평균 기온은 {sum(tavgs)/len(tavgs):.2f}")

    rainfalls = read_rainfall(weather_filename)
    print(f"총 강수량은 {sum(rainfalls):.2f}")


if __name__ == "__main__":
    main()