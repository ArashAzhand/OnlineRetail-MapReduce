import csv

with open('Online_Retail.csv', encoding='ISO-8859-1') as infile, \
     open('Online_Retail_Clean.csv', 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader, None)
    writer.writerow(header)

    for row in reader:
        try:
            if len(row) < 8:
                continue

            invoice, stock, desc, qty, date, price, customer, country = row

            # Required fields
            if not invoice.strip() or not stock.strip() or not qty.strip() or not price.strip():
                continue

            # Fill missing/blank fields
            desc = desc if desc.strip() else "Unknown"
            customer = customer if customer.strip() else "0"
            country = country if country.strip() else "Unknown"

            # Final row
            cleaned = [
                invoice.strip(),
                stock.strip(),
                desc.strip(),
                qty.strip(),
                date.strip() if date.strip() else "1970-01-01",
                price.strip(),
                customer.strip(),
                country.strip()
            ]

            writer.writerow(cleaned)
        except Exception:
            continue
