# Yatmo examples

Small, self-contained pages showing how to put [Yatmo](https://yatmo.com) neighbourhood intelligence on a real estate
website: the map with points of interest and travel times, the written neighbourhood text, a complete property page,
search by travel time, and the REST API from a server.

<p align="center">
  <img src="https://raw.githubusercontent.com/Yatmo/.github/main/profile/img/map-and-summary.png" width="720" alt="Yatmo map and neighbourhood summary on a property page">
</p>

| Example | Shows | Plugin |
|---|---|---|
| [01-iframe](01-iframe/) | The six display modes of the iframe, isochrones and routes | [Iframe](https://documentation.yatmo.com/plugins/iframe) |
| [02-javascript-map](02-javascript-map/) | The map in your own element, route from the property, full screen | [JavaScript map](https://documentation.yatmo.com/plugins/js-map) |
| [03-summary-table](03-summary-table/) | Nearest places by category with travel times, no map | [JavaScript summary](https://documentation.yatmo.com/plugins/js-summary) |
| [04-neighbourhood-text](04-neighbourhood-text/) | The written description of the area, with headings and bold places | [Summary as text](https://documentation.yatmo.com/plugins/js-summary-text) |
| [05-property-page](05-property-page/) | A complete listing page: facts, discreet map (circle), neighbourhood text | Iframe + text |
| [06-travel-time-search](06-travel-time-search/) | "Homes within 15 minutes by bike": the reachable area and the matching listings on the map | [Travel-time search](https://documentation.yatmo.com/plugins/advanced/travel-time-search), [listings](https://documentation.yatmo.com/plugins/advanced/listings) |
| [07-rest-api](07-rest-api/) | Summary and neighbourhood text from a server, in shell and Python | [REST API](https://documentation.yatmo.com/api) |
| [08-npm-packages](08-npm-packages/) | The same from npm: `@yatmo/sdk` on the server (text as HTML, nearest places), `@yatmo/maps` in the browser | [@yatmo/sdk](https://www.npmjs.com/package/@yatmo/sdk), [@yatmo/maps](https://www.npmjs.com/package/@yatmo/maps) |
| [09-react](09-react/) | A complete listing page in React (Vite) with `YatmoMap`, `YatmoPois` and `YatmoNeighbourhoodText` | [@yatmo/react](https://www.npmjs.com/package/@yatmo/react) |
| [10-web-components](10-web-components/) | The same with three HTML elements and one script from a CDN, no framework, no build | [@yatmo/elements](https://www.npmjs.com/package/@yatmo/elements) |
| [11-vue](11-vue/) | The listing page in Vue 3 (Vite) with the same components | [@yatmo/vue](https://www.npmjs.com/package/@yatmo/vue) |
| [12-webflow](12-webflow/) | A Webflow-style property page with no backend: three snippets fed by the address of the CMS (also Wix, Squarespace, Framer) | [Webflow tutorial](https://documentation.yatmo.com/plugins/webflow), [@yatmo/elements](https://www.npmjs.com/package/@yatmo/elements) |

## Run them

1. Get a Yatmo licence key: [yatmo.com](https://yatmo.com). The web examples use your **frontend** key, the one locked to
   your domains; the API examples use your **backend** key ([keys explained](https://documentation.yatmo.com/license)).
2. Put the frontend key in [`config.js`](config.js), and add the domain you serve the examples from to the key's
   allowed domains (localhost included).
3. Serve the folder with any static server, for example `npx serve .` or `python3 -m http.server`, and open an example.
   Opening the files directly (`file://`) does not work: the plugins are loaded from `map.yatmo.com`.

No build step, no dependency: each example is one HTML file (08, 09 and 11 add npm packages; 09 and 11 are Vite apps, see their READMEs).

## Other integrations

- WordPress: [wordpress.org/plugins/yatmo-map](https://wordpress.org/plugins/yatmo-map/) ([source](https://github.com/Yatmo/yatmo-plugin-wordpress))
- Odoo 17 to 20: [apps.odoo.com](https://apps.odoo.com/apps/modules/20.0/yatmo_map) ([source](https://github.com/Yatmo/yatmo-plugin-odoo))
- Mobile: [iOS](https://github.com/Yatmo/yatmo-sdk-ios), [Android](https://github.com/Yatmo/yatmo-sdk-android),
  [React Native](https://github.com/Yatmo/yatmo-sdk-react-native), [Flutter](https://github.com/Yatmo/yatmo-sdk-flutter)
- AI assistants: [MCP server](https://documentation.yatmo.com/mcp)

MIT licence. Live, pre-configured demos of every plugin are on the [documentation site](https://documentation.yatmo.com).
