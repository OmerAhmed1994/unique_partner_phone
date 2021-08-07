

from odoo import _, api, fields, models



class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Res Partner'

    _sql_constraints = [
        ('phone_uniq', 'unique(phone)', 'The phone must be unique!'),
        ('mobile_uniq', 'unique(mobile)', 'The mobile must be unique!')
    ]
    
    @api.model
    def create(self, values):
        if values.get('phone'):
            values['phone'] = "00965" + values.get('phone') 
        if values.get('mobile'):
            values['mobile'] = "00965" + values.get('mobile') 
        if values.get('phone') and not values.get('mobile'):
            values['mobile'] = values.get('phone') 
        return super(ResPartner, self).create(values)