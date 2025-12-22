# Repository Guidelines

This repository is a curated, text-only catalog of tools and resources.
Use this guide when editing entries or adding new sections.

## Project Structure & Organization

- `README.md` – main catalog (by topic, type, language, tags, roadmap).
- `LICENSE` – MIT license for the catalog content.
- Do not add build output, vendored binaries, or large assets; keep everything
  as Markdown or small text files.

## Build, Test, and Development Commands

- Edit Markdown directly in your editor.
- Preview: `glow README.md` (or your editor’s Markdown preview).
- Lint: `npx markdownlint-cli README.md AGENTS.md agent-prompt.md` to enforce basic
  style rules.
- Link check: `npx markdown-link-check README.md AGENTS.md agent-prompt.md` to
  catch dead or redirected links.

## Coding Style & Naming Conventions

- Prefer bullets over tables; keep lines ≤ 100 characters.
- Catalog entry format:
  `**Name** – short note *(Language • Type • Topic • use cases)* — [Name](https://example.com)`.
- Bold the project name, use an en dash before the note, and italicize the tag
  tuple exactly as shown.
- Prefer canonical project URLs (homepage or primary repo) and strip tracking
  parameters; default to `https`.

## Testing Guidelines

- Treat `markdownlint-cli` and `markdown-link-check` as the primary “test” suite.
- Run both before opening a PR and fix any reported issues.
- When adding many links, spot-check HTTP 200 responses and obvious spelling
  errors.

## Commit & Pull Request Guidelines

- Commit messages: present tense, concise (≤ 72 chars), similar to
  `add nostr relay options`.
- PRs should outline sections touched, example entries added or updated, and
  the results of lint and link checks.
- Link related issues where relevant; add screenshots only when layout changes
  materially.

## Security & Curation Tips

- Favor audited, open-source, and self-hostable tools; flag experimental or
  unmaintained projects in the note.
- Do not include secrets, tokens, or PII in URLs.
- Keep the repository text-only for easier review, mirroring, and long-term
  maintenance.
