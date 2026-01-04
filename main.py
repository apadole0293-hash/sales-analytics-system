from utils.file_handler import read_sales_data
from utils.data_processor import parse_transactions
from utils.validator import validate_and_filter
from utils.api_handler import fetch_all_products, create_product_mapping, enrich_sales_data
from utils.report_generator import generate_sales_report

def main():
    try:
        print("SALES ANALYTICS SYSTEM")

        raw = read_sales_data("data/sales_data.txt")
        parsed = parse_transactions(raw)

        valid, invalid, summary = validate_and_filter(parsed)

        products = fetch_all_products()
        mapping = create_product_mapping(products)

        enriched = enrich_sales_data(valid, mapping)

        generate_sales_report(valid, enriched)

        print("PROCESS COMPLETED SUCCESSFULLY")

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    main()
