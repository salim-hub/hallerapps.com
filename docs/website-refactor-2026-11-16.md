# Website refactor — 16 November 2026

## Delivery status

Implemented locally and browser checked. No Git push, production deployment, DNS change, Android modification or certification application was performed. Release is blocked on production data-practice reconciliation and hosting eligibility, not on the static checks below. Existing app-ads.txt changes predate this work and were left intact.

## Architecture and audit

Static HTML/CSS/JS; no framework, package manager, build, lint or test runner exists. CNAME specifies hallerapps.com; origin is github.com/salim-hub/hallerapps.com.git. Existing documentation identifies GitHub Pages hosting. No deployment workflow is tracked; actual Pages account settings, DNS ownership, hosting billing and production headers were inaccessible. No tracker, form backend, cookies or storage API in the website code. Removed Google Fonts requests; system fonts and local artwork now serve the site. Existing verification HTML, robots.txt, app advertising records, CNAME and store package identifiers are preserved.

Issues corrected: mixed website/application privacy; support restricted to two apps; Royal portfolio cross-promotion; internal audit language in Royal legal pages; inconsistent metadata/canonicals/footer; offscreen mobile navigation; empty favicon and manifest; missing custom 404.

## Content and sections

- Home and Apps: coherent dark/green portfolio, factual descriptions, shared generated cards, adult featured-game label, correct game detail URL, app-specific policy links where verified.
- Support: removed entire “Our Applications” list and response-time promises. Universal email support, troubleshooting checklist, sensitive-data warning, official purchase/refund help, compact Royal legal/responsible-play links. No fake form.
- Website Privacy: removed selector, QR tab, Royal listing, “choose a policy” introduction and public technical review notes. Covers operator, GitHub access information, site cookies/tracking, Gmail correspondence, external links, retention/deletion, conditional rights and revision date.
- QR policy migrated intact to /apps/qr-scanner/privacy/. /privacy/#qr-policy and #qr-scanner redirect there with JavaScript. Plain /privacy/ remains website-only. Without JavaScript the old fragment shows the website policy; QR remains accessible directly and through the catalog. Existing external Google Sites policies were not edited or removed.
- Royal landing: exact app title; authentic local art; prominent adult warning and correct Play CTA; source-backed classic actions and optional purchase/ad features; visible full age, entertainment, no-money/no-prize/no-redemption/IAP/ad/success disclosures; practical responsible play with independent Gambling Therapy; compact legal/support links; removed large More Apps section and prevented generator from restoring it.
- Royal Privacy: removed “Details awaiting confirmation” and internal investigation commentary, retaining material SDK, provider, rights, purchase, backup and deletion-limit disclosures. Added source-backed achievement/player-ID processing. Updated 16 November. Terms retain consumer rights and local-wallet recovery limitations; removed reviewed-build editorial language.
- Unified semantic primary navigation, skip links, focus styles, responsive always-visible mobile links, shared operator/email footer, contact refresh with useful fallback, real SVG/ICO favicon, valid manifest, canonical/OG metadata and sitemap including independent policies.

## Application evidence and blockers

Read only: /Users/salimkarsanbas/StudioProjects/HALLER/Royal-Card-Club/. Code is under app/src/main/java/com/haller/royalcardclub, not a root core directory. app/build.gradle.kts declares version 1.3. Prior 14 November repository reports are historical, not proof of the current production binary.

PlayGamesAccount.kt handles authentication. PlayGamesAchievements.kt retrieves currentPlayer.playerId, stores achievements_player_owner_v1 in preferences, uses local wallet counters as an outbox, unlockImmediate/setStepsImmediate, and guards account mismatch. This synchronizes achievement progress, not wallet balances or full saved games. Corrected the old broad claim that no player identity is persisted. No marketing promise of live achievements was added because live-release correspondence is unavailable. Backup XML includes the game preferences file. AnalyticsTracker forwards release events when configured. RewardedAds uses UMP canRequestAds gating and privacy options. Existing Analytics/Crashlytics, startup RevenueCat/Play Billing disclosures remain; Remote Config SDK inclusion does not prove active fetching.

Unresolved before release: exact live binary/source correspondence; external Royal Google Sites policy could not be retrieved; production Firebase retention, consent/withdrawal controls, Remote Config activity, AdMob/UMP settings, RevenueCat integrations, deletion operations, lawful bases and transfer safeguards require operator/console confirmation. Public wording cleanup does not resolve these operational gaps. Do not certify them as verified. No independent legal sign-off performed.

## Store and external checks

Web tool retrieved current listings for Identify AI, LumaSweep, Room Designer, Moneira and QR Scanner, confirming names/packages and existing external policy destinations. Room Designer policy retrieved; other Google Sites destinations were exposed by store links but could not be fetched. Royal and Pomme listing retrieval failed; preserved their valid existing package URLs and prior verification dates, without changing availability based on a tool error. Royal CTA is exactly https://play.google.com/store/apps/details?id=com.haller.royalcardclub. Production hallerapps.com could not be retrieved. QR public listing uses hallerapps@gmail.com for support while developer contact is hallerappsinfo@gmail.com: reconcile in Console if appropriate.

## Google Ads and manual account tasks

Official sources read 16 November 2026:
- https://support.google.com/adspolicy/answer/15132179
- https://support.google.com/adspolicy/answer/17199930 (posted July 13, effective September 14)
- https://support.google.com/googleplay/answer/2479637

Website content addresses simulated entertainment, adult/legal age, no minors-oriented promotion, no money/prizes, purchases, no redemption, genuine operator/contact and accessible legal/responsible-play information. No unrelated gambling brands or fake certification were introduced. Campaigns, all app locales, ad creatives and served third-party advertisements still require review.

The current main policy excludes sites hosted on free platforms. The September update reiterates no free subdomains, direct business domain ownership/control, domain relevance and account/MCC policy health. Custom-domain GitHub Pages does not itself prove compliance. Obtain an explicit Google determination on this arrangement and actual plan; if ineligible, migrate to eligible hosting while retaining domain and all routes. Verify registrar control, DNS records, HTTPS and Pages configuration with account access. No automatic DNS/hosting migration is justified by the evidence.

Submit Social Casino certification through Google Ads account; choose eligible countries and Group 1 or 2, check local distribution licensing where applicable, and account/MCC policy health. Türkiye is absent from the retrieved social-casino country list. Do not infer campaign geography from operator address. No certification granted or guaranteed.

Play Console: reconcile Data safety with actual SDK/player-ID/achievement flows and retention/deletion, keep adult target audience, verify current store website/policy URLs. Once policies are production-accurate and deployed, update the privacy URL to /apps/royal-blackjack/privacy/ and align the external policy. AppConstants.kt still links Google Sites Privacy/Terms; change only in a separately authorized app release. Do not change IARC artificially.

## Executed validation

- python3 scripts/generate-app-cards.py: pass, seven cards on each portfolio page; never touches Royal landing.
- python3 scripts/check-site.py: pass, ten pages, local links/assets/fragments, single h1, duplicate IDs, image dimensions/alt, privacy separation and essential game disclosures.
- node --check assets/js/main.js: pass.
- git diff --check: pass.
- Browser: all eight principal routes at 360, 768 and 1440px; no horizontal overflow. Home desktop and Royal tablet visually inspected. No broken image detected at mobile width. No captured console warnings/errors. Contact lands on Support; legacy QR hash lands on dedicated policy. Custom 404 rendered directly; GitHub production unknown-route behavior remains a deployment check.
- One batch navigation timed out; resumed successfully and rechecked tablet/desktop routes at confirmed viewport dimensions.
- No npm build/lint/test commands exist. Browser checks are focused checks, not a complete WCAG or performance certification; real-device, email delivery, purchase and production smoke tests remain manual.

## Files

- `404.html`
- `app-ads.txt` — pre-existing user change; untouched.
- `apps/index.html`
- `apps/qr-scanner/privacy/index.html`
- `apps/royal-blackjack/index.html`
- `apps/royal-blackjack/privacy/index.html`
- `apps/royal-blackjack/terms/index.html`
- `assets/css/legal.css`
- `assets/css/style.css`
- `assets/favicon.svg`
- `assets/js/main.js`
- `contact/index.html`
- `data/apps.json`
- `docs/website-refactor-2026-11-16.md`
- `favicon.ico`
- `index.html`
- `manifest.json`
- `privacy/index.html`
- `scripts/check-site.py`
- `scripts/generate-app-cards.py`
- `sitemap.xml`
- `support/index.html`
