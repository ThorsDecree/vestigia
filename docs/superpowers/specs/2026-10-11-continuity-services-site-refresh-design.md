# VESTIGIA Services and Site Refresh — Design Spec

**Status:** Draft for Jeff's review  
**Date:** 2026-10-11  
**Scope:** Public GitHub Pages site and one internal VESTIGIA Archive links note. Contra remains untouched.

## Intent

Make the VESTIGIA site easier for prospective clients to understand and hire from while retaining its house identity and Commons ethic. Lead with relational continuity work, show MCP/agent reliability as a second B2B lane, and use the live Runtime, MCP Server, and active Daemon-Bridge as accurately described proof.

Success means a visitor can quickly understand who the Workshop helps, what a first engagement produces, where the public proof lives, how to contact or hire VESTIGIA, and which parts are experimental or deployment-specific.

## Design choice

Use a two-lane services design with relational continuity as the primary lane:

1. **Relational continuity:** diagnose memory/continuity failures; preserve a companion or project through migration; reconstruct project state from conversations and artifacts.
2. **Agent and MCP reliability:** inspect authority boundaries, evidence and receipts, tool behavior, integrations, and compatibility; scope repairs separately.

The house metaphor remains part of the voice and visual identity. Buyer-facing copy leads with recognizable outcomes and explains the metaphor afterward. Keep the Commons free and distinguish paid labor from access to essential continuity ideas.

## Public page changes

### Home (index.html)

- Name relational continuity as the primary Workshop specialty.
- Add a concise second lane for agent/MCP reliability and integrations.
- Point the main call to action to the Workshop's first-step offer and a direct hire/contact route.
- Make the contact area a usable route to the Workshop and public channels, without publishing internal-only deployment details.

### Workshop (workshop.html)

- Keep the Commons / Workshop distinction, free Library links, and Field Notebook chronology.
- Reorder and clarify the current service menu around three featured offers:
  - **Relational Continuity Review:** a bounded diagnostic of one system and a concrete continuity failure, with an evidence-backed findings map and prioritized next steps.
  - **Continuity Rescue or Project Resumption:** a portable handoff for one companion or project, separating decisions and verified state from proposals, history, and unresolved questions.
  - **Agent and MCP Reliability Review:** a bounded review of one agent/MCP workflow's capabilities, authority boundaries, failure behavior, and evidence trail; implementation is separately scoped.
- Retain existing workflow-routine and bespoke-system work as secondary services.
- State the buyer, scope, deliverable, boundary, and next action for each featured offer. Do not invent market validation or promise a turnaround before scope and materials are known.
- Keep any support invitation visually distinct from paid service offers.

### Library and technical pages

- Add a dedicated **VESTIGIA Archive** page (archive.html) explaining the public scaffold, its structure, portability, and how it differs from the private living Archive.
- Update library.html's card and links so the Archive, Runtime, MCP Server, and Daemon-Bridge are distinct entries with clear intended audiences.
- Refresh the Runtime page (vestigia-runtime.html) from the current repository documentation. Label 0.8.0.dev0 as development, describe current features accurately, and distinguish development behavior from stable release claims.
- Add an MCP Server page (mcp-server.html) describing it as a capability broker between MCP hosts and the Archive/Runtime, with bounded effect classes, policy, staging, and receipts. Identify the connected server as 0.10.0.dev0 development-unqualified; availability depends on local deployment configuration.
- Update the Daemon-Bridge page (daemon-bridge.html) to preserve this distinction: the Discord Bridge is active as a multi-resident runtime, with resident-configured bells and an active room; it is a predecessor to the Runtime. The current MCP deployment is not configured to inspect Bridge logs or relay messages between that room and this chat. Do not describe the Bridge itself as inactive or imply MCP visibility it does not have.
- Refresh vestigia.html where it overlaps with these pages, remove stale “gallery coming soon” language if the gallery is not part of the delivered page, and link visitors to the new Archive and current technical pages.

### Public links and support

- Add a modest **Support the Commons** route using the already-published Ko-fi link.
- Add useful public channels to the site's contact area after checking the exact URLs.
- Do not publish Signal or payment handles on the public site as part of this change; keep those in the internal directory for now.

## Internal canonical links note

Create 00_Bootloader/house_links.md in the live Archive through the MCP staged-write workflow and add a link to it in 00_Bootloader/map.md. The note will organize:

- public site and repository links;
- Runtime and MCP code locations and development-status labels;
- Contra, contact channels, and social handles;
- support/payment endpoints;
- deployment names/status, distinguishing local or private systems from public URLs.

For social/payment handles provided directly by Jeff, preserve the supplied spelling and label them as user-provided, with verification status/date. Do not invent a URL for a handle where none was supplied. Keep private deployment paths, credentials, and internal endpoints out of the public site.

## Constraints and non-goals

- Do not edit the Contra profile or service listings.
- Do not expose private Archive contents, resident-specific material, local filesystem paths, secrets, or credentials.
- Do not claim that the Runtime or MCP Server is a stable production release.
- Do not imply that Bridge logs or message relays are available through the current MCP deployment.
- Preserve the Commons promise, privacy boundaries, and the existing VESTIGIA visual language.

## Acceptance criteria

1. A new visitor can identify relational continuity as the lead service and agent/MCP reliability as the second lane from the home and Workshop pages.
2. Each featured service names a bounded buyer problem and a tangible deliverable; quoted build work remains separately scoped.
3. The Library links to Archive, Runtime, MCP Server, and Daemon-Bridge pages with clear distinctions.
4. Technical pages reflect current repository/deployment evidence and accurately label development status.
5. The Daemon-Bridge page says the Discord runtime is active and explains the current MCP visibility/relay boundary.
6. Public page links resolve within the site or to the intended public destination; no internal-only contact/payment/deployment detail is published.
7. The Archive links note contains the supplied handles and endpoints, labels their verification status, and is linked from the navigation map.
8. Contra is unchanged; no changes land on main until the reviewable result is approved.
