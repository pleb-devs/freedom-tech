# Repository Guidelines

## Project Structure & Module Organization
- `README.md` curates the technology catalog; keep entries within the existing type/topic/language sections and preserve alphabetical order inside each list.
- Each entry follows `Name – note *(Language • Type • Topic • Use cases)* — [link]`; reuse bolding, emphasis, and punctuation so the index stays scannable.
- Store any new contributor-facing docs under the repository root; avoid creating unused folders until a new content theme clearly requires it.

## Build, Test, and Development Commands
- Run `npx markdownlint README.md AGENTS.md` to enforce indentation, heading depth, and spacing rules before opening a pull request.
- Validate outbound links with `npx markdown-link-check README.md` so the catalog stays current.
- Use `git diff --check` to catch stray whitespace (the catalog uses one blank line between sections).

## Coding Style & Naming Conventions
- Write concise, factual descriptions in the present tense; avoid marketing language or first-person commentary.
- Use bullet lists with `*` markers, bold library names, and en dashes (`–`) exactly as shown in existing entries.
- Prefer sentence case for headings (`## By Type`, `### Libraries / SDKs`) and title case for new top-level sections.

## Testing Guidelines
- Treat linting and link checks as the required “test suite”; run both commands locally and note any deliberately ignored failures in the pull request.
- When adding multiple entries, preview the Markdown (e.g., VS Code or `glow README.md`) to confirm nested headings render correctly.
- For substantial edits, cross-check “Quick Index” anchors to ensure new headings match existing links.

## Commit & Pull Request Guidelines
- Recent commits are short, README-focused messages (e.g., `Update README.md`); continue with a concise, imperative summary such as `docs: add nostr relay tooling`.
- Squash minor wording tweaks into the feature commit to keep history tidy; force-push only when rebasing your own work.
- Pull requests should include: 1) a one-paragraph summary of the changes, 2) any relevant screenshots of rendered Markdown (optional), and 3) a checklist showing lint and link checks have passed.
