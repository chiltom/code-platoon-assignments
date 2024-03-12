import csv


def format_data(file_path):
    raw_data = []

    # Grab raw data from file and populate list
    with open(file_path, mode='r', newline='') as csvfile:
        data_reader = csv.DictReader(csvfile, restkey='toppings')
        for line in data_reader:
            raw_data.append(line)

    for datum in raw_data:
        for index, val in enumerate(datum['toppings']):
            datum['toppings'][index] = int(val)

    print(raw_data)

    # Make field names for csv file with keys from datum object
    fieldnames = []
    for key in raw_data[0].keys():
        fieldnames.append(key)

    with open(file_path, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for datum in raw_data:
            writer.writerow({'order_id': datum['order_id'], 'customer_id': datum['customer_id'], 'date': datum['date'],
                            'pizza_type': datum['pizza_type'], 'store_id': datum['store_id'], 'toppings': list(datum['toppings'])})


format_data('./data/orders.csv')
