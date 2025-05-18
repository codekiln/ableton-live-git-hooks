# `ableton-live-git-hooks-docs` AGENTS.md

This file provides specific guidance for the Codex agent when working with Logseq content in this directory.

## Logseq Directory Structure

- `pages/` - Main documentation pages in Logseq Flavored Markdown (LFM)
  - Follows diataxis documentation framework
  - Contains conceptual, how-to, and reference guides
- `journals/` - Daily notes and progress tracking
- `logseq/` - Logseq application data (ignore)

## Codex Agent Rules for Logseq Content

### Critical Rules
1. **Frontmatter Protection**
   - NEVER modify `tags::` frontmatter in any page
   - Other frontmatter attributes may be modified when explicitly instructed
   - Frontmatter must use kebab-case and `:: ` separator

2. **Markdown Formatting**
   - ALL content must use Logseq Flavored Markdown (LFM)
   - Every line must start with a bullet point (`-`)
   - Use TAB for indentation (not spaces)
   - Headings must be prefixed with bullet points
   - No blank lines between content
   - Code blocks must be properly nested inside bullet points

3. **Link Handling**
   - Use `[[Page Name]]` for internal links
   - Use `#tag` for tags
   - When linking to assets, follow the asset linker rules

4. **Content Structure**
   - Follow proper heading hierarchy:
     - `#` (H1) only at root level
     - `##` (H2) only at first indent
     - `###` (H3) only at second indent
   - Use bullet points for all content
   - Maintain logical nesting of content

### Codex Agent Permissions
- The agent operates in "Suggest" mode by default
- Can read any file in this directory
- Requires approval for:
  - All file writes/patches
  - Any shell commands
- When modifying content:
  - Must preserve existing `tags::` frontmatter
  - Must follow LFM formatting rules
  - Must maintain proper indentation and bullet structure

### Reference Rules
The agent must follow all rules defined in `../.cursor/rules/logseq-cursor-rules/`. Key rules include:
- [logseq-flavored-markdown.mdc](../.cursor/rules/logseq-cursor-rules/logseq-flavored-markdown.mdc) - Core LFM formatting
- [convert-from-md-to-lfm.mdc](../.cursor/rules/logseq-cursor-rules/convert-from-md-to-lfm.mdc) - Conversion guidelines
- [logseq-directory-structure.mdc](../.cursor/rules/logseq-cursor-rules/logseq-directory-structure.mdc) - Directory organization
- [logseq-naming-conventions.mdc](../.cursor/rules/logseq-cursor-rules/logseq-naming-conventions.mdc) - Tag and namespace rules
- [logseq-asset-linker.mdc](../.cursor/rules/logseq-cursor-rules/logseq-asset-linker.mdc) - Asset handling

Additional rules in the same directory cover specific use cases like:
- Person pages
- Slides
- YouTube notes
- Forum posts
- AI model details
- Typical week structure

The agent should review all rules in the directory to ensure complete compliance with Logseq conventions.

