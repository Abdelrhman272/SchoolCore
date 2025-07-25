from odoo import models, fields, api

class EduTeacher(models.Model):
    _name = 'edu.teacher'
    _description = 'Teacher Record'
    _inherit = ['mail.thread']

    name = fields.Char(required=True)
    employee_ref = fields.Many2one('hr.employee')
    subject_ids = fields.Many2many('edu.subject')
    phone = fields.Char()
    email = fields.Char()
    active = fields.Boolean(default=True)
