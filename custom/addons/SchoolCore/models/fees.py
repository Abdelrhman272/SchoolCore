from odoo import models, fields, api

class EduFees(models.Model):
    _name = 'edu.fees'
    _description = 'School Fees'

    name = fields.Char()
    student_id = fields.Many2one('edu.student')
    amount = fields.Float()
    due_date = fields.Date()
    paid = fields.Boolean(default=False)
    is_overdue = fields.Boolean(compute='_compute_is_overdue')

    @api.depends('due_date', 'paid')
    def _compute_is_overdue(self):
        for rec in self:
            rec.is_overdue = not rec.paid and rec.due_date < fields.Date.today()
