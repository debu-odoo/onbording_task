from odoo import models

class ProductProduct(models.Model):
    _inherit = 'product.product'



    def name_get(self):
        result = []
        
        for record in self:
            name = record.name +'-'+ '['+record.detailed_type+']'
            # name = record.name +'-'+ self.env['product.product']._columns['detailed_type'].selection
            result.append((record.id, name))
        return result

