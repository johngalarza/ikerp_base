from odoo.addons.web.controllers.webmanifest import WebManifest


class IkerpWebManifest(WebManifest):

    def _icon_path(self):
        return 'ikerp_base/static/description/icon.png'

    def _get_webmanifest(self):
        manifest = super()._get_webmanifest()
        manifest['name'] = 'IKERP'
        manifest['background_color'] = '#3B82F6'
        manifest['theme_color'] = '#3B82F6'
        manifest['icons'] = [{
            'src': '/ikerp_base/static/description/icon.png',
            'sizes': '192x192',
            'type': 'image/png',
        }, {
            'src': '/ikerp_base/static/description/icon.png',
            'sizes': '512x512',
            'type': 'image/png',
        }]
        return manifest
