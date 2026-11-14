# Royal Blackjack certification readiness — 14 November 2026

This review supersedes earlier reports **only** on confirmed controller identity:
the owner explicitly confirmed that Salim Karşanbaş is the operator/data controller
and authorised publication of the postal address displayed on Google Play.
No licence or regulatory authorisation has been asserted.

## Website release

- Kept the existing policy, structure, routes and original Important Information.
- Added adult eligibility and a no-money/no-prize/no-redemption/IAP/ad summary
  next to the download CTA, with direct Privacy, Terms, Support and responsible
  play links. Added a responsible-play section and independent support resource.
- Clarified Analytics approximate location/purchase events, AdMob identifiers,
  recipient data flows and practical limits of pseudonymous deletion requests.
- Privacy identifies the confirmed legal person, postal address and email.
  Royal landing/privacy/terms footers identify the operator and email.
- The entire general /privacy/ page, including QR policy, is byte-identical to
  the start of this task. No Android application code or SDK config changed.

## Evidence available for application declarations

| Declaration | Verification | Remaining scope |
| --- | --- | --- |
| Adult/legal gambling age only | Owner confirmation, website disclosures, Android English disclaimer used by LobbyScreen, ChipStoreScreen and ProfileScreen | Confirm all shipped locales and live binary; campaign must not target minors. No identity/age-verification feature verified; Google’s disclaimer requirement does not itself mandate a particular technical age gate. |
| No real-money gambling or prizes of real-world value | Owner confirmation, source virtual-chip gameplay and shared disclaimer; clear website statements | No live APK or all ad creatives reviewed. |
| Chips cannot be redeemed for cash/prizes | Shared app disclaimer, local wallet, Terms and landing | Do not imply external redemption or financial returns in campaign creative. |
| Optional in-app purchases | Consumable chip-store implementation, RevenueCat startup/reconciliation, Play Billing, disclaimer and website | Active products/receipts and Play Console configuration not tested. |
| Optional rewarded ads | AdMob rewarded implementation only on user watch action, UMP canRequestAds gate, local reward-credit flow | Active AdMob/UMP console settings, mediation and real ad deliveries not independently tested. |
| Analytics/identifiers disclosed | Firebase Analytics custom release events, Crashlytics dependencies/config and source; Google SDK disclosures | Live data traffic, property retention/consent and provider-side integrations unavailable. Remote Config dependency confirmed; active fetching not found. |
| Controller identity/contact | Public developer listing plus explicit owner confirmation in this task | No inferred company registration or licence number. |
| Working store/policy/support destinations | HTTP, HTML anchors and local/browser checks | Mailbox delivery and support response time not tested. |

## App changes / operational actions still required

1. **App document links:** `utils/AppConstants.kt` still points Privacy and Terms
   to Google Sites. Update to the new hallerapps.com routes in an authorised app
   release and change the Play Console policy link; this website task did not
   modify the Android project. Old online text differs from reviewed release
   event forwarding, production-ad properties, startup RevenueCat and Play Games.
2. **Firebase consent and withdrawal:** no setConsent, collection-disable or
   separate in-app Analytics/Crashlytics setting was found. Where required,
   implement appropriate consent before collection and a withdrawal/control flow.
   AdMob UMP does not automatically control Firebase. Verify applicability for
   each target country rather than asserting universal consent compliance.
3. **Deletion:** implement/verify a real process to locate pseudonymous records,
   process requests and coordinate with providers, respecting required retention.
   Android local clearing and an email address are not proof of SDK data deletion.
4. **Live release:** verify exact source/version-to-Play-binary correspondence,
   merged manifest, locales, runtime disclosures, real purchase/ad behavior and
   all actual third-party processing. No app installation/run was performed.

## Play Console / business confirmations

The public Data safety page checked in this task still declares “No data collected”,
“Diagnostics” shared for Analytics and “Data can't be deleted”. This conflicts
with, or leaves unexplained, the documented SDK/event flows and privacy-request
route. Reconcile using Play definitions and exceptions for the exact live release;
do not blindly mark every SDK data type as sharing or declare that a policy edit
has fixed Data safety. Private Play Console was not accessed.

Confirm Analytics retention, Crashlytics handling, AdMob UMP/personalisation,
RevenueCat offerings/integrations, legal grounds, transfers and actual operational
retention. No unverified deadline or transfer agreement has been invented.

## Google Ads policy comparison

Source read: https://support.google.com/adspolicy/answer/15132179?hl=en
Social-casino section requires legal-gambling-age disclaimers, no minors, no
real-money gambling/real-world prizes, IAP disclosure, no real-money casino
branding, certification for supported territories, and distribution licensing
where applicable. Website statements cover these content topics; no Google Ads
approval, campaign setting or local licence has been verified.

Additional eligibility matters must not be omitted from the application review:

- Target countries and Group 1/2 selection must match Google's current list;
  Türkiye is not listed as a social-casino advertising destination. No target
  countries were specified by the owner. Do not infer them from the postal address.
- Ads, actual app/screenshots and supplied assets require real-money-brand review;
  absence throughout third-party served ads was not established by website checks.
- The current policy also says certification is unavailable for sites hosted on
  free platforms or third-party-host subdomains. This site uses its own domain
  with GitHub Pages; paid/free hosting eligibility was not verified. Obtain a
  Google determination or use demonstrably eligible hosting before confirming
  that declaration. No hosting migration was performed or assumed necessary.
- A licence number must be shown only when actually applicable, verified and
  supplied. A social-casino policy is not evidence that a gambling licence exists.
- Certification requests are submitted through the Google Ads account under the
  current social-casino process. No certification form was submitted in this task.

SDK primary references:
https://support.google.com/analytics/answer/11582702?hl=en
https://developers.google.com/admob/android/privacy/play-data-disclosure

Conclusion: web content and links are improved; unresolved app, Console and
business assertions must not be confirmed as already satisfied in an application.
