from src.main import ParseData
from src.Price import kwh_price

if __name__ == "__main__":
    p = ParseData()
    p.parseData(
        "https://hgy780tcj2.execute-api.eu-central-1.amazonaws.com/dev/data",
        "interviewee",
        "muchpassword")
    # time = kwh_price.kWhPrice(False,13544,0.85,45,"start","ew","sa")
    # print(time.getComplex())
    # print(time.getkWhPrice())
