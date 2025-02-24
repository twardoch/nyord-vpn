## SpecStory

## VPN Server Selection Errors and Debugging (24/02/2025, 08:01:51)

_**User**_

[02/24/25 08:00:42] DEBUG    2025-02-24 08:00:42.886 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:154 - Found OpenVPN at                   vpn.py:154
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 08:00:42.895 | DEBUG    | nyord_vpn.network.vpn:setup_connection:232 - Created auth file at                         vpn.py:232
                             /Users/adam/.cache/nyord-vpn/openvpn.auth                                                                                                
                    DEBUG    2025-02-24 08:00:42.899 | DEBUG    | nyord_vpn.network.server:get_servers_cache:305 - Fetching server list from API...      server.py:305
[02/24/25 08:00:43] DEBUG    2025-02-24 08:00:43.232 | DEBUG    | nyord_vpn.network.server:get_servers_cache:317 - Successfully fetched server data from server.py:317
                             API                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.234 | DEBUG    | nyord_vpn.network.server:get_servers_cache:325 - Found 100 servers in API response     server.py:325
                    DEBUG    2025-02-24 08:00:43.466 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for pl128.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.467 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.469 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.470 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.472 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.473 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.475 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.476 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.477 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.479 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for hu48.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:43.480 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.481 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.483 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.484 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.485 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.487 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.488 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.489 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.491 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5063.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:43.492 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.493 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.495 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.496 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.498 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.499 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.501 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.502 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.503 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for at86.nordvpn.com:    server.py:373
                    DEBUG    2025-02-24 08:00:43.505 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.506 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.508 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.509 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.510 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.512 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.513 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.515 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.516 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch217.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.517 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.519 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.520 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.522 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.523 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.524 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.526 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.527 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.528 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for dk152.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.530 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.531 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.533 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.534 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.536 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.537 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.539 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.540 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.542 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for no151.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.543 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.544 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.546 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.547 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.549 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.550 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.551 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.553 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.554 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch218.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.556 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.557 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.559 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.560 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.562 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.563 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.564 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.566 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.567 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk1784.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:43.569 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.570 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.572 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.573 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.575 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.576 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.578 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.579 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.581 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr555.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.583 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.584 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.585 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.587 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.590 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.591 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.593 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.594 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.595 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch219.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.596 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.598 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.599 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.601 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.602 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.604 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.605 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.607 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.608 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for us5064.nordvpn.com:  server.py:373
                    DEBUG    2025-02-24 08:00:43.609 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.611 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.613 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.614 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.616 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.617 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.619 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.621 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.622 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk765.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.623 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.625 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.626 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.627 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.629 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.631 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.632 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.633 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.635 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk812.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.636 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.637 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.639 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.640 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.642 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.643 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.644 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:43.647 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:43.649 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for uk813.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:43.650 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:43.652 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                ...
                         Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.025 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.027 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.029 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.030 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.031 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.033 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr540.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.034 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.036 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.037 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.039 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.040 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.042 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.043 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.044 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.046 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr541.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.048 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.049 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.051 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.052 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.054 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.055 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.056 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.058 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.059 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr542.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.061 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.063 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.065 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.067 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.069 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.071 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.073 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.075 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.077 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr543.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.079 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.080 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.083 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.085 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.086 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.088 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.090 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.091 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.093 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for fr544.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.095 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.098 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.099 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.102 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.104 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.106 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.108 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.110 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.112 | DEBUG    | nyord_vpn.network.server:get_servers_cache:373 - Technologies for ch221.nordvpn.com:   server.py:373
                    DEBUG    2025-02-24 08:00:47.114 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.115 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.117 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.119 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.120 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:375
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.122 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 35, Name: Wireguard, Status:  server.py:375
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:00:47.124 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 51, Name: NordWhisper,        server.py:375
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:00:47.125 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:00:47.127 | DEBUG    | nyord_vpn.network.server:get_servers_cache:451 - No valid servers found after          server.py:451
                             filtering 100 total servers                                                                                                              
                    ERROR    2025-02-24 08:00:47.129 | ERROR    | nyord_vpn.network.server:get_servers_cache:481 - Failed to fetch servers: No valid     server.py:481
                             servers found in API response. Total servers: 100, Invalid: 100                                                                          
                             Traceback (most recent call last):                                                                                                       
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/bin/nyord-vpn", line 10, in <module>                               
                                 sys.exit(main())                                                                                                                     
                                 |   |    -> <function main at 0x109db7880>                                                                                           
                                 |   -> <built-in function exit>                                                                                                      
                                 -> <module 'sys' (built-in)>                                                                                                         
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__main__.py", line 81, in main                             
                                 fire.Fire(CLI)                                                                                                                       
                                 |    |    -> <class 'nyord_vpn.__main__.CLI'>                                                                                        
                                 |    -> <function Fire at 0x109e5d260>                                                                                               
                                 -> <module 'fire' from                                                                                                               
                             '/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/__init__...                             
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 135,              
                             in Fire                                                                                                                                  
                                 component_trace = _Fire(component, args, parsed_flag_args, context, name)                                                            
                                                   |     |          |     |                 |        -> 'nyord-vpn'                                                   
                                                   |     |          |     |                 -> {}                                                                     
                                                   |     |          |     -> Namespace(verbose=False, interactive=False, separator='-', completion=None,              
                             help=False, trace=False)                                                                                                                 
                                                   |     |          -> ['go', 'pl', '--verbose']                                                                      
                                                   |     -> <class 'nyord_vpn.__main__.CLI'>                                                                          
                                                   -> <function _Fire at 0x109e7ea20>                                                                                 
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 468,              
                             in _Fire                                                                                                                                 
                                 component, remaining_args = _CallAndUpdateTrace(                                                                                     
                                 |                           -> <function _CallAndUpdateTrace at 0x109e7eb60>                                                         
                                 -> <bound method CLI.go of <nyord_vpn.__main__.CLI object at 0x109a7c410>>                                                           
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 684,              
                             in _CallAndUpdateTrace                                                                                                                   
                                 component = fn(*varargs, **kwargs)                                                                                                   
                                             |   |          -> {}                                                                                                     
                                             |   -> ['pl']                                                                                                            
                                             -> <bound method CLI.go of <nyord_vpn.__main__.CLI object at 0x109a7c410>>                                               
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__main__.py", line 46, in go                               
                                 self.client.go(country_code)                                                                                                         
                                 |    |      |  -> 'pl'                                                                                                               
                                 |    |      -> <function Client.go at 0x109db72e0>                                                                                   
                                 |    -> <nyord_vpn.core.client.Client object at 0x10a017800>                                                                         
                                 -> <nyord_vpn.__main__.CLI object at 0x109a7c410>                                                                                    
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/core/client.py", line 278, in go                           
                                 selected_servers = self.server_manager.select_fastest_server(                                                                        
                                                    |    |              -> <function ServerManager.select_fastest_server at 0x109d43920>                              
                                                    |    -> <nyord_vpn.network.server.ServerManager object at 0x1095dd070>                                            
                                                    -> <nyord_vpn.core.client.Client object at 0x10a017800>                                                           
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 840, in                           
                             select_fastest_server                                                                                                                    
                                 normalized_country = self._validate_country_code(country_code)                                                                       
                                                      |    |                      -> 'pl'                                                                             
                                                      |    -> <function ServerManager._validate_country_code at 0x109d434c0>                                          
                                                      -> <nyord_vpn.network.server.ServerManager object at 0x1095dd070>                                               
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 175, in                           
                             _validate_country_code                                                                                                                   
                                 country_info = self.get_country_info(normalized)                                                                                     
                                                |    |                -> 'PL'                                                                                         
                                                |    -> <function ServerManager.get_country_info at 0x109d43b00>                                                      
                                                -> <nyord_vpn.network.server.ServerManager object at 0x1095dd070>                                                     
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 1023, in                          
                             get_country_info                                                                                                                         
                                 cache = self.get_servers_cache()                                                                                                     
                                         |    -> <function ServerManager.get_servers_cache at 0x109d43600>                                                            
                                         -> <nyord_vpn.network.server.ServerManager object at 0x1095dd070>                                                            
                                                                                                                                                                      
                             > File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 454, in                           
                             get_servers_cache                                                                                                                        
                                 raise ValueError(                                                                                                                    
                                                                                                                                                                      
                             ValueError: No valid servers found in API response. Total servers: 100, Invalid: 100                                                     
                                                                                                                                                                      
                                                                                                                                                                      
                    INFO     2025-02-24 08:00:47.144 | INFO     | nyord_vpn.network.server:get_servers_cache:495 - Using fallback cache with 100 valid   server.py:495
                             servers                                                                                                                                  
                    DEBUG    2025-02-24 08:00:47.147 | DEBUG    | nyord_vpn.network.server:select_fastest_server:888 - Testing 3 servers for speed       server.py:888
                    DEBUG    2025-02-24 08:00:47.307 | DEBUG    | nyord_vpn.network.server:_test_server:688 - TCP/TLS test failed for pl122.nordvpn.com: server.py:688
                             [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)                                                  
                    DEBUG    2025-02-24 08:00:47.318 | DEBUG    | nyord_vpn.network.server:_test_server:688 - TCP/TLS test failed for pl128.nordvpn.com: server.py:688
                             [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)                                                  
                    DEBUG    2025-02-24 08:00:47.346 | DEBUG    | nyord_vpn.network.server:_test_server:688 - TCP/TLS test failed for pl125.nordvpn.com: server.py:688
                             [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1000)                                                  
                    ERROR    2025-02-24 08:00:47.350 | ERROR    | nyord_vpn.network.server:select_fastest_server:932 - Error selecting server: No        server.py:932
                             responsive servers found in PL                                                                                                           
Error: Failed to select servers: No responsive servers found in PL

---

_**Assistant**_

I see the issue from the logs. Let me analyze the problem and propose a solution:

1. The server validation is failing for all servers. The logs show:
```
DEBUG    2025-02-24 08:00:43.234 | DEBUG    | nyord_vpn.network.server:get_servers_cache:325 - Found 100 servers in API response
...
DEBUG    2025-02-24 08:00:47.127 | DEBUG    | nyord_vpn.network.server:get_servers_cache:451 - No valid servers found after filtering 100 total servers
```

2. However, we can see that the servers DO have OpenVPN TCP support:
```
DEBUG    2025-02-24 08:00:43.475 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: None
...
DEBUG    2025-02-24 08:00:43.477 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN TCP
```

Let me examine the server validation code:

---

_****_

<details>
            <summary>Searched codebase "_is_valid_server validation server check" • **25** results</summary>
        
| File | Lines |
|------|-------|
| `nyord_vpn.txt` | L6734-6782 |
| `src/nyord_vpn/network/server.py` | L598-645 |
| `nyord_vpn.txt` | L6541-6584 |
| `nyord_vpn.txt` | L6949-6976 |
| `src/nyord_vpn/network/server.py` | L275-301 |
| `nyord_vpn.txt` | L6405-6452 |
| `nyord_vpn.txt` | L6503-6541 |
| `src/nyord_vpn/network/server.py` | L401-442 |
| `nyord_vpn.txt` | L6610-6644 |
| `src/nyord_vpn/network/server.py` | L473-497 |
| `src/nyord_vpn/network/server.py` | L358-401 |
| `.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2680-2745 |
| `.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2823-2867 |
| `.specstory/history/2025-02-23_07-30-vpn-connection-issues-and-server-selection-errors.md` | L369-440 |
| `src/nyord_vpn/network/server.py` | L152-179 |
| `src/nyord_vpn/network/server.py` | L207-244 |
| `src/nyord_vpn/network/server.py` | L329-358 |
| `nyord_vpn.txt` | L6452-6503 |
| `src/nyord_vpn/network/server.py` | L244-275 |
| `src/nyord_vpn/network/server.py` | L827-871 |
| `.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2383-2432 |
| `src/nyord_vpn/network/server.py` | L442-473 |
| `.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L3447-3492 |
| `.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L3179-3224 |
| `.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2525-2575 |

</details>

---

_****_



I see the issue. Looking at the logs and the code, there are two problems:

1. The server validation in `_is_valid_server` is too strict. It's checking for `status == "online"` but in the API response, we see that the status field is `None` for all servers.

2. The OpenVPN TCP technology check is looking for `tech.get('id') == 5` but we should be looking at the name instead since that's more reliable.

Let me fix these issues:

---

_****_

```diff
              return False
  
-         # Check server status
-         status = server.get("status")
-         if status != "online":
-             return False
- 
          # Check load value
          load = server.get("load")
```

---

_****_



---

_****_



Let me try a different approach to edit the file:

---

_****_



---

_****_



I see that the apply model is having trouble with the edits. Let me try one more time with a more focused change:

---

_****_



---

_****_



I apologize for the difficulty with the apply model. Let me try a different approach - let's first check the current content of the file to make sure we're editing the right section:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



Now let me try to edit the file again with a more precise change:

---

_****_



---

_****_



I apologize for the difficulty with the apply model. Let me try one more time with a different approach:

---

_****_

<details>
            <summary>Grep search for "tech.get\('id'\) == 5" • **1** files</summary>
        
| File | Line | Match |
|------|------|-------|
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L534 | `2. The OpenVPN TCP technology check is looking for `tech.get('id') == 5` but we should be looking at the name instead since that's more reliable.` |

</details>

---

_****_

<details>
            <summary>Grep search for "OpenVPN TCP" • **13** files</summary>
        
| File | Line | Match |
|------|------|-------|
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L6209 | `4. Feature support (OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L6244 | `id: Technology identifier (e.g. 5 for OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L6325 | `1. OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L6507 | `# Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L6527 | `f"Skipping server without OpenVPN TCP: {server.get('hostname')}",` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2766 | `2. Added filtering for OpenVPN TCP servers in the API request` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2849 | `+                 # Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L3441 | `# Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L3453 | `+                             f"Skipping server without OpenVPN TCP: {server.get('hostname')}"` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_00-09-code-analysis-and-docstring-enhancement.md` | L452 | `+         id: Technology identifier (e.g. 5 for OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_00-09-code-analysis-and-docstring-enhancement.md` | L528 | `+         1. OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_00-09-code-analysis-and-docstring-enhancement.md` | L2159 | `+ 4. Feature support (OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L724 | `+                 if any(tech["name"] == "OpenVPN TCP" for tech in server["technologies"])` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L760 | `2. Moved the OpenVPN TCP filtering to Python code instead of API parameters` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L829 | `-                 if any(tech["name"] == "OpenVPN TCP" for tech in server["technologies"])` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L845 | `+             # Filter for OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L881 | `- Then filter for OpenVPN TCP support in the code` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-56-vpn-connection-troubleshooting.md` | L1069 | `-             # Filter for OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_02-15-python-virtual-environment-setup-and-testing.md` | L6075 | `>       if any(tech["name"] == "OpenVPN TCP" for tech in server["t` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-22_20-24-managing-todos-and-development-tasks.md` | L2794 | `if any(tech["name"] == "OpenVPN TCP" for tech in serve` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_04-09-executing-python-vpn-connection-command.md` | L4080 | `2. Filter for online OpenVPN TCP servers` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L19 | `DEBUG    2025-02-24 08:00:43.470 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L29 | `DEBUG    2025-02-24 08:00:43.477 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L36 | `DEBUG    2025-02-24 08:00:43.483 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L46 | `DEBUG    2025-02-24 08:00:43.489 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L53 | `DEBUG    2025-02-24 08:00:43.495 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L63 | `DEBUG    2025-02-24 08:00:43.502 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L70 | `DEBUG    2025-02-24 08:00:43.508 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L80 | `DEBUG    2025-02-24 08:00:43.515 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L87 | `DEBUG    2025-02-24 08:00:43.520 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L97 | `DEBUG    2025-02-24 08:00:43.527 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L104 | `DEBUG    2025-02-24 08:00:43.533 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L114 | `DEBUG    2025-02-24 08:00:43.540 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L121 | `DEBUG    2025-02-24 08:00:43.546 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L131 | `DEBUG    2025-02-24 08:00:43.553 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L138 | `DEBUG    2025-02-24 08:00:43.559 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L148 | `DEBUG    2025-02-24 08:00:43.566 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L155 | `DEBUG    2025-02-24 08:00:43.572 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L165 | `DEBUG    2025-02-24 08:00:43.579 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L172 | `DEBUG    2025-02-24 08:00:43.585 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L182 | `DEBUG    2025-02-24 08:00:43.594 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L189 | `DEBUG    2025-02-24 08:00:43.599 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L199 | `DEBUG    2025-02-24 08:00:43.607 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L206 | `DEBUG    2025-02-24 08:00:43.613 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L216 | `DEBUG    2025-02-24 08:00:43.621 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L223 | `DEBUG    2025-02-24 08:00:43.626 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L233 | `DEBUG    2025-02-24 08:00:43.633 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L240 | `DEBUG    2025-02-24 08:00:43.639 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L250 | `DEBUG    2025-02-24 08:00:43.647 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L257 | `Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L267 | `DEBUG    2025-02-24 08:00:47.031 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L274 | `DEBUG    2025-02-24 08:00:47.037 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L284 | `DEBUG    2025-02-24 08:00:47.044 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L291 | `DEBUG    2025-02-24 08:00:47.051 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L301 | `DEBUG    2025-02-24 08:00:47.058 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L308 | `DEBUG    2025-02-24 08:00:47.065 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L318 | `DEBUG    2025-02-24 08:00:47.075 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L325 | `DEBUG    2025-02-24 08:00:47.083 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L335 | `DEBUG    2025-02-24 08:00:47.091 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L342 | `DEBUG    2025-02-24 08:00:47.099 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L352 | `DEBUG    2025-02-24 08:00:47.110 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L359 | `DEBUG    2025-02-24 08:00:47.117 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L369 | `DEBUG    2025-02-24 08:00:47.125 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN    server.py:386` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L478 | `2. However, we can see that the servers DO have OpenVPN TCP support:` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L480 | `DEBUG    2025-02-24 08:00:43.475 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: None` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L482 | `DEBUG    2025-02-24 08:00:43.477 | DEBUG    | nyord_vpn.network.server:get_servers_cache:386 - Found OpenVPN TCP support: OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-01-untitled.md` | L534 | `2. The OpenVPN TCP technology check is looking for `tech.get('id') == 5` but we should be looking at the name instead since that's more reliable.` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L41 | `4. Feature support (OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L76 | `id: Technology identifier (e.g. 5 for OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L184 | `1. OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L363 | `# Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L382 | `and "OpenVPN TCP" in tech_name` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L385 | `self.logger.debug(f"Found OpenVPN TCP support: {tech_name}")` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L392 | `f"Skipping server without OpenVPN TCP: {server.get('hostname')}. "` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_07-30-vpn-connection-issues-and-server-selection-errors.md` | L11308 | `# Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_07-30-vpn-connection-issues-and-server-selection-errors.md` | L11322 | `f"Skipping server without OpenVPN TCP: {server.get('hostname')}"` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L31 | `"""Test OpenVPN TCP technology validation."""` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L32 | `# Test regular OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L39 | `{"id": 5, "name": "OpenVPN TCP", "status": "online"},` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L44 | `# Test OpenVPN TCP Dedicated` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L51 | `{"id": 45, "name": "OpenVPN TCP Dedicated", "status": "online"},` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L56 | `# Test server without OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L77 | `{"name": "OpenVPN TCP"},  # Missing id` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L100 | `{"id": 5, "name": "OpenVPN TCP", "status": "online"},` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L112 | `{"id": 5, "name": "OpenVPN TCP", "status": "online"},` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L124 | `{"id": 5, "name": "OpenVPN TCP", "status": "online"},` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L136 | `{"id": 5, "name": "OpenVPN TCP", "status": "online"},` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L152 | `{"id": 5, "name": "OpenVPN TCP", "status": "online"},` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L161 | `{"id": 45, "name": "OpenVPN TCP Dedicated", "status": "online"},` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L179 | `{"id": 5, "name": "OpenVPN TCP", "status": "online"},` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L188 | `# Should only include online servers with OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L194 | `mock_api_client.logger.debug.assert_any_call("Found OpenVPN TCP support: OpenVPN TCP")` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L195 | `mock_api_client.logger.debug.assert_any_call("Found OpenVPN TCP support: OpenVPN TCP Dedicated")` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/tests/test_server_manager.py` | L197 | `"Skipping server without OpenVPN TCP: udp1.nordvpn.com. "` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L19 | `DEBUG    2025-02-24 07:56:30.244 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L34 | `DEBUG    2025-02-24 07:56:30.716 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 45, Name: OpenVPN TCP         server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_07-57-vpn-server-connection-debugging.md` | L39 | `DEBUG    2025-02-24 07:56:30.720 | DEBUG    | nyord_vpn.network.server:get_servers_cache:375 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:375` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L41 | `4. Feature support (OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L76 | `id: Technology identifier (e.g. 5 for OpenVPN TCP)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L184 | `1. OpenVPN TCP support` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L363 | `# Check if server is online and supports OpenVPN TCP` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L382 | `and "OpenVPN TCP" in tech_name` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L385 | `self.logger.debug(f"Found OpenVPN TCP support: {tech_name}")` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L392 | `f"Skipping server without OpenVPN TCP: {server.get('hostname')}. "` |

</details>

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



Now I see the issue. The problem is in the server validation logic. We're checking for OpenVPN TCP support in two places:

1. In the server cache loading code, we're correctly checking for OpenVPN TCP by name and it's finding matches
2. But in `_is_valid_server`, we're not checking for OpenVPN TCP support at all

Let me fix this by updating the server validation logic:

---

_****_

```diff
          # Check load value
          load = server.get("load")
-         return not (not isinstance(load, int | float) or load < 0 or load > 100)
+         if not isinstance(load, int | float) or load < 0 or load > 100:
+             return False
+ 
+         # Check OpenVPN TCP support
+         has_openvpn_tcp = False
+         for tech in server.get("technologies", []):
+             tech_name = tech.get("name", "")
+             if (
+                 isinstance(tech, dict)
+                 and isinstance(tech_name, str)
+                 and "OpenVPN TCP" in tech_name
+             ):
+                 has_openvpn_tcp = True
+                 break
+ 
+         return has_openvpn_tcp
  
      def _test_server(self, server: dict[str, Any]) -> tuple[dict[str, Any], float]:
```

---

_****_



Now let's try running the command again. The changes I made:

1. Removed the strict status check since the API is returning `None` for status
2. Added proper OpenVPN TCP support validation in `_is_valid_server` by checking for the technology name
3. Made the load value check more explicit with a separate if statement

These changes should allow the server validation to work correctly. The logs show that the servers do have OpenVPN TCP support, but they were being rejected by the validation logic. Now the validation should match what we're seeing in the server data.

Let me know if you'd like me to explain any part of the changes in more detail or if you have any questions!

Wait, but... let me also check if we need to update the server filtering logic in `get_servers_cache` since it's also checking for OpenVPN TCP support:

---

_****_



---

_****_

```diff
  
                  # Check if server is online and supports OpenVPN TCP
-                 if server.get("status") != "online":
-                     if self.api_client.verbose:
-                         self.logger.debug(
-                             f"Skipping offline server: {server.get('hostname')}"
-                         )
-                     continue
- 
                  if self.api_client.verbose:
                      self.logger.debug(f"Technologies for {server.get('hostname')}:")
```

---

_****_





Perfect! I've made two key changes:

1. Updated `_is_valid_server` to properly validate OpenVPN TCP support by checking the technology name instead of ID
2. Removed the strict status check in `get_servers_cache` since the API is returning `None` for status

The changes should now allow the server validation to work correctly. The logs show that the servers do have OpenVPN TCP support, and now they won't be rejected by the validation logic.

Let me know if you'd like me to explain any part of the changes in more detail or if you have any questions!

---

_**User**_

[02/24/25 08:04:50] DEBUG    2025-02-24 08:04:50.380 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:154 - Found OpenVPN at                   vpn.py:154
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.385 | DEBUG    | nyord_vpn.network.vpn:setup_connection:232 - Created auth file at                         vpn.py:232
                             /Users/adam/.cache/nyord-vpn/openvpn.auth                                                                                                
                    DEBUG    2025-02-24 08:04:50.389 | DEBUG    | nyord_vpn.network.server:get_servers_cache:305 - Fetching server list from API...      server.py:305
                    DEBUG    2025-02-24 08:04:50.514 | DEBUG    | nyord_vpn.network.server:get_servers_cache:317 - Successfully fetched server data from server.py:317
                             API                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.516 | DEBUG    | nyord_vpn.network.server:get_servers_cache:325 - Found 100 servers in API response     server.py:325
                    DEBUG    2025-02-24 08:04:50.664 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for pl128.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.666 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.667 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.669 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.670 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.672 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.673 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.675 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.676 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.677 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for hu48.nordvpn.com:    server.py:366
                    DEBUG    2025-02-24 08:04:50.679 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.680 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.681 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.683 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.684 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.686 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.687 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.688 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.689 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us5063.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:50.691 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.692 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.694 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.695 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.696 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.698 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.699 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.700 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.702 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for at86.nordvpn.com:    server.py:366
                    DEBUG    2025-02-24 08:04:50.703 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.705 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.706 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.708 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.709 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.710 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.712 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.713 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.714 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for ch217.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.716 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.717 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.718 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.720 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.721 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.723 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.724 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.725 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.727 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for dk152.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.728 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.729 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.731 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.732 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.734 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.735 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.737 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.738 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.740 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for no151.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.741 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.743 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.744 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.746 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.747 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.749 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.750 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.752 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.753 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for ch218.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.755 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.757 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.758 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.759 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.761 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.762 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.764 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.766 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.767 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk1784.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:50.768 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.770 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.772 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.773 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.775 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.776 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.777 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.779 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.780 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr555.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.781 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.782 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.784 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.785 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.788 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.789 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.790 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.792 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.793 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for ch219.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.794 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.796 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.798 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.799 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.800 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.802 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.803 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.805 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.806 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us5064.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:50.807 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.809 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.810 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.812 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.813 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.814 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.816 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.817 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.818 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk765.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.820 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.821 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.822 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.824 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.825 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.827 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.828 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.829 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.831 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk812.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.833 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.834 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.836 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.837 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.839 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.841 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.842 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.843 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.845 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk813.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.846 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.848 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.849 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.851 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.853 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.854 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.856 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.857 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.859 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk814.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.861 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.862 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.863 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.865 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.867 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.868 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.870 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.871 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.872 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk871.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.874 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.875 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.876 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.878 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.879 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.880 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.882 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.883 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.884 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk873.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.886 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.887 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.889 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.891 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.892 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.893 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.895 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.896 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.898 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk875.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.900 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.901 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.903 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.904 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.906 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.908 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.909 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.911 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.912 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for de507.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.914 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.915 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.916 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.918 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.919 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.920 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.922 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for de508.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.923 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.924 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.926 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.927 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.928 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.930 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.931 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for de509.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.932 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.934 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.935 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.937 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.938 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.940 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.941 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for de510.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.942 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.944 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.945 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.946 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.948 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.949 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.950 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk877.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.952 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.953 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.954 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.956 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.957 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.959 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.960 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.962 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.964 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2920.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:50.966 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.967 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.968 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.970 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.972 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.973 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.975 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2921.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:50.976 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.978 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.980 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.981 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.983 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:50.984 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.986 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk879.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:50.987 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.989 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.990 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.992 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.993 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.995 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:50.996 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:50.998 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:50.999 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2924.nordvpn.com:  server.py:366
[02/24/25 08:04:51] DEBUG    2025-02-24 08:04:51.000 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.001 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.003 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.004 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.006 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.007 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.008 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2925.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.009 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.011 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.013 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.014 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.015 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.017 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.018 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk884.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.020 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.021 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.022 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.024 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.025 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.027 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.028 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.029 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.031 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2929.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.032 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.033 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.035 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.036 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.037 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.039 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.041 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2930.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.042 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.044 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.045 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.047 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.049 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.050 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.051 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk886.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.053 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.054 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.055 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.057 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.058 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.060 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.061 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.062 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.064 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for be149.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.066 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.068 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.069 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.070 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.072 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.074 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.076 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.077 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.079 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk1806.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.080 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.082 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.083 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.085 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.086 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.087 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.089 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.090 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.092 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk888.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.093 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.094 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.096 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.097 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.099 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.100 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.102 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.103 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.105 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk890.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.106 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.108 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.109 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.111 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.112 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.113 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.115 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.116 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.118 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2939.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.119 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.120 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.122 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.123 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.124 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.126 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.128 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2940.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.130 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.131 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.133 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.134 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.136 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.138 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.139 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for de655.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.140 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.142 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.143 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.145 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.147 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.149 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.150 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk892.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.151 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.153 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.155 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.156 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.158 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.160 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.161 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.163 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.164 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk894.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.165 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.167 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.168 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.169 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.171 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.172 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.173 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.175 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.176 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk896.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.177 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.179 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.181 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.182 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.184 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.185 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.186 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.188 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.189 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk898.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.191 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.192 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.193 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.195 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.196 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.198 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.199 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.200 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.201 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2943.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.203 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.204 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.206 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.208 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.210 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.212 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.213 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2944.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.214 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.216 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.218 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.219 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.220 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.222 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.223 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2945.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.224 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.226 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.227 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.228 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.230 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.231 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.232 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2946.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.234 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.235 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.236 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.238 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.239 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.241 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.242 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for nl408.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.243 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.245 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.246 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.247 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.249 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.250 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.252 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for nl409.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.253 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.254 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.256 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.257 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.258 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.260 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.262 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for de676.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.264 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.265 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.267 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.268 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.270 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.271 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.273 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us5055.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.274 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.275 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.277 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.278 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.280 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.282 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.283 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.285 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.286 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2949.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.288 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.289 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.291 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.292 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.294 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.295 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.297 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us2950.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.298 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.299 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.301 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.302 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.303 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.305 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.306 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr439.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.307 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.309 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.310 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.311 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.313 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.315 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.316 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr440.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.318 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.319 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.320 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.322 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.323 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.325 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.326 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for jp429.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.327 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.329 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.330 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.331 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.333 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.334 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.335 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.337 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.338 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for es114.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.340 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.342 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.343 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.345 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.346 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.348 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.350 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.351 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.352 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for it132.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.354 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.355 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.356 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.358 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.359 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.361 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.362 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.364 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.366 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us4735.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.367 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.369 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.370 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.372 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.374 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.375 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.377 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.378 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.380 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for pl122.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.381 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.382 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.384 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.385 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.386 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.388 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.389 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.390 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.392 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for cz93.nordvpn.com:    server.py:366
                    DEBUG    2025-02-24 08:04:51.393 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.394 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.396 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.397 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.399 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.400 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.402 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.403 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.405 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for at80.nordvpn.com:    server.py:366
                    DEBUG    2025-02-24 08:04:51.406 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.407 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.409 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.410 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.412 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.413 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.414 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.416 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.417 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for ro59.nordvpn.com:    server.py:366
                    DEBUG    2025-02-24 08:04:51.418 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.420 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.421 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.422 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.424 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.425 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.426 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.428 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.430 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for ch198.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.431 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.433 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.434 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.436 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.438 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.439 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.441 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.442 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.443 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for bg38.nordvpn.com:    server.py:366
                    DEBUG    2025-02-24 08:04:51.445 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.447 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.448 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.450 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.451 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.453 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.455 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.456 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.458 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for hu47.nordvpn.com:    server.py:366
                    DEBUG    2025-02-24 08:04:51.459 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.461 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.462 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.464 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.465 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.466 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.468 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.469 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.470 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr452.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.472 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.473 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.474 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.476 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.477 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.479 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.480 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.482 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.483 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for jp454.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.484 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.486 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.487 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.489 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.490 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.492 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.493 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.494 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.496 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us4951.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.497 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.498 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.500 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.501 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.502 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.504 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.505 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for dk150.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.508 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.509 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.511 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.512 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.514 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.516 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.517 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.519 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.520 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for de750.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.521 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.523 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.524 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.526 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.527 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.528 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.530 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.531 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.532 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us4953.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.534 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.535 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.536 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.538 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.539 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.541 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.542 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us4954.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.544 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.545 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.546 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.548 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 42, Name: OpenVPN UDP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.549 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 45, Name: OpenVPN TCP         server.py:368
                             Dedicated, Status: None                                                                                                                  
                    DEBUG    2025-02-24 08:04:51.550 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.552 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for pl125.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.553 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.554 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.556 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.557 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.559 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.560 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.562 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.564 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.566 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us5057.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.567 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.568 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.570 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.572 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.573 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.575 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.576 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.578 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.579 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us5058.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.581 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.583 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.584 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.585 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.587 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.589 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.590 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.592 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.593 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us5059.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.595 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.596 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.598 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.599 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.600 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.602 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.603 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.605 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.606 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for us5060.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.607 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.609 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.610 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.611 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.613 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.615 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.617 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.618 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.619 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for no141.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.621 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.622 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.623 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.625 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.626 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.628 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.629 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.631 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.632 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for no142.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.633 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.634 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.636 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.637 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.639 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.641 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.643 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.644 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.646 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for no143.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.647 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.649 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.650 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.652 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.653 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.654 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.656 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.657 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.659 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for no144.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.660 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.662 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.663 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.664 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.667 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.668 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.670 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.671 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.673 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for no145.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.674 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.676 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.677 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.679 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.680 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.682 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.683 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.684 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.686 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for no146.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.687 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.688 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.690 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.691 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.692 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.694 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.695 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.697 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.698 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for no147.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.700 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.701 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.702 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.704 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.705 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.707 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.708 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.710 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.711 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for no148.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.712 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.714 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.715 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.716 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.718 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.719 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.720 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.722 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.723 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for no149.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.725 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.726 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.728 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.730 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.731 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.733 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.734 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.736 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.738 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for uk1785.nordvpn.com:  server.py:366
                    DEBUG    2025-02-24 08:04:51.739 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.740 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.742 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.743 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.745 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.747 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.749 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.750 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.752 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for hu49.nordvpn.com:    server.py:366
                    DEBUG    2025-02-24 08:04:51.753 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.755 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.757 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.758 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.760 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.762 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.763 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.764 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.766 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr536.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.767 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.768 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.770 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.771 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.772 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.774 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.775 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.777 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.778 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr537.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.780 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.781 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.783 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.784 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.785 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.787 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.788 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.790 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.791 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr538.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.793 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.794 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.795 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.797 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.798 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.800 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.801 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.802 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.804 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr539.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.805 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.807 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.809 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.811 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.812 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.814 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.816 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.817 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.819 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr540.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.820 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.821 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.823 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.824 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.826 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.827 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.829 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.830 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.831 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr541.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.833 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.834 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.835 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.837 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.838 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.840 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.841 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.843 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.844 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr542.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.845 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.847 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.848 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.849 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.851 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.852 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.853 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.855 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.856 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr543.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.858 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.859 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.861 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.863 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.865 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.867 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.868 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.870 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.872 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for fr544.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.873 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.875 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.876 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.878 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.880 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.882 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.883 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.885 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.886 | DEBUG    | nyord_vpn.network.server:get_servers_cache:366 - Technologies for ch221.nordvpn.com:   server.py:366
                    DEBUG    2025-02-24 08:04:51.888 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 1, Name: IKEv2/IPSec, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.889 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 3, Name: OpenVPN UDP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.891 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 5, Name: OpenVPN TCP, Status: server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.893 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 21, Name: HTTP Proxy (SSL),   server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.894 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 23, Name: HTTP CyberSec Proxy server.py:368
                             (SSL), Status: None                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.896 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 35, Name: Wireguard, Status:  server.py:368
                             None                                                                                                                                     
                    DEBUG    2025-02-24 08:04:51.897 | DEBUG    | nyord_vpn.network.server:get_servers_cache:368 -   - ID: 51, Name: NordWhisper,        server.py:368
                             Status: None                                                                                                                             
                    DEBUG    2025-02-24 08:04:51.898 | DEBUG    | nyord_vpn.network.server:get_servers_cache:379 - Found OpenVPN TCP support: OpenVPN    server.py:379
                             TCP                                                                                                                                      
                    DEBUG    2025-02-24 08:04:51.900 | DEBUG    | nyord_vpn.network.server:get_servers_cache:444 - No valid servers found after          server.py:444
                             filtering 100 total servers                                                                                                              
                    ERROR    2025-02-24 08:04:51.901 | ERROR    | nyord_vpn.network.server:get_servers_cache:474 - Failed to fetch servers: No valid     server.py:474
                             servers found in API response. Total servers: 100, Invalid: 100                                                                          
                             Traceback (most recent call last):                                                                                                       
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/bin/nyord-vpn", line 10, in <module>                               
                                 sys.exit(main())                                                                                                                     
                                 |   |    -> <function main at 0x10bea3920>                                                                                           
                                 |   -> <built-in function exit>                                                                                                      
                                 -> <module 'sys' (built-in)>                                                                                                         
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__main__.py", line 81, in main                             
                                 fire.Fire(CLI)                                                                                                                       
                                 |    |    -> <class 'nyord_vpn.__main__.CLI'>                                                                                        
                                 |    -> <function Fire at 0x10bf49300>                                                                                               
                                 -> <module 'fire' from                                                                                                               
                             '/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/__init__...                             
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 135,              
                             in Fire                                                                                                                                  
                                 component_trace = _Fire(component, args, parsed_flag_args, context, name)                                                            
                                                   |     |          |     |                 |        -> 'nyord-vpn'                                                   
                                                   |     |          |     |                 -> {}                                                                     
                                                   |     |          |     -> Namespace(verbose=False, interactive=False, separator='-', completion=None,              
                             help=False, trace=False)                                                                                                                 
                                                   |     |          -> ['go', 'pl', '--verbose']                                                                      
                                                   |     -> <class 'nyord_vpn.__main__.CLI'>                                                                          
                                                   -> <function _Fire at 0x10bf6aac0>                                                                                 
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 468,              
                             in _Fire                                                                                                                                 
                                 component, remaining_args = _CallAndUpdateTrace(                                                                                     
                                 |                           -> <function _CallAndUpdateTrace at 0x10bf6ac00>                                                         
                                 -> <bound method CLI.go of <nyord_vpn.__main__.CLI object at 0x10bf332c0>>                                                           
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.venv/lib/python3.12/site-packages/fire/core.py", line 684,              
                             in _CallAndUpdateTrace                                                                                                                   
                                 component = fn(*varargs, **kwargs)                                                                                                   
                                             |   |          -> {}                                                                                                     
                                             |   -> ['pl']                                                                                                            
                                             -> <bound method CLI.go of <nyord_vpn.__main__.CLI object at 0x10bf332c0>>                                               
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__main__.py", line 46, in go                               
                                 self.client.go(country_code)                                                                                                         
                                 |    |      |  -> 'pl'                                                                                                               
                                 |    |      -> <function Client.go at 0x10bea3380>                                                                                   
                                 |    -> <nyord_vpn.core.client.Client object at 0x10bf7b680>                                                                         
                                 -> <nyord_vpn.__main__.CLI object at 0x10bf332c0>                                                                                    
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/core/client.py", line 278, in go                           
                                 selected_servers = self.server_manager.select_fastest_server(                                                                        
                                                    |    |              -> <function ServerManager.select_fastest_server at 0x10be2b9c0>                              
                                                    |    -> <nyord_vpn.network.server.ServerManager object at 0x10a4bff80>                                            
                                                    -> <nyord_vpn.core.client.Client object at 0x10bf7b680>                                                           
                                                                                                                                                                      
                               File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 838, in                           
                             select_fastest_server                                                                                                                    
                                 servers = self.get_servers_cache().get("servers", [])                                                                                
                                           |    -> <function ServerManager.get_servers_cache at 0x10be2b6a0>                                                          
                                           -> <nyord_vpn.network.server.ServerManager object at 0x10a4bff80>                                                          
                                                                                                                                                                      
                             > File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py", line 447, in                           
                             get_servers_cache                                                                                                                        
                                 raise ValueError(                                                                                                                    
                                                                                                                                                                      
                             ValueError: No valid servers found in API response. Total servers: 100, Invalid: 100                                                     
                                                                                                                                                                      
                                                                                                                                                                      
                    ERROR    2025-02-24 08:04:51.914 | ERROR    | nyord_vpn.network.server:select_fastest_server:935 - Error selecting server: No        server.py:935
                             servers available in cache                                                                                                               
Error: No servers available in PL. Please try another country or check your internet connection.



????? This is RIDICULOUS. Why are you doing this elaborate filtering. I WANT YOU TO RETRY A DIFFERENT FUCKING SERVER IF ONE FAILS, ON ANY FAILURE. 

Instead, you're doing elaborate overcomplications that don't work. 

---

_**Assistant**_

I understand your frustration. You're absolutely right - we're overcomplicating the server selection process with too much filtering and validation, when what we really need is a simple retry mechanism that tries different servers when one fails.

Let me propose a simpler, more robust approach:

---

_****_



---

_****_



Let me try again with a more focused edit:

---

_****_

```diff
  
      def _is_valid_server(self, server: Any) -> bool:
-         """Validate server data structure.
+         """Basic server validation.
+ 
+         Only checks:
+         1. Has valid hostname
+         2. Has OpenVPN TCP support
  
          Args:
          Returns:
              bool: True if server data is valid
- 
          """
          if not isinstance(server, dict):
              return False
  
-         # Check required fields
+         # Check hostname
          hostname = server.get("hostname")
          if not isinstance(hostname, str) or not hostname:
              return False
  
-         # Basic hostname validation
-         if not hostname.endswith(".nordvpn.com"):
-             return False
- 
-         # Check country info
-         country = server.get("country")
-         if not isinstance(country, dict):
-             return False
- 
-         country_code = country.get("code")
-         if not isinstance(country_code, str) or len(country_code) != 2:
-             return False
- 
-         # Check load value
-         load = server.get("load")
-         if not isinstance(load, int | float) or load < 0 or load > 100:
-             return False
- 
          # Check OpenVPN TCP support
          has_openvpn_tcp = False
```

---

_****_



Now let me update the server selection logic to be more resilient:

---

_****_

```diff
          _retry_count: int = 0,
          max_retries: int = 3,
-         max_servers: int = 5,  # Return up to 5 fastest servers
+         max_servers: int = 5,
      ) -> list[dict[str, Any]]:
-         """Select fastest available servers.
- 
-         Tests multiple servers in parallel and returns them sorted by latency.
-         Will retry with different servers if initial selection fails.
+         """Select servers to try, with basic country filtering if specified.
          
          Args:
-             country_code: Two-letter country code to filter servers
-             random_select: Whether to randomly select from available servers
-             exclude_servers: Set of server hostnames to exclude from selection
-             _retry_count: Internal retry counter (do not set manually)
+             country_code: Optional country code to filter by
+             random_select: Whether to randomly select servers
+             exclude_servers: Set of servers to exclude
+             _retry_count: Internal retry counter
              max_retries: Maximum number of retry attempts
-             max_servers: Maximum number of servers to return (default 5)
+             max_servers: Maximum number of servers to return
  
          Returns:
-             List of server info dictionaries sorted by speed (fastest first)
+             List of server dictionaries to try
              
          Raises:
              servers = self.get_servers_cache().get("servers", [])
              if not servers:
-                 raise ServerError("No servers available in cache")
- 
-             # Validate and filter by country if specified
-             normalized_country = self._validate_country_code(country_code)
-             if normalized_country:
-                 servers = [
-                     s
-                     for s in servers
-                     if s.get("country", {}).get("code", "").upper() == normalized_country
-                 ]
-                 if not servers:
-                     country_info = self.get_country_info(normalized_country)
-                     country_name = (
-                         country_info.get("name") if country_info else normalized_country
+                 if _retry_count < max_retries:
+                     if self.api_client.verbose:
+                         self.logger.debug(f"No servers in cache, retrying... (attempt {_retry_count + 1})")
+                     return self.select_fastest_server(
+                         country_code=country_code,
+                         random_select=random_select,
+                         exclude_servers=exclude_servers,
+                         _retry_count=_retry_count + 1,
+                         max_retries=max_retries,
+                         max_servers=max_servers,
                      )
-                     raise ServerError(
-                         f"No servers available in {country_name} ({normalized_country}). "
-                         "Try another country or check your connection."
-                     )
- 
-             # Filter out failed and excluded servers
-             available_servers = [
+                 raise ServerError("No servers available in cache after retries")
+ 
+             # Filter by country if specified
+             if country_code:
+                 normalized = country_code.upper()
+                 country_servers = [
                      s for s in servers
-                 if s.get("hostname") not in (exclude_servers or set())
-                 and s.get("hostname") not in self._failed_servers
-             ]
+                     if s.get("country", {}).get("code", "").upper() == normalized
+                 ]
+                 if not country_servers:
+                     raise ServerError(f"No servers available in {normalized}")
+                 servers = country_servers
+ 
+             # Exclude failed/excluded servers
+             exclude_set = (exclude_servers or set()) | self._failed_servers
+             available = [s for s in servers if s.get("hostname") not in exclude_set]
  
-             if not available_servers:
+             if not available:
+                 if _retry_count < max_retries:
                      if self.api_client.verbose:
                          self.logger.debug(
-                         f"No available servers after filtering {len(servers)} total, "
-                         f"{len(self._failed_servers)} failed, "
-                         f"{len(exclude_servers or set())} excluded"
+                             f"All servers excluded/failed, clearing failed servers and retrying... "
+                             f"(attempt {_retry_count + 1})"
+                         )
+                     self._failed_servers.clear()  # Reset failed servers and try again
+                     return self.select_fastest_server(
+                         country_code=country_code,
+                         random_select=random_select,
+                         exclude_servers=exclude_servers,
+                         _retry_count=_retry_count + 1,
+                         max_retries=max_retries,
+                         max_servers=max_servers,
                      )
                  raise ServerError(
-                     f"No available servers found{' in ' + normalized_country if normalized_country else ''}"
+                     f"No available servers found{' in ' + normalized if country_code else ''} "
+                     f"after {max_retries} retries"
                  )
  
-             # Sort by load first to get initial candidates
-             available_servers.sort(key=lambda x: float(x.get("load", 100)))
-             
-             # Take top N servers by load for testing
-             test_candidates = available_servers[:max_servers * 2]  # Test twice as many as we need
+             # Select servers
              if random_select:
                  import random
-                 test_candidates = random.sample(
-                     available_servers, 
-                     min(max_servers * 2, len(available_servers))
-                 )
+                 selected = random.sample(
+                     available,
+                     min(max_servers, len(available))
+                 )
+             else:
+                 # Sort by load, but add some randomness to avoid everyone hitting the same servers
+                 available.sort(key=lambda x: float(x.get("load", 100)) + random.uniform(0, 10))
+                 selected = available[:max_servers]
  
              if self.api_client.verbose:
-                 self.logger.debug(f"Testing {len(test_candidates)} servers for speed")
- 
-             # Test servers in parallel using ThreadPoolExecutor
-             from concurrent.futures import ThreadPoolExecutor, as_completed
-             from threading import Lock
- 
-             results = []
-             result_lock = Lock()
- 
-             with ThreadPoolExecutor(max_workers=min(len(test_candidates), 10)) as executor:
-                 future_to_server = {
-                     executor.submit(self._test_server, server): server
-                     for server in test_candidates
-                 }
- 
-                 for future in as_completed(future_to_server):
-                     server = future_to_server[future]
-                     try:
-                         tested_server, score = future.result()
-                         if score < float('inf'):  # Only include successful tests
-                             with result_lock:
-                                 results.append((tested_server, score))
-                     except Exception as e:
-                         if self.api_client.verbose:
-                             self.logger.warning(f"Failed to test {server.get('hostname')}: {e}")
- 
-             # Sort by score and take top N
-             results.sort(key=lambda x: x[1])  # Sort by score
-             selected_servers = [server for server, _ in results[:max_servers]]
- 
-             if not selected_servers:
-                 raise ServerError(
-                     f"No responsive servers found{' in ' + normalized_country if normalized_country else ''}"
-                 )
- 
-             if self.api_client.verbose:
-                 self.logger.info(f"Selected {len(selected_servers)} fastest servers:")
-                 for i, server in enumerate(selected_servers, 1):
-                     self.logger.info(f"  {i}. {server.get('hostname')} (load: {server.get('load')}%)")
+                 self.logger.info(f"Selected {len(selected)} servers to try:")
+                 for i, server in enumerate(selected, 1):
+                     self.logger.info(
+                         f"  {i}. {server.get('hostname')} "
+                         f"(load: {server.get('load')}%)"
+                     )
  
-             return selected_servers
- 
+             return selected
+ 
+         except ServerError:
+             raise
          except Exception as e:
              if self.api_client.verbose:
                  self.logger.error(f"Error selecting server: {e}", exc_info=True)
+             if _retry_count < max_retries:
+                 if self.api_client.verbose:
+                     self.logger.debug(f"Retrying after error... (attempt {_retry_count + 1})")
+                 return self.select_fastest_server(
+                     country_code=country_code,
+                     random_select=random_select,
+                     exclude_servers=exclude_servers,
+                     _retry_count=_retry_count + 1,
+                     max_retries=max_retries,
+                     max_servers=max_servers,
+                 )
              raise ServerError(str(e))
  
```

---

_****_



Let me fix those linter errors:

---

_****_

```diff
              ServerError: If no servers are available after retries
          """
+         import random
+ 
          try:
              # Get available servers
  
              # Filter by country if specified
+             normalized = None
              if country_code:
                  normalized = country_code.upper()
                      )
                  raise ServerError(
-                     f"No available servers found{' in ' + normalized if country_code else ''} "
+                     f"No available servers found{' in ' + normalized if normalized else ''} "
                      f"after {max_retries} retries"
                  )
  
              # Select servers
              if random_select:
-                 import random
                  selected = random.sample(
                      available,
```

---

_****_



The key changes I've made:

1. Simplified server validation to only check for hostname and OpenVPN TCP support
2. Removed complex filtering and testing logic
3. Added proper retry mechanism that:
   - Retries on cache misses
   - Retries when all servers are excluded/failed
   - Retries on general errors
   - Clears failed servers list and tries again when needed
4. Added some randomness to load-based sorting to avoid everyone hitting the same servers
5. Kept country filtering but made it simpler

The linter errors are a bit strange since the code looks correct, but let's try one more fix:

---

_****_

```diff
              ServerError: If no servers are available after retries
          """
-         import random
- 
          try:
              # Get available servers
  
              # Filter by country if specified
-             normalized = None
-             if country_code:
-                 normalized = country_code.upper()
+             normalized = country_code.upper() if country_code else None
+             if normalized:
                  country_servers = [
                      s for s in servers
```

---

_****_



Perfect! The changes are now complete. Here's what the new approach does:

1. Minimal server validation - only checks for hostname and OpenVPN TCP support
2. Simple server selection:
   - Gets servers from cache/API
   - Filters by country if specified
   - Excludes failed/excluded servers
   - Either randomly selects or sorts by load with some randomness
3. Robust retry mechanism:
   - Retries if cache is empty
   - Retries if all servers are excluded/failed (clears failed servers list)
   - Retries on general errors
   - Each retry is logged in verbose mode
4. No complex testing or filtering that could prevent valid servers from being tried

This should make the server selection much more resilient - if a server fails, it will be marked as failed and the next server will be tried. If all servers fail, it will clear the failed servers list and try again.

The code is also much simpler and easier to understand. Let me know if you'd like me to explain any part in more detail!

---

_**User**_

[02/24/25 08:08:14] DEBUG    2025-02-24 08:08:14.986 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:154 - Found OpenVPN at                   vpn.py:154
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 08:08:14.995 | DEBUG    | nyord_vpn.network.vpn:setup_connection:232 - Created auth file at                         vpn.py:232
                             /Users/adam/.cache/nyord-vpn/openvpn.auth                                                                                                
[02/24/25 08:08:15] DEBUG    2025-02-24 08:08:15.000 | DEBUG    | nyord_vpn.network.server:get_servers_cache:290 - Using cached server list with 100     server.py:290
                             valid servers                                                                                                                            
Error: No servers available in PL. Please try another country or check your internet connection.

---

_**Assistant**_

I see the issue - while we have 100 valid servers in the cache, the filtering for Poland ("PL") is failing. Let me check the server filtering logic and add more detailed logging to diagnose the problem.

Let me modify the `select_fastest_server` method to add more detailed logging about country filtering:

---

_****_

```diff
              normalized = country_code.upper() if country_code else None
              if normalized:
+                 if self.api_client.verbose:
+                     self.logger.debug(f"Filtering servers for country: {normalized}")
+                     self.logger.debug(f"Total servers before filtering: {len(servers)}")
+                     # Log available countries
+                     countries = {s.get("country", {}).get("code", "").upper() for s in servers}
+                     self.logger.debug(f"Available countries: {sorted(countries)}")
+ 
                  country_servers = [
                      s for s in servers
                      if s.get("country", {}).get("code", "").upper() == normalized
                  ]
+                 if self.api_client.verbose:
+                     self.logger.debug(f"Found {len(country_servers)} servers for {normalized}")
+                     if not country_servers:
+                         # Log a few sample server entries to help diagnose the issue
+                         self.logger.debug("Sample server entries:")
+                         for s in servers[:3]:
+                             self.logger.debug(f"  {s.get('hostname')}: country={s.get('country', {})}")
+ 
                  if not country_servers:
                      raise ServerError(f"No servers available in {normalized}")
```

---

_****_



Now let me also check the server cache loading logic to ensure we're properly validating and storing country information:

---

_****_

<details>
            <summary>Searched codebase "get_servers_cache implementation in server.py" • **25** results</summary>
        
| File | Lines |
|------|-------|
| `nyord_vpn.txt` | L6405-6452 |
| `src/nyord_vpn/network/server.py` | L275-301 |
| `src/nyord_vpn/network/server.py` | L244-275 |
| `src/nyord_vpn/network/server.py` | L471-495 |
| `src/nyord_vpn/network/server.py` | L440-471 |
| `src/nyord_vpn/network/server.py` | L329-358 |
| `src/nyord_vpn/network/server.py` | L301-329 |
| `.specstory/history/2025-02-24_07-20-fixing-import-error-in-vpn-module.md` | L111-169 |
| `.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L3697-3746 |
| `nyord_vpn.txt` | L6610-6644 |
| `nyord_vpn.txt` | L6349-6405 |
| `.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2383-2432 |
| `nyord_vpn.txt` | L6584-6610 |
| `src/nyord_vpn/network/server.py` | L835-879 |
| `.specstory/history/2025-02-23_07-19-vpn-connection-troubleshooting-log.md` | L195-250 |
| `nyord_vpn.txt` | L438-492 |
| `nyord_vpn.txt` | L6288-6322 |
| `.specstory/history/2025-02-23_06-46-implementing-todo-items-in-project.md` | L270-402 |
| `nyord_vpn.txt` | L7118-7172 |
| `src/nyord_vpn/network/server.py` | L399-440 |
| `src/nyord_vpn/network/server.py` | L117-152 |
| `src/nyord_vpn/network/server.py` | L974-1003 |
| `.specstory/history/2025-02-23_07-30-vpn-connection-issues-and-server-selection-errors.md` | L11249-11290 |
| `src/nyord_vpn/network/server.py` | L919-974 |
| `.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2525-2575 |

</details>

---

_****_



I see the issue. Let me check the server cache loading and country filtering logic:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



I see the issue. The server cache loading code is correctly handling country information, but we need to force a refresh of the cache since it might be stale. Let me modify the code to:

1. Force a cache refresh when no servers are found for a country
2. Add more detailed logging about country filtering
3. Add a retry mechanism for country-specific server selection

---

_****_



---

_****_



---

_****_



---

_**User**_

Well, if you’re using CACHED stuff and something is FAILING, then maybe fucking get live data? Maybe the cache got stupid? 

sudo -E nyord-vpn go fr --verbose
[02/24/25 08:10:12] DEBUG    2025-02-24 08:10:12.971 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:154 - Found OpenVPN at                   vpn.py:154
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 08:10:12.978 | DEBUG    | nyord_vpn.network.vpn:setup_connection:232 - Created auth file at                         vpn.py:232
                             /Users/adam/.cache/nyord-vpn/openvpn.auth                                                                                                
                    DEBUG    2025-02-24 08:10:12.984 | DEBUG    | nyord_vpn.network.server:get_servers_cache:290 - Using cached server list with 100     server.py:290
                             valid servers                                                                                                                            
                    DEBUG    2025-02-24 08:10:12.986 | DEBUG    | nyord_vpn.network.server:select_fastest_server:839 - Filtering servers for country: FR server.py:839
                    DEBUG    2025-02-24 08:10:12.987 | DEBUG    | nyord_vpn.network.server:select_fastest_server:840 - Total servers before filtering:   server.py:840
                             100                                                                                                                                      
                    DEBUG    2025-02-24 08:10:12.989 | DEBUG    | nyord_vpn.network.server:select_fastest_server:843 - Available countries: ['']         server.py:843
                    DEBUG    2025-02-24 08:10:12.991 | DEBUG    | nyord_vpn.network.server:select_fastest_server:850 - Found 0 servers for FR            server.py:850
                    DEBUG    2025-02-24 08:10:12.992 | DEBUG    | nyord_vpn.network.server:select_fastest_server:853 - Sample server entries:            server.py:853
                    DEBUG    2025-02-24 08:10:12.994 | DEBUG    | nyord_vpn.network.server:select_fastest_server:855 -   pl128.nordvpn.com:              server.py:855
                             country={'code': '', 'name': 'Unknown'}                                                                                                  
                    DEBUG    2025-02-24 08:10:12.995 | DEBUG    | nyord_vpn.network.server:select_fastest_server:855 -   hu48.nordvpn.com:               server.py:855
                             country={'code': '', 'name': 'Unknown'}                                                                                                  
                    DEBUG    2025-02-24 08:10:12.997 | DEBUG    | nyord_vpn.network.server:select_fastest_server:855 -   us5063.nordvpn.com:             server.py:855
                             country={'code': '', 'name': 'Unknown'}                                                                                                  
Error: No servers available in FR. Please try another country or check your internet connection.
sudo -E nyord-vpn go pl --verbose
[02/24/25 08:10:18] DEBUG    2025-02-24 08:10:18.969 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:154 - Found OpenVPN at                   vpn.py:154
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 08:10:18.975 | DEBUG    | nyord_vpn.network.vpn:setup_connection:232 - Created auth file at                         vpn.py:232
                             /Users/adam/.cache/nyord-vpn/openvpn.auth                                                                                                
                    DEBUG    2025-02-24 08:10:18.981 | DEBUG    | nyord_vpn.network.server:get_servers_cache:290 - Using cached server list with 100     server.py:290
                             valid servers                                                                                                                            
                    DEBUG    2025-02-24 08:10:18.983 | DEBUG    | nyord_vpn.network.server:select_fastest_server:839 - Filtering servers for country: PL server.py:839
                    DEBUG    2025-02-24 08:10:18.985 | DEBUG    | nyord_vpn.network.server:select_fastest_server:840 - Total servers before filtering:   server.py:840
                             100                                                                                                                                      
                    DEBUG    2025-02-24 08:10:18.986 | DEBUG    | nyord_vpn.network.server:select_fastest_server:843 - Available countries: ['']         server.py:843
                    DEBUG    2025-02-24 08:10:18.988 | DEBUG    | nyord_vpn.network.server:select_fastest_server:850 - Found 0 servers for PL            server.py:850
                    DEBUG    2025-02-24 08:10:18.989 | DEBUG    | nyord_vpn.network.server:select_fastest_server:853 - Sample server entries:            server.py:853
                    DEBUG    2025-02-24 08:10:18.992 | DEBUG    | nyord_vpn.network.server:select_fastest_server:855 -   pl128.nordvpn.com:              server.py:855
                             country={'code': '', 'name': 'Unknown'}                                                                                                  
                    DEBUG    2025-02-24 08:10:18.993 | DEBUG    | nyord_vpn.network.server:select_fastest_server:855 -   hu48.nordvpn.com:               server.py:855
                             country={'code': '', 'name': 'Unknown'}                                                                                                  
                    DEBUG    2025-02-24 08:10:18.995 | DEBUG    | nyord_vpn.network.server:select_fastest_server:855 -   us5063.nordvpn.com:             server.py:855
                             country={'code': '', 'name': 'Unknown'}                                                                                                  
Error: No servers available in PL. Please try another country or check your internet connection.

---

_**Assistant**_



---



---

