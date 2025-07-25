from odoo import models, fields, api

class EduComputedMixin(models.AbstractModel):
    _name = 'edu.computed.mixin'
    _description = 'Generic Computation Helpers'

    @api.model
    def calculate_average(self, records, field_name):
        values = [getattr(r, field_name, 0.0) for r in records]
        return sum(values) / len(values) if values else 0.0
