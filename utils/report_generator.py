from datetime import datetime
from collections import defaultdict

def generate_sales_report(transactions, enriched, output_file="output/sales_report.txt"):
    with open(output_file, "w", encoding="utf-8") as f:

        # 1. HEADER
        f.write("SALES ANALYTICS REPORT\n")
        f.write("=" * 50 + "\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write(f"Records Processed: {len(transactions)}\n\n")

        # Common calculations
        total_revenue = sum(t["Quantity"] * t["UnitPrice"] for t in transactions)
        avg_order_value = total_revenue / len(transactions) if transactions else 0
        dates = [t["Date"] for t in transactions]

        # 2. OVERALL SUMMARY
        f.write("OVERALL SUMMARY\n")
        f.write("-" * 50 + "\n")
        f.write(f"Total Revenue: ₹{total_revenue:,.2f}\n")
        f.write(f"Total Transactions: {len(transactions)}\n")
        f.write(f"Average Order Value: ₹{avg_order_value:,.2f}\n")
        f.write(f"Date Range: {min(dates)} to {max(dates)}\n\n")

        # 3. REGION-WISE PERFORMANCE
        region_data = defaultdict(lambda: {"sales": 0, "count": 0})

        for t in transactions:
            amount = t["Quantity"] * t["UnitPrice"]
            region_data[t["Region"]]["sales"] += amount
            region_data[t["Region"]]["count"] += 1

        f.write("REGION-WISE PERFORMANCE\n")
        f.write("-" * 50 + "\n")
        f.write("Region | Sales | % of Total | Transactions\n")

        for region, data in sorted(region_data.items(), key=lambda x: x[1]["sales"], reverse=True):
            percent = (data["sales"] / total_revenue) * 100
            f.write(f"{region} | ₹{data['sales']:,.0f} | {percent:.2f}% | {data['count']}\n")
        f.write("\n")

        # 4. TOP PRODUCTS
        product_sales = defaultdict(lambda: {"qty": 0, "revenue": 0})

        for t in transactions:
            product_sales[t["ProductName"]]["qty"] += t["Quantity"]
            product_sales[t["ProductName"]]["revenue"] += t["Quantity"] * t["UnitPrice"]

        f.write("TOP SELLING PRODUCTS\n")
        f.write("-" * 50 + "\n")
        f.write("Product | Quantity Sold | Revenue\n")

        for p, v in sorted(product_sales.items(), key=lambda x: x[1]["revenue"], reverse=True)[:5]:
            f.write(f"{p} | {v['qty']} | ₹{v['revenue']:,.0f}\n")
        f.write("\n")

        # 5. TOP CUSTOMERS
        customer_data = defaultdict(lambda: {"spent": 0, "count": 0})

        for t in transactions:
            customer_data[t["CustomerID"]]["spent"] += t["Quantity"] * t["UnitPrice"]
            customer_data[t["CustomerID"]]["count"] += 1

        f.write("TOP CUSTOMERS\n")
        f.write("-" * 50 + "\n")
        f.write("CustomerID | Total Spent | Orders\n")

        for c, v in sorted(customer_data.items(), key=lambda x: x[1]["spent"], reverse=True)[:5]:
            f.write(f"{c} | ₹{v['spent']:,.0f} | {v['count']}\n")
        f.write("\n")

        # 6. DAILY SALES TREND
        daily_data = defaultdict(lambda: {"revenue": 0, "transactions": 0, "customers": set()})

        for t in transactions:
            date = t["Date"]
            daily_data[date]["revenue"] += t["Quantity"] * t["UnitPrice"]
            daily_data[date]["transactions"] += 1
            daily_data[date]["customers"].add(t["CustomerID"])

        f.write("DAILY SALES TREND\n")
        f.write("-" * 50 + "\n")
        f.write("Date | Revenue | Transactions | Unique Customers\n")

        for d in sorted(daily_data):
            f.write(
                f"{d} | ₹{daily_data[d]['revenue']:,.0f} | "
                f"{daily_data[d]['transactions']} | {len(daily_data[d]['customers'])}\n"
            )
        f.write("\n")

        # 7. PRODUCT PERFORMANCE ANALYSIS
        low_performers = [p for p, v in product_sales.items() if v["qty"] < 5]

        f.write("PRODUCT PERFORMANCE ANALYSIS\n")
        f.write("-" * 50 + "\n")
        f.write(f"Low Performing Products (qty < 5): {', '.join(low_performers) if low_performers else 'None'}\n\n")

        # 8. API ENRICHMENT SUMMARY
        enriched_count = sum(1 for t in enriched if t.get("API_Enriched"))
        failed_count = len(enriched) - enriched_count
        success_rate = (enriched_count / len(enriched)) * 100 if enriched else 0

        f.write("API ENRICHMENT SUMMARY\n")
        f.write("-" * 50 + "\n")
        f.write(f"Total Products Enriched: {enriched_count}\n")
        f.write(f"Success Rate: {success_rate:.2f}%\n")
        f.write(f"Failed Enrichments: {failed_count}\n")
