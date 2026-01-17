def average_valid_measurements(values):
    total = 0
    count = 0

    for v in values:
        if v is not None:
            try:
                total += float(v)
                count += 1
            except (TypeError, ValueError):
                continue
            
    return total / count if count > 0 else 0.0
