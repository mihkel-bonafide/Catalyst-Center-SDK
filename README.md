This is current working code for the Cisco Catalyst Center SDK (as of Oct 2025).

objectify.py: takes host info and creates a device-info object that can be operated on by other modules

list_full_device_info.py: creates a JSON output file called "output.json" that neatly displays the key-value pairs obtained by 
the SDK (this is intended to help build any desired parsing modules or whathaveyou, such as the script below)

get_device_info.py: creates a JSON object file called "devices.json" with device IDs and management IPs