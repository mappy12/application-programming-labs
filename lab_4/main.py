import pandas as pd

def main():
    df = pd.read_csv("catsCsv")
    print(df.head())

if __name__ == "__main__":
    main()