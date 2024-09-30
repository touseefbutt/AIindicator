import pandas as pd

# URL for NASDAQ listed stock tickers
nasdaq_url = 'https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt'

# Function to download and save NASDAQ tickers
def download_nasdaq_tickers():
    try:
        # Read the NASDAQ listed tickers file
        df = pd.read_csv(nasdaq_url, sep='|', skiprows=1)
        
        # Clean the DataFrame (remove rows with NaN and reset the index)
        df = df.dropna().reset_index(drop=True)

        # Save to a local CSV file
        df.to_csv('nasdaq_tickers.csv', index=False)
        print("Tickers downloaded and saved to 'nasdaq_tickers.csv'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    download_nasdaq_tickers()