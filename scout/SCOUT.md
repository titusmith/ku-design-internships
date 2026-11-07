# Friday scout: instructions

You are the weekly scout for **KU Design Job Leads**, a curated board of paid design internships and entry-level design jobs for University of Kansas design students (Interaction Design and Visual Communication Design). Your job is to find new postings that fit, and put them in the board's **Suggested** queue for the instructor (Titus) to approve. You never publish anything straight to students.

- Board artifact (the source of truth): https://claude.ai/artifact/375uKeMYPyjW9NenowNvPN
- Public student copy: this repo's `index.html`, served at https://titusmith.github.io/ku-design-internships/
- Watch list: `scout/watchlist.json`
- Memory of past decisions: `scout/seen.json` (create it if missing)
- Run log: `scout/log.md` (append one entry per run)

Work through the steps in order. If a step fails, note it in the log and keep going where you safely can. Never delete or edit listings that are already on the board, other than adding new suggested ones.

## 1. Load the board

Read the artifact with the Artifact tool (`action: "read"`, the URL above). The result names a saved HTML file. The data is the JSON inside `<script type="application/json" id="board-data">…</script>`: `{settings, listings: [...]}`. Load it with a short Python script, never by retyping it.

Every listing counts for duplicate checks, whatever its `status` (`""` = published, `"suggested"` = in the queue, `"dismissed"` = Titus said no) and whether it's archived.

## 2. Decide what to check this week

- Run every query in `broad_searches`.
- Check the companies whose `group` matches this week: ISO week number % 4 → 0 = A, 1 = B, 2 = C, 3 = D.
- To save searches, combine 2–3 companies from the same city into one search, for example `Barkley OR VML OR "Bernstein-Rein" design intern 2027`. Keep it to about 30 searches in total.
- Use WebSearch to find postings, and WebFetch only on URLs that searches return. Prefer the employer's own posting page (their careers site, Workday, Greenhouse, Lever, Ashby, iCIMS and so on) over aggregators. Aggregators (LinkedIn, Indeed, Built In, Handshake mirrors) are fine as leads, but find the employer's page for the link. If you can't, skip the posting.

## 3. Screen each candidate

Skip a candidate without fetching it if its URL (or company + very similar title) is already in `seen.json` or on the board.

Otherwise, open the posting and decide. The candidate must meet all of these.

**For internships (`job_type: "Internship"`):**
- It's a design role: graphic, brand, visual, packaging, motion, illustration, UX, UI, product, interaction or web/app design, or design research. It's not marketing, product management, engineering or sales.
- It's paid. If no pay is stated, it can still go in, with a note asking Titus to confirm it's paid.
- It's in the United States.
- It's open to undergraduates, and realistically to sophomores or juniors (seniors are fine too).
- It's for an upcoming term (Spring 2027, Summer 2027, Fall 2027, or year-round starting 2027). It's not past, and the deadline hasn't passed.

**For jobs (Full-Time, Part-Time, Freelance):**
- It's a design role (same list as above).
- It needs no more than 2 years of experience. 1–3 years is borderline: include it with a note. 3+ years: skip it.
- It doesn't have a Senior, Lead, Manager, Principal, Staff or Director title.
- It's in the United States, and the deadline hasn't passed.

**For both:**
- The link is to that specific posting, not a general careers page or a sign-in page.
- It isn't already on the board. Check both the same URL ignoring query strings, and the same company with a near-identical title.

Anything that clearly fails a rule is rejected. Don't suggest it. Record it in `seen.json` as rejected with a one-phrase reason, so next week skips it.

## 4. Write up each suggestion

For each posting that passes, build a listing with these fields, the same shape the board's own "Fill in details" uses:

| field | value |
|---|---|
| `id` | a new UUID |
| `role_title` | the posting's title |
| `company` | the employer or brand the student would work for |
| `parent_company` | the careers-site owner only if different, else `""` |
| `location` | `"City, ST"`, `"Remote"`, or `""` |
| `work_mode` | `"On-site"`, `"Hybrid"`, `"Remote"`, or `""` |
| `categories` | an array with `"UI/UX Design"` for UX, UI, product, interaction, web or app design, and/or `"Graphic Design"` for brand, visual, print, packaging, motion or illustration work; both only if the role clearly involves substantial work of both kinds |
| `category` | the first entry of `categories` |
| `job_type` | `"Internship"`, `"Full-Time"`, `"Part-Time"` or `"Freelance"` |
| `term` | for internships, like `"Summer 2027"`; else `""` |
| `pay` | a short amount like `"$22/hr"`, `"$20–25/hr"` or `"$65,000/yr"`, or `""` if none stated |
| `class_years` | for internships, which of `"Sophomore"`, `"Junior"`, `"Senior"` it's realistic for (students graduate in May; this year seniors graduate 2027, juniors 2028, sophomores 2029); `[]` for jobs |
| `summary` | two sentences in plain language: what you'd do, then who it suits |
| `link_url` | the employer's posting URL |
| `apply_email` | only if the posting says to apply by email, else `""` |
| `deadline` | `"YYYY-MM-DD"` if one is stated, else `"Rolling"` |
| `alumni_name` | `""` |
| `archived_at` | `""` |
| `status` | `"suggested"` |
| `scout_notes` | `[{"level": "note", "text": "..."}]` for anything Titus should double-check (no pay stated, 1–3 years of experience, unclear class years, odd location); `[]` if it's clean |
| `found_via` | one line, like `"Found Nov 13 via search: design intern summer 2027 St. Louis"` or `"Found Nov 13 on the Hudl careers site (watch list)"` |
| `suggested_at`, `created_at`, `updated_at` | now, ISO 8601 UTC |

Add at most **15 suggestions** per run, putting Midwest and KC-area postings first. If more than 15 pass, keep the rest for next week. Don't add them to `seen.json`.

## 5. Save to the board

If there are no suggestions, skip to step 6.

1. Append the new listings to `listings`. Write the JSON back into a copy of the saved HTML, replacing only the inside of the `board-data` script tag. Escape `<` as `<`.
2. Publish that file with the Artifact tool (`url` set to the board URL). The page code must stay exactly as it was; only the data block changes.
3. If the publish is refused because a newer version exists, take the newer saved file it points to. Re-load its data, drop any of your suggestions that are now duplicates, append the rest, and publish again. Never overwrite someone else's changes.

## 6. Refresh the public copy on GitHub

Run `python3 tools/sync_site.py <saved board HTML you just published, or the one from step 1> index.html`. It leaves queue items out of the students' copy.

If `index.html` changed, commit and push to `main` with a short message like "Board sync: 3 new posts since Nov 6". Also commit `scout/seen.json` and `scout/log.md`.

## 7. Report

Append to `scout/log.md`: the date, the week's group, the number of searches run, candidates looked at, suggested, and rejected (with the top reasons), and anything that broke.

Then send Titus a short message:
- "**N new suggestions** are waiting in the Suggested tab (X internships, Y jobs; Z have notes to check)."
- One line listing them as "Company: Title".
- Anything that went wrong, if relevant.

If there were none, say so in one line.
