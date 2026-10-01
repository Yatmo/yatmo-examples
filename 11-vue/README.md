# Vue listing page with @yatmo/vue

A complete real estate listing page in Vue 3 (Vite): facts, the Yatmo neighbourhood map, the nearest places and the
neighbourhood text, with the [@yatmo/vue](https://www.npmjs.com/package/@yatmo/vue) components.

```bash
npm install
echo "VITE_YATMO_KEY=your_frontend_key" > .env
npm run dev
```

Add the dev server's origin (localhost) to the allowed domains of your frontend key. For a Nuxt page that renders
the text on the server (indexable), see the [@yatmo/vue README](https://www.npmjs.com/package/@yatmo/vue#server-rendering-for-search-engines).
