"""Country data and mapping utilities for NordVPN."""

from typing import TypedDict


class CountryInfo(TypedDict):
    """Type definition for country information."""

    id: str
    name: str


# Mapping of ISO 3166-1 alpha-2 codes to NordVPN country IDs
NORDVPN_COUNTRY_IDS: dict[str, str] = {
    "AL": "2",  # Albania
    "DZ": "3",  # Algeria
    "AD": "5",  # Andorra
    "AR": "10",  # Argentina
    "AM": "11",  # Armenia
    "AU": "13",  # Australia
    "AT": "14",  # Austria
    "AZ": "15",  # Azerbaijan
    "BS": "16",  # Bahamas
    "BD": "18",  # Bangladesh
    "BE": "21",  # Belgium
    "BZ": "22",  # Belize
    "BM": "24",  # Bermuda
    "BT": "25",  # Bhutan
    "BO": "26",  # Bolivia
    "BA": "27",  # Bosnia and Herzegovina
    "BR": "30",  # Brazil
    "BN": "32",  # Brunei
    "BG": "33",  # Bulgaria
    "KH": "36",  # Cambodia
    "CA": "38",  # Canada
    "KY": "40",  # Cayman Islands
    "CL": "43",  # Chile
    "CO": "47",  # Colombia
    "CR": "52",  # Costa Rica
    "HR": "54",  # Croatia
    "CY": "56",  # Cyprus
    "CZ": "57",  # Czech Republic
    "DK": "58",  # Denmark
    "DO": "61",  # Dominican Republic
    "EC": "63",  # Ecuador
    "EG": "64",  # Egypt
    "SV": "65",  # El Salvador
    "EE": "68",  # Estonia
    "FI": "73",  # Finland
    "FR": "74",  # France
    "GE": "80",  # Georgia
    "DE": "81",  # Germany
    "GH": "82",  # Ghana
    "GR": "84",  # Greece
    "GL": "85",  # Greenland
    "GU": "88",  # Guam
    "GT": "89",  # Guatemala
    "HN": "96",  # Honduras
    "HK": "97",  # Hong Kong
    "HU": "98",  # Hungary
    "IS": "99",  # Iceland
    "IN": "100",  # India
    "ID": "101",  # Indonesia
    "IE": "104",  # Ireland
    "IM": "243",  # Isle of Man
    "IL": "105",  # Israel
    "IT": "106",  # Italy
    "JM": "107",  # Jamaica
    "JP": "108",  # Japan
    "JE": "244",  # Jersey
    "KZ": "110",  # Kazakhstan
    "KE": "111",  # Kenya
    "LA": "118",  # Laos
    "LV": "119",  # Latvia
    "LB": "120",  # Lebanon
    "LI": "124",  # Liechtenstein
    "LT": "125",  # Lithuania
    "LU": "126",  # Luxembourg
    "MY": "131",  # Malaysia
    "MT": "134",  # Malta
    "MX": "140",  # Mexico
    "MD": "142",  # Moldova
    "MC": "143",  # Monaco
    "MN": "144",  # Mongolia
    "ME": "146",  # Montenegro
    "MA": "147",  # Morocco
    "MM": "149",  # Myanmar
    "NP": "152",  # Nepal
    "NL": "153",  # Netherlands
    "NZ": "156",  # New Zealand
    "NG": "159",  # Nigeria
    "MK": "128",  # North Macedonia
    "NO": "163",  # Norway
    "PK": "165",  # Pakistan
    "PA": "168",  # Panama
    "PG": "169",  # Papua New Guinea
    "PY": "170",  # Paraguay
    "PE": "171",  # Peru
    "PH": "172",  # Philippines
    "PL": "174",  # Poland
    "PT": "175",  # Portugal
    "PR": "176",  # Puerto Rico
    "RO": "179",  # Romania
    "RS": "192",  # Serbia
    "SG": "195",  # Singapore
    "SK": "196",  # Slovakia
    "SI": "197",  # Slovenia
    "ZA": "200",  # South Africa
    "KR": "114",  # South Korea
    "ES": "202",  # Spain
    "LK": "203",  # Sri Lanka
    "SE": "208",  # Sweden
    "CH": "209",  # Switzerland
    "TH": "214",  # Thailand
    "TT": "218",  # Trinidad and Tobago
    "TR": "220",  # Turkey
    "UA": "225",  # Ukraine
    "AE": "226",  # United Arab Emirates
    "GB": "227",  # United Kingdom
    "US": "228",  # United States
    "UY": "230",  # Uruguay
    "UZ": "231",  # Uzbekistan
    "VE": "233",  # Venezuela
    "VN": "234",  # Vietnam
}


def get_country_id(country_code: str) -> str | None:
    """Get NordVPN country ID from ISO 3166-1 alpha-2 country code.

    Args:
        country_code: ISO 3166-1 alpha-2 country code (e.g., 'US')

    Returns:
        str | None: NordVPN country ID if found, None otherwise
    """
    return NORDVPN_COUNTRY_IDS.get(country_code.upper())
