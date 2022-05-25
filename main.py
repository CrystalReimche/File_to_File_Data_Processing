# ----------------------------------------------------------------------------
# Created By  : Crystal Reimche
# Created Date: 05/17/2022
# version ='3.9.7'
# ---------------------------------------------------------------------------
""" This program will accept a CSV file and return a fixed width file """

import csv
import company


def main():
    # user_file = 'ProjectDataSet-500.csv'
    user_file = input('Enter the file name: ')
    destination_file = 'final_output.txt'

    with open(user_file, 'r') as csv_file:
        with open(destination_file, 'w') as final_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for line in csv_reader:
                co = company.Company(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7],
                                     line[8], line[9], line[10], line[11], line[12], line[13])

                print(co.return_company_name(), co.return_last_name(), co.return_first_name(), co.return_street(),
                      co.return_city(), co.return_state(), co.return_zip(), co.return_main_phone(),
                      co.return_alt_phone(), co.return_alpha_key(), co.return_beta_key(), co.return_region(),
                      co.return_company_code(), co.return_customer_type(), co.return_customer_limit(),
                      co.return_company_id(),
                      file=final_file)
                line_count += 1
            print(f'\nThere were a total of {line_count} lines added to {destination_file}.', file=final_file)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
