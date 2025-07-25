from odoo import models, fields

class EduTransportRoute(models.Model):
    _name = 'edu.transport.route'
    _description = 'Transport Routes'

    name = fields.Char()
    driver_name = fields.Char()
    vehicle_number = fields.Char()
    stops = fields.Text()
