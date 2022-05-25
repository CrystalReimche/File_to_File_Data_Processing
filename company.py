from helper_functions import *


class Company:
    """ Returns an object from a CSV file in the format needed by end user. """

    def __init__(self, company_id, company_name, company_contact, street, city, state, zip_code, main_phone, alt_phone,
                 key_code, company_code, region, customer_limit, customer_type):
        """ creating a constructor to assign input data to parameters """
        self.company_id = company_id
        self.company_name = company_name
        self.company_contact = company_contact
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.main_phone = main_phone
        self.alt_phone = alt_phone
        self.key_code = key_code
        self.company_code = company_code
        self.region = region
        self.customer_limit = customer_limit
        self.customer_type = customer_type

    def return_company_name(self):
        """ Sets the fixed width to given constant. Pads left with spaces
        :return: Company name in fixed width form
        """
        return set_width(self.company_name, COMPANY_NAME)

    def return_last_name(self):
        """ Sets the fixed width to given constant. Pads left with spaces.
        :return: Company contact last name in fixed width form
        """
        # returns number of spaces in company contact
        name_spaces = check_space(self.company_contact)
        # splits company contact anywhere there is a space
        name_combo = self.company_contact.split(' ')
        # if there is only one space in the contact, return second element
        if name_spaces == 1:
            return set_width(name_combo[1], COMPANY_CONTACT_LAST_NAME)
        # if there are none or more than one space, return the last element
        else:
            return set_width(name_combo[-1], COMPANY_CONTACT_LAST_NAME)

    def return_first_name(self):
        """ Sets the fixed width to given constant. Pads left with spaces.
        :return: company contact first name in fixed width form
        """
        # splits company contact anywhere there is a space
        name_combo = self.company_contact.split(' ')
        # returns the first element
        return set_width(name_combo[0], COMPANY_CONTACT_FIRST_NAME)

    def return_street(self):
        """ Sets the fixed width to given constant. Pads left with spaces.
        :return: Company street address in fixed width form.
        """
        return set_width(self.street, COMPANY_STREET)

    def return_city(self):
        """ Sets the fixed width to given constant. Pads left with spaces.
        :return: Company city in fixed width form.
        """
        return set_width(self.city, COMPANY_CITY)

    def return_state(self):
        """ Sets the fixed width to given constant.  If given state is not US recognized, XX is returned.
        :return: Company state two letter state abbreviation in fixed width form.
        """
        return set_width(state_to_abbrev(self.state), COMPANY_STATE)

    def return_zip(self):
        """ Sets the fixed width to given constant. If padding is needed, zip code is changed to all ###.
        :return: Company zip code in fixed width form.
        """
        # grabs how many characters in given zip code string
        char_count = get_char_count(self.zip_code)
        if char_count == COMPANY_ZIP:
            return set_width(self.zip_code, COMPANY_ZIP)
        elif char_count > COMPANY_ZIP:
            return set_width(self.zip_code[0:COMPANY_ZIP], COMPANY_ZIP)
        else:
            return '#' * char_count

    def return_main_phone(self):
        """ Sets the fixed width to given constant. Pads left with spaces.
        :return: Company contact main phone with no hyphens in fixed width form.
        """
        # removes hyphen from given string
        main = remove_hyphen(self.main_phone)
        # checks if phone string is all numbers and no alphas
        if main.isdigit():
            return set_width(main, COMPANY_MAIN_PHONE)
        else:
            return set_width("ERROR", COMPANY_MAIN_PHONE)

    def return_alt_phone(self):
        """ Sets the fixed width to given constant. Pads left with spaces.
        :return: Company contact alt phone with no hyphens in fixed width form.
        """
        # removes hyphen from given string
        alt = remove_hyphen(self.alt_phone)
        # checks if phone string is all numbers and no alphas
        if alt.isdigit():
            return set_width(alt, COMPANY_ALT_PHONE)
        else:
            return set_width("ERROR", COMPANY_ALT_PHONE)

    def return_alpha_key(self):
        """ Sets the fixed width to given constant. Pads right with zeros.
        :return: Company alpha key in fixed width form.
        """
        return set_width(self.key_code[0: 10], ALPHA_KEY_VALUE, True)

    def return_beta_key(self):
        """ Sets the fixed width to given constant. Pads left with x.
        :return: Company beta key in fixed width form.
        """
        return set_width(self.key_code[-26:], BETA_KEY_VALUE, True)

    def return_region(self):
        """ Sets the fixed width to given constant. Pads right with spaces.
        :return: Company region in fixed width form.
        """
        return set_width(self.region, REGION, True)

    def return_company_code(self):
        """ Sets the fixed width to given constant. Pads left with spaces.
        :return: Company code in fixed width form.
        """
        return set_width(self.company_code, COMPANY_CODE)

    def return_customer_type(self):
        """ Sets the fixed width to given constant.
        :return: Customer type in fixed width form.
        """
        return set_width(self.customer_type, CUSTOMER_TYPE)

    def return_customer_limit(self):
        """ Sets the fixed width to given constant. Pads left with spaces.
        :return: Customer limit amount in K values in fixed width form.
        """
        k = int(int(self.customer_limit) / 1000)
        return set_width(str(k), CUSTOMER_LIMIT)

    def return_company_id(self):
        """ Sets the fixed width to given constant. Pads left with X.
        :return: Company ID in fixed width form.
        """
        return set_width(self.company_id, CUSTOMER_ID, False, True)


