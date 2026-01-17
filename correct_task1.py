
def calculate_average_order_value(orders):
    total = 0
    count = 0
    
    for order in orders:
        
        if order["status"] != "cancelled":
            count += 1
            total += order["amount"]
    
    return total/count if count != 0 else 0.0
