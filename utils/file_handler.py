def read_sales_data(filename):
    """
    Reads sales data handling encoding issues
    """
    encodings = ['utf-8', 'latin-1', 'cp1252']

    for enc in encodings:
        try:
            with open(filename, 'r', encoding=enc) as file:
                lines = file.readlines()
                return [line.strip() for line in lines if line.strip()]
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            raise FileNotFoundError("Sales file not found")

    raise Exception("Unable to read file")
