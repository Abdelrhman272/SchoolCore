# -*- coding: utf-8 -*-
from odoo import models, fields, api


class EduAcademicYear(models.Model):
    _name = 'edu.academic.year'
    _description = 'Academic Year'

    name = fields.Char(string="Academic Year", required=True)
    date_start = fields.Date(string="Start Date", required=True)
    date_end = fields.Date(string="End Date", required=True)
    active = fields.Boolean(default=True)


class EduStudentGrade(models.Model):
    _name = 'edu.student.grade'
    _description = 'Student Grade'

    student_id = fields.Many2one('edu.student', string="Student", ondelete="cascade")
    subject_id = fields.Many2one('edu.subject', string="Subject")
    exam_type = fields.Selection([
        ('monthly', 'Monthly'),
        ('term', 'Term'),
        ('final', 'Final')
    ], string="Exam Type")
    score = fields.Float(string="Score")
    max_score = fields.Float(string="Max Score")
    academic_year_id = fields.Many2one('edu.academic.year', string="Academic Year")


class EduStudent(models.Model):
    _name = 'edu.student'
    _description = 'Student'

    name = fields.Char(string="Student Name", required=True)
    student_code = fields.Char(string="Student Code", readonly=True, copy=False, default='New')
    birth_date = fields.Date(string="Date of Birth")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender")
    parent_id = fields.Many2one('res.partner', string="Parent")
    stage_id = fields.Many2one('edu.stage', string="Stage")
    class_id = fields.Many2one('edu.class', string="Class")
    academic_year_id = fields.Many2one('edu.academic.year', string="Academic Year")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('enrolled', 'Enrolled'),
        ('graduated', 'Graduated'),
        ('withdrawn', 'Withdrawn'),
        ('rejected', 'Rejected'),
        ('archived', 'Archived')
    ], string='Status', default='draft')

    grade_ids = fields.One2many('edu.student.grade', 'student_id', string="Grades")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('student_code', 'New') == 'New':
                vals['student_code'] = self.env['ir.sequence'].next_by_code('edu.student') or 'New'
        return super().create(vals_list)