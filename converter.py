import json
import csv

def convert_orders(orders_in, orders_out, conversion_rate = 0.92, tax_rate = 1.19):
    try:
        with open(orders_in, mode = "r") as file:
            r_orders = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{orders_in}' could not be found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file '{orders_in}' does not contain valid JSON data.")
        return
    
    p_orders = []

    for order in r_orders:
        temp_orders = []
        order_id = order.get("order_id", "")
        date = order.get("date", "")
        customer = order.get("customer", {})
        customer_first_name = customer.get("first_name", "").strip()
        customer_last_name = customer.get("last_name", "").strip()
        customer_email = customer.get("email", "")
        items = order.get("items", [])
        for item in items:
            try:
                product_name = item.get("product_name", "")
                quantity = item.get("quantity", 0)
                net_price_usd = item.get("net_price_usd", 0.0) / quantity
                gross_price_eur = net_price_usd * conversion_rate * tax_rate
                temp_orders.append({
                    "order_id": order_id,
                    "date": date,
                    "customer_name": f"{customer_first_name} {customer_last_name}",
                    "customer_email": customer_email,
                    "product_name": product_name,
                    "quantity": quantity,
                    "gross_price_eur": round(gross_price_eur, 2)
                })
            except (ValueError, TypeError, ZeroDivisionError) as e:
                print(f"Warning: Corrupted item skipped in order {order_id} ({e}).")
        p_orders.extend(temp_orders)
        
    with open(orders_out, mode = "w", newline = "") as file:
        fieldnames = [ "order_id", "date", "customer_name", "customer_email", "product_name", "quantity", "gross_price_eur" ]
        writer = csv.DictWriter(file, fieldnames = fieldnames, delimiter = "\t")
        writer.writeheader()
        writer.writerows(p_orders)

if __name__ == "__main__":
    orders_in = "./orders.json"
    orders_out = "./orders.csv"
    convert_orders(orders_in, orders_out)