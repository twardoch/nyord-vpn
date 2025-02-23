## SpecStory

## Comparing VPN Management Tools: openpyn vs nyord (23/02/2025, 05:54:53)

_**User**_

@openpyn-nordvpn.txt So what can you say about this, compared to our @nyord_vpn.txt 

---

_**Assistant**_

Let me analyze the openpyn-nordvpn codebase and compare it to our project:

1. Core Functionality:
- openpyn is a mature Python CLI tool specifically designed for managing NordVPN OpenVPN connections
- It has extensive features like:
  - Automatic server selection based on load/latency
  - Systemd service integration
  - Firewall/killswitch functionality 
  - DNS leak protection
  - Support for special server types (P2P, Netflix, etc.)
  - Desktop notifications
  - Detailed logging

2. Key Differences:
- openpyn is NordVPN-specific while our project aims to be provider-agnostic
- openpyn has more advanced features around server selection and management
- openpyn uses systemd for service management while we're aiming for a more portable approach
- openpyn has more complex firewall rule management
- openpyn is CLI-focused while we plan to have both CLI and GUI interfaces

3. Things We Could Learn From:
- Their approach to caching API responses (see api.py get_json_cached())
- The firewall management code could be useful reference
- Their systemd service management
- The way they handle configuration file updates
- Their approach to DNS leak protection

4. Areas Where We Could Improve:
- Make our solution provider-agnostic 
- Add a GUI interface
- Use modern Python features (they support Python 3.5+, we can target newer versions)
- Implement better error handling and recovery
- Add better logging and monitoring capabilities
- Make installation and updates more streamlined

5. Code Quality:
- openpyn's code is well-structured but could use modernization
- Some functions are quite long and could be broken down
- Error handling could be more consistent
- Documentation is decent but could be more comprehensive

Let me know if you'd like me to dive deeper into any of these aspects or explore other comparisons between the codebases.

Wait, but... we should also consider:

6. Security Considerations:
- openpyn handles credentials securely but stores them in plaintext
- Their firewall rules are comprehensive but could be more granular
- The DNS leak protection is good but could be enhanced

7. Performance:
- Their caching mechanism helps reduce API load
- Server selection could be parallelized for faster results
- Config file handling could be more efficient

Wait, but... looking at maintainability:

8. Maintainability & Testing:
- They have basic pytest setup but coverage could be better
- Code organization is logical but some modules are tightly coupled
- Dependencies are well-managed but could be updated
- Documentation could be more detailed for contributors

This analysis gives us good insights for developing our VPN solution while learning from both the strengths and areas for improvement in openpyn.

---

_**User**_

python -m openpyn -c pl
/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/_private/openpyn-nordvpn/openpyn/firewall.py:366: SyntaxWarning: invalid escape sequence '\.'
  "pattern": "^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$"
2025-02-23 05:59:13 [ERROR] Credentials not found: Please run 'sudo openpyn --init' first
2025-02-23 05:59:13 [CRITICAL] please run 'sudo openpyn --init' first. /Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/_private/openpyn-nordvpn/openpyn/files not found
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/_private/openpyn-nordvpn/openpyn/__main__.py", line 1395, in <module>
    sys.exit(main())
             ^^^^^^
  File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/_private/openpyn-nordvpn/openpyn/__main__.py", line 178, in main
    return_code = run(
                  ^^^^
  File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/_private/openpyn-nordvpn/openpyn/__main__.py", line 576, in run
    if (use_systemd_resolved or use_resolvconf) is False and skip_dns_patch is False and test is False:
        ^^^^^^^^^^^^^^^^^^^^
UnboundLocalError: cannot access local variable 'use_systemd_resolved' where it is not associated with a value



sudo python -m openpyn --init
Password:
Downloading ovpn.zip: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████| 33.5M/33.5M [00:02<00:00, 14.4MB/s]
Extracting ovpn.zip: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████| 41.6M/41.6M [00:03<00:00, 12.5MB/s]

2025-02-23 05:59:57 [INFO] Storing credentials in '/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/_private/openpyn-nordvpn/openpyn/credentials' with openvpn compatible 'auth-user-pass' file format
Enter your username for NordVPN, i.e youremail@yourmail.com: QPgGeGqEYQcNtqKwfV82De24
Enter the password for NordVPN: 
2025-02-23 06:00:19 [INFO] Awesome, the credentials have been saved in '/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/_private/openpyn-nordvpn/openpyn/credentials'



python -m openpyn -c pl
According to NordVPN, Least Busy 10 Servers in PL With 'Load' Less Than 70 Which Support OPENVPN-UDP Are: [['pl143', 6], ['pl125', 7], ['pl135', 7], ['pl133', 8], ['pl134', 8], ['pl139', 8], ['pl141', 8], ['pl144', 8], ['pl146', 8], ['pl153', 8]]
Sending Pings To Servers
Ping Response From pl143   min/avg/max/mdev = [18, 21, 26, 3] 
Ping Response From pl125   min/avg/max/mdev = [21, 24, 32, 4] 
Ping Response From pl135   min/avg/max/mdev = [18, 23, 33, 5] 
Ping Response From pl133   min/avg/max/mdev = [18, 19, 21, 1] 
Ping Response From pl134   min/avg/max/mdev = [19, 22, 25, 2] 
Ping Response From pl139   min/avg/max/mdev = [17, 25, 32, 5] 
Ping Response From pl141   min/avg/max/mdev = [19, 21, 25, 2] 
Ping Response From pl144   min/avg/max/mdev = [18, 19, 21, 1] 
Ping Response From pl146   min/avg/max/mdev = [18, 21, 22, 1] 
Ping Response From pl153   min/avg/max/mdev = [20, 26, 31, 4] 

Top 10 Servers with Best Ping Are: ['pl133', 'pl144', 'pl146', 'pl141', 'pl143', 'pl134', 'pl135', 'pl125', 'pl139', 'pl153']


Out of the Best Available Servers, Chose pl133
2025-02-23 06:00:45 [SUCCESS] CONNECTING TO SERVER pl133 ON PORT udp
2025-02-23 06:00:45 [WARNING] Your OS 'darwin' Does not have '/sbin/resolvconf'
2025-02-23 06:00:45 [NOTICE] Manually applying patch to tunnel DNS through the VPN tunnel by modifying '/etc/resolv.conf'
Changing DNS servers to NordVPN's DNS Servers
nameserver nordDNS1 = 103.86.99.100
nameserver nordDNS2 = 103.86.96.100
nameserver openDNS3 = 208.67.222.220
2025-02-23 06:00:45 DEPRECATED OPTION: --cipher set to 'AES-256-CBC' but missing in --data-ciphers (AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305). OpenVPN ignores --cipher for cipher negotiations. 
2025-02-23 06:00:45 WARNING: Using --management on a TCP port WITHOUT passwords is STRONGLY discouraged and considered insecure
2025-02-23 06:00:45 OpenVPN 2.6.13 x86_64-apple-darwin23.6.0 [SSL (OpenSSL)] [LZO] [LZ4] [PKCS11] [MH/RECVDA] [AEAD]
2025-02-23 06:00:45 library versions: OpenSSL 3.4.0 22 Oct 2024, LZO 2.10
2025-02-23 06:00:45 MANAGEMENT: TCP Socket listening on [AF_INET]127.0.0.1:7015
2025-02-23 06:00:45 WARNING: --ping should normally be used with --ping-restart or --ping-exit
2025-02-23 06:00:45 TCP/UDP: Preserving recently used remote address: [AF_INET]84.17.55.82:1194
2025-02-23 06:00:45 Socket Buffers: R=[786896->786896] S=[9216->9216]
2025-02-23 06:00:45 UDPv4 link local: (not bound)
2025-02-23 06:00:45 UDPv4 link remote: [AF_INET]84.17.55.82:1194
2025-02-23 06:00:45 TLS: Initial packet from [AF_INET]84.17.55.82:1194, sid=a90b7558 d265524c
2025-02-23 06:00:45 WARNING: this configuration may cache passwords in memory -- use the auth-nocache option to prevent this
2025-02-23 06:00:46 VERIFY OK: depth=2, C=PA, O=NordVPN, CN=NordVPN Root CA
2025-02-23 06:00:46 VERIFY OK: depth=1, O=NordVPN, CN=NordVPN CA10
2025-02-23 06:00:46 VERIFY KU OK
2025-02-23 06:00:46 Validating certificate extended key usage
2025-02-23 06:00:46 ++ Certificate has EKU (str) TLS Web Server Authentication, expects TLS Web Server Authentication
2025-02-23 06:00:46 VERIFY EKU OK
2025-02-23 06:00:46 VERIFY X509NAME OK: CN=pl133.nordvpn.com
2025-02-23 06:00:46 VERIFY OK: depth=0, CN=pl133.nordvpn.com
2025-02-23 06:00:46 Control Channel: TLSv1.3, cipher TLSv1.3 TLS_AES_256_GCM_SHA384, peer certificate: 4096 bits RSA, signature: RSA-SHA512, peer temporary key: 253 bits X25519
2025-02-23 06:00:46 [pl133.nordvpn.com] Peer Connection Initiated with [AF_INET]84.17.55.82:1194
2025-02-23 06:00:46 TLS: move_session: dest=TM_ACTIVE src=TM_INITIAL reinit_src=1
2025-02-23 06:00:46 TLS: tls_multi_process: initial untrusted session promoted to trusted
2025-02-23 06:00:47 SENT CONTROL [pl133.nordvpn.com]: 'PUSH_REQUEST' (status=1)
2025-02-23 06:00:47 PUSH: Received control message: 'PUSH_REPLY,redirect-gateway def1,dhcp-option DNS 103.86.96.100,dhcp-option DNS 103.86.99.100,explicit-exit-notify,comp-lzo no,route-gateway 10.100.0.1,topology subnet,ping 60,ping-restart 180,ifconfig 10.100.0.2 255.255.0.0,peer-id 8,cipher AES-256-GCM'
2025-02-23 06:00:47 WARNING: You have specified redirect-gateway and redirect-private at the same time (or the same option multiple times). This is not well supported and may lead to unexpected results
2025-02-23 06:00:47 OPTIONS IMPORT: --ifconfig/up options modified
2025-02-23 06:00:47 OPTIONS IMPORT: route options modified
2025-02-23 06:00:47 OPTIONS IMPORT: route-related options modified
2025-02-23 06:00:47 OPTIONS IMPORT: --ip-win32 and/or --dhcp-option options modified
2025-02-23 06:00:47 Opened utun device utun4
2025-02-23 06:00:47 /sbin/ifconfig utun4 delete
ifconfig: ioctl (SIOCDIFADDR): Can't assign requested address
2025-02-23 06:00:47 NOTE: Tried to delete pre-existing tun/tap instance -- No Problem if failure
2025-02-23 06:00:47 /sbin/ifconfig utun4 10.100.0.2 10.100.0.2 netmask 255.255.0.0 mtu 1500 up
2025-02-23 06:00:47 /sbin/route add -net 10.100.0.0 10.100.0.2 255.255.0.0
add net 10.100.0.0: gateway 10.100.0.2
2025-02-23 06:00:47 /sbin/route add -net 84.17.55.82 192.168.0.1 255.255.255.255
add net 84.17.55.82: gateway 192.168.0.1
2025-02-23 06:00:47 /sbin/route add -net 0.0.0.0 10.100.0.1 128.0.0.0
add net 0.0.0.0: gateway 10.100.0.1
2025-02-23 06:00:47 /sbin/route add -net 128.0.0.0 10.100.0.1 128.0.0.0
add net 128.0.0.0: gateway 10.100.0.1
2025-02-23 06:00:47 Initialization Sequence Completed
2025-02-23 06:00:47 Data Channel: cipher 'AES-256-GCM', peer-id: 8, compression: 'stub'
2025-02-23 06:00:47 Timers: ping 60, ping-restart 180
2025-02-23 06:00:47 Protocol options: explicit-exit-notify 1


{HANGS...}





sudo nyord-vpn go pl


sudo nyord-vpn go pl --verbose
[02/23/25 06:01:59] DEBUG    2025-02-23 06:01:59.716 | DEBUG    | nyord_vpn.client:status:377 - Current IP: 89.64.28.48                                  client.py:377
2025-02-23 06:01:59.716 | DEBUG    | nyord_vpn.client:status:377 - Current IP: 89.64.28.48
2025-02-23 06:01:59.716 | DEBUG    | nyord_vpn.client:status:377 - Current IP: 89.64.28.48
                    DEBUG    2025-02-23 06:01:59.723 | DEBUG    | nyord_vpn.client:status:384 - Initial IP: None                                         client.py:384
2025-02-23 06:01:59.723 | DEBUG    | nyord_vpn.client:status:384 - Initial IP: None
2025-02-23 06:01:59.723 | DEBUG    | nyord_vpn.client:status:384 - Initial IP: None
                    DEBUG    2025-02-23 06:01:59.725 | DEBUG    | nyord_vpn.client:status:385 - Connected IP: None                                       client.py:385
2025-02-23 06:01:59.725 | DEBUG    | nyord_vpn.client:status:385 - Connected IP: None
2025-02-23 06:01:59.725 | DEBUG    | nyord_vpn.client:status:385 - Connected IP: None
                    DEBUG    2025-02-23 06:01:59.811 | DEBUG    | nyord_vpn.client:status:394 - OpenVPN running: False                                   client.py:394
2025-02-23 06:01:59.811 | DEBUG    | nyord_vpn.client:status:394 - OpenVPN running: False
2025-02-23 06:01:59.811 | DEBUG    | nyord_vpn.client:status:394 - OpenVPN running: False
                    INFO     2025-02-23 06:01:59.952 | INFO     | nyord_vpn.client:go:560 - Ensuring no existing VPN connection...                       client.py:560
2025-02-23 06:01:59.952 | INFO     | nyord_vpn.client:go:560 - Ensuring no existing VPN connection...
2025-02-23 06:01:59.952 | INFO     | nyord_vpn.client:go:560 - Ensuring no existing VPN connection...
Disconnected from VPN
[02/23/25 06:02:04] INFO     2025-02-23 06:02:04.271 | INFO     | nyord_vpn.client:go:582 - Normal IP: 89.64.28.48                                       client.py:582
2025-02-23 06:02:04.271 | INFO     | nyord_vpn.client:go:582 - Normal IP: 89.64.28.48
2025-02-23 06:02:04.271 | INFO     | nyord_vpn.client:go:582 - Normal IP: 89.64.28.48
                    INFO     2025-02-23 06:02:04.274 | INFO     | nyord_vpn.client:go:593 - Connecting to Poland                                         client.py:593
2025-02-23 06:02:04.274 | INFO     | nyord_vpn.client:go:593 - Connecting to Poland
2025-02-23 06:02:04.274 | INFO     | nyord_vpn.client:go:593 - Connecting to Poland
  Available servers in pl   
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━┓
┃ Server            ┃ Load ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━┩
│ pl171.nordvpn.com │   5% │
│ pl143.nordvpn.com │   6% │
│ pl154.nordvpn.com │   7% │
│ pl146.nordvpn.com │   7% │
│ pl156.nordvpn.com │   8% │
└───────────────────┴──────┘
                    INFO     2025-02-23 06:02:04.584 | INFO     | nyord_vpn.client:go:605 - Selected server: pl171.nordvpn.com                           client.py:605
2025-02-23 06:02:04.584 | INFO     | nyord_vpn.client:go:605 - Selected server: pl171.nordvpn.com
2025-02-23 06:02:04.584 | INFO     | nyord_vpn.client:go:605 - Selected server: pl171.nordvpn.com
                    DEBUG    2025-02-23 06:02:04.586 | DEBUG    | nyord_vpn.client:go:642 - Running command: sudo openvpn --config                       client.py:642
                             /Users/adam/Library/Caches/nyord-vpn/openvpn.ovpn --auth-user-pass /Users/adam/Library/Caches/nyord-vpn/openvpn.auth                     
                             --daemon --verb 3 --connect-retry 2 --connect-timeout 30 --resolv-retry infinite --log                                                   
                             /Users/adam/Library/Caches/nyord-vpn/openvpn.log --ping 10 --ping-restart 60 --persist-tun --persist-key                                 
2025-02-23 06:02:04.586 | DEBUG    | nyord_vpn.client:go:642 - Running command: sudo openvpn --config /Users/adam/Library/Caches/nyord-vpn/openvpn.ovpn --auth-user-pass /Users/adam/Library/Caches/nyord-vpn/openvpn.auth --daemon --verb 3 --connect-retry 2 --connect-timeout 30 --resolv-retry infinite --log /Users/adam/Library/Caches/nyord-vpn/openvpn.log --ping 10 --ping-restart 60 --persist-tun --persist-key
2025-02-23 06:02:04.586 | DEBUG    | nyord_vpn.client:go:642 - Running command: sudo openvpn --config /Users/adam/Library/Caches/nyord-vpn/openvpn.ovpn --auth-user-pass /Users/adam/Library/Caches/nyord-vpn/openvpn.auth --daemon --verb 3 --connect-retry 2 --connect-timeout 30 --resolv-retry infinite --log /Users/adam/Library/Caches/nyord-vpn/openvpn.log --ping 10 --ping-restart 60 --persist-tun --persist-key
⠹ Connecting...                    DEBUG    2025-02-23 06:02:04.872 | DEBUG    | nyord_vpn.client:status:377 - Current IP: 89.64.28.48                                  client.py:377
2025-02-23 06:02:04.872 | DEBUG    | nyord_vpn.client:status:377 - Current IP: 89.64.28.48
2025-02-23 06:02:04.872 | DEBUG    | nyord_vpn.client:status:377 - Current IP: 89.64.28.48
                    DEBUG    2025-02-23 06:02:04.876 | DEBUG    | nyord_vpn.client:status:384 - Initial IP: 89.64.28.48                                  client.py:384
2025-02-23 06:02:04.876 | DEBUG    | nyord_vpn.client:status:384 - Initial IP: 89.64.28.48
2025-02-23 06:02:04.876 | DEBUG    | nyord_vpn.client:status:384 - Initial IP: 89.64.28.48
                    DEBUG    2025-02-23 06:02:04.878 | DEBUG    | nyord_vpn.client:status:385 - Connected IP: None                                       client.py:385
2025-02-23 06:02:04.878 | DEBUG    | nyord_vpn.client:status:385 - Connected IP: None
2025-02-23 06:02:04.878 | DEBUG    | nyord_vpn.client:status:385 - Connected IP: None
                    DEBUG    2025-02-23 06:02:04.933 | DEBUG    | nyord_vpn.client:status:394 - OpenVPN running: True                                    client.py:394
2025-02-23 06:02:04.933 | DEBUG    | nyord_vpn.client:status:394 - OpenVPN running: True
2025-02-23 06:02:04.933 | DEBUG    | nyord_vpn.client:status:394 - OpenVPN running: True
⠦ Waiting for VPN connection...[02/23/25 06:02:07] DEBUG    2025-02-23 06:02:07.613 | DEBUG    | nyord_vpn.client:status:377 - Current IP: 95.214.217.199                               client.py:377
2025-02-23 06:02:07.613 | DEBUG    | nyord_vpn.client:status:377 - Current IP: 95.214.217.199
2025-02-23 06:02:07.613 | DEBUG    | nyord_vpn.client:status:377 - Current IP: 95.214.217.199
                    DEBUG    2025-02-23 06:02:07.615 | DEBUG    | nyord_vpn.client:status:384 - Initial IP: 89.64.28.48                                  client.py:384
2025-02-23 06:02:07.615 | DEBUG    | nyord_vpn.client:status:384 - Initial IP: 89.64.28.48
2025-02-23 06:02:07.615 | DEBUG    | nyord_vpn.client:status:384 - Initial IP: 89.64.28.48
                    DEBUG    2025-02-23 06:02:07.617 | DEBUG    | nyord_vpn.client:status:385 - Connected IP: None                                       client.py:385
2025-02-23 06:02:07.617 | DEBUG    | nyord_vpn.client:status:385 - Connected IP: None
2025-02-23 06:02:07.617 | DEBUG    | nyord_vpn.client:status:385 - Connected IP: None
⠧ Waiting for VPN connection...                    DEBUG    2025-02-23 06:02:07.671 | DEBUG    | nyord_vpn.client:status:394 - OpenVPN running: True                                    client.py:394
2025-02-23 06:02:07.671 | DEBUG    | nyord_vpn.client:status:394 - OpenVPN running: True
2025-02-23 06:02:07.671 | DEBUG    | nyord_vpn.client:status:394 - OpenVPN running: True
⠋ Waiting for VPN connection...                    INFO     2025-02-23 06:02:07.875 | INFO     | nyord_vpn.client:go:701 - Successfully connected to Poland                             client.py:701
2025-02-23 06:02:07.875 | INFO     | nyord_vpn.client:go:701 - Successfully connected to Poland
2025-02-23 06:02:07.875 | INFO     | nyord_vpn.client:go:701 - Successfully connected to Poland
                    INFO     2025-02-23 06:02:07.877 | INFO     | nyord_vpn.client:go:704 - Private IP: 95.214.217.199                                   client.py:704
2025-02-23 06:02:07.877 | INFO     | nyord_vpn.client:go:704 - Private IP: 95.214.217.199
2025-02-23 06:02:07.877 | INFO     | nyord_vpn.client:go:704 - Private IP: 95.214.217.199
⠋ Waiting for VPN connection...

---

_**Assistant**_



---



---

