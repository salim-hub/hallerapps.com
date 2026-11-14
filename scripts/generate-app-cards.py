"""Render the shared app card template as crawlable, buildless HTML."""
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS = json.loads((ROOT / 'data/apps.json').read_text())


def card(app, heading):
    royal = app['slug'] == 'royalcardclub'
    featured = '<span class="catalog-featured">Featured game · Adults only</span>' if royal else ''
    details = '<a class="card-link" href="/apps/royal-blackjack">Explore the game →</a>' if royal else ''
    return f'''<article class="card app-card{' app-card-featured' if royal else ''}">
    <div class="app-card-top">
        <img class="catalog-icon" src="{escape(app['image'])}" alt="{escape(app['name'])} app icon" width="80" height="80" loading="lazy" decoding="async">
        {featured}
    </div>
    <div class="card-content">
        <{heading}>{escape(app['name'])}</{heading}>
        <p>{escape(app['description'])}</p>
    </div>
    <div class="app-actions">
        <a class="button" href="{escape(app['url'])}">Get it on Google Play<span class="sr-only"> — {escape(app['name'])}</span></a>
        {details}
    </div>
</article>'''


for file, slot in [('index.html', 'home'), ('apps/index.html', 'catalog'), ('apps/royal-blackjack/index.html', 'more')]:
    more = slot == 'more'
    apps = [app for app in APPS if not more or app['slug'] != 'royalcardclub']
    title = 'More Apps by Haller Apps' if more else 'Our Apps'
    cards = '\n'.join(card(app, 'h3' if slot != 'catalog' else 'h2') for app in apps)
    intro = '' if slot == 'catalog' else f'<div class="catalog-heading"><span class="badge">Explore Haller Apps</span><h2 id="{slot}-apps-title">{title}</h2><p>Find your next everyday essential.</p></div>'
    label = 'aria-label="Our applications"' if slot == 'catalog' else f'aria-labelledby="{slot}-apps-title"'
    output = f'<section class="app-catalog container" {label}>\n{intro}\n<div class="app-grid">\n{cards}\n</div>\n</section>'
    output = '\n'.join(line.rstrip() for line in output.splitlines())
    path = ROOT / file
    source = path.read_text()
    start, end = f'<!-- APP_CATALOG:{slot}:START -->', f'<!-- APP_CATALOG:{slot}:END -->'
    source, count = re.subn(re.escape(start) + r'.*?' + re.escape(end), lambda _: start + '\n' + output + '\n' + end, source, flags=re.S)
    assert count == 1, f'Missing catalog slot: {file}'
    path.write_text(source)
    print(f'Rendered {len(apps)} cards: {file}')
