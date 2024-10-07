class ItemToPurchase:
    
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
    
    # Add print_item_cost method
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        # Format the cost to two decimal places
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

# Main function
def main():
    items = []
    
    for i in range(3):
        print(f"\nItem {i + 1}")
        item = ItemToPurchase()
        
        print("Enter the item name:")
        item.item_name = input()
        
        print("Enter the item price:")
        item.item_price = float(input())
        
        print("Enter the item quantity:")
        item.item_quantity = int(input())
        
        items.append(item)
    
    # Print the total cost
    print("\nTOTAL COST")
    total = 0
    for item in items:
        item.print_item_cost()
        total += item.item_price * item.item_quantity
    
    # Format the total to two decimal places
    print(f"\nTotal: ${total:.2f}")

# Ensure the main function is only called when the script is run directly
if __name__ == "__main__":
    main()

