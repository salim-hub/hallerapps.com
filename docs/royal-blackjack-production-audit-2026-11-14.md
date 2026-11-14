# Haller Apps production audit — 14 November 2026

## Result

The site is reachable, but this audit does **not** establish certification readiness.
The legal operator identity, live release configuration, Data safety discrepancies,
consent and deletion procedures remain unresolved. Public Play data is the visible
published declaration; authenticated Play Console settings were not accessible.

## Production HTTP and link checks

| Page | Initial production status |
| --- | --- |
| https://hallerapps.com/ | 200 |
| https://hallerapps.com/privacy/ | 200 |
| https://hallerapps.com/apps/royal-blackjack/ | 200 |
| https://hallerapps.com/apps/royal-blackjack/privacy/ | 200 |
| https://hallerapps.com/apps/royal-blackjack/terms/ | 200 |
| https://hallerapps.com/support/ | 200 |

Fetched HTML for each page and inspected every same-domain href/src. All 21
unique internal destinations/assets returned final HTTP 200. All 25 fragment
links resolved to existing IDs. Directory links without a trailing slash can
redirect to their slash form. mailto links are addresses, not HTTP endpoints;
email delivery and support response times were not tested. The Google Play
Royal link returns HTTP 200 and identifies com.haller.royalcardclub.

## Eight requested Royal checks

| Check | Finding |
| --- | --- |
| SDK and data disclosures | Substantially consistent with supplied source: Firebase Analytics release events, Crashlytics, AdMob/UMP, startup RevenueCat/Google Play Billing, local wallet/backup and Play Games. Exact live binary, console configuration and all provider-side integrations are unverified. Remote Config inclusion is disclosed without claiming active fetching. |
| Terms complete and accessible | HTTP 200, static HTML, linked from landing/privacy/support. Requested adult entertainment, no real-money gambling, chips/no redemption, optional purchases, refunds, responsible play and contact sections exist. This is scope coverage, not a legal opinion that a complete enforceable agreement exists in every jurisdiction. |
| Legal gambling age | Landing page visibly states legal gambling age only. Terms/privacy additionally specify 18 or local legal gambling age, whichever is higher. Source does not establish identity/age verification. |
| Responsible play/support | Landing says Play responsibly; Terms advise breaks/time/spending limits. Support includes gameplay/purchase/privacy assistance. Added an independently verified Gambling Therapy link to support and Terms; not a claim of affiliation or built-in self-exclusion. |
| No cash redemption | Explicit on landing and Terms: chips have no monetary value and cannot be redeemed for cash or real-world prizes. |
| Purchases and rewarded ads | Both explicitly disclosed on landing and in Terms/privacy; purchases optional, ads user initiated. |
| Controller identity/contact | Brand Haller Apps and hallerappsinfo@gmail.com exist. A verified legal natural-person/entity identity and postal contact address are **not** supplied in the policy. Public Play developer identity is not by itself proof of legal controller identity or permission to substitute it. Owner confirmation is needed. |
| Play destination | Real visible anchor, correct package, no nofollow, HTTP 200. Published store still links the older Google Sites privacy document. |

## Public Data safety comparison

Source: https://play.google.com/store/apps/datasafety?id=com.haller.royalcardclub&hl=en&gl=US

| Published Play declaration | Website/source evidence | Action |
| --- | --- | --- |
| No data collected | Analytics custom release events and SDK identifiers, Crashlytics diagnostics, AdMob and RevenueCat processing are documented/implemented. | Review all SDK collection under Play definitions, exceptions and the actual released version; do not simply copy a generic SDK checklist or change the policy to claim zero collection. |
| Diagnostics shared, purpose Analytics | Website also explains advertising identifiers/interactions, purchase information and other providers. | Determine collection versus sharing and applicable service-provider exceptions per actual configuration. Current public declaration alone does not verify completeness. |
| Data can't be deleted | Policy provides email requests and local Android deletion but no automatic provider deletion guarantee. | Verify operational request handling and provider workflows; align Play declaration with what can actually be deleted. An email link alone does not prove a deletion process. |
| Encrypted in transit | Provider HTTPS connections are used in source; live traffic for every SDK was not captured. | Validate released network behavior before treating the Play claim as independently verified. |

The source was read at the owner-supplied Royal-Card-Club path, not modified.
Earlier source review evidence is in royal-blackjack-privacy-review.md.
No live SDK traffic, Firebase/AdMob/RevenueCat console or production APK was inspected.

## Corrections in this release

1. General /privacy/ QR tab no longer states that Firebase collects no personal
   identifiers or exclusively non-personal aggregated information. It describes
   app-instance/ad identifiers, event data, configuration/consent dependencies
   and potential personal-data status. No Crashlytics use is invented for QR.
2. Narrowed the contradictory QR blanket no-personal-data statement so local
   scanning is distinguished from SDK telemetry. Scan/generation/PDF features,
   other apps and the QR tab structure remain unchanged. QR event payloads and
   production configuration require its own source review.
3. Website policy no longer claims all browsing involves no personal information
   or invents host log deletion periods. GitHub Pages and external Google Fonts
   connection processing are explained with provider links.
4. Added independent Gambling Therapy resources to Terms and Royal support.
   Existing Royal Important Information statements are unchanged.

## Certification-related gaps, separately

1. **Identity/privacy completeness:** obtain verified legal controller name,
   contact/address details, lawful bases, applicable transfers, actual retention
   and deletion process. Pending fields mean the policy is not finalised.
2. **Data safety mismatch:** reconcile published Play answers with the exact live
   release and SDK data. Only public declaration inspected, not a private form.
3. **Consent:** no separate Firebase consent/withdrawal control was found in the
   reviewed source. AdMob UMP does not establish Analytics consent. Required
   jurisdiction-specific consent behavior must be checked in the app.
4. **Document consistency:** app source and Play listing still link older Google
   Sites policies, which differ from current source on release analytics,
   production-ad configuration, RevenueCat startup access and Play Games. Update
   links/documents through an authorised app/Play Console change.
5. **Google Ads eligibility:** supported target country/group, adult targeting,
   certification status and any locally required distribution licence remain
   unverified. Website disclaimers alone do not establish eligibility. No
   licence number, approval or operator legal identity has been invented.
6. **Game/ad destination review:** no actual app session or ad creative review
   was performed. Validate the required adult/no-real-money/no-real-world-prize
   disclosures in the actual app and confirm no real-money casino branding.
   Site visible text contains the required disclosures; asset-wide trademark
   clearance and absence of third-party branding inside delivered ads are not
   independently established by this audit.

Social-casino requirements reference:
https://support.google.com/adspolicy/answer/15132179?hl=en
The social-casino section requires adult disclaimers, no real-money gambling or
real-world prizes, IAP disclosure, certification in supported countries and
applicable local distribution authorisations. Responsible-play resources improve
user support; this audit does not portray a specific support URL as a universal
social-casino certification requirement.

Other primary references:
https://support.google.com/analytics/answer/11593727
https://support.google.com/analytics/answer/9234069
https://developers.google.com/admob/android/privacy/play-data-disclosure
https://firebase.google.com/support/privacy
https://gamblingtherapy.org/
