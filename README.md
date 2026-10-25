# Lyripass

Your music library, with every word in time.

![Lyripass library with sample tracks](docs/lyripass-preview.png)

Lyripass is a redesigned fork of [LRCGET](https://github.com/tranxuanthang/lrcget), built with Vue 3 and Tauri 2. Its graphite studio interface, coral and sky accents, frosted panels, and split-color wordmark take inspiration from [Dustalexw’s Frickoss](https://github.com/dustalexw/frickoss). Lyripass is an independent fork, not an official Dustalexw or LRCLIB release.

## Use it

Open **Lyripass.app**, add your music folders, and choose **Open my library**. A mounted NAS folder works like a local folder. Use **Get lyrics** for bulk downloads, a track’s search button for individual matches, and **Edit** for the existing word-timing editor. Export LRC, plain text, or embedded lyrics using the existing export controls. Embedded export remains an experimental setting inherited from LRCGET.

Lyrics stay in the app’s internal storage until you export. Automatic export is optional. Lyripass uses its own application identity (`app.lyripass.desktop`) and starts with a separate database from LRCGET. It does not migrate or replace an existing LRCGET library.

The supplied macOS build is for Apple silicon, signed locally but not notarized. The source retains upstream Windows and Linux support; only macOS has been built for this redesign.

## Development

Install Node.js, Rust, and the [Tauri prerequisites](https://v2.tauri.app/start/prerequisites/).

```sh
npm install
npm run tauri dev
```

A plain browser cannot access the native filesystem or player. Use the Tauri development command for a functioning app.

```sh
npm test
npm run lint
npm run build
npm run tauri build -- --bundles app
```

## What changed

- Lyripass app name, icon, window identity, and About dialog.
- Folder onboarding with a clear explanation of the library workflow.
- Compact collection controls and segmented library navigation.
- A persistent lyrics inspector with clickable lyric cues, individual search, and editing.
- Graphite/coral/sky theme throughout the library, editor, dialogs, and player, with light and dark appearances.
- Empty and no-result library states and accessible labels on track actions.

The underlying scanner, player, lyrics matching, word-sync editor, publication tools, and export queues come from LRCGET. The inherited queue test now advances enough simulated time for the existing download pacing.

## Credits

LRCGET is © Thang Tran and contributors, MIT licensed. Its license is retained in `LICENSE`; the original README is retained in `UPSTREAM.md`. Lyrics are provided by [LRCLIB](https://lrclib.net). Dustalexw’s public app sources informed the visual direction; their code and artwork are not bundled. The Lyripass icon is an original SVG included in `public/lyripass.svg`.
