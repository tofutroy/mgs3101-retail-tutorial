#Step 1: Pandas Import    
import pandas as pd
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda value: f'{value:,.2f}')

def pandas_import():
    print("\n" + "=" * 70)
    print("STEP 1: PANDAS IMPORT")
    print("=" * 70)

pandas_import()
print("Pandas imported successfully.")

#Step 2: First Function 
def demo_pandas_fundamentals():
    print("\n" + "=" * 70)
    print("STEP 2: PANDAS FUNDAMENTALS")
    print("=" * 70)

demo_pandas_fundamentals()

daily_sales = pd.Series([1250.50, 2100.00, 1850.75, 3200.20, 4100.00],
                            index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
                            name='Daily_Sales_USD'
)
print("\nDaily sales Series:")
print(daily_sales)
print(f"Total weekly sales: ${daily_sales.sum():,.2f}")
toy_orders = pd.DataFrame({
    'OrderID': [1001, 1002, 1003, 1004],
    'Quantity': [15, 8, 25, 2],
    'UnitPrice': [12.50, 45.00, 12.50, 350.00],
    'CustomerType': ['B2C', 'B2B', 'B2C', 'B2B']
})
toy_orders['LineTotal'] = toy_orders['Quantity'] * toy_orders['UnitPrice']
print("\nOrders with vectorized line totals:")
print(toy_orders)
large_b2b_orders = toy_orders[
    (toy_orders['CustomerType'] == 'B2B') &
    (toy_orders['LineTotal'] >= 500)
]
print("\nB2B orders worth $500 or more:")
print(large_b2b_orders)



#GUIDED PRACTICE
#1. Friday Sales ≈ 4100.00
#2. OrderID 1004: 1004*2 =700
#3. If  customer type is 'B2B' and line total is >= 500 = 'large_b2b_orders
#4. Row 3 - Line total still > than 600

#STEP 3 :RETAIL FILE INSPECTION
def load_and_inspect_data():
    print("\n" + "=" * 70)
    print("STEP 3: LOAD AND INSPECT RETAIL DATA")
    print("=" * 70)    

    df_2009 = pd.read_csv('Retail 2009-10-4.csv')
    df_2010 = pd.read_csv('Retail 2010-11-1.csv')

    print(f"2009-10 records: {len(df_2009):,}")
    print(f"2010-11 records: {len(df_2010):,}")
    print(f"Columns: {df_2009.columns.tolist()}")

    print("\nFirst three rows from 2009-10:")
    print(df_2009.head(3))

    print("\nMissing Customer IDs:")
    print(f"2009-10: {df_2009['Customer ID'].isna().sum():,}")
    print(f"2010-11: {df_2010['Customer ID'].isna().sum():,}")

    return df_2009, df_2010 
df_2009, df_2010 = load_and_inspect_data()

#INSPECTION QUESTION
#1. There are 3 rows b/c of the code in row 56
#2. Column names are Invoice, StockCode, Description, Quantity, InvoiceDate, Price, CustomerID, Country
#3. InvoiceDate is not a datetime value b/c we didn't use any functions that converts the invoicedate to such
#4. Dropping missing customerID understates total sales as removing it removes any sales that were made by this demographic. The business cares about conversions not ID

