class Style:
    """Een class om een kledingstuk te beschrijven"""

    def __init__(self, style_id, style_name, product_type, textile, textile_certifications, size_range, sizes):
        self.style_id = style_id
        self.style_name = style_name
        self.product_type = product_type
        self.textile = textile
        self.textile_certifications = textile_certifications
        self.size_range = size_range
        self.sizes = sizes
        self.remarks = ""

    def get_description_style(self):
        """Toont een volledig beschrijf van kledingstuk"""
        print(f"Style ID: style: {self.style_id}")
        print(f"Style name: {self.style_name}")
        print(f"Product type: {self.product_type}")
        print(f"Textile: {self.textile}")
        print(f"Textile certifications: {self.textile_certifications}")
        print(f"Size range: {self.size_range}")
        print(f"sizes: {self.sizes}")
        print(f"Remarks: {self.remarks}")








clothing_piece = Style("PL100", "Storm Jacket", "Jacket", "recycled polyester",
                       "RCS", "Mens garment", "S-XXL")
clothing_piece.get_description_style()







