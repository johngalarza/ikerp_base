from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home
from odoo.addons.web.controllers.session import Session


class IkerpHome(Home):

    # ROOT
    @http.route('/', type='http', auth='none')
    def index(self, **kw):
        return request.redirect('/ikerp')

    # REEMPLAZA /odoo ORIGINAL
    @http.route(
        ['/odoo', '/odoo/<path:path>'],
        type='http',
        auth='none',
        readonly=Home._web_client_readonly,
    )
    def odoo_redirect(self, path=None, **kw):
        target = '/ikerp' + (f'/{path}' if path else '')
        qs = request.httprequest.query_string.decode()
        if qs:
            target = f'{target}?{qs}'
        return request.redirect(target)

    # NUEVA RUTA
    @http.route(
        ['/ikerp', '/ikerp/<path:path>'],
        type='http',
        auth='user',
        readonly=Home._web_client_readonly,
    )
    def ikerp_web(self, s_action=None, **kw):
        return super().web_client(s_action=s_action, **kw)

    def _login_redirect(self, uid, redirect=None):
        url = super()._login_redirect(uid, redirect)

        if url.startswith('/odoo'):
            return url.replace('/odoo', '/ikerp', 1)

        return url


class IkerpSession(Session):

    @http.route('/web/session/logout', type='http', auth='none')
    def logout(self, redirect='/ikerp'):
        return super().logout(redirect=redirect)