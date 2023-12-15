"""Attribute Tags for IPP."""
from .enums import IppTag

ATTRIBUTE_TAG_MAP = {
    "attributes-charset": IppTag.CHARSET,
    "attributes-natural-language": IppTag.LANGUAGE,
    "document-number": IppTag.INTEGER,
    "printer-uri": IppTag.URI,
    "requesting-user-name": IppTag.NAME,
    "job-id": IppTag.INTEGER,
    "document-name": IppTag.NAME,
    "job-name": IppTag.NAME,
    "document-format": IppTag.MIME_TYPE,
    "last-document": IppTag.BOOLEAN,
    "copies": IppTag.INTEGER,
    "job-cancel-after": IppTag.INTEGER,
    "job-hold-until": IppTag.KEYWORD,
    "job-k-octets": IppTag.INTEGER,
    "job-impressions-completed": IppTag.INTEGER,
    "job-media-sheets-completed": IppTag.INTEGER,
    "job-originating-host-name": IppTag.NAME,
    "job-originating-user-name": IppTag.NAME,
    "job-printer-state-message": IppTag.TEXT,
    "job-printer-state-reasons": IppTag.KEYWORD,
    "job-priority": IppTag.INTEGER,
    "number-up": IppTag.INTEGER,
    "job-sheets": IppTag.NAME,
    "job-uri": IppTag.URI,
    "job-state": IppTag.ENUM,
    "job-state-reasons": IppTag.KEYWORD,
    "job-uuid": IppTag.URI,
    "requested-attributes": IppTag.KEYWORD,
    "member-uris": IppTag.URI,
    "operations-supported": IppTag.ENUM,
    "ppd-name": IppTag.NAME,
    "printer-state-reason": IppTag.KEYWORD,
    "printer-is-shared": IppTag.BOOLEAN,
    "printer-error-policy": IppTag.NAME,
    "printer-geo-location": IppTag.URI,
    "printer-info": IppTag.TEXT,
    "printer-organization": IppTag.TEXT,
    "printer-organizational-unit": IppTag.TEXT,
    "which-jobs": IppTag.KEYWORD,
    "my-jobs": IppTag.BOOLEAN,
    "purge-jobs": IppTag.BOOLEAN,
    "hold-job-until": IppTag.KEYWORD,
    "job-printer-uri": IppTag.URI,
    "printer-location": IppTag.TEXT,
    "printer-state": IppTag.ENUM,
    "printer-state-reasons": IppTag.KEYWORD,
    "printer-up-time": IppTag.INTEGER,
    "printer-uri-supported": IppTag.URI,
    "document-state": IppTag.ENUM,
    "device-uri": IppTag.URI,
    "ipp-attribute-fidelity": IppTag.BOOLEAN,
    "finishings": IppTag.ENUM,
    "orientation-requested": IppTag.ENUM,
    "print-quality": IppTag.ENUM,
    "time-at-creation": IppTag.INTEGER,
    "time-at-processing": IppTag.INTEGER,
    "time-at-completed": IppTag.INTEGER,
    "x-dimension": IppTag.INTEGER,
    "y-dimension": IppTag.INTEGER,
    "media-top-margin": IppTag.INTEGER,
    "media-bottom-margin": IppTag.INTEGER,
    "media-right-margin": IppTag.INTEGER,
    "media-left-margin": IppTag.INTEGER,
    "media-source": IppTag.KEYWORD,
    "media-type": IppTag.KEYWORD,
}
