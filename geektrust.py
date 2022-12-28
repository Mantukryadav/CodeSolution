from sys import argv

def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
        # Add your code here to process input commands.
        products = {
            'TSHIRT': {'price': 1000, 'discount': 10, 'max_quantity': 2},
            'NOTEBOOK': {'price': 200, 'discount': 20, 'max_quantity': 3},
            'JACKET': {'price': 2000, 'discount': 5, 'max_quantity': 2},
            'CAP': {'price': 500, 'discount': 20, 'max_quantity': 2},
            'PENS': {'price': 300, 'discount': 10, 'max_quantity': 3},
            'MARKER': {'price': 500, 'discount': 5, 'max_quantity': 3},
        }
        purchases = {}
        def add_item(name, quantity):
            if name in products:
                if quantity > products[name]['max_quantity']:
                    print("ERROR_QUANTITY_EXCEEDED")
            else:
                if name in purchases:
                     purchases[name]['quantity'] += quantity
                else:
                    purchases[name] = {'quantity': quantity}
            print("ITEM_ADDED")
        def print_bill():
            total_amount = 0
            total_discount = 0
            for name, details in purchases.items():
                price = products[name]['price']
                discount = products[name]['discount']
                quantity = details['quantity']
                amount = price * quantity
                total_amount += amount
                if total_amount > 1000:
                    total_discount += (discount/100) * amount
            if total_amount > 3000:
                total_discount += (5/100) * total_amount
            total_amount_to_pay = total_amount - total_discount
            sales_tax = (10/100) * total_amount_to_pay
            total_amount_to_pay += sales_tax
            print(f"TOTAL_DISCOUNT {total_discount:.2f}")
            print(f"TOTAL_AMOUNT_TO_PAY {total_amount_to_pay:.2f}")
            # add_item('TSHIRT', 2)
            # add_item('NOTEBOOK', 1)
            # print_bill()
        product_name = input("Enter the name of product")
        product_quantity = input("Enter the quantity of product") 
        add_item(product_name, product_quantity)
        print_bill
        output = "" #process the input command and get the output
        # Once it is processed print the output using the command System.out.println()
        print(output)
    
if __name__ == "__main__":
    main()