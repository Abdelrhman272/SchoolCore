from odoo import models, fields

class EduTeacher(models.Model):
    _name = 'edu.teacher'
    _description = 'Teacher Record'
    _inherit = ['mail.thread']

    name = fields.Char(required=True)
    employee_ref = fields.Many2one('hr.employee', string="Employee")
    user_id = fields.Many2one('res.users', string="User Account")
    phone = fields.Char()
    email = fields.Char()
    active = fields.Boolean(default=True)

    subject_ids = fields.Many2many('edu.subject', string="Subjects")
    class_ids = fields.Many2many('edu.class', string="Classes")
