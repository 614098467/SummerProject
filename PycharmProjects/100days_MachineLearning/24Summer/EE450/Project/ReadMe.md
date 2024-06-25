## EE450-FinalProject ReadMe

#### Full Name: Ge Zhou

#### Student ID: 1837445242

#### Description:
My project contains five C++ files,each file corresponds to a server
    
    - client.cpp
    - serverM.cpp
    - serverC.cpp
    - serverRTH.cpp
    - serverEEB.cpp
#### Format of exchanged messages
Please enter your username and press Enter. 
Please enter your password and press Enter. Non-members can just press Enter during password input.
Please write the complete name of the room, for example: EEB201
Please capitalize the first letter of the date, for example: Thursday
Please do not add any spaces to the time, for example: 12pm 

#### The process of bug
When the previous client does not exit legally, 
the next client will be unable to log in, 
and there may be a sticky packet situation. 
I tried my best to solve this problem, but it didn't work. 
If this happens, the reasonable way to deal with it is 
to restart all clients.

#### Re-used code:
The code ideas are all created by myself, without reference to other people's works. The use of some functions and 
debugging part use the AI tool ChatGPT