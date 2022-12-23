# Django BkashPay (fake-payment-sample)
A. to run this project- 
      1. download this project
      2. go to basedirectory (where manage.py exists)
      3. run "py manage.py runserver"

B. This app contains these applications
  
 ![Screenshot 2022-12-23 173118](https://user-images.githubusercontent.com/58982471/209330039-7fabab73-8e31-4697-9701-ff4fdbb47c4d.png)

  
# How to implement this to your project?

    A. copy the app "bkash"  to your project

   ![Screenshot 2022-12-23 170828](https://user-images.githubusercontent.com/58982471/209325846-7c168491-897a-4125-be84-7a38770c191e.png)

    B. connect it to your settings.py file 

   ![Screenshot 2022-12-23 171107](https://user-images.githubusercontent.com/58982471/209326090-67b28fec-637f-440d-8a02-39bc578fc3e8.png)

    C. Make sure to copy the static files to your project

   ![Screenshot 2022-12-23 171322](https://user-images.githubusercontent.com/58982471/209326438-1ea81d14-97b1-419d-a8f4-f960e663fd74.png)

    D. Make sure you have declared the static directory in 'settings.py'

   ![Screenshot 2022-12-23 171447](https://user-images.githubusercontent.com/58982471/209326673-f43936e2-b297-4844-8fef-b4dba70cb01b.png)

    E. join with app url: 

   ![Screenshot 2022-12-23 172258](https://user-images.githubusercontent.com/58982471/209327810-b9037bf3-e64b-487d-915e-120eafec95ba.png)


    F. go to 'http://localhost:8000/bkash/'to test if everything is working

.

    G. In views.py of the app, change 'amount' and other dictionaries according to your project. 
    
    In this dummy payment system, only amount is visible. you can change the views.py to adjust 'amount'
    
    variable according to your needs.


(give a star if it worked for you)


Happy coding!
