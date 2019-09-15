# Recording_Studio_Booking

The user enters their name, band member details, instruments played, booking dates, and payment method.
Input is validated and booking application receipt is printed and written to a file.

Input example:

```
Enter your name: Fionn O Reilly
Enter your email: fionn@gmail.com
Enter a contact number: 0861234567
Enter the date you would like to start (dd/mm/yyyy): 03/01/2020
How many members in the band? 3
How many days? 4
There is room for 5 session musicians - How many do you want? 1

What is band member #1's name? Jim O Brien
What is Jim O Brien's instrument? Piano
What is band member #2's name? Tim Gormley
What is Tim Gormley's instrument? Drums
What is band member #3's name? Daniella Shaw
What is Daniella Shaw's instrument? Vocals

Payment options
 1: Credit Card (5% levy)
 2: Cash (5% discount)
 3: Cheque
Choose a payment option from the above list (type '1', '2' or '3') 1
```

Output example:

```
Booking Application
 -------------------- 
Requested by:  Fionn O Reilly (Email:  fionn@gmail.com | Phone: 0861234567 )
Date requested --> 03/01/2020 

Band Members - Instrument
 --------------------
1: Jim O Brien - Piano
2: Tim Gormley - Drums
3: Daniella Shaw - Vocals

Includes 1 session musicians per day.
Payment will be €1428.0 to be paid by credit card.
```
