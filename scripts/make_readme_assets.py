#!/usr/bin/env python3
"""Regenerate Lyripass's SVG README header and badges with Python's standard library."""
from pathlib import Path
import html
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
VERSION = json.loads((ROOT / 'package.json').read_text())['version']
FONT = '-apple-system, BlinkMacSystemFont, Segoe UI, Arial, sans-serif'


def badge(filename, label, value, color):
    label_width = max(76, len(label) * 7 + 26)
    value_width = len(value) * 7 + 28
    width = label_width + value_width
    (DOCS / filename).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="30" viewBox="0 0 {width} 30" role="img" aria-label="{html.escape(label + ': ' + value)}">
  <title>{html.escape(label + ': ' + value)}</title>
  <defs><clipPath id="r"><rect width="{width}" height="30" rx="6"/></clipPath></defs>
  <g clip-path="url(#r)"><path fill="#20222c" d="M0 0h{width}v30H0z"/><path fill="{color}" d="M{label_width} 0h{value_width}v30H{label_width}z"/></g>
  <g font-family="{FONT}" font-size="10" font-weight="700" text-anchor="middle" letter-spacing=".8"><text x="{label_width / 2}" y="19" fill="#f5f1ea">{html.escape(label)}</text><text x="{label_width + value_width / 2}" y="19" fill="#0b0d12">{html.escape(value)}</text></g>
</svg>\n''')


def main():
    DOCS.mkdir(exist_ok=True)
    icon = (ROOT / 'public' / 'lyripass.svg').read_text()
    inner = re.sub(r'^.*?<svg[^>]*>', '', icon, count=1).rsplit('</svg>', 1)[0]
    bars = []
    for index in range(23):
        t = index / 22
        height = 160 + 290 * math.sin(math.pi * t) * (.6 + .4 * abs(math.cos(index * 1.35)))
        rgb = tuple(round(a + (b - a) * t) for a, b in zip((255, 90, 78), (92, 200, 255)))
        bars.append(f'<rect x="{1910 + index * 28}" y="{390 - height / 2:.1f}" width="14" height="{height:.1f}" rx="7" fill="rgb{rgb}" opacity=".22"/>')
    (DOCS / 'readme-header.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="2560" height="760" viewBox="0 0 2560 760" role="img" aria-labelledby="title description">
  <title id="title">lyripass — Every word, in time.</title>
  <desc id="description">A graphite banner with the Lyripass waveform icon, a cream and coral wordmark, and a coral-to-sky waveform. Synced lyrics for your collection, powered by LRCGET and LRCLIB.</desc>
  <defs>
    <linearGradient id="backdrop" x2="0" y2="1"><stop stop-color="#20242e"/><stop offset="1" stop-color="#0b0d12"/></linearGradient>
    <radialGradient id="coral-glow"><stop stop-color="#ff5a4e" stop-opacity=".12"/><stop offset="1" stop-color="#ff5a4e" stop-opacity="0"/></radialGradient>
    <radialGradient id="sky-glow"><stop stop-color="#5cc8ff" stop-opacity=".12"/><stop offset="1" stop-color="#5cc8ff" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="2560" height="760" fill="url(#backdrop)"/>
  <ellipse cx="550" cy="300" rx="1000" ry="620" fill="url(#coral-glow)"/>
  <ellipse cx="2270" cy="470" rx="930" ry="670" fill="url(#sky-glow)"/>
  {''.join(bars)}
  <svg x="100" y="178" width="400" height="400" viewBox="0 0 1024 1024">{inner}</svg>
  <g font-family="{FONT}">
    <rect x="2000" y="62" width="248" height="54" rx="27" fill="#0e1015" stroke="#96a0b0" stroke-opacity=".35" stroke-width="2"/>
    <circle cx="2031" cy="89" r="8" fill="#5cc8ff"/>
    <text x="2053" y="98" font-size="25" fill="#f5f1ea">macOS build</text>
    <rect x="2265" y="62" width="180" height="54" rx="27" fill="#ff5a4e" fill-opacity=".12" stroke="#ff5a4e" stroke-opacity=".5" stroke-width="2"/>
    <text x="2355" y="98" text-anchor="middle" font-size="25" font-weight="600" fill="#ff5a4e">v{html.escape(VERSION)}</text>
    <text x="614" y="224" fill="#5cc8ff" font-size="25" font-weight="700" letter-spacing="2.8">SYNCED LYRICS · A DUSTALEXW APP</text>
    <text x="605" y="383" fill="#f5f1ea" font-size="164" font-weight="750" letter-spacing="-8">lyri<tspan fill="#ff5a4e">pass</tspan></text>
    <text x="614" y="473" fill="#f5f1ea" font-size="47" font-weight="500" letter-spacing="-.8">Every word, in time.</text>
    <text x="614" y="529" fill="#96a0b0" font-size="28">Find synced lyrics. Fine-tune the timing. Keep them with your music.</text>
    <g font-size="23" fill="#f5f1ea">
      <rect x="614" y="585" width="278" height="54" rx="27" fill="#ffffff" fill-opacity=".035" stroke="#ffffff" stroke-opacity=".12"/>
      <circle cx="644" cy="612" r="8" fill="#ff5a4e"/><text x="665" y="620">Built on LRCGET</text>
      <rect x="908" y="585" width="273" height="54" rx="27" fill="#ffffff" fill-opacity=".035" stroke="#ffffff" stroke-opacity=".12"/>
      <circle cx="938" cy="612" r="8" fill="#5cc8ff"/><text x="959" y="620">Lyrics by LRCLIB</text>
      <rect x="1197" y="585" width="294" height="54" rx="27" fill="#ffffff" fill-opacity=".035" stroke="#ffffff" stroke-opacity=".12"/>
      <circle cx="1227" cy="612" r="8" fill="#7ed6b8"/><text x="1248" y="620">LRC · TXT · embedded</text>
    </g>
  </g>
</svg>\n''')
    badge('badge-version.svg', 'VERSION', 'V' + VERSION, '#ff5a4e')
    badge('badge-build.svg', 'BUILD', 'MACOS APP', '#5cc8ff')
    badge('badge-license.svg', 'LICENSE', 'MIT', '#7ed6b8')
    print('Generated the README header and three badges.')


if __name__ == '__main__':
    main()
