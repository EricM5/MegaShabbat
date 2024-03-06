# View Attendees from TicketLeap


This is a program assigned to automatically generate a report of who is attending a given event that is hosted on [TicketLeap](www.ticketleap.com) .

Note: An account and event must be created on [TicketLeap](www.ticketleap.com) for this program to work correctly.

## Installation Instructions

### Clone the Repository
First, clone the repository in the desired directory by running the following command:

```
$ git clone git@github.com:EricM5/MegaShabbat.git
```

Then, 

```
$ git cd MegaShabbat
```

### Setup Environment Variables

Copy the .env.sample into your own .env file with the following:

```
$ cp .env.sample .env
```

Then fill in the following fields:

 ```USERNAME```, ```PASSWORD```, ```EVENT_PAGE``` 

 
 ```USERNAME```: username (email) for [TicketLeap](www.ticketleap.com) 

 ```PASSWORD```: password for [TicketLeap](www.ticketleap.com) 

 ```EVENT_PAGE```: url for event 'Reports' page in [TicketLeap](www.ticketleap.com) 