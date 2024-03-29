hostname
clientid
persistent
option rapid_commit
option domain_name_servers, domain_name, domain_search, host_name
option classless_static_routes
option ntp_servers
option interface_mtu
require dhcp_server_identifier
slaac private
interface eth0
interface wlan0

static ip_address = 192.168.168.200
static routers = 192.168.168.1
static domain_name_servers = 192.168.168.1
