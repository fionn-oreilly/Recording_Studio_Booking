# Author:      Fionn O Reilly
# Filename:    Recording_Studio_Booking.py
# Description: User inputs band member details, booking dates and payment method.
#              All inputs are validated,
#              A booking application receipt is printed and sent to .txt file.

from datetime import date
from datetime import datetime


def main():
    band_manager_name = manager_name()
    band_manager_email = manger_email()
    band_manager_number = manger_number()
    start_date = get_start_date()
    num_members = num_band_members()
    number_of_days = num_days()
    num_session_musicians = session_musicians(num_members)
    member_list, instrument_list = member_details(num_members)

    cost = initial_cost(number_of_days, num_session_musicians)
    payment_method, cost = final_cost(cost)

    print_receipt(band_manager_name, band_manager_email, band_manager_number, start_date,
                  member_list, instrument_list, num_session_musicians, payment_method, cost)


# Getting and validating input from user
# Getting band manager name
def manager_name():
    valid = False
    while valid is False:
        band_manager_name = input('Enter your name: ')
        if band_manager_name.replace(" ", "") == '':
            print('ERROR - Field cannot be blank')
            valid = False
        elif not all(l.isalpha() or l.isspace() for l in band_manager_name):
            print('ERROR - Name must be letters only')
            valid = False
        else:
            return band_manager_name


# Getting band manager email
def manger_email():
    valid = False
    while valid is False:
        band_manager_email = input('Enter your email: ')
        if '@' not in band_manager_email or '.com' not in band_manager_email:
            print('ERROR - Invalid email, please try again.')
        else:
            return band_manager_email


# Getting band manager number
def manger_number():
    valid = False
    while valid is False:
        band_manager_number = input('Enter a contact number: ')
        length = len(band_manager_number)
        if not band_manager_number.isnumeric():
            print('ERROR - Numbers only')
        elif 12 <= length <= 8:
            print('ERROR - Phone number must be between 8 and 12 digits long')
        else:
            return band_manager_number


# Getting start date request
def get_start_date():
    valid = False
    while valid is False:
        start_date = (input('Enter the date you would like to start (dd/mm/yyyy): '))
        try:
            datetime.strptime(start_date, '%d/%m/%Y')
            valid_date_format = True
        except Exception:
            print('ERROR - Date must be in DD/MM/YYYY')
            valid_date_format = False
        if valid_date_format is True:
            # Make sure given date is not before current date
            start_date = datetime.strptime(str(start_date), '%d/%m/%Y').date().strftime('%d/%m/%Y')
            if datetime.strptime(start_date, '%d/%m/%Y').date() < date.today():
                print('ERROR - Start date must be after the current date')
            else:
                return start_date


# Getting number of band members
def num_band_members():
    valid = False
    while valid is False:
        try:
            num_band_members = int(input('How many members in the band? '))
            if num_band_members < 1 or num_band_members > 8:
                print('ERROR - Number of band members must be between 1 and 8')
            else:
                return num_band_members
        except Exception:
            print('ERROR - Please enter a number between 1 and 8')


# Getting the requested number of days
def num_days():
    valid = False
    while valid is False:
        try:
            num_days = int(input('How many days? '))
            if num_days < 1:
                print('ERROR - Number of days must be above zero')
            else:
                return num_days
        except Exception:
            print('ERROR - Field cannot be blank')


# Getting number of session musicians
def session_musicians(num_band_members):
    MAX_BAND_MEMBERS = 8
    num_session_musicians = 0
    valid = False
    while valid is False:
        try:
            available_slots = MAX_BAND_MEMBERS - num_band_members
            if available_slots == 0:
                print('You have no room for session musicians')
                break
            num_session_musicians = int(input('There is room for ' + str(available_slots) +
                                              ' session musicians - How many do you want? '))
            if num_session_musicians < 0:
                print('ERROR - Please enter a number above 0')
            elif num_session_musicians > available_slots:
                print('ERROR - There are only', available_slots, 'available for session musicians')
            else:
                valid = True
        except Exception:
            print('ERROR - Field cannot be blank')
    print()
    return num_session_musicians


# Get band member names and their instruments from user
# Add name and instruments to list
def member_details(num_band_members):
    band_member_list = []
    instrument_list = []

    i = 1
    valid = False
    while i <= num_band_members:
        while valid is False:
            band_member_name = input('What is band member' + ' #' + str(i) + '\'s name? ')
            if band_member_name.replace(" ", "") == '':
                print('ERROR - Field cannot be blank')
            elif not all(l.isalpha() or l.isspace() for l in band_member_name):
                print('ERROR - Names must be letters only')
            else:
                valid = True

        valid = False
        while valid is False:
            band_member_instrument = input('What is ' + band_member_name + '\'s instrument? ')
            if band_member_instrument.replace(" ", "") == '':
                print('ERROR - Field cannot be blank')
            elif not all(l.isalpha() or l.isspace() for l in band_member_instrument):
                print('ERROR - Instrument name must be letters only')
            else:
                valid = True

        valid = False
        band_member_list.append(band_member_name)
        instrument_list.append(band_member_instrument)
        i += 1
        if i > num_band_members:
            valid = True
    return band_member_list, instrument_list


# Calculating initial cost before payment method selection
def initial_cost(num_days, num_session_musicians):
    ONE_DAY_COST_PER_DAY = 260
    TWO_TO_FOUR_DAY_COST_PD = 240
    FIVE_TO_EIGHT_DAY_COST_PD = 210
    NINE_OR_MORE_DAYS_COST_PD = 200
    SESSION_MEMBER_COST_PD = 100
    initial_cost = 0

    if num_days == 1:
        initial_cost = (ONE_DAY_COST_PER_DAY * num_days) + \
                       ((SESSION_MEMBER_COST_PD * num_session_musicians) * num_days)
    elif num_days >= 2 and num_days <= 4:
        initial_cost = (TWO_TO_FOUR_DAY_COST_PD * num_days) + \
                       ((SESSION_MEMBER_COST_PD * num_session_musicians) * num_days)
    elif num_days >= 5 and num_days <= 8:
        initial_cost = (FIVE_TO_EIGHT_DAY_COST_PD * num_days) + \
                       ((SESSION_MEMBER_COST_PD * num_session_musicians) * num_days)
    elif num_days >= 9:
        initial_cost = (NINE_OR_MORE_DAYS_COST_PD * num_days) + \
                       ((SESSION_MEMBER_COST_PD * num_session_musicians) * num_days)
    return initial_cost


# Letting the user pick a payment method and calculate final cost
def final_cost(initial_cost):
    CASH_DISCOUNT = 1 - 0.05
    CREDIT_CARD_LEVY = 1 + 0.05
    CREDIT_CARD = 1
    CASH = 2
    CHEQUE = 3
    final_cost = 0

    valid = False
    while valid is False:
        try:
            print('\nPayment options\n 1: Credit Card (5% levy)\n 2: Cash (5% discount)\n 3: Cheque')
            payment_choice = int(input('Choose a payment option from the above list (type \'1\', \'2\' or \'3\') '))
            if payment_choice > 3 or payment_choice < 1:
                print('\n>>>ERROR - Please choose \'1\', \'2\' or \'3\'<<<')
            else:
                valid = True
        except Exception:
            print('\n>>>ERROR - Field cannot be blank<<<')

    # Calculating final cost based on payment option
    payment_method = ''
    if payment_choice == CREDIT_CARD:
        payment_method = 'credit card'
        final_cost = initial_cost * CREDIT_CARD_LEVY
    elif payment_choice == CASH:
        payment_method = 'cash'
        final_cost = initial_cost * CASH_DISCOUNT
    elif payment_choice == CHEQUE:
        payment_method = 'cheque'
        final_cost = initial_cost
    return payment_method, final_cost


# Printing the booking request and writing to .txt file
def print_receipt(band_manager_name, band_manager_email, band_manager_number, start_date,
                  band_member_list, instrument_list, num_session_musicians, payment_method,
                  final_cost):

    DASHLINE = '-' * 20
    print('\nBooking Application\n', DASHLINE, '\nRequested by: ', band_manager_name,
          '(Email: ', band_manager_email, '| Phone:', band_manager_number, ')')
    print('Date requested -->', start_date, '\n\nBand Members - Instrument\n', DASHLINE)

    # Printing list of band member names and their instruments using for loop
    item_number = 1
    for i, l in zip(band_member_list, instrument_list):
        print(str(item_number) + ':', i, '-', l)
        item_number += 1
    print('\nIncludes', num_session_musicians, 'session musicians per day.')
    print('Payment will be', '€' + str(final_cost), 'to be paid by', payment_method + '.')

    # Sending receipt to .txt file
    projectreceipt = open(band_manager_name + ' Receipt.txt', 'w')
    projectreceipt.write('\nBooking Application\n' + DASHLINE + '\nRequested by: ' + band_manager_name +
                         '(Email: ' + str(band_manager_email) + ' | Phone: ' + str(band_manager_number) + ')')
    projectreceipt.write('\nDate requested --> ' + start_date + '\n\nBand Members - Instruments\n' + DASHLINE + '\n')
    item_number = 1

    for i, l in zip(band_member_list, instrument_list):
        projectreceipt.write(str(item_number) + ': ' + i + ' - ' + l + '\n')
        item_number += 1
    projectreceipt.write('\nIncludes ' + str(num_session_musicians) + ' session musicians per day.')
    projectreceipt.write('\nPayment will be ' + '€' + str(final_cost) + ' to be paid by ' + payment_method + '.')
    projectreceipt.close()


main()
