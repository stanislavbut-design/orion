# ADR-006 — Stable Business Codes

**Status:** Approved

**Date:** 2026-07-06

## Context

Business identifiers should remain stable regardless of localization.

## Decision

Business logic shall never depend on translated text.

Stable business codes shall be used wherever application logic requires persistent identifiers.

## Rationale

Translated labels may change.

Business identifiers should not.

## Consequences

- Logic operates on stable codes.
- Translations affect presentation only.
- Localization cannot change business behavior.

## Related Documents

- ADR-005 Internationalization
- STD-002 Database