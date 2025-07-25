from odoo import http
from odoo.http import request

class PortalParentController(http.Controller):

    @http.route(['/parent/dashboard'], type='http', auth='user', website=True)
    def parent_dashboard(self, **kw):
        parent = request.env.user.partner_id
        students = request.env['edu.student'].search([('parent_id', '=', parent.id)])
        return request.render('SchoolCore.parent_dashboard_template', {
            'students': students
        })
