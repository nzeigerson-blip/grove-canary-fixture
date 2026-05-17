# grove-canary-fixture

Sandbox fixture repository for the Grove v2 end-to-end canary
(Sprint 13 — C2).  See
[`nzeigerson-blip/grove-delivery-framework`](https://github.com/nzeigerson-blip/grove-delivery-framework)
`.github/workflows/v2-canary.yml` for the workflow that drives this repo.

## Contract

- `src/canary.py` contains a **deliberate bug** in `add()` — do not "fix" it
  on `main`.  The bug is the canary stimulus.
- `tests/test_canary.py` is the verification target.  When the bug is in
  place these tests are **red** on `main`; a passing canary run produces
  a PR whose CI is **green** without the bug being merged.
- Each canary run opens a fresh issue describing the bug (the workflow
  uses GitHub Issues as the dispatch artifact), runs the v2 delivery
  framework against the canary umbrella in `grove-platform`, and expects:

  1. A new PR opened by `grove-delivery-dev` against `main` here.
  2. `ci` workflow green on that PR (tests pass once the bug is fixed
     **on the PR branch**, not on main).
  3. Session Handoff posted on the canary umbrella sub-issue.
  4. No `handoff-rejected` label.

## Not for human use

This repo is not a product surface.  Don't merge canary PRs; the daily
workflow will retire any open PRs older than 7 days.
