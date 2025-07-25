from odoo import models, fields

class EduPOSItem(models.Model):
    _name = 'edu.pos.item'
    _description = 'POS Items for School'

    name = fields.Char(required=True)
    product_id = fields.Many2one('product.product')
    price = fields.Float()
    category = fields.Char()
