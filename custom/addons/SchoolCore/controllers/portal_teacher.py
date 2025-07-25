from odoo import http
from odoo.http import request

class PortalTeacherController(http.Controller):

    @http.route(['/teacher/dashboard'], type='http', auth='user', website=True)
    def teacher_dashboard(self, **kw):
        teacher = request.env['edu.teacher'].search([('email', '=', request.env.user.email)], limit=1)
        return request.render('SchoolCore.teacher_dashboard_template', {
            'teacher': teacher
        })
