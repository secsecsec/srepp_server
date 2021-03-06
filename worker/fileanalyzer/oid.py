#!/usr/bin/env python

###############################################################################
#
# Summit Route End Point Protection
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#
###############################################################################

OID_LOOKUP = {
    (1, 2, 840, 113549, 2, 2): 'md2',
    (1, 2, 840, 113549, 2, 4): 'md4',
    (1, 2, 840, 113549, 2, 5): 'md5',
    (1, 3, 14, 3, 2, 26): 'sha1',
    (2, 16, 840, 1, 101, 3, 4, 2, 1): 'sha256',
    (2, 16, 840, 1, 101, 3, 4, 2, 2): 'sha384',
    (2, 16, 840, 1, 101, 3, 4, 2, 3): 'sha512',

    (1, 2, 840, 113549, 1, 1, 1): 'rsa',
    (1, 2, 840, 113549, 1, 1, 2): 'rsa-md2',
    (1, 2, 840, 113549, 1, 1, 3): 'rsa-md4',
    (1, 2, 840, 113549, 1, 1, 4): 'rsa-md5',
    (1, 2, 840, 113549, 1, 1, 5): 'rsa-sha1',
    (1, 3, 36, 3, 3, 1, 1): 'rsa-sha1',  # Two rsa-sha1 values
    (1, 3, 36, 3, 3, 1, 2): 'rsa-ripemd160',
    (1, 2, 840, 113549, 1, 1, 11): 'rsa-sha256',
    (1, 2, 840, 113549, 1, 1, 13): 'rsa-sha512',

    (1, 2, 840, 10040, 4, 1): 'dsa',
    (1, 2, 840, 10040, 4, 3): 'dsa-sha1',
    (1, 3, 14, 3, 2, 27): 'dsa-sha1',  # Another
    (2, 16, 840, 1, 101, 2, 1, 1, 2): 'dsa-sha1',  # Yet another
}

# From https://support.microsoft.com/kb/287547?wa=wsignin1.0
szOID_CTL                   = "1.3.6.1.4.1.311.10.1"
szOID_CATALOG_LIST          = "1.3.6.1.4.1.311.12.1.1"
szOID_CATALOG_LIST_MEMBER   = "1.3.6.1.4.1.311.12.1.2"
CAT_MEMBERINFO_OBJID        = "1.3.6.1.4.1.311.12.2.2"
SPC_INDIRECT_DATA_OBJID     = "1.3.6.1.4.1.311.2.1.4"


Microsoft_OID  = "1.3.6.1.4.1.311"

Authenticode = "1.3.6.1.4.1.311.2"
# Software Publishing (with associated encoders/decoders)
SPC_INDIRECT_DATA_OBJID                 = "1.3.6.1.4.1.311.2.1.4"
SPC_STATEMENT_TYPE_OBJID                = "1.3.6.1.4.1.311.2.1.11"
SPC_SP_OPUS_INFO_OBJID                  = "1.3.6.1.4.1.311.2.1.12"
SPC_PE_IMAGE_DATA_OBJID                 = "1.3.6.1.4.1.311.2.1.15"
SPC_SP_AGENCY_INFO_OBJID                = "1.3.6.1.4.1.311.2.1.10"
SPC_MINIMAL_CRITERIA_OBJID              = "1.3.6.1.4.1.311.2.1.26"
SPC_FINANCIAL_CRITERIA_OBJID            = "1.3.6.1.4.1.311.2.1.27"
SPC_LINK_OBJID                          = "1.3.6.1.4.1.311.2.1.28"
SPC_HASH_INFO_OBJID                     = "1.3.6.1.4.1.311.2.1.29"
SPC_SIPINFO_OBJID                       = "1.3.6.1.4.1.311.2.1.30"

# Software Publishing (with NO associated encoders/decoders)
SPC_CERT_EXTENSIONS_OBJID               = "1.3.6.1.4.1.311.2.1.14"
SPC_RAW_FILE_DATA_OBJID                 = "1.3.6.1.4.1.311.2.1.18"
SPC_STRUCTURED_STORAGE_DATA_OBJID       = "1.3.6.1.4.1.311.2.1.19"
SPC_JAVA_CLASS_DATA_OBJID               = "1.3.6.1.4.1.311.2.1.20"
SPC_INDIVIDUAL_SP_KEY_PURPOSE_OBJID     = "1.3.6.1.4.1.311.2.1.21"
SPC_COMMERCIAL_SP_KEY_PURPOSE_OBJID     = "1.3.6.1.4.1.311.2.1.22"
SPC_CAB_DATA_OBJID                      = "1.3.6.1.4.1.311.2.1.25"
SPC_GLUE_RDN_OBJID                      = "1.3.6.1.4.1.311.2.1.25"

CTL_for_Software_Publishers_Trusted_CAs    = "1.3.6.1.4.1.311.2.2"
# (sub-subtree is defined for Software Publishing trusted CAs)
szOID_TRUSTED_CODESIGNING_CA_LIST       = "1.3.6.1.4.1.311.2.2.1"
szOID_TRUSTED_CLIENT_AUTH_CA_LIST       = "1.3.6.1.4.1.311.2.2.2"
szOID_TRUSTED_SERVER_AUTH_CA_LIST       = "1.3.6.1.4.1.311.2.2.3"

TimeStamping = "1.3.6.1.4.1.311.3"
# (with Associated encoder/decoders)
SPC_TIME_STAMP_REQUEST_OBJID            = "1.3.6.1.4.1.311.3.2.1"

Permissions = "1.3.6.1.4.1.311.4"

Crypto_2_0 = "1.3.6.1.4.1.311.10"
# PKCS #7 ContentType Object Identifier for Certificate Trust List (CTL)
szOID_CTL                               = "1.3.6.1.4.1.311.10.1"
# Sorted CTL Extension
szOID_SORTED_CTL                        = "1.3.6.1.4.1.311.10.1.1"

# Next Update Location extension or attribute. Value is an encoded GeneralNames
szOID_NEXT_UPDATE_LOCATION              = "1.3.6.1.4.1.311.10.2"

# Enhanced Key Usage (Purpose)
#   Signer of CTLs
szOID_KP_CTL_USAGE_SIGNING              = "1.3.6.1.4.1.311.10.3.1"

#   Signer of TimeStamps
szOID_KP_TIME_STAMP_SIGNING             = "1.3.6.1.4.1.311.10.3.2"

#   Can use strong encryption in export environment
szOID_SERVER_GATED_CRYPTO               = "1.3.6.1.4.1.311.10.3.3"
szOID_SERIALIZED                        = "1.3.6.1.4.1.311.10.3.3.1"

#   Can use encrypted file systems (EFS)
szOID_EFS_CRYPTO                        = "1.3.6.1.4.1.311.10.3.4"
szOID_EFS_RECOVERY                      = "1.3.6.1.4.1.311.10.3.4.1"

#   Can use Windows Hardware Compatible (WHQL)
szOID_WHQL_CRYPTO                       = "1.3.6.1.4.1.311.10.3.5"

#   Signed by the NT5 build lab
szOID_NT5_CRYPTO                        = "1.3.6.1.4.1.311.10.3.6"

#   Signed by and OEM of WHQL
szOID_OEM_WHQL_CRYPTO                   = "1.3.6.1.4.1.311.10.3.7"

#   Signed by the Embedded NT
szOID_EMBEDDED_NT_CRYPTO                = "1.3.6.1.4.1.311.10.3.8"

#   Signer of a CTL containing trusted roots
szOID_ROOT_LIST_SIGNER                  = "1.3.6.1.4.1.311.10.3.9"

#   Can sign cross-cert and subordinate CA requests with qualified
#     subordination (name constraints, policy mapping, etc.)
szOID_KP_QUALIFIED_SUBORDINATION        = "1.3.6.1.4.1.311.10.3.10"

#   Can be used to encrypt/recover escrowed keys
szOID_KP_KEY_RECOVERY                   = "1.3.6.1.4.1.311.10.3.11"

#   Signer of documents
szOID_KP_DOCUMENT_SIGNING               = "1.3.6.1.4.1.311.10.3.12"

#   Microsoft Attribute Object Identifiers
szOID_YESNO_TRUST_ATTR                  = "1.3.6.1.4.1.311.10.4.1"

#   Microsoft Music
szOID_DRM                               = "1.3.6.1.4.1.311.10.5.1"

#   Microsoft DRM EKU
szOID_DRM_INDIVIDUALIZATION             = "1.3.6.1.4.1.311.10.5.2"

#   Microsoft Licenses
szOID_LICENSES                          = "1.3.6.1.4.1.311.10.6.1"
szOID_LICENSE_SERVER                    = "1.3.6.1.4.1.311.10.6.2"

#   Microsoft CERT_RDN attribute Object Identifiers
szOID_MICROSOFT_RDN_PREFIX              = "1.3.6.1.4.1.311.10.7"
#   Special RDN containing the KEY_ID. Its value type is CERT_RDN_OCTET_STRING.
szOID_KEYID_RDN                         = "1.3.6.1.4.1.311.10.7.1"

#   Microsoft extension in a CTL to add or remove the certificates. The
#   extension type is an INTEGER. 0 =&amp;gt; add certificate, 1 =&amp;gt; remove certificate
szOID_REMOVE_CERTIFICATE                = "1.3.6.1.4.1.311.10.8.1"

#   Microsoft certificate extension containing cross certificate distribution
#   points. ASN.1 encoded as follows:
#         CrossCertDistPoints ::= SEQUENCE {
#             syncDeltaTime               INTEGER (0 4294967295) OPTIONAL,
#             crossCertDistPointNames     CrossCertDistPointNames
#         } --#public--
#              CrossCertDistPointNames ::= SEQUENCE OF GeneralNames

szOID_CROSS_CERT_DIST_POINTS            = "1.3.6.1.4.1.311.10.9.1"


Microsoft_CMC_OIDs                         = "1.3.6.1.4.1.311.10.10"

#     Similar to szOID_CMC_ADD_EXTENSIONS. Attributes replaces Extensions.
szOID_CMC_ADD_ATTRIBUTES                = "1.3.6.1.4.1.311.10.10.1"

#     Microsoft certificate property OIDs        = "1.3.6.1.4.1.311.10.11"
#     The OID component following the prefix contains the PROP_ID (decimal)
szOID_CERT_PROP_ID_PREFIX               = "1.3.6.1.4.1.311.10.11"

CryptUI                                    = "1.3.6.1.4.1.311.10.12"
szOID_ANY_APPLICATION_POLICY            = "1.3.6.1.4.1.311.10.12.1"

Catalog = "1.3.6.1.4.1.311.12"
szOID_CATALOG_LIST                      = "1.3.6.1.4.1.311.12.1.1"
szOID_CATALOG_LIST_MEMBER               = "1.3.6.1.4.1.311.12.1.2"
CAT_NAMEVALUE_OBJID                     = "1.3.6.1.4.1.311.12.2.1"
CAT_MEMBERINFO_OBJID                    = "1.3.6.1.4.1.311.12.2.2"

Microsoft_PKCS10_OIDs = "1.3.6.1.4.1.311.13"
szOID_RENEWAL_CERTIFICATE               = "1.3.6.1.4.1.311.13.1"
szOID_ENROLLMENT_NAME_VALUE_PAIR        = "1.3.6.1.4.1.311.13.2.1"
szOID_ENROLLMENT_CSP_PROVIDER           = "1.3.6.1.4.1.311.13.2.2"

Microsoft_Java = "1.3.6.1.4.1.311.15"

Microsoft_Outlook_Exchange = "1.3.6.1.4.1.311.16"
Outlook_Express                       = "1.3.6.1.4.1.311.16.4"
# Used by OL/OLEXP to identify which certificate signed the PKCS # 7 message

Microsoft_PKCS12_attributes = "1.3.6.1.4.1.311.17"
szOID_LOCAL_MACHINE_KEYSET              = "1.3.6.1.4.1.311.17.1"

Microsoft_Hydra = "1.3.6.1.4.1.311.18"

Microsoft_ISPU_Test = "1.3.6.1.4.1.311.19"

Microsoft_Enrollment_Infrastructure = "1.3.6.1.4.1.311.20"
szOID_AUTO_ENROLL_CTL_USAGE             = "1.3.6.1.4.1.311.20.1"
# Extension contain certificate type
szOID_ENROLL_CERTTYPE_EXTENSION         = "1.3.6.1.4.1.311.20.2"
szOID_ENROLLMENT_AGENT                  = "1.3.6.1.4.1.311.20.2.1"
szOID_KP_SMARTCARD_LOGON                = "1.3.6.1.4.1.311.20.2.2"
szOID_NT_PRINCIPAL_NAME                 = "1.3.6.1.4.1.311.20.2.3"
szOID_CERT_MANIFOLD                     = "1.3.6.1.4.1.311.20.3"

Microsoft_CertSrv_Infrastructure = "1.3.6.1.4.1.311.21"
# CertSrv (with associated encoders/decoders)
szOID_CERTSRV_CA_VERSION                = "1.3.6.1.4.1.311.21.1"

Microsoft_Directory_Service = "1.3.6.1.4.1.311.25"
szOID_NTDS_REPLICATION                  = "1.3.6.1.4.1.311.25.1"

IIS = "1.3.6.1.4.1.311.30"

Windows_updates_and_service_packs = "1.3.6.1.4.1.311.31"
szOID_PRODUCT_UPDATE                    = "1.3.6.1.4.1.311.31.1"

Fonts = "1.3.6.1.4.1.311.40"

Microsoft_Licensing_and_Registration = "1.3.6.1.4.1.311.41"

Microsoft_Corporate_PKI_ITG = "1.3.6.1.4.1.311.42"

CAPICOM = "1.3.6.1.4.1.311.88"
szOID_CAPICOM                           = "1.3.6.1.4.1.311.88"      # Reserved for CAPICOM.
szOID_CAPICOM_VERSION                   = "1.3.6.1.4.1.311.88.1"    # CAPICOM version
szOID_CAPICOM_ATTRIBUTE                 = "1.3.6.1.4.1.311.88.2"    # CAPICOM attribute
szOID_CAPICOM_DOCUMENT_NAME             = "1.3.6.1.4.1.311.88.2.1"  # Document type attribute
szOID_CAPICOM_DOCUMENT_DESCRIPTION      = "1.3.6.1.4.1.311.88.2.2"  # Document description attribute
szOID_CAPICOM_ENCRYPTED_DATA            = "1.3.6.1.4.1.311.88.3"    # CAPICOM encrypted data message.
szOID_CAPICOM_ENCRYPTED_CONTENT         = "1.3.6.1.4.1.311.88.3.1"  # CAPICOM content of encrypted data.
Microsoft_OID = "1.3.6.1.4.1.311"

Authenticode = "1.3.6.1.4.1.311.2"
#     Software Publishing (with associated encoders/decoders)
SPC_INDIRECT_DATA_OBJID                 = "1.3.6.1.4.1.311.2.1.4"
SPC_STATEMENT_TYPE_OBJID                = "1.3.6.1.4.1.311.2.1.11"
SPC_SP_OPUS_INFO_OBJID                  = "1.3.6.1.4.1.311.2.1.12"
SPC_PE_IMAGE_DATA_OBJID                 = "1.3.6.1.4.1.311.2.1.15"
SPC_SP_AGENCY_INFO_OBJID                = "1.3.6.1.4.1.311.2.1.10"
SPC_MINIMAL_CRITERIA_OBJID              = "1.3.6.1.4.1.311.2.1.26"
SPC_FINANCIAL_CRITERIA_OBJID            = "1.3.6.1.4.1.311.2.1.27"
SPC_LINK_OBJID                          = "1.3.6.1.4.1.311.2.1.28"
SPC_HASH_INFO_OBJID                     = "1.3.6.1.4.1.311.2.1.29"
SPC_SIPINFO_OBJID                       = "1.3.6.1.4.1.311.2.1.30"

#     Software Publishing (with NO associated encoders/decoders)
SPC_CERT_EXTENSIONS_OBJID               = "1.3.6.1.4.1.311.2.1.14"
SPC_RAW_FILE_DATA_OBJID                 = "1.3.6.1.4.1.311.2.1.18"
SPC_STRUCTURED_STORAGE_DATA_OBJID       = "1.3.6.1.4.1.311.2.1.19"
SPC_JAVA_CLASS_DATA_OBJID               = "1.3.6.1.4.1.311.2.1.20"
SPC_INDIVIDUAL_SP_KEY_PURPOSE_OBJID     = "1.3.6.1.4.1.311.2.1.21"
SPC_COMMERCIAL_SP_KEY_PURPOSE_OBJID     = "1.3.6.1.4.1.311.2.1.22"
SPC_CAB_DATA_OBJID                      = "1.3.6.1.4.1.311.2.1.25"
SPC_GLUE_RDN_OBJID                      = "1.3.6.1.4.1.311.2.1.25"

#     CTL for Software Publishers Trusted CAs    = "1.3.6.1.4.1.311.2.2"
#     (sub-subtree is defined for Software Publishing trusted CAs)
szOID_TRUSTED_CODESIGNING_CA_LIST       = "1.3.6.1.4.1.311.2.2.1"
szOID_TRUSTED_CLIENT_AUTH_CA_LIST       = "1.3.6.1.4.1.311.2.2.2"
szOID_TRUSTED_SERVER_AUTH_CA_LIST       = "1.3.6.1.4.1.311.2.2.3"

Time_Stamping = "1.3.6.1.4.1.311.3"
#(with Associated encoder/decoders)
SPC_TIME_STAMP_REQUEST_OBJID            = "1.3.6.1.4.1.311.3.2.1"

Permissions = "1.3.6.1.4.1.311.4"

Crypto_2_0 = "1.3.6.1.4.1.311.10"
#     PKCS #7 ContentType Object Identifier for Certificate Trust List (CTL)
szOID_CTL                               = "1.3.6.1.4.1.311.10.1"
#     Sorted CTL Extension
szOID_SORTED_CTL                        = "1.3.6.1.4.1.311.10.1.1"

#     Next Update Location extension or attribute. Value is an encoded GeneralNames
szOID_NEXT_UPDATE_LOCATION              = "1.3.6.1.4.1.311.10.2"

#     Enhanced Key Usage (Purpose)
#        Signer of CTLs
szOID_KP_CTL_USAGE_SIGNING              = "1.3.6.1.4.1.311.10.3.1"

#        Signer of TimeStamps
szOID_KP_TIME_STAMP_SIGNING             = "1.3.6.1.4.1.311.10.3.2"

#     Can use strong encryption in export environment
szOID_SERVER_GATED_CRYPTO               = "1.3.6.1.4.1.311.10.3.3"
szOID_SERIALIZED                        = "1.3.6.1.4.1.311.10.3.3.1"

#     Can use encrypted file systems (EFS)
szOID_EFS_CRYPTO                        = "1.3.6.1.4.1.311.10.3.4"
szOID_EFS_RECOVERY                      = "1.3.6.1.4.1.311.10.3.4.1"

#     Can use Windows Hardware Compatible (WHQL)
szOID_WHQL_CRYPTO                       = "1.3.6.1.4.1.311.10.3.5"

#     Signed by the NT5 build lab
szOID_NT5_CRYPTO                        = "1.3.6.1.4.1.311.10.3.6"

#     Signed by and OEM of WHQL
szOID_OEM_WHQL_CRYPTO                   = "1.3.6.1.4.1.311.10.3.7"

#     Signed by the Embedded NT
szOID_EMBEDDED_NT_CRYPTO                = "1.3.6.1.4.1.311.10.3.8"

#     Signer of a CTL containing trusted roots
szOID_ROOT_LIST_SIGNER                  = "1.3.6.1.4.1.311.10.3.9"

#     Can sign cross-cert and subordinate CA requests with qualified
#     subordination (name constraints, policy mapping, etc.)
szOID_KP_QUALIFIED_SUBORDINATION        = "1.3.6.1.4.1.311.10.3.10"

#     Can be used to encrypt/recover escrowed keys
szOID_KP_KEY_RECOVERY                   = "1.3.6.1.4.1.311.10.3.11"

#     Signer of documents
szOID_KP_DOCUMENT_SIGNING               = "1.3.6.1.4.1.311.10.3.12"

#     Limits the valid lifetime of the signature to the lifetime of the certificate.
szOID_KP_LIFETIME_SIGNING               = "1.3.6.1.4.1.311.10.3.13"
szOID_KP_MOBILE_DEVICE_SOFTWARE         = "1.3.6.1.4.1.311.10.3.14"

#     Microsoft Attribute Object Identifiers
szOID_YESNO_TRUST_ATTR                  = "1.3.6.1.4.1.311.10.4.1"

#     Microsoft Music
szOID_DRM                               = "1.3.6.1.4.1.311.10.5.1"

#     Microsoft DRM EKU
szOID_DRM_INDIVIDUALIZATION             = "1.3.6.1.4.1.311.10.5.2"

#     Microsoft Licenses
szOID_LICENSES                          = "1.3.6.1.4.1.311.10.6.1"
szOID_LICENSE_SERVER                    = "1.3.6.1.4.1.311.10.6.2"

#     Microsoft CERT_RDN attribute Object Identifiers
szOID_MICROSOFT_RDN_PREFIX              = "1.3.6.1.4.1.311.10.7"
#     Special RDN containing the KEY_ID. Its value type is CERT_RDN_OCTET_STRING.
szOID_KEYID_RDN                         = "1.3.6.1.4.1.311.10.7.1"

#  Microsoft extension in a CTL to add or remove the certificates. The
#  extension type is an INTEGER. 0 => add certificate, 1 => remove certificate
#     szOID_REMOVE_CERTIFICATE                = "1.3.6.1.4.1.311.10.8.1"
#
#  Microsoft certificate extension containing cross certificate distribution
#  points. ASN.1 encoded as follows:
#      CrossCertDistPoints ::= SEQUENCE {
#          syncDeltaTime               INTEGER (0 4294967295) OPTIONAL,
#          crossCertDistPointNames     CrossCertDistPointNames
#      } --#public--
#           CrossCertDistPointNames ::= SEQUENCE OF GeneralNames

szOID_CROSS_CERT_DIST_POINTS            = "1.3.6.1.4.1.311.10.9.1"


#     Microsoft CMC OIDs                         = "1.3.6.1.4.1.311.10.10"

#     Similar to szOID_CMC_ADD_EXTENSIONS. Attributes replaces Extensions.
szOID_CMC_ADD_ATTRIBUTES                = "1.3.6.1.4.1.311.10.10.1"

#     Microsoft certificate property OIDs        = "1.3.6.1.4.1.311.10.11"
#     The OID component following the prefix contains the PROP_ID (decimal)
szOID_CERT_PROP_ID_PREFIX               = "1.3.6.1.4.1.311.10.11"

#     CryptUI                                    = "1.3.6.1.4.1.311.10.12"
szOID_ANY_APPLICATION_POLICY            = "1.3.6.1.4.1.311.10.12.1"

# Catalog = "1.3.6.1.4.1.311.12"
szOID_CATALOG_LIST                      = "1.3.6.1.4.1.311.12.1.1"
szOID_CATALOG_LIST_MEMBER               = "1.3.6.1.4.1.311.12.1.2"
CAT_NAMEVALUE_OBJID                     = "1.3.6.1.4.1.311.12.2.1"
CAT_MEMBERINFO_OBJID                    = "1.3.6.1.4.1.311.12.2.2"

# Microsoft PKCS10 OIDs = "1.3.6.1.4.1.311.13"
szOID_RENEWAL_CERTIFICATE               = "1.3.6.1.4.1.311.13.1"
szOID_ENROLLMENT_NAME_VALUE_PAIR        = "1.3.6.1.4.1.311.13.2.1"
szOID_ENROLLMENT_CSP_PROVIDER           = "1.3.6.1.4.1.311.13.2.2"
szOID_OS_VERSION                        = "1.3.6.1.4.1.311.13.2.3"

Microsoft_Java = "1.3.6.1.4.1.311.15"

Microsoft_Outlook_Exchange = "1.3.6.1.4.1.311.16"
#       Used by OL/OLEXP to identify which certificate signed the PKCS # 7 message
szOID_MICROSOFT_Encryption_Key_Preference  = "1.3.6.1.4.1.311.16.4"

# Microsoft PKCS12 attributes = "1.3.6.1.4.1.311.17"
szOID_LOCAL_MACHINE_KEYSET              = "1.3.6.1.4.1.311.17.1"

#Microsoft Hydra = "1.3.6.1.4.1.311.18"
#     License Info root
szOID_PKIX_LICENSE_INFO                 = "1.3.6.1.4.1.311.18.1"

#     Manufacturer value
szOID_PKIX_MANUFACTURER                 = "1.3.6.1.4.1.311.18.2"

#     Manufacturer Specfic Data
szOID_PKIX_MANUFACTURER_MS_SPECIFIC     = "1.3.6.1.4.1.311.18.3"

#     OID for Certificate Version Stamp
szOID_PKIX_HYDRA_CERT_VERSION           = "1.3.6.1.4.1.311.18.4"

#     OID for License Server to identify licensed product.
szOID_PKIX_LICENSED_PRODUCT_INFO        = "1.3.6.1.4.1.311.18.5"

#     OID for License Server specific info.
szOID_PKIX_MS_LICENSE_SERVER_INFO       = "1.3.6.1.4.1.311.18.6"

#     Extension OID reserved for product policy module - only one is allowed.
szOID_PKIS_PRODUCT_SPECIFIC_OID         = "1.3.6.1.4.1.311.18.7"
szOID_PKIS_TLSERVER_SPK_OID             = "1.3.6.1.4.1.311.18.8"

#Microsoft ISPU Test = "1.3.6.1.4.1.311.19"

#Microsoft Enrollment Infrastructure = "1.3.6.1.4.1.311.20"
szOID_AUTO_ENROLL_CTL_USAGE             = "1.3.6.1.4.1.311.20.1"
#     Extension contain certificate type
szOID_ENROLL_CERTTYPE_EXTENSION         = "1.3.6.1.4.1.311.20.2"
szOID_ENROLLMENT_AGENT                  = "1.3.6.1.4.1.311.20.2.1"
szOID_KP_SMARTCARD_LOGON                = "1.3.6.1.4.1.311.20.2.2"
szOID_NT_PRINCIPAL_NAME                 = "1.3.6.1.4.1.311.20.2.3"
szOID_CERT_MANIFOLD                     = "1.3.6.1.4.1.311.20.3"

# Microsoft CertSrv Infrastructure = "1.3.6.1.4.1.311.21"
#     CertSrv (with associated encoders/decoders)
szOID_CERTSRV_CA_VERSION                = "1.3.6.1.4.1.311.21.1"

#     Contains the sha1 hash of the previous version of the CA certificate.
szOID_CERTSRV_PREVIOUS_CERT_HASH        = "1.3.6.1.4.1.311.21.2"

#     Delta CRLs only. Contains the base CRL Number of the corresponding base CRL.
szOID_CRL_VIRTUAL_BASE                  = "1.3.6.1.4.1.311.21.3"

#     Contains the time when the next CRL is expected to be published. This may be sooner than the CRL's NextUpdate field.
szOID_CRL_NEXT_PUBLISH                  = "1.3.6.1.4.1.311.21.4"

#     Enhanced Key Usage for CA encryption certificate
szOID_KP_CA_EXCHANGE                    = "1.3.6.1.4.1.311.21.5"

#     Enhanced Key Usage for key recovery agent certificate
szOID_KP_KEY_RECOVERY_AGENT             = "1.3.6.1.4.1.311.21.6"

#     Certificate template extension (v2)
szOID_CERTIFICATE_TEMPLATE              = "1.3.6.1.4.1.311.21.7"

#     The root oid for all enterprise specific oids
szOID_ENTERPRISE_OID_ROOT               = "1.3.6.1.4.1.311.21.8"

#     Dummy signing Subject RDN
szOID_RDN_DUMMY_SIGNER                  = "1.3.6.1.4.1.311.21.9"

#     Application Policies extension -- same encoding as szOID_CERT_POLICIES
szOID_APPLICATION_CERT_POLICIES         = "1.3.6.1.4.1.311.21.10"

#     Application Policy Mappings -- same encoding as szOID_POLICY_MAPPINGS
szOID_APPLICATION_POLICY_MAPPINGS       = "1.3.6.1.4.1.311.21.11"

#     Application Policy Constraints -- same encoding as szOID_POLICY_CONSTRAINTS
szOID_APPLICATION_POLICY_CONSTRAINTS    = "1.3.6.1.4.1.311.21.12"

szOID_ARCHIVED_KEY_ATTR                 = "1.3.6.1.4.1.311.21.13"
szOID_CRL_SELF_CDP                      = "1.3.6.1.4.1.311.21.14"

#     Requires all certificates below the root to have a non-empty intersecting issuance certificate policy usage.
szOID_REQUIRE_CERT_CHAIN_POLICY         = "1.3.6.1.4.1.311.21.15"
szOID_ARCHIVED_KEY_CERT_HASH            = "1.3.6.1.4.1.311.21.16"
szOID_ISSUED_CERT_HASH                  = "1.3.6.1.4.1.311.21.17"

#     Enhanced key usage for DS email replication
szOID_DS_EMAIL_REPLICATION              = "1.3.6.1.4.1.311.21.19"

szOID_REQUEST_CLIENT_INFO               = "1.3.6.1.4.1.311.21.20"
szOID_ENCRYPTED_KEY_HASH                = "1.3.6.1.4.1.311.21.21"
szOID_CERTSRV_CROSSCA_VERSION           = "1.3.6.1.4.1.311.21.22"

#Microsoft Directory Service = "1.3.6.1.4.1.311.25"
szOID_NTDS_REPLICATION                  = "1.3.6.1.4.1.311.25.1"

#IIS = "1.3.6.1.4.1.311.30"
szOID_IIS_VIRTUAL_SERVER                = "1.3.6.1.4.1.311.30.1"

Microsoft_WWOps_BizExt = "1.3.6.1.4.1.311.43"


#Microsoft Peer Networking = "1.3.6.1.4.1.311.44"
#     Subtrees for genaral use including pnrp, IM, and grouping
# szOID_PEERNET_GENERAL
szOID_PEERNET_PNRP                      = "1.3.6.1.4.1.311.44.1"
szOID_PEERNET_IDENTITY                  = "1.3.6.1.4.1.311.44.2"
szOID_PEERNET_GROUPING                  = "1.3.6.1.4.1.311.44.3"

#     Property that contains the type of the certificate (GMC, GRC, etc.)
szOID_PEERNET_CERT_TYPE                 = "1.3.6.1.4.1.311.44.0.1"

#     Type of the value in the 'other' name: peer name
szOID_PEERNET_PEERNAME                  = "1.3.6.1.4.1.311.44.0.2"

#     Type : classifier
szOID_PEERNET_CLASSIFIER                = "1.3.6.1.4.1.311.44.0.3"

#     Property containing the version of the certificate
szOID_PEERNET_CERT_VERSION              = "1.3.6.1.4.1.311.44.0.4"

#     PNRP specific properties
szOID_PEERNET_PNRP_ADDRESS              = "1.3.6.1.4.1.311.44.1.1"
szOID_PEERNET_PNRP_FLAGS                = "1.3.6.1.4.1.311.44.1.2"
szOID_PEERNET_PNRP_PAYLOAD              = "1.3.6.1.4.1.311.44.1.3"
szOID_PEERNET_PNRP_ID                   = "1.3.6.1.4.1.311.44.1.4"

#     Identity flags, placeholder
szOID_PEERNET_IDENTITY_FLAGS            = "1.3.6.1.4.1.311.44.2.2"

#     Peer name of the group
szOID_PEERNET_GROUPING_PEERNAME         = "1.3.6.1.4.1.311.44.3.1"

#     Group flags: placeholder
szOID_PEERNET_GROUPING_FLAGS            = "1.3.6.1.4.1.311.44.3.2"

#     List of roles in the GMC
szOID_PEERNET_GROUPING_ROLES            = "1.3.6.1.4.1.311.44.3.3"

#     List of classifiers in the GMC
szOID_PEERNET_GROUPING_CLASSIFIERS      = "1.3.6.1.4.1.311.44.3.5"

Mobile_Devices_Code_Signing = "1.3.6.1.4.1.311.45"

#CAPICOM = "1.3.6.1.4.1.311.88"
#     Reserved for CAPICOM.
szOID_CAPICOM                           = "1.3.6.1.4.1.311.88"

#     CAPICOM version
szOID_CAPICOM_VERSION                   = "1.3.6.1.4.1.311.88.1"

#     CAPICOM attribute
szOID_CAPICOM_ATTRIBUTE                 = "1.3.6.1.4.1.311.88.2"

#     Document type attribute
szOID_CAPICOM_DOCUMENT_NAME             = "1.3.6.1.4.1.311.88.2.1"

#     Document description attribute
szOID_CAPICOM_DOCUMENT_DESCRIPTION      = "1.3.6.1.4.1.311.88.2.2"

#     CAPICOM encrypted data message.
szOID_CAPICOM_ENCRYPTED_DATA            = "1.3.6.1.4.1.311.88.3"

#     CAPICOM content of encrypted data.
szOID_CAPICOM_ENCRYPTED_CONTENT         = "1.3.6.1.4.1.311.88.3.1"
