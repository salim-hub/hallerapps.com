# Royal Blackjack website release

The existing site is buildless HTML/CSS/JavaScript, using folder/index.html routes,
Inter typography and shared CSS variables. No framework, dependency installation,
or compiled production build is required. Git origin is the existing
salim-hub/hallerapps.com repository; CNAME remains hallerapps.com.

New route: /apps/royal-blackjack (directory hosting may redirect to trailing slash).
The page uses static HTML, a canonical URL, title/description, Open Graph metadata,
and visible disclosures. Home and /apps/ link to it and to the supplied Play URL.

Content evidence: the owner explicitly confirmed all five requested disclosures
in this chat on 2026-11-14. The game source was not available for independent
verification. No additional gameplay features have been claimed.

Official icon source: og:image from
https://play.google.com/store/apps/details?id=com.haller.royalcardclub&hl=en&gl=US
Downloaded 2026-11-14 from Google Play's play-lh.googleusercontent.com CDN.

Checks: local page HTTP 200 after directory redirect; Google Play HTTP 200;
all local HTML href/src targets exist; sitemap XML parses; JavaScript syntax and
git diff whitespace checks pass. Browser checks cover landing page desktop/mobile,
visible disclosures, home-to-page navigation, and application catalog.
Existing privacy/support/contact source content is preserved.

Before certification: provide a Royal Blackjack-specific privacy policy and any
applicable Terms from approved actual documents. Current privacy page covers the
website and QR app, not Royal Blackjack; no policy or Terms have been invented.
Review target-country eligibility, campaign adult targeting and certification
requirements in Google's current Social casino games policy:
https://support.google.com/adspolicy/answer/15132179?hl=en
Website changes do not constitute certification approval.

Existing local app-ads.txt modifications are outside this release and preserved.

## Full application catalog — 2026-11-14

Verified the developer page (id=9167703004087120294), then all eight requested
package detail pages with hl=en&gl=US. All returned HTTP 200, appeared in the
developer catalog, and linked back to the supplied developer ID. No requested
application was inaccessible. The developer page also lists com.haller.loca;
it is outside the requested eight-app scope and has not been added.

`data/apps.json` retains official titles, short store descriptions, package IDs,
icon source URLs and verification date. Royal Blackjack's current store title
is Royal Blackjack: 21 Card Game. No extra features were invented.

Icons are hosted in assets/images-apps as 512x512 lossless WebP files; total
catalog icon weight is approximately 1.37 MB, reduced from 2.84 MB PNG downloads.
The existing Royal PNG remains available for its original hero and OG URLs.

Regenerate the shared static card component with:

    python3 scripts/generate-app-cards.py

This requires only the Python standard library and emits checked-in HTML for
home (8 cards), /apps/ (8 cards) and Royal's More Apps section (7 cards).
No runtime framework or dependency was added. Existing GitHub Pages automatic
build/deploy remains the production pipeline.

Validation: correct card counts and local assets; deterministic regeneration;
JavaScript syntax; whitespace; unchanged SEO heads and byte-identical Royal
Important Information block; browser desktop 1440px (3 columns) and mobile
390px (1 column, no horizontal overflow), including More Apps.

## Royal Blackjack legal pages — 14 November 2026

Added /apps/royal-blackjack/privacy/ and /apps/royal-blackjack/terms/, with visible
links on the landing page, an app-policy entry on /privacy/, Royal support on
/support/, and sitemap entries. Shared legal.css preserves the existing design.

The owner supplied the Android source path for this release. Verified Firebase
Analytics/Crashlytics, AdMob/UMP, RevenueCat/Play Billing, local storage/backup and
Play Games flows. See docs/royal-blackjack-privacy-review.md for evidence and
pending configuration/legal details. No SDK, controller identity, licence or
retention duration was invented. Android sources and Play Console were not changed.

Checks: original website/QR policy tabs and Royal Important Information unchanged
byte for byte; all local HTML links/assets resolve; sitemap XML; one H1 per new
page; no nested paragraphs; JavaScript syntax; git diff whitespace. Browser QA:
new policies desktop/mobile, no horizontal overflow, working privacy table of
contents, and QR policy tab remains usable. Existing static deployment pipeline
remains GitHub Pages; no package build system or dependency was introduced.
