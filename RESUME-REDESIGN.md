# Resume: Homepage Hero Redesign

> Local scratch note — NOT committed to git, NOT published on the live site.
> Paste the prompt below into a new Claude Code session to pick this back up.

## Current state (as of 2026-08-17)
- LIVE site (`main`, GitHub Pages) = the OLD pre-redesign homepage.
  We reverted it (revert commit `8b1bd5d`) because I ran out of time.
- The FULL redesign is preserved on branch `redesign-hero-2026-08-17`
  (local + origin), tip `ec47027`. It already includes the Safari shader fix.
- Private artifact of the finished hero:
  https://claude.ai/code/artifact/9b9e7e07-fe34-4f2c-a9ed-a53e33d4be24
- The ONLY open item before relaunching: confirm the Safari cloud fix renders
  correctly on real Mac Safari AND iPhone Safari.

---

## Prompt to paste into a new session

Resume my portfolio homepage hero redesign.
Project: /Users/anieajamian/Documents/Claude-Projects/portfolio

START HERE:
1. Read the memory file `shader-hero-direction.md` in this project's Claude
   memory dir — it has the full history, design decisions, palette, the real
   A-monogram path, and every fix/gotcha from the last session.

CURRENT STATE:
- The LIVE site (main, GitHub Pages) is the OLD pre-redesign homepage. We
  reverted it on 2026-08-17 (revert commit 8b1bd5d) because I ran out of time.
- ALL of the redesign work is preserved on branch `redesign-hero-2026-08-17`
  (local + origin), tip commit `ec47027`. That branch is complete and includes
  the latest Safari fix. Don't rebuild from scratch — start from that branch.
- Private artifact of the finished hero:
  https://claude.ai/code/artifact/9b9e7e07-fe34-4f2c-a9ed-a53e33d4be24

WHAT THE REDESIGN IS (on that branch):
- WebGL "sunset clouds" hero on the homepage: my logo-color sky with drifting
  clouds and my white "A" monogram woven INTO the shader so it fades in/out as
  the clouds move (baked at the "Present" intensity).
- Headline "Hi, I'm Anie — I design the screens where the stakes are *highest*
  and the rules are *messiest*." with a serif-italic title line under it
  ("Senior / Staff Product Designer based in Los Angeles, CA"), intro starting
  "15+ years…", single "See selected work" CTA.
- Site-wide contact button reworded to "Say hello" (sentence case).
- Reduced repetitive phrasing (pivotal / consequential / friction-filled).
- Mobile tuned darker/more vivid so it's not washed out.

THE ONE OPEN ITEM before relaunching:
- On DESKTOP Safari the hero was breaking (hard blobs, washed out, blown-out A)
  because the shader used a sin()-based noise hash that loses precision on
  Apple GPUs. I replaced it with a sin-free hash (Hoskins hash12) on the branch,
  but I could NOT test real Safari in-session. FIRST STEP: verify the hero
  renders correctly (soft clouds, no washout) on Mac Safari AND iPhone Safari.

GOAL FOR THIS SESSION:
1. Verify the Safari fix on real Safari (Mac + iPhone). If still broken, the
   next levers are noted in the memory file (bound the animation time term,
   force highp everywhere, or add a richer non-WebGL fallback).
2. Once it looks right everywhere, merge `redesign-hero-2026-08-17` into main
   and push to go live. Confirm with me before pushing.

Note: my Mac's /etc/hosts may still point anieajamian.com at old WordPress —
verify the live build from the GitHub Pages URL or another device if unsure.
