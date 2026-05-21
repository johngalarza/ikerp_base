/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from "@web/core/utils/patch";

patch(NavBar.prototype, {
    getMenuItemHref(payload) {
        return `/ikerp/${payload.actionPath || "action-" + payload.actionID}`;
    },
});
