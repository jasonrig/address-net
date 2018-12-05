from collections import OrderedDict
from typing import Union

# Categorical types as per the GNAF dataset, see: https://data.gov.au/dataset/geocoded-national-address-file-g-naf
flat_types = ('ANTENNA', 'APARTMENT', 'AUTOMATED TELLER MACHINE', 'BARBECUE', 'BLOCK', 'BOATSHED', 'BUILDING',
              'BUNGALOW', 'CAGE', 'CARPARK', 'CARSPACE', 'CLUB', 'COOLROOM', 'COTTAGE', 'DUPLEX', 'FACTORY', 'FLAT',
              'GARAGE', 'HALL', 'HOUSE', 'KIOSK', 'LEASE', 'LOBBY', 'LOFT', 'LOT', 'MAISONETTE', 'MARINE BERTH',
              'OFFICE', 'PENTHOUSE', 'REAR', 'RESERVE', 'ROOM', 'SECTION', 'SHED', 'SHOP', 'SHOWROOM', 'SIGN', 'SITE',
              'STALL', 'STORE', 'STRATA UNIT', 'STUDIO', 'SUBSTATION', 'SUITE', 'TENANCY', 'TOWER', 'TOWNHOUSE',
              'UNIT', 'VAULT', 'VILLA', 'WARD', 'WAREHOUSE', 'WORKSHOP')

level_types = ('BASEMENT', 'FLOOR', 'GROUND', 'LEVEL', 'LOBBY', 'LOWER GROUND FLOOR', 'MEZZANINE', 'OBSERVATION DECK',
               'PARKING', 'PENTHOUSE', 'PLATFORM', 'PODIUM', 'ROOFTOP', 'SUB-BASEMENT', 'UPPER GROUND FLOOR')

street_types = ('ACCESS', 'ACRE', 'AIRWALK', 'ALLEY', 'ALLEYWAY', 'AMBLE', 'APPROACH', 'ARCADE', 'ARTERIAL', 'ARTERY',
                'AVENUE', 'BANAN', 'BANK', 'BAY', 'BEACH', 'BEND', 'BOARDWALK', 'BOULEVARD', 'BOULEVARDE', 'BOWL',
                'BRACE', 'BRAE', 'BRANCH', 'BREAK', 'BRETT', 'BRIDGE', 'BROADWALK', 'BROADWAY', 'BROW', 'BULL',
                'BUSWAY', 'BYPASS', 'BYWAY', 'CAUSEWAY', 'CENTRE', 'CENTREWAY', 'CHASE', 'CIRCLE', 'CIRCLET',
                'CIRCUIT', 'CIRCUS', 'CLOSE', 'CLUSTER', 'COLONNADE', 'COMMON', 'COMMONS', 'CONCORD', 'CONCOURSE',
                'CONNECTION', 'COPSE', 'CORNER', 'CORSO', 'COURSE', 'COURT', 'COURTYARD', 'COVE', 'CRESCENT', 'CREST',
                'CRIEF', 'CROOK', 'CROSS', 'CROSSING', 'CRUISEWAY', 'CUL-DE-SAC', 'CUT', 'CUTTING', 'DALE', 'DASH',
                'DELL', 'DENE', 'DEVIATION', 'DIP', 'DISTRIBUTOR', 'DIVIDE', 'DOCK', 'DOMAIN', 'DOWN', 'DOWNS',
                'DRIVE', 'DRIVEWAY', 'EASEMENT', 'EAST', 'EDGE', 'ELBOW', 'END', 'ENTRANCE', 'ESPLANADE', 'ESTATE',
                'EXPRESSWAY', 'EXTENSION', 'FAIRWAY', 'FIREBREAK', 'FIRELINE', 'FIRETRACK', 'FIRETRAIL', 'FLAT',
                'FLATS', 'FOLLOW', 'FOOTWAY', 'FORD', 'FORESHORE', 'FORK', 'FORMATION', 'FREEWAY', 'FRONT', 'FRONTAGE',
                'GAP', 'GARDEN', 'GARDENS', 'GATE', 'GATEWAY', 'GLADE', 'GLEN', 'GRANGE', 'GREEN', 'GROVE', 'GULLY',
                'HARBOUR', 'HAVEN', 'HEATH', 'HEIGHTS', 'HIGHROAD', 'HIGHWAY', 'HIKE', 'HILL', 'HILLS', 'HOLLOW',
                'HUB', 'INLET', 'INTERCHANGE', 'ISLAND', 'JUNCTION', 'KEY', 'KEYS', 'KNOLL', 'LADDER', 'LANDING',
                'LANE', 'LANEWAY', 'LEAD', 'LEADER', 'LINE', 'LINK', 'LOOKOUT', 'LOOP', 'LYNNE', 'MALL', 'MANOR',
                'MART', 'MAZE', 'MEAD', 'MEANDER', 'MEW', 'MEWS', 'MILE', 'MOTORWAY', 'NOOK', 'NORTH', 'NULL',
                'OUTLET', 'OUTLOOK', 'OVAL', 'PALMS', 'PARADE', 'PARADISE', 'PARK', 'PARKWAY', 'PART', 'PASS',
                'PASSAGE', 'PATH', 'PATHWAY', 'PENINSULA', 'PIAZZA', 'PLACE', 'PLAZA', 'POCKET', 'POINT', 'PORT',
                'PRECINCT', 'PROMENADE', 'PURSUIT', 'QUAD', 'QUADRANT', 'QUAY', 'QUAYS', 'RAMBLE', 'RAMP', 'RANGE',
                'REACH', 'REEF', 'RESERVE', 'REST', 'RETREAT', 'RETURN', 'RIDE', 'RIDGE', 'RIGHT OF WAY', 'RING',
                'RISE', 'RISING', 'RIVER', 'ROAD', 'ROADS', 'ROADWAY', 'ROTARY', 'ROUND', 'ROUTE', 'ROW', 'ROWE',
                'RUE', 'RUN', 'SERVICEWAY', 'SHUNT', 'SKYLINE', 'SLOPE', 'SOUTH', 'SPUR', 'SQUARE', 'STEPS',
                'STRAIGHT', 'STRAIT', 'STRAND', 'STREET', 'STRIP', 'SUBWAY', 'TARN', 'TERRACE', 'THOROUGHFARE',
                'THROUGHWAY', 'TOLLWAY', 'TOP', 'TOR', 'TRACK', 'TRAIL', 'TRAMWAY', 'TRAVERSE', 'TRIANGLE', 'TRUNKWAY',
                'TUNNEL', 'TURN', 'TWIST', 'UNDERPASS', 'VALE', 'VALLEY', 'VERGE', 'VIADUCT', 'VIEW', 'VIEWS', 'VILLA',
                'VILLAGE', 'VILLAS', 'VISTA', 'VUE', 'WADE', 'WALK', 'WALKWAY', 'WATERS', 'WATERWAY', 'WAY', 'WEST',
                'WHARF', 'WOOD', 'WOODS', 'WYND', 'YARD')

street_suffix_types = OrderedDict([('CN', 'CENTRAL'), ('DE', 'DEVIATION'), ('E', 'EAST'), ('EX', 'EXTENSION'),
                                   ('IN', 'INNER'), ('LR', 'LOWER'), ('ML', 'MALL'), ('N', 'NORTH'),
                                   ('NE', 'NORTH EAST'), ('NW', 'NORTH WEST'), ('OF', 'OFF'), ('ON', 'ON'),
                                   ('OT', 'OUTER'), ('OP', 'OVERPASS'), ('S', 'SOUTH'), ('SE', 'SOUTH EAST'),
                                   ('SW', 'SOUTH WEST'), ('UP', 'UPPER'), ('W', 'WEST')])

states = OrderedDict([('ACT', 'AUSTRALIAN CAPITAL TERRITORY'), ('NSW', 'NEW SOUTH WALES'),
                      ('NT', 'NORTHERN TERRITORY'), ('OT', 'OTHER TERRITORIES'), ('QLD', 'QUEENSLAND'),
                      ('SA', 'SOUTH AUSTRALIA'), ('TAS', 'TASMANIA'), ('VIC', 'VICTORIA'),
                      ('WA', 'WESTERN AUSTRALIA')])

# Abbreviaitons from METeOR identifier: 429387
# see https://meteor.aihw.gov.au/content/index.phtml/itemId/429387/pageDefinitionItemId/tag.MeteorPrinterFriendlyPage
street_type_abbreviation = {'ACCESS': 'ACCS', 'ALLEY': 'ALLY', 'ALLEYWAY': 'ALWY', 'AMBLE': 'AMBL', 'APPROACH': 'APP',
                            'ARCADE': 'ARC', 'ARTERIAL': 'ARTL', 'ARTERY': 'ARTY', 'AVENUE': 'AV', 'BANAN': 'BA',
                            'BEND': 'BEND', 'BOARDWALK': 'BWLK', 'BOULEVARD': 'BVD', 'BRACE': 'BR', 'BRAE': 'BRAE',
                            'BREAK': 'BRK', 'BROW': 'BROW', 'BYPASS': 'BYPA', 'BYWAY': 'BYWY', 'CAUSEWAY': 'CSWY',
                            'CENTRE': 'CTR', 'CHASE': 'CH', 'CIRCLE': 'CIR', 'CIRCUIT': 'CCT', 'CIRCUS': 'CRCS',
                            'CLOSE': 'CL', 'CONCOURSE': 'CON', 'COPSE': 'CPS', 'CORNER': 'CNR', 'COURT': 'CT',
                            'COURTYARD': 'CTYD', 'COVE': 'COVE', 'CRESCENT': 'CR', 'CREST': 'CRST', 'CROSS': 'CRSS',
                            'CUL-DE-SAC': 'CSAC', 'CUTTING': 'CUTT', 'DALE': 'DALE', 'DIP': 'DIP', 'DRIVE': 'DR',
                            'DRIVEWAY': 'DVWY', 'EDGE': 'EDGE', 'ELBOW': 'ELB', 'END': 'END', 'ENTRANCE': 'ENT',
                            'ESPLANADE': 'ESP', 'EXPRESSWAY': 'EXP', 'FAIRWAY': 'FAWY', 'FOLLOW': 'FOLW',
                            'FOOTWAY': 'FTWY', 'FORMATION': 'FORM', 'FREEWAY': 'FWY', 'FRONTAGE': 'FRTG',
                            'GAP': 'GAP', 'GARDENS': 'GDNS', 'GATE': 'GTE', 'GLADE': 'GLDE', 'GLEN': 'GLEN',
                            'GRANGE': 'GRA', 'GREEN': 'GRN', 'GROVE': 'GR', 'HEIGHTS': 'HTS', 'HIGHROAD': 'HIRD',
                            'HIGHWAY': 'HWY', 'HILL': 'HILL', 'INTERCHANGE': 'INTG', 'JUNCTION': 'JNC', 'KEY': 'KEY',
                            'LANE': 'LANE', 'LANEWAY': 'LNWY', 'LINE': 'LINE', 'LINK': 'LINK', 'LOOKOUT': 'LKT',
                            'LOOP': 'LOOP', 'MALL': 'MALL', 'MEANDER': 'MNDR', 'MEWS': 'MEWS', 'MOTORWAY': 'MTWY',
                            'NOOK': 'NOOK', 'OUTLOOK': 'OTLK', 'PARADE': 'PDE', 'PARKWAY': 'PWY', 'PASS': 'PASS',
                            'PASSAGE': 'PSGE', 'PATH': 'PATH', 'PATHWAY': 'PWAY', 'PIAZZA': 'PIAZ', 'PLAZA': 'PLZA',
                            'POCKET': 'PKT', 'POINT': 'PNT', 'PORT': 'PORT', 'PROMENADE': 'PROM', 'QUADRANT': 'QDRT',
                            'QUAYS': 'QYS', 'RAMBLE': 'RMBL', 'REST': 'REST', 'RETREAT': 'RTT', 'RIDGE': 'RDGE',
                            'RISE': 'RISE', 'ROAD': 'RD', 'ROTARY': 'RTY', 'ROUTE': 'RTE', 'ROW': 'ROW', 'RUE': 'RUE',
                            'SERVICEWAY': 'SVWY', 'SHUNT': 'SHUN', 'SPUR': 'SPUR', 'SQUARE': 'SQ', 'STREET': 'ST',
                            'SUBWAY': 'SBWY', 'TARN': 'TARN', 'TERRACE': 'TCE', 'THOROUGHFARE': 'THFR',
                            'TOLLWAY': 'TLWY', 'TOP': 'TOP', 'TOR': 'TOR', 'TRACK': 'TRK', 'TRAIL': 'TRL',
                            'TURN': 'TURN', 'UNDERPASS': 'UPAS', 'VALE': 'VALE', 'VIADUCT': 'VIAD', 'VIEW': 'VIEW',
                            'VISTA': 'VSTA', 'WALK': 'WALK', 'WALKWAY': 'WKWY', 'WHARF': 'WHRF', 'WYND': 'WYND'}

ordinal_words = [
    'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh',
    'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth',
    'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 'twenty-fourth', 'twenty-fifth', 'twenty-sixth',
    'twenty-seventh', 'twenty-eighth', 'twenty-ninth', 'thirtieth', 'thirty-first', 'thirty-second', 'thirty-third',
    'thirty-fourth', 'thirty-fifth', 'thirty-sixth', 'thirty-seventh', 'thirty-eighth', 'thirty-ninth', 'fortieth',
    'forty-first', 'forty-second', 'forty-third', 'forty-fourth', 'forty-fifth', 'forty-sixth', 'forty-seventh',
    'forty-eighth', 'forty-ninth', 'fiftieth', 'fifty-first', 'fifty-second', 'fifty-third', 'fifty-fourth',
    'fifty-fifth', 'fifty-sixth', 'fifty-seventh', 'fifty-eighth', 'fifty-ninth', 'sixtieth', 'sixty-first',
    'sixty-second', 'sixty-third', 'sixty-fourth', 'sixty-fifth', 'sixty-sixth', 'sixty-seventh', 'sixty-eighth',
    'sixty-ninth', 'seventieth', 'seventy-first', 'seventy-second', 'seventy-third', 'seventy-fourth', 'seventy-fifth',
    'seventy-sixth', 'seventy-seventh', 'seventy-eighth', 'seventy-ninth', 'eightieth', 'eighty-first', 'eighty-second',
    'eighty-third', 'eighty-fourth', 'eighty-fifth', 'eighty-sixth', 'eighty-seventh', 'eighty-eighth', 'eighty-ninth',
    'ninetieth', 'ninety-first', 'ninety-second', 'ninety-third', 'ninety-fourth', 'ninety-fifth', 'ninety-sixth',
    'ninety-seventh', 'ninety-eighth', 'ninety-ninth', 'one hundredth'
]

cardinal_words = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
    'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two',
    'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine', 'thirty',
    'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four', 'thirty-five', 'thirty-six', 'thirty-seven',
    'thirty-eight', 'thirty-nine', 'forty', 'forty-one', 'forty-two', 'forty-three', 'forty-four', 'forty-five',
    'forty-six', 'forty-seven', 'forty-eight', 'forty-nine', 'fifty', 'fifty-one', 'fifty-two', 'fifty-three',
    'fifty-four', 'fifty-five', 'fifty-six', 'fifty-seven', 'fifty-eight', 'fifty-nine', 'sixty', 'sixty-one',
    'sixty-two', 'sixty-three', 'sixty-four', 'sixty-five', 'sixty-six', 'sixty-seven', 'sixty-eight', 'sixty-nine',
    'seventy', 'seventy-one', 'seventy-two', 'seventy-three', 'seventy-four', 'seventy-five', 'seventy-six',
    'seventy-seven', 'seventy-eight', 'seventy-nine', 'eighty', 'eighty-one', 'eighty-two', 'eighty-three',
    'eighty-four', 'eighty-five', 'eighty-six', 'eighty-seven', 'eighty-eight', 'eighty-nine', 'ninety', 'ninety-one',
    'ninety-two', 'ninety-three', 'ninety-four', 'ninety-five', 'ninety-six', 'ninety-seven', 'ninety-eight',
    'ninety-nine', 'one hundred'
]


def _lookup(t: str, types: [str]) -> int:
    """
    Looks up the value, t, from the array of types
    :param t: value to lookup
    :param types: list of types from which to lookup
    :return: an integer value > 0 if found, or 0 if not found
    """
    try:
        return types.index(t.strip().upper()) + 1
    except ValueError:
        return 0


def _reverse_lookup(idx: int, types: [str]) -> str:
    """
    Converts an integer value back to the string representation
    :param idx: integer value
    :param types: list of types
    :return: the string value or None if not found (idx == 0)
    """
    if idx == 0:
        return ''
    else:
        return types[idx - 1]


def lookup_state(state: Union[str, int], reverse_lookup=False) -> Union[str, int]:
    """
    Converts the representation for the geographic state
    :param state: string or int to lookup
    :param reverse_lookup: True if converting int to string, or False if string to int
    :return: the encoded value
    """
    if reverse_lookup:
        return _reverse_lookup(state, list(states.keys()))
    return _lookup(state, list(states.keys()))


def expand_state(state: str) -> str:
    """
    Converts an abbreviated state name to the full name, e.g. "VIC" -> "VICTORIA"
    :param state: abbreviated state
    :return: full state
    """
    return states[state.strip().upper()]


def lookup_street_type(street_type: Union[str, int], reverse_lookup=False) -> Union[str, int]:
    """
    Converts the representation for the street type
    :param street_type: string or int to lookup
    :param reverse_lookup: True if converting int to string, or False if string to int
    :return: the encoded value
    """
    if reverse_lookup:
        return _reverse_lookup(street_type, street_types)
    return _lookup(street_type, street_types)


def abbreviate_street_type(street_type: str) -> str:
    """
    Converts an full street type to the abbreviated name, e.g. "STREET" -> "ST"
    :param street_type: full street type
    :return: abbreviated street type
    """
    try:
        return street_type_abbreviation[street_type.strip().upper()]
    except KeyError:
        return street_type


def lookup_street_suffix(street_suffix: Union[str, int], reverse_lookup=False) -> Union[str, int]:
    """
    Converts the representation for the street type suffix
    :param street_suffix: string or int to lookup
    :param reverse_lookup: True if converting int to string, or False if string to int
    :return: the encoded value
    """
    if reverse_lookup:
        return _reverse_lookup(street_suffix, list(street_suffix_types.keys()))
    return _lookup(street_suffix, list(street_suffix_types.keys()))


def expand_street_type_suffix(street_suffix: str) -> str:
    """
    Converts an abbreviated street suffix to the full name, e.g. "N" -> "NORTH"
    :param street_suffix: abbreviated street suffix
    :return: full street suffix
    """
    try:
        return street_suffix_types[street_suffix.strip().upper()]
    except KeyError:
        return street_suffix


def lookup_level_type(level_type: Union[str, int], reverse_lookup=False) -> Union[str, int]:
    """
    Converts the representation for the level type
    :param level_type: string or int to lookup
    :param reverse_lookup: True if converting int to string, or False if string to int
    :return: the encoded value
    """
    if reverse_lookup:
        return _reverse_lookup(level_type, level_types)
    return _lookup(level_type, level_types)


def lookup_flat_type(flat_type: Union[str, int], reverse_lookup=False) -> Union[str, int]:
    """
    Converts the representation for the flat type
    :param flat_type: string or int to lookup
    :param reverse_lookup: True if converting int to string, or False if string to int
    :return: the encoded value
    """
    if reverse_lookup:
        return _reverse_lookup(flat_type, flat_types)
    return _lookup(flat_type, flat_types)


# Adapted from http://code.activestate.com/recipes/576888-format-a-number-as-an-ordinal/
def num2word(value, output='ordinal_words'):
    """
    Converts zero or a *postive* integer (or their string
    representations) to an ordinal/cardinal value.
    :param value: the number to convert
    :param output: one of 'ordinal_words', 'ordinal', 'cardinal'
    """
    try:
        value = int(value)
    except ValueError:
        return value

    assert output in (
    'ordinal_words', 'ordinal', 'cardinal'), "`output` must be one of 'ordinal_words', 'ordinal' or 'cardinal'"

    if output == 'ordinal_words' and (0 < value < 100):
        val = ordinal_words[value - 1]
    elif output == 'ordinal_words':
        raise ValueError("'ordinal_words' only supported between 1 and 100")
    elif output == 'ordinal':
        if value % 100 // 10 != 1:
            if value % 10 == 1:
                val = u"%d%s" % (value, "st")
            elif value % 10 == 2:
                val = u"%d%s" % (value, "nd")
            elif value % 10 == 3:
                val = u"%d%s" % (value, "rd")
            else:
                val = u"%d%s" % (value, "th")
        else:
            val = u"%d%s" % (value, "th")
    else:
        val = cardinal_words[value - 1]

    return val.upper()
