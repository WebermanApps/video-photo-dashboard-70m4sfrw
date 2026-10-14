# Video & Photo Dashboard

Internal dashboard for the Video & Photo agent, published with GitHub Pages:
https://webermanapps.github.io/video-photo-dashboard-70m4sfrw/

## Report runs
Every Morning or Evening report run must also update `report.json`:
- `type`: `"Morning"` or `"Evening"`
- `posted`: post time in ICT ISO 8601, e.g. `2026-10-14T04:50:00+07:00`
- `summary`: the one-line report summary shown on the dashboard

Keep it in step with the report section in `index.html`.
