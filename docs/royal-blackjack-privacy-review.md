# Royal Blackjack privacy and terms evidence — 14 November 2026

## Scope

Website-only changes. Android sources were read at the user-provided
`/Users/salimkarsanbas/StudioProjects/HALLER/Royal-Card-Club/` path and were not
modified. Reviewed source declares package com.haller.royalcardclub, version 1.2
(versionCode 4). Correspondence to the live Play binary is not established.

## Verified evidence

- `app/build.gradle.kts`: Firebase Crashlytics/Remote Config, Mobile Ads, UMP,
  RevenueCat and Play Games dependencies; production ads gated on valid build
  properties. `gradle.properties` contains production-format ad and games IDs.
  Presence is not proof of console activation or a functioning ad inventory.
- `analytics/build.gradle.kts`: Firebase Analytics, advertising-ID and install
  referrer dependencies. No standalone app install-referrer reporting flow found.
- `core/analytics/AnalyticsTracker.kt` and `analytics/.../EventManager.kt`: debug
  local logging; release custom game events forwarded to Firebase when configured.
  This contradicts the older online policy's debug-only custom analytics claim.
- `RoyalCardClubApplication.kt`, `core/store/ChipStoreRepository.kt`,
  `paywall/.../PaywallsRepositoryImpl.kt`: RevenueCat configured at startup with
  generated app-user ID; products and customer transactions queried; Google Play
  consumable purchases verified/reconciled. Additional RevenueCat diagnostics
  enabled only in debug. Do not claim service contact occurs only after purchase.
- `core/ads/RewardedAds.kt`: user-initiated AdMob rewarded ads, UMP gate and
  required privacy-options entry point; local pending reward UUID and retry;
  no automatic gameplay ads in this flow. Reward completion does not require
  advertisement clicks. No separate Firebase consent/disable control found.
- `core/games/PlayGamesAccount.kt`: conditional Play Games sign-in, in-memory
  status, no persistent player identity in this component; no progress sync.
- `core/data/SettingsRepository.kt`, `WalletStore.kt`: local preferences,
  game/wallet state, statistics, recovery and credited-transaction ledger.
- `app/src/main/AndroidManifest.xml`: app-level internet/vibration permissions,
  backup enabled; SDK manifest contributions require merged-release review.
- `res/xml/backup_rules.xml`, `data_extraction_rules.xml`: game preferences file
  can be backed up/transferred; separate pending-ad-reward preferences excluded.
- `utils/AppConstants.kt`: current app links remain Google Sites policy/terms.
- Adult eligibility, no real-money gambling, no real-world prizes, non-redeemable
  chips and optional purchases/ads were explicitly confirmed by the owner earlier
  in this chat and are consistent with the existing legal documents/game flows.

## Public sources read

- Google Play detail and Data safety pages for com.haller.royalcardclub.
- Existing policy: https://sites.google.com/view/royalcardclubprivacy/home
- Existing Terms: https://sites.google.com/view/royalcardclubterms/home
- https://firebase.google.com/support/privacy
- https://developers.google.com/admob/android/privacy/play-data-disclosure
- https://support.google.com/googleplay/answer/2479637?hl=en
- https://support.google.com/adspolicy/answer/15132179?hl=en

## Pending operator verification / certification blockers

1. Play Data safety currently says no data collected, diagnostics shared for
   analytics, and data cannot be deleted. Reconcile against the actual release,
   Firebase events, SDK identifiers, ads, purchases, and privacy-request process.
2. Verify live release matches the supplied source. Existing Google Sites
   policies are stale on custom release analytics, production-ad configuration,
   startup RevenueCat access and Play Games. Update them or migrate the app and
   Play Console links to the new canonical pages. No Android/Console changes
   were made in this website task.
3. Confirm Analytics property retention and consent controls, Crashlytics
   handling, active Remote Config use, AdMob/UMP privacy-message configuration,
   personalisation/mediation and RevenueCat offerings/server-side integrations.
4. Confirm lawful grounds, operator's legal identity, applicable transfer
   safeguards, processing locations and actual retention/deletion procedure.
   No legal entity identifier, licence, transfer contract or retention duration
   has been invented. Brand/contact are provided; legal identity is pending.
5. Source has no separate Firebase collection/withdrawal setting. Validate
   required consent before enabling processing in each target territory. UMP
   ad consent is not Firebase consent. Website text cannot repair app behavior.
6. Validate adult targeting/eligibility in the app and campaign, supported
   countries, and any applicable distribution authorisations. No Google Ads
   certification or licensing approval is claimed by this release.

## Website changes

New /apps/royal-blackjack/privacy/ and /terms/ with title, description, canonical,
Open Graph, static HTML, table of contents and responsive shared styling.
Royal landing page links to both; general privacy page links to app privacy;
support includes Royal gameplay/purchase/privacy assistance; sitemap updated.
Existing QR policy and website policy/tab content preserved byte for byte.
Existing Social Casino Important Information preserved byte for byte.
