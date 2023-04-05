class MenuItem:
    def __init__(self, name, price, category, description, ingredients, is_vegetatrian = True, is_spicy = True):
        
        self.name = name
        self.price = price
        self.category = category
        self.description = description
        self.price = price
        self.ingredients = ingredients
        self.vegetatrian = is_vegetatrian
        self.is_spicy = is_spicy
        
class Menu:
    def __init__(self):
        self.items = []
        
    def add_items(self, item):
        self.items.append(item)
        
    def get_items_by_category(self, category):
        return [item for item in self.items if item.category == category]
    
    def get_item_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None
    
    def display(self):
        categories = set([item.category for item in self.items])
        for category in categories:
            print(f"{category.title()}:")
            items = self.get_items_by_category(category)
            for item in items:
                print(f" - {item}")
            print()
            
class Order:
    def __init__(self):
        self.items = []
        
    def add_tiem(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def display(self):
        for item in self.items:
            print(f"-  {item}")
    
    def get_total(self):
        return sum([item.price for item in self.items])
        
        
    
    
        
        
    
    
    
    