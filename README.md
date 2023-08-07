# SSL-Sniffer
SSL Sniffer is a command line tool that checks if hosts have valid SSL certificates for port 443. It is a Python tool that can be installed using pip.

## Installation

To install SSL Sniffer, you can run the following command:

pip install ssl_sniffer


## Usage

To use SSL Sniffer, you can run the following command:

ssl_sniffer [hosts]

The hosts argument is a list of hosts that you want to check. For example, to check the hosts www.example.com, www.google.com, and www.yahoo.com, you would run the following command:

ssl_sniffer www.example.com www.google.com www.yahoo.com

Output
SSL Sniffer will print a message for each host that it checks. If the host has a valid SSL certificate, the message will say "The host <host> has a valid SSL certificate for port 443.". If the host does not have a valid SSL certificate, the message will say "The host <host> does not have a valid SSL certificate for port 443.".

Author
SSL Sniffer was created by @thatonesecguy.

License
SSL Sniffer is licensed under the MIT License.
