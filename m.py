import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#File path
INPUT_FILE = "mobile_phone_prices.csv"
OUTPUT_DIR = "mobile_outputs"
FIG_DIR = os.path.join(OUTPUT_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)


#1.Data Collection
def load_data(file_path):
    #Load dataset from CSV.
    print("Step 1: Data Collection")
    df = pd.read_csv(file_path)
    print(df.head(), "\n")
    return df

#2.Data Clenning
def clean_data(df):
    #Remove duplicates and handle missing values.
    print("Step 2: Data Cleaning")
    df.drop_duplicates(inplace=True)
    df.fillna({
        "Price": df["Price"].median(),
        "Storage_GB": df["Storage_GB"].mode()[0],
        "RAM_GB": df["RAM_GB"].mode()[0]
    }, inplace=True)
    print("Cleaned Data Preview:\n", df.head(), "\n")
    return df

#3.Data analyzing
def analyze_data(df):
    #Perform basic data analysis.
    print("Step 3: Data Analysis")

    print("\nSummary Statistics:")
    print(df.describe())

    avg_price = df.groupby("Brand")["Price"].mean()
    print("\nAverage Price by Brand:\n", avg_price)

    avg_ram = df.groupby("Brand")["RAM_GB"].mean()
    print("\nAverage RAM by Brand:\n", avg_ram)

    return avg_price, avg_ram

#Save data
def save_cleaned_data(df, output_path):
    #Save the cleaned dataset to CSV.
    df.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to {output_path}\n")


#4.Data Visualization
def visualize_data(df, avg_price):
    #Create and save different visualizations.
    print("Step 4: Data Visualization")

    # Price Distribution
    plt.figure()
    sns.histplot(df["Price"], bins=10, kde=True)
    plt.title("Price Distribution of Mobiles")
    plt.xlabel("Price (INR)")
    plt.ylabel("Count")
    plt.show()

    # Average Price by Brand
    plt.figure()
    avg_price.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Average Price by Brand")
    plt.xlabel("Brand")
    plt.ylabel("Average Price (INR)")
    plt.xticks(rotation=45)
    plt.show()

    # Storage vs Price
    plt.figure()
    sns.scatterplot(data=df, x="Storage_GB", y="Price", hue="Brand")
    plt.title("Storage vs Price")
    plt.xlabel("Storage (GB)")
    plt.ylabel("Price (INR)")
    plt.legend(title="Brand", bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()

    # RAM vs Price
    plt.figure()
    sns.scatterplot(data=df, x="RAM_GB", y="Price", hue="OS")
    plt.title("RAM vs Price by OS")
    plt.xlabel("RAM (GB)")
    plt.ylabel("Price (INR)")
    plt.legend(title="OS")
    plt.tight_layout()
    plt.show()

#Main Function
def main():
    df = load_data(INPUT_FILE)
    df = clean_data(df)
    avg_price, _ = analyze_data(df)
    save_cleaned_data(df, os.path.join(OUTPUT_DIR, "cleaned_mobile_data.csv"))
    visualize_data(df, avg_price)
    print("Analysis Complete!")



if __name__ == "__main__":
    main()
