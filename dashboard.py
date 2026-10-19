import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_FILE = "sales_data.csv"
OUTPUT_DIR = "visualizations"

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        df.columns = (
            df.columns.str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )
        print("Dataset loaded:", df.shape)
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df = load_data(DATA_FILE)

    if df is None:
        return

    print(df.head())
    print(df.describe(include="all"))

    candidates = [
        "total_sales", "sales", "revenue",
        "amount", "price"
    ]
    sales_column = next(
        (col for col in candidates if col in df.columns),
        None
    )

    if sales_column:
        plt.figure(figsize=(9, 5))
        sns.histplot(data=df, x=sales_column, kde=True)
        plt.title("Sales Distribution")
        plt.tight_layout()
        plt.savefig(
            os.path.join(OUTPUT_DIR, "sales_distribution.png"),
            dpi=150
        )
        plt.close()
        print("Sales distribution chart saved.")
    else:
        print("Sales column not identified.")
        print("Available columns:", df.columns.tolist())

if __name__ == "__main__":
    main()
