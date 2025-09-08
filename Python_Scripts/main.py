import pandas as pd

def read():
    df = pd.read_excel(r"C:\Users\HP\Downloads\Financial Sample.xlsx")
    df.dropna(subset=["Discount Band"],inplace=True)
    return df.to_json(orient="records")

def main():
    return read()

if __name__ == "__main__":
    main()