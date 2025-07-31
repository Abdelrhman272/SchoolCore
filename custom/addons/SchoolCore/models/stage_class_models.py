from odoo import models, fields

class EduStage(models.Model):
    _name = 'edu.stage'
    _description = 'Education Stage'

    name = fields.Char(string="Stage Name", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(default=True)
    class_ids = fields.One2many('edu.class', 'stage_id', string="Classes")


class EduClass(models.Model):
    _name = 'edu.class'
    _description = 'Class'

    name = fields.Char(string="Class Name", required=True)
    stage_id = fields.Many2one('edu.stage', string="Stage", required=True)
    academic_year_id = fields.Many2one('edu.academic.year', string="Academic Year")
    code = fields.Char(string="Code")
    capacity = fields.Integer(string="Capacity")
    active = fields.Boolean(default=True)
