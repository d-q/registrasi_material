from odoo import models, fields, api, _
from odoo.exceptions import UserError

class RegistrasiMaterial(models.Model):
    _name = 'registrasi.material'
    _description = 'Registrasi Material'

    code = fields.Char(string='Material Code')
    name = fields.Char(string='Material Name')
    type = fields.Selection(
        selection=[
            ('fabric', 'Fabric'),
            ('jeans', 'Jeans'),
            ('cotton', 'Cotton'),
            ],
        string='Material Type')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one(string="Currency", related='company_id.currency_id', readonly=True)
    price = fields.Monetary(string='Material Buy Price', store=True)
    supplier = fields.Many2one('res.partner', string='Supplier')

    @api.model
    def create(self, vals):
        if vals.get('price') < 100.0:
            raise UserError('Material Buy Price tidak boleh di bawah 100')
        result = super(RegistrasiMaterial, self).create(vals)    
        return result