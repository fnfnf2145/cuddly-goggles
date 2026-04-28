def main():
    weather_filename = ""
    tavgs = read_tavgs(weather_filename)

    print(f"욘평균기온은{sum(tavgs)/len(tavgs)}")

    rainfalls = read


def read_rainfall(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        rainfalls = []
        for line in lines[1:]:
            tokens=line.split(",")
            print(tokens[4])
    return dataset