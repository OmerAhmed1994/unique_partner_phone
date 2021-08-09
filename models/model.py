

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError



class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Res Partner'

    _sql_constraints = [
        ('phone_uniq', 'unique(phone)', 'The phone must be unique!'),
        ('mobile_uniq', 'unique(mobile)', 'The mobile must be unique!')
    ]
    
    def get_number(self,number):
        return number[6:] if number[:5] != '00965' else number[5:] if number[:4] != '+965' else number

    @api.model
    def create(self, values):
        if values.get('phone'):
            phone = self.get_number(values.get('phone'))
            partner = self.search([('phone','like',phone)])
            if partner:
                raise ValidationError(_('The phone must be unique'))
        if values.get('mobile'):
            mobile = self.get_number(values.get('mobile'))
            partner = self.search([('mobile','like',mobile)])
            if partner:
                raise ValidationError(_('The mobile must be unique'))
        if values.get('phone') and values.get('phone')[:5] != '00965' and values.get('phone')[:4] != '+965':
            values['phone'] = "00965" + values.get('phone') 
        if values.get('mobile') and values.get('mobile')[:5] != '00965' and values.get('mobile')[:4] != '+965':
            values['mobile'] = "00965" + values.get('mobile') 
        if values.get('phone') and not values.get('mobile'):
            values['mobile'] = values.get('phone') 
        
        return super(ResPartner, self).create(values)
    
    def write(self, values):
        for p in self:
            if values.get('phone'):
                phone = self.get_number(values.get('phone'))
                partner = self.search([('id','!=',p.id),('phone','like',phone)])
                if partner:
                    raise ValidationError(_('The phone must be unique'))
            if values.get('mobile'):
                mobile = self.get_number(values.get('mobile'))
                partner = self.search([('id','!=',p.id),('mobile','like',mobile)])
                if partner:
                    raise ValidationError(_('The mobile must be unique'))
            if values.get('phone') and values.get('phone')[:5] != '00965' and values.get('phone')[:4] != '+965':
                values['phone'] = "00965" + values.get('phone') 
            if values.get('mobile') and values.get('mobile')[:5] != '00965' and values.get('mobile')[:4] != '+965':
                values['mobile'] = "00965" + values.get('mobile') 
            if values.get('phone') and not values.get('mobile'):
                values['mobile'] = values.get('phone') 
        return super(ResPartner, self).write(values)
   