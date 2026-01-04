def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    valid = []
    invalid = 0

    for t in transactions:
        try:
            if t["Quantity"] <= 0 or t["UnitPrice"] <= 0:
                raise ValueError
            if not t["TransactionID"].startswith("T"):
                raise ValueError
            if not t["CustomerID"].startswith("C"):
                raise ValueError

            amount = t["Quantity"] * t["UnitPrice"]

            if region and t["Region"] != region:
                continue
            if min_amount and amount < min_amount:
                continue
            if max_amount and amount > max_amount:
                continue

            valid.append(t)
        except:
            invalid += 1

    summary = {
        "total_input": len(transactions),
        "invalid": invalid,
        "final_count": len(valid)
    }

    return valid, invalid, summary
