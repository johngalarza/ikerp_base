import re

from markupsafe import Markup

from odoo.addons.web.controllers.database import Database


class IkerpDatabase(Database):

    def _render_template(self, **d):
        rendered = super()._render_template(**d)
        body = str(rendered)
        body = body.replace(
            '/web/static/img/logo2.png',
            '/ikerp_base/static/description/banner.png',
        )
        body = re.sub(r'\bOdoo\b', 'IKERP', body)
        return Markup(body)
