# Recording_Studio_Booking

The user enters their name, band member details, instruments played, booking dates, and payment method.
Input is validated and booking application receipt is printed and written to a file.

Input example:

```
Enter your name: Fionn O Reilly
Enter your email: fionn@gmail.com
Enter a contact number: 0862420345
Enter the date you would like to start (dd/mm/yyyy): 03/01/2020
How many members in the band? 4
How many days? 3
There is room for 4 session musicians - How many do you want? 1

What is band member #1's name? Jim
What is Jim's instrument? Piano
What is band member #2's name? Tim
What is Tim's instrument? Guitar
What is band member #3's name? Kim
What is Kim's instrument? Drums
What is band member #4's name? Lim
What is Lim's instrument? Vocals

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
Requested by:  Fionn O Reilly (Email:  fionn@gmail.com | Phone: 0862420345 )
Date requested --> 03/01/2020 

Band Members - Instrument
 --------------------
1: Jim - Piano
2: Tim - Guitar
3: Kim - Drums
4: Lim - Vocals

Includes 1 session musicians per day.
Payment will be €1071.0 to be paid by credit card.
```
