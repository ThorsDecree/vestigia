# VESTIGIA Services and Site Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Update the VESTIGIA GitHub Pages site to lead with relational continuity, present agent/MCP reliability as a second lane, explain current projects accurately, and add a canonical Archive links note.

**Architecture:** Keep the existing static HTML/CSS site and visual system. Add two focused technical pages (Archive and MCP Server), update the existing Home, Workshop, Library, Runtime, Shell, and Daemon-Bridge pages, and maintain social/deployment inventory in the live Archive through its staged-write boundary. Work remains on the isolated feature branch; no write to main.

**Tech Stack:** Static HTML/CSS, Python standard-library HTML parsing for a small site contract test, GitHub connector, VESTIGIA MCP Archive staged writes.

**Spec:** docs/superpowers/specs/2026-10-11-continuity-services-site-refresh-design.md

## Global Constraints

- Relational continuity is the primary Workshop lane; agent/MCP reliability is the second.
- Keep Commons materials free and paid labor distinct.
- Do not edit Contra.
- Label Runtime 0.8.0.dev0 and MCP Server 0.10.0.dev0 as development releases.
- Describe the Discord Daemon-Bridge as active and multi-resident, with resident-configured bells.
- State that the connected MCP deployment cannot inspect Bridge logs or relay Bridge messages.
- Do not publish Signal or payment handles on the site; record them in the internal Archive note.
- Do not expose credentials, local filesystem paths, resident-private material, or unverified deployment endpoints.
- Publish no branch to main; prepare a reviewable draft pull request.

## Review Focus

- Internal relative links and fragment IDs — test every local link in the edited pages.
- Technical version/status drift — assert the two development versions are labeled accurately.
- Bridge activity vs. MCP visibility — assert the site states both facts without conflating them.
- Public/private contact boundary — assert the public site omits Signal and payment handles while the Archive note contains user-supplied entries.
- Commons/paid-work distinction — assert the Workshop retains its free Commons language and separate paid services.

---

### Task 1: Add site contract checks

**Files:**
- Create: tests/test_site_contract.py

**Interfaces:**
- Consumes: edited site HTML files in the repository root.
- Produces: standard-library unittest checks runnable with python -m unittest tests.test_site_contract.

- [ ] **Step 1: Write the failing tests**
  - Add these checks using Python HTMLParser and unittest: test_internal_links_resolve; test_library_links_to_archive_and_mcp; test_versions_are_labeled_as_development; test_bridge_activity_and_mcp_boundary_are_distinct; test_workshop_leads_with_two_lanes_and_keeps_commons; and test_public_site_omits_signal_and_payment_handles.
  - test_internal_links_resolve parses href/src references in the scoped pages and asserts each local target file and any supplied fragment ID exists.
  - test_library_links_to_archive_and_mcp asserts library.html links to archive.html and mcp-server.html.
  - test_versions_are_labeled_as_development asserts Runtime 0.8.0.dev0 and MCP 0.10.0.dev0 appear with development labels.
  - test_bridge_activity_and_mcp_boundary_are_distinct asserts the Bridge is active and the MCP log/relay boundary is explicit.
  - test_workshop_leads_with_two_lanes_and_keeps_commons asserts relational continuity, agent/MCP reliability, and free Commons language remain present.
  - test_public_site_omits_signal_and_payment_handles asserts user-provided Signal/CashApp/PayPal identifiers are absent from public HTML.

- [ ] **Step 2: Run the tests against the branch baseline**
  - Run: python -m unittest tests.test_site_contract -v
  - Expected: FAIL because the new pages and approved copy have not been added yet; any import or parser error is a test defect to fix before continuing.

- [ ] **Step 3: Keep the checks limited to observable page contracts**
  - Use Python HTMLParser and pathlib only. Avoid network requests and third-party dependencies.

---

### Task 2: Implement the public services and technical pages

**Files:**
- Modify: index.html
- Modify: workshop.html
- Modify: library.html
- Modify: vestigia-runtime.html
- Modify: vestigia.html
- Modify: daemon-bridge.html
- Create: archive.html
- Create: mcp-server.html

**Interfaces:**
- Consumes: approved design spec and the public site contract tests from Task 1.
- Produces: linked, buyer-readable pages with current, deployment-qualified project descriptions.

- [ ] **Step 1: Re-run the Task 1 tests and confirm expected failures**
- [ ] **Step 2: Update Home and Workshop copy**
  - Lead with relational continuity and name agent/MCP reliability as a second lane.
  - Feature bounded diagnostic, continuity/project handoff, and MCP/agent reliability review offers.
  - Keep secondary workflow/build services and the Field Notebook.
  - Add a direct Workshop/Contra contact route and a modest Support the Commons route using the existing Ko-fi link.
- [ ] **Step 3: Add Archive and MCP Server pages; update Library routes**
  - Explain the public Archive scaffold separately from the private living Archive.
  - Describe MCP as a policy-bounded capability broker; label connected deployment status as development-unqualified.
  - Add distinct Library cards for Archive, Runtime, MCP Server, and active Daemon-Bridge.
- [ ] **Step 4: Refresh existing technical pages**
  - Update Runtime features and development label using current repository evidence.
  - Remove stale gallery-coming-soon language from the Shell page and point to current project pages.
  - Describe the Bridge as active in Discord with resident-configured bells; clarify that MCP cannot inspect its logs or relay its messages.
- [ ] **Step 5: Run the contract tests**
  - Run: python -m unittest tests.test_site_contract -v
  - Expected: PASS with all local links resolving and all required copy/status checks satisfied.

---

### Task 3: Add the canonical Archive links note

**Files:**
- Create: live Archive 00_Bootloader/house_links.md
- Modify: live Archive 00_Bootloader/map.md

**Interfaces:**
- Consumes: user-provided profile/contact/support identifiers and the MCP deployment's current write grants.
- Produces: a source-of-truth inventory with public/private status labels, verification dates, and a map entry.

- [ ] **Step 1: Inspect write capabilities and current map hash**
  - Confirm create/replace grants for 00_Bootloader and read the live map content hash.
- [ ] **Step 2: Stage the new note and map update**
  - Use archive.stage_text for each file with expected base absent for the new note and the exact current map hash for the replacement.
- [ ] **Step 3: Inspect both durable proposals**
  - Confirm exact targets/content digest and unchanged base.
- [ ] **Step 4: Promote the links note first, then the map**
  - Use each exact stage id and proposal digest; promotion refuses stale bases.
- [ ] **Step 5: Read both live files and verify**
  - Confirm the user-provided spellings, private/public labels, map link, and absence of credentials/local paths.

---

### Task 4: Verify and prepare review

**Files:**
- Inspect: all edited HTML pages and tests/test_site_contract.py
- Create: draft pull request on the feature branch

**Interfaces:**
- Consumes: completed Tasks 1-3.
- Produces: a verified branch and draft pull request for Jeff's final review before publishing.

- [ ] **Step 1: Run the full site contract tests and repository checks available for this static site**
- [ ] **Step 2: Fetch each changed GitHub file and inspect the actual branch diff**
- [ ] **Step 3: Confirm no Contra files or main-branch files changed**
- [ ] **Step 4: Create a draft pull request describing scope, checks, Archive note handling, and known development-status limits**
- [ ] **Step 5: Report the draft PR and request final approval before merge/deployment**
