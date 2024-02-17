

Python scripts of Telnet server and client.

Important files: 
* client.py - default client script
* sample_server_lvl1.py - default server script (no addons)
* sample_server_lvl2.py - adds authentication, error handling, and set of whitelisted commands
* sample_server_lvl3.py - further adds rate limiting, set of blocked IP's, and heartbeat protocol

Instructions: 
* start server session by running python server script
* use client script to initiate telnet session. Use localhost if running locally (127.0.0.1) and then specify port as run by server script (default is port 2323)
* you now have a telnet session between the client and server terminals! More specifically, you gain access of the server directory within the client terminal

Within small_samples I've also written some small examples of functionalities that could be used to expand on the server script. In the future I'd like to use this to make a small MUD game, similar to Aardwolf.
