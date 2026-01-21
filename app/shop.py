from decimal import Decimal


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
        self.name = name
        self.location = location
        self.products = {
            prod_name: Decimal(str(prod_price))
            for prod_name, prod_price in products.items()
        }

    def get_products_price(self, customer_cart: dict) -> Decimal:
        result = 0
        for product_key, customer_key in zip(self.products, customer_cart):
            result += self.products[product_key] * customer_cart[customer_key]

        return Decimal(str(result))

    def bough_info(self, customer_cart: dict) -> None:
        print("You have bought:")
        for product_key, customer_key in zip(self.products, customer_cart):
            _sum = (self.products[product_key]
                    * customer_cart[customer_key]
                    )
            if _sum == int(_sum):
                _sum = int(_sum)
            print(f"{customer_cart[customer_key]} "
                  f"{product_key}s for {_sum} dollars")
        total_sum = self.get_products_price(customer_cart)
        print(f"Total cost is {total_sum} dollars")
        print("See you again!\n")
