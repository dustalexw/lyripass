# Validation — Lyripass 0.1.0

- Built an Apple-silicon macOS app using `npm run tauri build -- --bundles app`.
- Verified the bundle identifier is `app.lyripass.desktop` and version is `0.1.0`.
- Verified the app’s local code signature with `codesign --verify --deep --strict`.
- Launched the native app and confirmed its separate first-run folder setup.
- `npm test`: 142 tests passed across 4 files. The inherited export workflow test clock was updated to accommodate existing request pacing.
- `npm run lint`: no errors; 71 existing warnings remain across the upstream codebase.
- `git diff --check`: passed.
- Browser interaction checks using official Tauri IPC mocks and synthetic sample tracks: folder add/remove, setup to library, playback selection, lyrics rendering, cue seeking, search, empty results, About, download options, export options, and opening the lyrics editor. No page errors.
- Visually reviewed setup, library, lyrics inspector, menus, and editor, including light and dark appearances and a 1024 × 700 compact window. Preview images use synthetic tracks and original sample lyrics.

The app is locally signed, not Apple-notarized. Windows and Linux builds, live LRCLIB downloads/publishing, and exports against a real music library were not exercised in this redesign pass.
