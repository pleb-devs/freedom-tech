# Repository Guidelines

## Project Structure & Module Organization
The catalog lives in `README.md`; it curates technologies by topic, type, language, and use case. Keep new entries inside the existing subsections and maintain alphabetical ordering within each bullet list. Store contributor-facing docs, like this guide, at the repository root and avoid creating new folders until a distinct content theme demands it. When adding assets (e.g., screenshots for PRs), place them under `docs/` only after confirming multiple files need the space.

## Build, Test, and Development Commands
Run `npx markdownlint README.md AGENTS.md` before submitting to enforce heading levels, spacing, and indentation. Use `npx markdown-link-check README.md` to confirm outbound links are valid. Execute `git diff --check` to catch trailing whitespace or missing blank lines between sections. Preview the Markdown with `glow README.md` or your editor’s preview to ensure nested anchors render correctly.

## Coding Style & Naming Conventions
Write concise, factual sentences in present tense and avoid marketing language. Use `*` for bullet markers, bold tool names, and en dashes to match the established entry format (`Name – note *(Language • Type • Topic • Use cases)* — [link]`). Keep headings in sentence case except for new top-level additions, which should use title case. When adding new sections, update the “Quick Index” list in `README.md` so anchors stay accurate.

## Testing Guidelines
Treat markdown linting and link checks as the required test suite; both must pass locally prior to a pull request. If a link check fails due to a temporary outage, note the URL and reason in the PR description. When introducing multiple entries, verify anchor changes manually by following each `Quick Index` link. Capture any preview discrepancies with screenshots to share in the review thread.

## Commit & Pull Request Guidelines
Use short, imperative commit messages (`docs: add nostr relay tooling`) consistent with recent history. Squash iterative wording tweaks into the primary change commit. Pull requests should contain a concise summary of the catalog additions, optional rendered Markdown screenshots, and a checklist confirming linting and link checks completed successfully. Link related issues or discussions when context helps reviewers.
