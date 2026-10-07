# Automated E-Commerce Order Data Converter (JSON to CSV)

A robust, production-ready Python script designed to automate the extraction, transformation, and formatting of nested e-commerce order logs. It converts complex JSON structures into clean, standardized CSV files optimized for direct import into accounting software, CRMs, or ERP systems.

## → Business Problem Solved

Online store owners frequently receive daily order logs from third-party APIs or international wholesale suppliers in complex, nested JSON formats. Manually restructuring this data or forcing standard libraries to handle messy data often results in system crashes, distorted prices, or missing data. 

**This solution automates that process in seconds by:**
* **Flattening Nested Data:** Splitting multi-item orders into clean, individual rows while preserving core customer tracking info.
* **Dynamic Currency & Tax Calculation:** Converting unit prices from USD to EUR and applying regional taxes automatically.
* **Fault-Tolerant Processing:** Skipping only corrupted line items (e.g., zero quantities or corrupted strings) instead of discarding the entire batch of orders, saving critical transaction history.

## → Technical Key Features

* **Zero-External Dependencies:** Built purely using Python's native standard libraries (`json` and `csv`)—no bulky installations required.
* **Defensive Architecture:** Complete exception shielding (`ValueError`, `TypeError`, `ZeroDivisionError`) to prevent workflow interruptions from unpredictable real-world inputs.
* **Highly Customizable:** Exposes flexible parameters for currency exchange rates and tax multipliers via clean function signatures.

## → Input vs. Output Preview

### Source Input (`orders.json`)
```json
[
  {
    "order_id": "ORD-2026-001",
    "date": "2026-10-05",
    "customer": { "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com" },
    "items": [
      { "product_name": "Mechanical Keyboard", "net_price_usd": 120.00, "quantity": 2 }
    ]
  }
]
```

### Standardized Output (`orders.csv` - Tab Delimited)
```text
order_id	date	customer_name	customer_email	product_name	quantity	net_price_eur
ORD-2026-001	2026-10-05	John Doe	john.doe@example.com	Mechanical Keyboard	2	65.69
```

## → Installation & Usage

### Prerequisites
* Python 3.x installed on your local machine.

### Execution
1. Place your target JSON file inside your directory.
2. Run the pipeline directly from your terminal:
   ```bash
   python convert_orders.py
   ```

### Custom Configuration
You can easily adjust conversion factors by modifying the function arguments in the execution block:
```python
convert_orders(orders_in, orders_out, currency_conversion=0.92, tax=1.19)
```

## → About my Work#
<p align="justify">
I build resilient Python automation scripts, desktop utilities, and custom data processing pipelines designed to save businesses hours of manual spreadsheet labor. While the repository code demonstrates a solution for a simplified, optimal scenario using sample data, the underlying architecture and defensive programming principles are fully representative of how I tackle highly complex, real-world data engineering challenges.
</p>

**Looking to automate your backend data operations?** Let's connect!