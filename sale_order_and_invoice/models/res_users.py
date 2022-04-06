from odoo import models

class ResUser(models.Model):
    _inherit = 'res.users'



    def name_get(self):
        result = []
        for record in self:
            name = record.name +'-'+ '['+record.login+']'
            result.append((record.id, name))
        return result