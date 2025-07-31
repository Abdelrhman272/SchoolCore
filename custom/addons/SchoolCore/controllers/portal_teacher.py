from odoo import http
from odoo.http import request

class PortalTeacherController(http.Controller):

    @http.route(['/my/teacher'], type='http', auth='user', website=True)
    def teacher_dashboard(self, **kw):
        user = request.env.user
        teacher = request.env['edu.teacher'].sudo().search([('user_id', '=', user.id)], limit=1)

        if not teacher:
            return request.render('website.404')

        return request.render('SchoolCore.teacher_dashboard_template', {
            'teacher': teacher
        })
