# Identity Resolution Service Framework

## Framework invariants

### IRF-001

Every Core Identity type shall have at most one registered matching strategy.

### IRF-002

Every registered strategy shall implement `IdentityMatchingStrategy`.

### IRF-003

`IdentityResolutionRequest` shall be immutable.

### IRF-004

`IdentityResolutionResult` shall be immutable.

### IRF-005

`IdentityResolutionService` shall coordinate resolution but shall not perform identity matching itself.

### IRF-006

The service shall remain independent of all functional modules.