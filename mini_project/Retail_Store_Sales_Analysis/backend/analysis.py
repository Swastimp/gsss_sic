import pandas as pd
import os

OUTPUT_FOLDER = os.path.join('backend', 'outputs')
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def analyze_sales(filepath):
    # Load dataset
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        raise ValueError(f"Error reading CSV: {e}")

    # Validate required columns
    required_cols = ['Sales', 'Date', 'StoreID']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Data Cleaning
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce').fillna(0)
    df.drop_duplicates(inplace=True)

    # Handle date conversion
    try:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    except Exception:
        raise ValueError("Date conversion failed")
    
    # Drop rows where Date is NaT
    df.dropna(subset=['Date'], inplace=True)

    if df.empty:
        raise ValueError("DataFrame is empty after cleaning")

    df.set_index('Date', inplace=True)
    df['Weekday'] = df.index.day_name()
    df['Month'] = df.index.month

    # Grouping & Aggregations
    store_sales = df.groupby('StoreID')['Sales'].sum().sort_values(ascending=False)
    avg_weekday_sales = df.groupby('Weekday')['Sales'].mean().reindex(
        ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    )

    # Derived Columns
    df['CumulativeSales'] = df.groupby('StoreID')['Sales'].cumsum()
    df['SalesCategory'] = df['Sales'].apply(lambda x: 'High' if x >= 5000 else 'Medium' if x >= 3000 else 'Low')

    # Export results
    cleaned_path = os.path.join(OUTPUT_FOLDER, 'cleaned_retail_sales.csv')
    store_sales_path = os.path.join(OUTPUT_FOLDER, 'store_sales_summary.csv')
    weekday_sales_path = os.path.join(OUTPUT_FOLDER, 'weekday_sales_summary.csv')

    try:
        df.to_csv(cleaned_path)
        store_sales.to_csv(store_sales_path)
        avg_weekday_sales.to_csv(weekday_sales_path)
    except Exception as e:
        raise ValueError(f"Error saving files: {e}")

    return {
        "cleaned": cleaned_path,
        "store_summary": store_sales_path,
        "weekday_summary": weekday_sales_path
    }
