from odoo import models, fields

class EduSubject(models.Model):
    _name = 'edu.subject'
    _description = 'School Subject'

    name = fields.Char(string='Subject Name', required=True)
    code = fields.Char(string='Subject Code')
