This document basically describes the data structures and the reason as to why they were chosen.

1.List of Dictionaries
  structure:
      parkingslots = [
{
              "ID": 1,
              "status": free
        }
    ]
It is used for slot monitoring, display and allocation.
it allows for fast scanning for available and it is easy to update.


2.Hash map
  structure:
     active sessions = {
     "ticket-001" ={
         "ticketID"
         "vehicle number"
         "check_in_time"
         "allocated slot"
         "status"
         }
    }
This is used during entry, fee calculation, barrier opening 
it provides a time complexity for update and deletion if the ticketID.


3.List of rate records
 structure:
     rates = [
       {
          "ID"
          "name"
          "check'-in_hour"
          "check_out_hour"
          "rate per hour"
        }
    }
it is used during rate update and fee calculation.
the reason why i used it is allows change in the rate without modifying the entire code


4.Append only list
  Structure:
     auditlog = {
        {   
           "time stamp"
           "ticketID"
           "details"
           "user"
        }
    }
it is used during audit conduction as recoreds are only updated and never deleted.
     
         
