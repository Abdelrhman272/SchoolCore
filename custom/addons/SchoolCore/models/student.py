from odoo import models, fields, api

class EduStudent(models.Model):
    _name = 'edu.student'
    _description = 'Student Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, tracking=True)
    student_code = fields.Char(required=True, copy=False, index=True)
    birth_date = fields.Date()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    class_level = fields.Char()
    parent_id = fields.Many2one('res.partner')
    email = fields.Char()
    phone = fields.Char()
    transport_id = fields.Many2one('edu.transport.route')
    fees_ids = fields.One2many('edu.fees', 'student_id')
    age = fields.Integer(compute='_compute_age')
    active = fields.Boolean(default=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            rec.age = 0
            if rec.birth_date:
                rec.age = fields.Date.today().year - rec.birth_date.year

    @api.onchange('parent_id')
    def _onchange_parent(self):
        if self.parent_id:
            self.email = self.parent_id.email
            self.phone = self.parent_id.phone

    _sql_constraints = [
        ('student_code_unique', 'UNIQUE(student_code)', 'Student code must be unique.')
    ]
