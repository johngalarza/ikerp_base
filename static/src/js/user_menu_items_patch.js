import { _t } from "@web/core/l10n/translation";
import { browser } from "@web/core/browser/browser";
import { rpc } from "@web/core/network/rpc";
import { registry } from "@web/core/registry";

const userMenu = registry.category("user_menuitems");

function ikerpAccountItem(env) {
    return {
        type: "item",
        id: "account",
        description: _t("My IKERP Account"),
        callback: () => {
            rpc("/web/session/account")
                .then((url) => {
                    browser.open(url, "_blank");
                })
                .catch(() => {
                    browser.open("/odoo", "_self");
                });
        },
        sequence: 60,
    };
}

if (userMenu.contains("odoo_account")) {
    userMenu.remove("odoo_account");
}
userMenu.add("odoo_account", ikerpAccountItem, { force: true });
