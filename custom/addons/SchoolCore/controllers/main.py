from odoo import http
from odoo.http import request

class EduMainController(http.Controller):
    
    @http.route(['/eduverse/home'], type='http', auth='public', website=True)
    def homepage(self, **kwargs):
        return request.render('SchoolCore.homepage_template')

    @http.route(['/eduverse/info'], type='json', auth='user')
    def get_school_info(self):
        return {
            'school_name': 'EduVerse Academy',
            'contact': '+123456789',
            'email': 'contact@eduverse.academy',
        }
