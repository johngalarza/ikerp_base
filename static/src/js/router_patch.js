/** @odoo-module **/

import { router, routerBus } from "@web/core/browser/router";
import { browser } from "@web/core/browser/browser";

const IKERP_PREFIX = "/ikerp";
const ODOO_PREFIX = "/odoo";

const originalStateToUrl = router.stateToUrl;
const originalUrlToState = router.urlToState;

router.stateToUrl = function (state) {
    const url = originalStateToUrl.call(this, state);
    if (url === ODOO_PREFIX || url.startsWith(ODOO_PREFIX + "/") || url.startsWith(ODOO_PREFIX + "?")) {
        return IKERP_PREFIX + url.slice(ODOO_PREFIX.length);
    }
    return url;
};

router.urlToState = function (urlObj) {
    if (urlObj.pathname === IKERP_PREFIX || urlObj.pathname.startsWith(IKERP_PREFIX + "/")) {
        const rewritten = new URL(urlObj.href);
        rewritten.pathname = ODOO_PREFIX + urlObj.pathname.slice(IKERP_PREFIX.length);
        return originalUrlToState.call(this, rewritten);
    }
    return originalUrlToState.call(this, urlObj);
};

browser.addEventListener("click", (ev) => {
    if (ev.defaultPrevented || ev.target.closest("[contenteditable]")) {
        return;
    }
    const a = ev.target.closest("a");
    const href = a?.getAttribute("href");
    if (!href || href.startsWith("#")) {
        return;
    }
    let url;
    try {
        url = new URL(a.href);
    } catch {
        return;
    }
    if (browser.location.host !== url.host || a.target === "_blank") {
        return;
    }
    const onIkerp = browser.location.pathname.startsWith(IKERP_PREFIX);
    const goesToIkerp =
        url.pathname === IKERP_PREFIX || url.pathname.startsWith(IKERP_PREFIX + "/");
    if (onIkerp && goesToIkerp) {
        ev.preventDefault();
        router.urlToState(url);
        if (url.hash) {
            browser.history.pushState({}, "", url.href);
        }
        new Promise((res) => setTimeout(res, 0)).then(() => routerBus.trigger("ROUTE_CHANGE"));
    }
});
