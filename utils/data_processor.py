def parse_transactions(raw_lines):
    transactions = []

    for line in raw_lines[1:]:  # skip header
        try:
            parts = line.split('|')
            if len(parts) != 8:
                continue

            tid, date, pid, pname, qty, price, cid, region = parts

            transaction = {
                "TransactionID": tid.strip(),
                "Date": date.strip(),
                "ProductID": pid.strip(),
                "ProductName": pname.replace(',', '').strip(),
                "Quantity": int(qty.replace(',', '')),
                "UnitPrice": float(price.replace(',', '')),
                "CustomerID": cid.strip(),
                "Region": region.strip()
            }

            transactions.append(transaction)
        except:
            continue

    return transactions
