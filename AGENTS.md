# Repository Guidelines

## Project Structure & Module Organization
- Root files: `README.md` (catalog) and `LICENSE` (MIT). No build output or binaries are tracked.
- Catalog sections: By Topic, By Type, By Language, Tag Glossary, and Roadmap. Place new entries in the most specific subsection; mirror across parallel lists only when it improves discovery.
- Entry format: `**Name** – short note *(Language • Type • Topic • use cases)* — [link]`. Keep tags aligned with the glossary and keep notes to one line.

## Build, Test, and Development Commands
- No build step; edit Markdown directly.
- Preview: `glow README.md` (or your editor’s Markdown preview) to spot formatting issues.
- Optional lint: `npx markdownlint README.md AGENTS.md`.
- Optional link check: `npx markdown-link-check README.md` to catch dead or redirected links.

## Coding Style & Naming Conventions
- Use bullets over tables; keep lines ≤ 100 chars.
- Bold the project name, use an en dash before the note, and italicize the tag tuple exactly as shown in the entry format.
- Sort items alphabetically within a subsection when practical; group closely related tools together if ordering helps comprehension.
- Prefer canonical links (project homepage or primary repo). Avoid tracker URLs and long redirects.
- Keep tone neutral and descriptive; avoid marketing language or subjective hype.

## Testing Guidelines
- Run `markdownlint` and the link check before opening a PR; fix any failures.
- Manually scan for duplicate entries, stale tags (topic/type/language), and obvious spelling errors.
- When adding many links, spot-check HTTP 200 responses and license compatibility.

## Commit & Pull Request Guidelines
- Commit messages: present-tense, concise (≤72 chars), similar to existing history (e.g., `add nostr relay options`).
- Separate structural changes (reordering/retitling) from new content when feasible.
- PR checklist: brief summary of sections touched, example of entries added/updated, results of lint/link checks, and any known gaps.
- Link related issues or requests; include screenshots only if Markdown layout changes materially.

## Security & Curation Tips
- Favor audited, open-source, and self-hostable tools; flag experimental or unmaintained projects in the note.
- Keep the repo text-only—no vendored binaries or large assets.
- Strip tokens, tracking params, or PII from URLs; default to `https`.
