class Collection:
    def __init__(self, collection_id, season_name, products, production_status):
        self.collection_id = collection_id
        self.season_name = season_name
        self.products = products
        self.production_status = production_status



class Product:
    def __init__(self, product_id, materials, size, fit, material_certifications,
                 colors, processes, supplier, gender, season):
        self.product_id = product_id
        self.materials = materials
        self.size = size
        self.fit = fit
        self.materials_certifications = material_certifications
        self.colors = colors
        self.processes = processes
        self.supplier = supplier
        self.gender = gender
        self.season = season

    def get_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"materials: {self.materials}")
        print(f"Size: {self.size}")
        print(f"Fit: {self.fit}")
        print(f"Materials certification: {self.materials_certifications}")
        print(f"Colors: {self.colors}")
        print(f"Processes: {self.processes}")
        print(f"Supplier: {self.supplier}")
        print(f"Gender: {self.gender}")
        print(f"SEASON: {self.season}")
