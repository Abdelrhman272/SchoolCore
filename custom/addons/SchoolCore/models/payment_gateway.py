from odoo import models, fields

class EduPaymentGateway(models.Model):
    _name = 'edu.payment.gateway'
    _description = 'Payment Gateway Configuration'

    name = fields.Char(required=True)
    provider = fields.Selection([
        ('fawry', 'Fawry'),
        ('paypal', 'PayPal'),
        ('stripe', 'Stripe'),
    ], required=True)
    api_key = fields.Char()
    secret_key = fields.Char()
    active = fields.Boolean(default=True)
