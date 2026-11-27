# Scout log

One entry per Friday run, newest at the bottom.

## 2026-11-07 (Sat, ISO week 45 → group B)
- Searches: ~40 WebSearch (14 broad + 15 group-B company combos + ~11 lookups for employer posting pages) — over the ~30 target because many leads were aggregator-only.
- Candidates looked at: 14 opened. Suggested: 3 (Uline, Love's Travel Stops, Viget). Rejected: 9 (recorded in seen.json).
- Top reject reasons: closed/filled or deadline passed (KC Current UX, John Deere, Duke Energy, Global Prairie, Kohl's); past or in-progress term (KC Current GD, KC Mavericks); too much experience (Lockton); stale (Royals 2023).
- Skipped, not recorded (no employer page found; retry next week): Amazon UX Designer Intern Summer 2027, Dick's Sporting Goods Product Design (UX) Summer 2027, Minnesota Star Tribune UX Internship Summer 2027, Wellabe Customer Engagement UX Intern Summer 2027, Trek UX/UI Design Intern.
- Issues: Workday pages can't be fetched from search-only rules (Duke Energy, Uline links came via job boards). Board publish was refused twice because the board was being edited live; merged onto the newest version each time (Version 112), no edits lost.

## 2026-11-13 (Fri, ISO week 46 → group C)
- Searches: 39 WebSearch (14 broad + 14 group-C company combos + 11 lookups for employer posting pages).
- Candidates looked at: 17 opened. Suggested: 5 (Gallup, Landor, Berlin Packaging, Immuta, Pattern). Rejected: 11 (recorded in seen.json).
- Top reject reasons: past term / Summer 2026 posting (VML, Workshop, Klaviyo, Sigma x2, Quantum Workplace); closed (JLL, Mars, GE Appliances, Tyson); not a design role (United Airlines Menu Design, Tyson MCD).
- Skipped, not recorded (no employer page found; retry next week): State Farm Summer 2027 UX Designer intern, Minnesota Star Tribune UX Internship Summer 2027 (2nd week), Workiva Spring/Summer 2027 Brand Design intern, Learning Resources Junior Graphic Designer.
- Group-C watch list was mostly quiet: no design postings found for Willoughby, Sporting KC, Oracle Health, American Century, Enterprise, Centene, Atomicdust, Bailey Lauerman, Buildertrend, Medtronic, U.S. Bank, Colle McVoy, Martin Williams, Northwestern Mutual (2027 UX not yet posted), Southwest, Western Union.
- Board published cleanly (Version 123), no conflict. Public index.html unchanged (only queue items added).

## 2026-11-19 (Thu, ISO week 47 → group D)
- Job boards: The Brand Identity (https://the-brandidentity.com/jobs) could NOT be checked — the fetch was blocked because its permission prompt went unanswered in this unattended run. No roles read from it.
- Searches: 32 WebSearch (14 broad + 14 group-D company combos + 4 employer-page lookups).
- Candidates looked at: 36 fetch attempts (12 failed or showed no content). Suggested: 3 (Mortenson, T-Mobile, Kettle). Rejected: 19 (recorded in seen.json).
- Top reject reasons: term past / Summer 2026 or older (One Design Co, Smartly, Walker Sands, Paradowski, m+a, GoFundMe, Carta, Capsule); no longer live (Workshop 2027, Ogilvy x2, AbelsonTaylor, Circa); not a design role (Polaris engineering/operations, Prophet media); not for undergrads (Prophet Design Intern); stale (Swanson Russell 2019 posting).
- Skipped, not recorded (retry next week): Nationwide UX Designer Internship Summer 2027 (no employer page found); O'Reilly UX Designer I, Ogilvy greenhouse 4634007005, Sporting KC Graphic Designer (teamworkonline 2189632), Gravis Robotics Design Internship, Polaris R31548/R31550/R31551/R31552 (one may be a CMF & Graphics intern) — fetch failed; Edward Jones 23843475/23843479 (page rendered no content); Wayground/Skillet Product Design Intern (no location/term/pay stated); defense-tech 2027 Early Career Associate Product Designer, Costa Mesa (ixdf, employer hidden); Minnesota Star Tribune UX Summer 2027 (3rd week, no employer page).
- Board published cleanly (Version 140), no conflict. Public index.html unchanged (only queue items added).

## 2026-11-19 (Thu, manual run started by Titus to try The Brand Identity board; ISO week 47 → group D)
- Job boards: The Brand Identity (https://the-brandidentity.com/jobs) was blocked again. WebFetch returned PROVENANCE_REQUIRED because the fetch permission prompt for that site went unanswered. No roles read. I didn't retry or try any workaround.
- Searches: 0 new. The full group-D and broad search set ran earlier today (see entry above), so a second identical pass would have repeated the same results. Every candidate rejected earlier today is already in seen.json.
- Board: re-read and unchanged since this morning's publish (Version 140). No new suggestions, nothing published, and index.html is unchanged.

## 2026-11-19 (Thu, by hand in Titus's chat)
- The Brand Identity checked by hand after the scheduled run couldn't open it: 23 roles. Suggested 1 (.raw Digital Design Internship: remote, € pay, closes Dec 2). Rejected Little Plains Product Designer and Digital Brand Designer (tagged Junior but need 3–5 and 4–7 yrs). The rest are mid, senior or director level, or outside the US.
- SCOUT.md updated: reach job boards through WebSearch first, so unattended runs can open them.

## 2026-11-20 (Fri, ISO week 47 → group D)
- Job boards: The Brand Identity could not be checked. Following the new search-first steps, all 3 of its `search` queries plus one extra (`"the-brandidentity.com/jobs" roles`) returned no the-brandidentity.com pages at all, so there was no URL this unattended run was allowed to open. No roles read.
- Group D was fully searched yesterday (same ISO week), so this run did the 14 broad searches, retried yesterday's skipped leads, and added a few new design-type searches (graphic/brand/visual/motion/packaging 2027) instead of repeating the group-D company combos.
- Searches: 31 WebSearch. Candidates opened: 34 (6 failed or rate-limited).
- Suggested: 4 (Landor Design Intern Spring 2027, Kettle Motion Design Intern, Athena Summer 2027 Motion Designer intern, Disney Creative Design Intern Spring 2027). Rejected: 21 (recorded in seen.json).
- Top reject reasons: not a design role (7 Milwaukee Tool engineering/IT/marketing/ID reqs, Samsung); term past (Milwaukee Tool Fall 2026 UX co-op, ACLU, A24, MATTE, DEPT); closed (Solace x2, INHF, Markham); too much experience (T-Mobile Designer, 3+ yrs); duplicate (Epic UX via RippleMatch).
- Skipped, not recorded (retry next week): Legends Global Graphic Design Intern, Chicago (teamworkonline 2164585, year of the summer term not stated); Sporting KC Graphic Designer (teamworkonline 2189632, fetch failed again); DLR Group greenhouse 5078335008 (fetch failed); RippleMatch 8353900002 and directapplication 4438540005 (rate-limited); Disney Graphic Design & Communications Intern Spring 2027, Lake Buena Vista (redirected to a generic page); Walt Disney Animation Studios Product Design Intern Summer 2027 (fetch failed); Universal Orlando Graphic Design Brand Creative Studio intern Summer 2027 (aggregator only, failed); Bunzl Jr Graphic Designer, Morton Grove IL (no employer page); Minnesota Star Tribune UX and Data Graphics Design internships Summer 2027, Nationwide UX Designer Internship Summer 2027 (no employer page found, 4th week for Star Tribune).
- Board published cleanly (Version 170), no conflict. Public index.html unchanged (only queue items added).

## 2026-11-27 (Fri, ISO week 48 → group A)
- Job boards: The Brand Identity could not be checked. All 3 of its `search` queries plus one extended search (`"the-brandidentity.com/jobs"`) returned no the-brandidentity.com pages (only LinkedIn, aggregators and other boards), so there was no URL this unattended run could open. No roles read. Third scheduled run in a row this has happened.
- Searches: 31 WebSearch (4 for The Brand Identity, 11 group-A company combos, 14 broad, 2 employer-page lookups).
- Candidates opened: 21 (4 failed: Oshkosh Design Intern Summer 2027 on Wellfound, Sporting KC Graphic Designer 2189632 (3rd failure), Gravis Robotics Design Internship (Lever apply page), plus Harley-Davidson's page showed no description).
- Suggested: 5 (Veterans United Intern, Graphic Designer; BDS Connected Solutions Junior Graphic Designer; Glantz Junior Graphic Designer; St. Jude Visual Arts Graphic Design Internship; Sokal Junior Graphic Designer). Rejected: 10 (recorded in seen.json).
- Top reject reasons: not a design role (Hudl x3 engineering/PM/QA, Veterans United generalist summer program); closed (Harley-Davidson, KU student hourly, MJH via Built In); term under way (BJC UI/UX); recruiter posting with no employer named (LandaJob).
- Skipped, not recorded (retry next week): Ibotta Product Design Intern, Denver, Summer 2027, $33.85/hr (good fit for juniors, but only on Built In; no employer page found); Terraboost Media Graphic Designer, Naperville (Built In only); Kansas City Chiefs Graphic Design Seasonal Assistant (Teamwork Online, no term or date); Legends Global Graphic Design Intern, Chicago (year still not stated); Minnesota Star Tribune UX Summer 2027 (5th week, no employer page); Oshkosh, Sporting KC, Gravis (fetch failed).
- Group A was otherwise quiet: no current design postings found for Hallmark, VML (2027 not yet posted), Callahan, Burns & McDonnell, Evergy, Jack Henry (only Summer 2026), Anheuser-Busch, Build-A-Bear, HLK, Union Pacific, Principal, Strategic America, General Mills, Optum, Carmichael Lynch, Capsule, American Family, Energy BBDO, Havas, Kraft Heinz, Sprout Social, Cummins, LPK, Ologie, Brown-Forman, VI Marketing, Frito-Lay, Cactus.
- Board published cleanly (Version 177), no conflict. Public index.html unchanged (only queue items added).
