from constants import *


def remove_hyphen(self):
    """ Removes any hyphens in the given string
    :param self: string obj
    :return: string obj without hyphens
    """
    return self.replace('-', '')


def check_space(self):
    """ Counts how many spaces there are in the given string
    :param self: string obj
    :return: int of spaces in string obj
    """
    count = 0
    # loop through each char until it reaches the end of the given string
    for i in range(0, len(self)):
        # Check each char if space or not
        if self[i] == " ":
            # If there is a space, increase counter
            count += 1
    return count


def get_char_count(self):
    """ Counts how many characters within the given string
    :param self: string obj
    :return: int of chars in string obj
    """
    count = 0
    for _ in self:
        count += 1
    return count


def set_width(self, fixed_width, switch_sides=False, big_x=False):
    """ Sets the fixed width of a given column.
    Takes in the given string and the max width for that column.
    Optional default parameters.
    :param self: string obj
    :param fixed_width: int constant
    :param switch_sides: bool
    :param big_x: bool
    :return: string in fixed width form
    """
    char_count = get_char_count(self)
    # Truncate given string if longer than fixed width
    if char_count > fixed_width:
        return self[0:fixed_width]

    # Add X to left of string if string is shorter than fixed width
    # and optional big_x parameter is set to true
    elif (char_count < fixed_width) & big_x:
        return self.rjust(fixed_width, "X")

    # If given string is shorter than fixed width and optional
    # switch_sides is set to true, assign padding side and symbol
    elif (char_count < fixed_width) & switch_sides:
        if fixed_width == ALPHA_KEY_VALUE:
            return self.ljust(fixed_width, "0")
        elif fixed_width == REGION:
            return self.ljust(fixed_width, " ")
        else:
            return self.rjust(fixed_width, "x")
    # If given string is shorter than fixed width and optional
    # parameters are still set to false
    elif char_count < fixed_width:
        return self.rjust(fixed_width, " ")
    else:
        return self


def state_to_abbrev(self):
    """ Returns two letter abbreviation of given state
    :param self: string obj
    :return: string
    """
    if self in us_state_to_abbrev:
        return us_state_to_abbrev.get(self)
    else:
        return 'XX'


us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
