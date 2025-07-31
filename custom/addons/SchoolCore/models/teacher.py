from odoo import models, fields, api

class EduTeacher(models.Model):
    _name = 'edu.teacher'
    _description = 'Teacher Record'
    _inherit = ['mail.thread']

    name = fields.Char(required=True)
    employee_ref = fields.Many2one('hr.employee')
    user_id = fields.Many2one('res.users', string="User Account")
    phone = fields.Char()
    email = fields.Char()
    active = fields.Boolean(default=True)
    subject_ids = fields.Many2many('edu.subject', string="Subjects")
    class_ids = fields.Many2many('edu.class', string="Classes")

    def action_link_users(self):
        linked_count = 0
        for teacher in self:
            if teacher.email and not teacher.user_id:
                user = self.env['res.users'].sudo().search([('email', '=', teacher.email)], limit=1)
                if user:
                    teacher.user_id = user
                    linked_count += 1
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Linking Complete',
                'message': f'{linked_count} teacher(s) linked to user accounts.',
                'type': 'success',
            }
        }
