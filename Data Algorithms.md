#Algorithms for Each Module

#Module 1:Slot display and monitoring
the purpose is to monitor every slot and update the status of the slots to the web display

**algorithm** 

 FUNCTION monitorslots()
       WHILE system is running DO
					status - readsensor(slot.id) // free or occupied
								 updateLiveDisplay(slot.id, status)
									notify the webmobileClients( slot.id, status0
					END IF
				END FOR
		WAIT 2 seconds
END FUNCTION

#Module 2:entry 
The purpose is to record whenever a vehicle comes into the parki8ng lot and assign it a slot.
 **	Algorithm**
 FUNCTION ProcessArrival(vehicle number)
		IF vehicle number is empty or invalid THEN
			display error ( invalid)
      RETURN
   END IF
 Freeslot - allocateslot

IF Freeslot is not available THEN
   Display( Parking is Full)
   RETURN
   END IF

	entrytime - check_in_time()
  ticketidv - generateuniqueTicket()
  CREATE new session
     session.ticketID - ticketID
     session.vehiclenumber - vehiclenumber
		 session.entrytime - entrytime
     session.allocatedslot - freeslot
     session.status- active

  	StoreSession(session)
    MarkSlotAsOccupied(freeslot)
    UpdateLiveDisplay(Freeslot, status)
    PrintOrDisplay(Freeslot, Occupied)
    OpenEntryBarrier()
END FUNCTION

#Module3: Slot Allocation
the purpose is to find a slot and allocate it to the incoming vehicle

**Algorithm**
	FUNCTION Allocateslot()
    FOR each slot in Parkingslot DO
      IF slot.status = Free THEN
        RETURN Slot.id
     END IF
    END FOR
    RETURN NULL
END FUNCTION

#Module4: Exit and Fee calculation
FUNCTION CalculateFee(ticketID)
    session = FindSession(ticketID)
    IF session is Null OR session. status is not active THEN
        RETURN error (invalid ticket)
    END IF

    exittime - Check_out_time
    durationminutes - differenceInMinutes(exittime, session.entrytime)

    rate - get current rate
    amountdue- CalculateAmount

    session.exittime - exittime
    session.durationminutes - durationminutes
    session.amountdue-amountdue
    session.status-awaitingpayment

    Updatesession
   RETURN amountdue
END FUNCTION

#Module5:Payment 
The purpose is to facilitate collection of the payment via any platform such as Mpesa or card or cash
**Algorithm**
FUCTION ProcessPayment(ticketID, amount, paymentmethod)
		session- findsession(ticketID)
    IF session is NULL or session.status is not awaiting payment THEN
       RETURN errorr(invalid)
    END IF
payment success is false

IF paymentmethod = Mpesa THEN 
   payment success - initiate Mpesa STK
ELSE IF paymentmethod = card THEN
    payment success - process card payment(amount)
ELSE IF paymentmethod = cash
   payment success - confirmed by attendant
END IF

IF payment success = TRUE THEN
   session.amountpaid - amount
   session.paymentmethod - paymentmethod
   session.paymenttime - Currenttime
   session.status - paid
   updatesession
   signal barrier to open(ticketID)
   RETURN
ELSE
   RETURN error(payment failed)
 END IF
END FUNCTION

#Module6:Barrier Control
the pirpose is to open and close the barrier once payment is completed

**Algorithm**
FUNCTION ControlBarrier
 // barrier = entry or exit
  //action = open or close
   IF action = open THEN
       IF barriertype = exit THEN
          session.status = paid THEN
                RETURN error(payment not confirmed )
             END IF
           END IF

         SendSignal(barriertype, open)
        wait until barrier is fully open
        startautoclosetimer(barriertype, 10seconds)
     ELSE
       Sendsignal(barriertype, close)
      END IF
END FUNCTION


#Module7: Rate management
the purpose is to allow change in parking rates

**algorithm**
FUNCTION update rate
   VALIDATE newrate details

   INSERT new record into rate tables
    SET previous rate as inavlid
    RETURN success
     END FUNCTION

  FUNCTION get current rate(currenttime)
   hour +currenttime.hour
  rate +find active rate
  RETURN rate
END FUNCTION

#Module8: audit and reporting module
**algorithm**
  FUNCTION logtransaction
    //eventtype examples:arrival. payment,ratechange,execption
    CREATE Auditrecord:
        timestamp - currenttime
        eventtype - eventtype
        details - details
        user - currentuser

     APPEND auditrecord to auditing
   END FUNCTION

 FUNCTION generatedailyreport
    totalvehicles- countsession
    totalrevenue - sumpayments
    paymentbreakdown - groupbypaymentmethod
    RETURN report
END FUNCTION

#Module9 - execption handling 
its purpose is tot handle unusual situations

**algorithm**
FUNCTION handle lost ticket
    sessions - find active session by vehicle number
    IF sessions is empty THEN
          RETURN error(no active session found)
     END IF

    IF sessions.count > 1 THEN
         ask attendant to correct session
     END IF 

     session - selected session
     amountdue - calculatefee(session ticketID)
     display message(lost ticketfee amount: )
     //proceed to payment
END FUNCTION


