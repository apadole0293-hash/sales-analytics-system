from datetime import datetime

def generate_sales_report(transactions, enriched, output_file="output/sales_report.txt"):
    total_revenue = sum(t["Quantity"] * t["UnitPrice"] for t in transactions)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("SALES ANALYTICS REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Generated: {datetime.now()}\n")
        file.write(f"Records Processed: {len(transactions)}\n\n")

        file.write("OVERALL SUMMARY\n")
        file.write(f"Total Revenue: ₹{total_revenue:,.2f}\n")
