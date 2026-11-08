# Raha — creative portfolio

An original, responsive portfolio prototype with four full case studies, a project archive, sticky project scenes, six process steps, draggable galleries, a custom cursor, falling hero labels, gaze-following footer eyes, and accessible contact interactions.

**All projects, names, biography and contact details are illustrative.** No real client results or testimonials are claimed. Social buttons explicitly explain that profiles have not been configured. The sample email is `hello@example.com` and is never opened as an outgoing message.

## Run

Node.js 22+; no npm dependencies or install step required.

```sh
npm run build
npm run check
npm run dev -- --port 4173
```

## Edit

- `src/content.mjs`: profile, email, social URLs, four projects, narrative, skills, process.
- `public/style.css`: central palette, font variables, responsive layout and reduced-motion styles.
- `public/app.js`: progressive enhancement, navigation, scrolling, cursor, eyes, carousels and copying.
- `src/build.mjs`: shared static page templates. Run the build after editing.
- `public/assets/`: original SVG concept illustrations; replace with final imagery and update the templates as needed.
- `public/fonts/`: locally hosted Bricolage Grotesque and DM Sans, under their included SIL Open Font Licenses.

## Routes and hosting

Build outputs six complete static HTML routes in `dist/`: `/`, `/work/`, `/work/sol/`, `/work/forma/`, `/work/orbit/`, `/work/slow-good/`. Every case route supports direct navigation and refresh without a rewrite service. All assets and links are relative, supporting the `/raha/` GitHub Pages subpath and standalone origins.

The GitHub Actions workflow publishes `dist/` through GitHub Pages **when Pages is configured to use GitHub Actions** in repository Settings → Pages. It does not modify DNS, nameservers, custom domains, or the owner's Cloudflare account. `.openai/hosting.json` identifies the separate owner-private review deployment.

## Accessibility and interactions

Native document scrolling; no wheel hijacking or mandatory scroll snapping between sections. Mobile navigation supports Escape and a focus loop. Each carousel supports visible controls, arrow keys, pointer dragging, and touch swiping. No autoplay gallery. The custom cursor is limited to fine pointers and disabled for reduced motion. Reduced motion disables entry animations and sticky project layering, leaving the entire document readable. Contact dialogs use the browser's native dialog focus handling. Clipboard failure exposes a manual selection path.

## Design references

Studied Hello Dani (colour, graphic personality, footer), Xhulia (project rhythm, case-study structure, labels and interaction), Bryce Willem (professional presentation and collaboration). The supplied reference recording was reviewed for desktop/mobile differences. All implementation, sample narratives and SVG concept artwork are original; reference-site code and portfolio work are not copied.

This prototype is ready for final content and a real contact configuration; RTL translation can be added centrally through the HTML language/direction and content data. No backend, tracking, external APIs or Cloudflare account changes are required.
