from dataclasses import dataclass

@dataclass
class BakeryOrder:
    order_id: int
    items: list[str]

class OrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, order:BakeryOrder):
        self.queue.append(order)

    def process_orders(self):
        while self.queue:
            current_order = self.queue.pop()
            print(f"Processing Order {current_order.order_id}...")
            for item in current_order.items:
                print(f"Preparing {item}")
            print(f"Order {current_order.order_id} is ready!\n")

# Create bakery orders
order1 = BakeryOrder(101, ["Croissant", "Eclair", "Baguette"])
order2 = BakeryOrder(102, ["Muffin", "Donut"])
order3 = BakeryOrder(103, ["Cake", "Cookie"])

# Create order queue
queue = OrderQueue()
queue.add_order(order1)
queue.add_order(order2)
queue.add_order(order3)

# Process orders
queue.process_orders()