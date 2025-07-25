from odoo import http
from odoo.http import request

class EduAPIService(http.Controller):

    @http.route('/api/students', type='json', auth='user')
    def get_students(self):
        students = request.env['edu.student'].search([])
        return [{'name': s.name, 'code': s.student_code} for s in students]

    @http.route('/api/fees/<int:student_id>', type='json', auth='user')
    def get_student_fees(self, student_id):
        fees = request.env['edu.fees'].search([('student_id', '=', student_id)])
        return [{'amount': f.amount, 'due_date': f.due_date, 'paid': f.paid} for f in fees]
