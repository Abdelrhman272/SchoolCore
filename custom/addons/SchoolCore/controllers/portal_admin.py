from odoo import http
from odoo.http import request

class PortalAdminController(http.Controller):

    @http.route(['/admin/dashboard'], type='http', auth='user', website=True)
    def admin_dashboard(self, **kw):
        student_count = request.env['edu.student'].search_count([])
        teacher_count = request.env['edu.teacher'].search_count([])
        fee_count = request.env['edu.fees'].search_count([])

        return request.render('SchoolCore.admin_dashboard_template', {
            'student_count': student_count,
            'teacher_count': teacher_count,
            'fee_count': fee_count
        })
