from .relationship_types import RelationshipType
from .role_types import RoleType

#
# Which identity type may perform each Role Type
#

ROLE_IDENTITY_MAP = {

    RoleType.ORGANIZATION: "organization",

    RoleType.COMPANY: "party",
    RoleType.PARTNER: "party",
    RoleType.CUSTOMER: "party",
    RoleType.SUPPLIER: "party",
    RoleType.PROVIDER: "party",
    RoleType.LENDER: "party",
    RoleType.INSURER: "party",
    RoleType.LESSOR: "party",

    RoleType.DIRECTOR: "person",
    RoleType.EMPLOYEE: "person",

}

#
# Which Role Types are permitted by each Relationship Type
#

RELATIONSHIP_ROLE_MAP = {

    RelationshipType.BIZ_STRUCTURE: {
        RoleType.ORGANIZATION,
        RoleType.COMPANY,
    },

    RelationshipType.BIZ_OWNERSHIP: {
        RoleType.PARTNER,
        RoleType.COMPANY,
    },

    RelationshipType.CORP_GOV: {
        RoleType.DIRECTOR,
        RoleType.COMPANY,
    },

    RelationshipType.EMPLOYMENT: {
        RoleType.COMPANY,
        RoleType.EMPLOYEE,
    },

    RelationshipType.SALES: {
        RoleType.COMPANY,
        RoleType.CUSTOMER,
    },

    RelationshipType.PURCHASE: {
        RoleType.COMPANY,
        RoleType.SUPPLIER,
    },

    RelationshipType.SERVICE: {
        RoleType.COMPANY,
        RoleType.PROVIDER,
    },

    RelationshipType.LOAN: {
        RoleType.COMPANY,
        RoleType.LENDER,
    },

    RelationshipType.INSURANCE: {
        RoleType.COMPANY,
        RoleType.INSURER,
    },

    RelationshipType.LEASE: {
        RoleType.COMPANY,
        RoleType.LESSOR,
    },

}