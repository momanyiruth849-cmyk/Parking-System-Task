1. Design goals
  the goals to be achieved are slot live display and allocation, payment, rate update and keep an audit trail.
  the design is useful in the sense that when a vehicle enters it, a session is created and slot allocation occurs and during exit the payment
  cord is made.is calculated and a reo
  The main entities are
     1. slot - it refers to the parking slots
     2. sessions - refers to the event
     3. rates- pricing rules
     4. users - refers to the system users who are basically the attendant and the vehicle owner
     5. payments - each vehicle payment made


   The following tables descibe what information is stored:
    1.Slots
   
      * slotID- its the unique number used to refer to the eveery slot in the parking lot
      * status- free or ocuppied

   2. sessions
   
       *sessionID - this is the unique number used to refer to the session
       *vehicle number - this is the vehicle registration number
       *slotID - the number used to refer to the slot
       *check in time - th etime the vehicle arrived at the parking lot
       *check out time - the time the vehicle checked out
       *amount due - calculated parking fee
       *amount paid - amount the driver pays
       *status -mactive, pending payment or paid

   3.rates
   
       *rateID - unique number for the rate
       *name - name of rate
       *rate per hour - price put up by the administrators of the system
       *status - whether or not the rate is in use

   4.payments
   
      *paymentID- number used to refer to that particular payment
      *amount - money paid during the session
      *payment method - the driver used mpesa, card or cash
      *time- the time the payment was received

   5.auditlog
   
       *logID- the unique number sed to refer to it
       * timestamp - the time the session occured
       *details - the details of the event that occured

   
       
   
