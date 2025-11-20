import pandas as pd
import matplotlib.pyplot as plt

## --- Configuration ---
FILE_NAME = 'sales_data.csv' # *** CHANGE THIS to your actual CSV file name ***
GROUP_BY_COLUMN = 'Product'  # *** CHANGE THIS to your category column (e.g., 'Region', 'Month') ***
SALES_COLUMN = 'Sales'       # *** CHANGE THIS to the column with the numerical sales/amount data ***
## ---------------------

def analyze_sales_data(file, group_col, sales_col):
    """
    Loads data, groups by a category, sums the sales, and plots the results.
    """
    try:
        # 1. Load CSV using Pandas
        df = pd.read_csv(file)
        print(f"Data loaded successfully from {file}.")
        print("\n--- First 5 rows of data ---")
        print(df.head())
        print("-" * 30)

        # 2. Use groupby(), sum()
        # Ensure the Sales column is numeric, coercing errors to handle non-numeric entries
        df[sales_col] = pd.to_numeric(df[sales_col], errors='coerce')
        df.dropna(subset=[sales_col], inplace=True) # Remove rows where Sales couldn't be converted
        # Calculate total sales for each group
        sales_summary = df.groupby(group_col)[sales_col].sum().reset_index()

        # Sort for easier interpretation
        sales_summary = sales_summary.sort_values(by=sales_col, ascending=False)
        
        print(f"\n--- Sales Summary by {group_col} (Top Sellers) ---")
        print(sales_summary)
        print("-" * 30)

        # 3. Use plot()
        plt.figure(figsize=(12, 7))
        
        # Create a bar chart (use kind='barh' for horizontal bars if many categories)
        sales_summary.plot(
            kind='bar', 
            x=group_col, 
            y=sales_col, 
            legend=False,
            ax=plt.gca(), # Use the current figure axes
            color='skyblue'
        ) 

       # Customize the plot
        plt.title(f'Total Sales Distribution by {group_col}', fontsize=16)
        plt.xlabel(group_col, fontsize=12)
        plt.ylabel(f'Total {sales_col}', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"\nError: File '{file}' not found. Please check the file path.")
    except KeyError as e:
        print(f"\nError: Column {e} not found. Check if '{GROUP_BY_COLUMN}' and '{SALES_COLUMN}' match your CSV columns.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Execute the analysis function
analyze_sales_data(FILE_NAME, GROUP_BY_COLUMN, SALES_COLUMN)