## SpecStory

## VPN Connection Troubleshooting and Improvements (24/02/2025, 07:15:13)

_**User**_

sudo -E nyord-vpn go de --verbose

[02/24/25 07:13:59] DEBUG    2025-02-24 07:13:59.327 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:156 - Found OpenVPN at                   vpn.py:156
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 07:13:59.334 | DEBUG    | nyord_vpn.network.vpn:status:894 - Connection status: process=False, initialized=False    vpn.py:894
                    DEBUG    2025-02-24 07:13:59.339 | DEBUG    | nyord_vpn.network.server:get_servers_cache:289 - Using cached server list with 100     server.py:289
                             valid servers                                                                                                                            
                    DEBUG    2025-02-24 07:13:59.342 | DEBUG    | nyord_vpn.network.server:get_servers_cache:289 - Using cached server list with 100     server.py:289
                             valid servers                                                                                                                            
                    INFO     2025-02-24 07:13:59.344 | INFO     | nyord_vpn.core.client:go:275 - Selected server: de655.nordvpn.com                      client.py:275
                    DEBUG    2025-02-24 07:13:59.557 | DEBUG    | nyord_vpn.network.vpn:_invalidate_ip_cache:979 - IP cache invalidated                     vpn.py:979
                    INFO     2025-02-24 07:13:59.560 | INFO     | nyord_vpn.network.vpn:disconnect:760 - Disconnected from VPN                              vpn.py:760
                    DEBUG    2025-02-24 07:13:59.562 | DEBUG    | nyord_vpn.network.vpn:connect:421 - Connecting to de655.nordvpn.com                       vpn.py:421
                    DEBUG    2025-02-24 07:13:59.563 | DEBUG    | nyord_vpn.utils.templates:log_debug:50 - Looking for config file at:                 templates.py:50
                             /Users/adam/.cache/nyord-vpn/configs/de655.nordvpn.com.tcp.ovpn                                                                          
                    DEBUG    2025-02-24 07:13:59.565 | DEBUG    | nyord_vpn.network.vpn:connect:432 - OpenVPN config for de655.nordvpn.com:                 vpn.py:432
                    DEBUG    2025-02-24 07:13:59.566 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   client                                              vpn.py:435
                    DEBUG    2025-02-24 07:13:59.568 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   dev tun                                             vpn.py:435
                    DEBUG    2025-02-24 07:13:59.569 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   proto tcp                                           vpn.py:435
                    DEBUG    2025-02-24 07:13:59.570 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote 194.31.54.4 443                              vpn.py:435
                    DEBUG    2025-02-24 07:13:59.572 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   resolv-retry infinite                               vpn.py:435
                    DEBUG    2025-02-24 07:13:59.573 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote-random                                       vpn.py:435
                    DEBUG    2025-02-24 07:13:59.574 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   nobind                                              vpn.py:435
                    DEBUG    2025-02-24 07:13:59.576 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   tun-mtu 1500                                        vpn.py:435
                    DEBUG    2025-02-24 07:13:59.577 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   tun-mtu-extra 32                                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.578 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   mssfix 1450                                         vpn.py:435
                    DEBUG    2025-02-24 07:13:59.579 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   persist-key                                         vpn.py:435
                    DEBUG    2025-02-24 07:13:59.581 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   persist-tun                                         vpn.py:435
                    DEBUG    2025-02-24 07:13:59.582 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping 15                                             vpn.py:435
                    DEBUG    2025-02-24 07:13:59.583 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping-restart 0                                      vpn.py:435
                    DEBUG    2025-02-24 07:13:59.585 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping-timer-rem                                      vpn.py:435
                    DEBUG    2025-02-24 07:13:59.586 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   reneg-sec 0                                         vpn.py:435
                    DEBUG    2025-02-24 07:13:59.587 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   comp-lzo no                                         vpn.py:435
                    DEBUG    2025-02-24 07:13:59.588 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   verify-x509-name CN=de655.nordvpn.com               vpn.py:435
                    DEBUG    2025-02-24 07:13:59.590 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                    DEBUG    2025-02-24 07:13:59.591 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote-cert-tls server                              vpn.py:435
                    DEBUG    2025-02-24 07:13:59.592 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                    DEBUG    2025-02-24 07:13:59.593 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   auth-user-pass                                      vpn.py:435
                    DEBUG    2025-02-24 07:13:59.595 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   verb 3                                              vpn.py:435
                    DEBUG    2025-02-24 07:13:59.596 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   pull                                                vpn.py:435
                    DEBUG    2025-02-24 07:13:59.597 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   fast-io                                             vpn.py:435
                    DEBUG    2025-02-24 07:13:59.598 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   cipher AES-256-CBC                                  vpn.py:435
                    DEBUG    2025-02-24 07:13:59.600 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   auth SHA512                                         vpn.py:435
                    DEBUG    2025-02-24 07:13:59.601 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   <ca>                                                vpn.py:435
                    DEBUG    2025-02-24 07:13:59.602 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----BEGIN CERTIFICATE-----                         vpn.py:435
                    DEBUG    2025-02-24 07:13:59.604 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MIIFCjCCAvKgAwIBAgIBATANBgkqhkiG9w0BAQ0FADA5MQswCQYDVQQGEwJQQTEQ                                                                         
                    DEBUG    2025-02-24 07:13:59.605 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MA4GA1UEChMHTm9yZFZQTjEYMBYGA1UEAxMPTm9yZFZQTiBSb290IENBMB4XDTE2                                                                         
                    DEBUG    2025-02-24 07:13:59.606 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MDEwMTAwMDAwMFoXDTM1MTIzMTIzNTk1OVowOTELMAkGA1UEBhMCUEExEDAOBgNV                                                                         
                    DEBUG    2025-02-24 07:13:59.608 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             BAoTB05vcmRWUE4xGDAWBgNVBAMTD05vcmRWUE4gUm9vdCBDQTCCAiIwDQYJKoZI                                                                         
                    DEBUG    2025-02-24 07:13:59.609 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             hvcNAQEBBQADggIPADCCAgoCggIBAMkr/BYhyo0F2upsIMXwC6QvkZps3NN2/eQF                                                                         
                    DEBUG    2025-02-24 07:13:59.610 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             kfQIS1gql0aejsKsEnmY0Kaon8uZCTXPsRH1gQNgg5D2gixdd1mJUvV3dE3y9FJr                                                                         
                    DEBUG    2025-02-24 07:13:59.612 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             XMoDkXdCGBodvKJyU6lcfEVF6/UxHcbBguZK9UtRHS9eJYm3rpL/5huQMCppX7kU                                                                         
                    DEBUG    2025-02-24 07:13:59.614 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             eQ8dpCwd3iKITqwd1ZudDqsWaU0vqzC2H55IyaZ/5/TnCk31Q1UP6BksbbuRcwOV                                                                         
                    DEBUG    2025-02-24 07:13:59.615 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             skEDsm6YoWDnn/IIzGOYnFJRzQH5jTz3j1QBvRIuQuBuvUkfhx1FEwhwZigrcxXu                                                                         
                    DEBUG    2025-02-24 07:13:59.617 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MP+QgM54kezgziJUaZcOM2zF3lvrwMvXDMfNeIoJABv9ljw969xQ8czQCU5lMVmA                                                                         
                    DEBUG    2025-02-24 07:13:59.619 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             37ltv5Ec9U5hZuwk/9QO1Z+d/r6Jx0mlurS8gnCAKJgwa3kyZw6e4FZ8mYL4vpRR                                                                         
                    DEBUG    2025-02-24 07:13:59.621 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             hPdvRTWCMJkeB4yBHyhxUmTRgJHm6YR3D6hcFAc9cQcTEl/I60tMdz33G6m0O42s                                                                         
                    DEBUG    2025-02-24 07:13:59.622 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             Qt/+AR3YCY/RusWVBJB/qNS94EtNtj8iaebCQW1jHAhvGmFILVR9lzD0EzWKHkvy                                                                         
                    DEBUG    2025-02-24 07:13:59.624 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             WEjmUVRgCDd6Ne3eFRNS73gdv/C3l5boYySeu4exkEYVxVRn8DhCxs0MnkMHWFK6                                                                         
                    DEBUG    2025-02-24 07:13:59.625 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MyzXCCn+JnWFDYPfDKHvpff/kLDobtPBf+Lbch5wQy9quY27xaj0XwLyjOltpiST                                                                         
                    DEBUG    2025-02-24 07:13:59.627 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             LWae/Q4vAgMBAAGjHTAbMAwGA1UdEwQFMAMBAf8wCwYDVR0PBAQDAgEGMA0GCSqG                                                                         
                    DEBUG    2025-02-24 07:13:59.628 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             SIb3DQEBDQUAA4ICAQC9fUL2sZPxIN2mD32VeNySTgZlCEdVmlq471o/bDMP4B8g                                                                         
                    DEBUG    2025-02-24 07:13:59.630 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             nQesFRtXY2ZCjs50Jm73B2LViL9qlREmI6vE5IC8IsRBJSV4ce1WYxyXro5rmVg/                                                                         
                    DEBUG    2025-02-24 07:13:59.632 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             k6a10rlsbK/eg//GHoJxDdXDOokLUSnxt7gk3QKpX6eCdh67p0PuWm/7WUJQxH2S                                                                         
                    DEBUG    2025-02-24 07:13:59.633 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             DxsT9vB/iZriTIEe/ILoOQF0Aqp7AgNCcLcLAmbxXQkXYCCSB35Vp06u+eTWjG0/                                                                         
                    DEBUG    2025-02-24 07:13:59.634 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             pyS5V14stGtw+fA0DJp5ZJV4eqJ5LqxMlYvEZ/qKTEdoCeaXv2QEmN6dVqjDoTAo                                                                         
                    DEBUG    2025-02-24 07:13:59.636 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             k0t5u4YRXzEVCfXAC3ocplNdtCA72wjFJcSbfif4BSC8bDACTXtnPC7nD0VndZLp                                                                         
                    DEBUG    2025-02-24 07:13:59.638 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             +RiNLeiENhk0oTC+UVdSc+n2nJOzkCK0vYu0Ads4JGIB7g8IB3z2t9ICmsWrgnhd                                                                         
                    DEBUG    2025-02-24 07:13:59.639 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             NdcOe15BincrGA8avQ1cWXsfIKEjbrnEuEk9b5jel6NfHtPKoHc9mDpRdNPISeVa                                                                         
                    DEBUG    2025-02-24 07:13:59.641 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             wDBM1mJChneHt59Nh8Gah74+TM1jBsw4fhJPvoc7Atcg740JErb904mZfkIEmojC                                                                         
                    DEBUG    2025-02-24 07:13:59.642 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             VPhBHVQ9LHBAdM8qFI2kRK0IynOmAZhexlP/aT/kpEsEPyaZQlnBn3An1CRz8h0S                                                                         
                    DEBUG    2025-02-24 07:13:59.644 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             PApL8PytggYKeQmRhl499+6jLxcZ2IegLfqq41dzIjwHwTMplg+1pKIOVojpWA==                                                                         
                    DEBUG    2025-02-24 07:13:59.646 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----END CERTIFICATE-----                           vpn.py:435
                    DEBUG    2025-02-24 07:13:59.647 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   </ca>                                               vpn.py:435
                    DEBUG    2025-02-24 07:13:59.649 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   key-direction 1                                     vpn.py:435
                    DEBUG    2025-02-24 07:13:59.650 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   <tls-auth>                                          vpn.py:435
                    DEBUG    2025-02-24 07:13:59.651 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----BEGIN OpenVPN Static key V1-----               vpn.py:435
                    DEBUG    2025-02-24 07:13:59.653 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   e685bdaf659a25a200e2b9e39e51ff03                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.654 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   0fc72cf1ce07232bd8b2be5e6c670143                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.655 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   f51e937e670eee09d4f2ea5a6e4e6996                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.658 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   5db852c275351b86fc4ca892d78ae002                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.661 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   d6f70d029bd79c4d1c26cf14e9588033                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.664 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   cf639f8a74809f29f72b9d58f9b8f5fe                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.666 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   fc7938eade40e9fed6cb92184abb2cc1                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.668 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   0eb1a296df243b251df0643d53724cdb                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.669 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   5a92a1d6cb817804c4a9319b57d53be5                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.671 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   80815bcfcb2df55018cc83fc43bc7ff8                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.672 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   2d51f9b88364776ee9d12fc85cc7ea5b                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.673 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   9741c4f598c485316db066d52db4540e                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.675 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   212e1518a9bd4828219e24b20d88f598                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.676 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   a196c9de96012090e333519ae18d3509                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.677 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   9427e7b372d348d352dc4c85e18cd4b9                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.679 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   3f8a56ddb2e64eb67adfc9b337157ff4                    vpn.py:435
                    DEBUG    2025-02-24 07:13:59.680 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----END OpenVPN Static key V1-----                 vpn.py:435
                    DEBUG    2025-02-24 07:13:59.681 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   </tls-auth>                                         vpn.py:435
                    DEBUG    2025-02-24 07:13:59.683 | DEBUG    | nyord_vpn.network.vpn:connect:449 - Auth file exists and has correct format               vpn.py:449
                    DEBUG    2025-02-24 07:13:59.685 | DEBUG    | nyord_vpn.network.vpn:connect:464 - Running OpenVPN command:                              vpn.py:464
                    DEBUG    2025-02-24 07:13:59.687 | DEBUG    | nyord_vpn.network.vpn:connect:465 - openvpn --config                                      vpn.py:465
                             /Users/adam/.cache/nyord-vpn/configs/de655.nordvpn.com.tcp.ovpn --auth-user-pass /Users/adam/.cache/nyord-vpn/openvpn.auth               
                             --verb 5 --connect-retry 2 --connect-timeout 10 --resolv-retry infinite --ping 10 --ping-restart 60 --script-security 2                  
                             --persist-tun --persist-key --nobind --fast-io --data-ciphers AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305:AES-256-CBC                      
                             --data-ciphers-fallback AES-256-CBC --auth-retry nointeract --auth-nocache --pull-filter ignore auth-token --tls-version-min             
                             1.2 --tls-cipher TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384:TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256 --redirect-gateway def1                     
                             --dhcp-option DNS 103.86.96.100 --dhcp-option DNS 103.86.99.100 --log /Users/adam/.cache/nyord-vpn/openvpn.log                           
[02/24/25 07:14:01] DEBUG    2025-02-24 07:14:01.324 | DEBUG    | nyord_vpn.network.vpn:connect:574 - Auth progress:                                        vpn.py:574
                    DEBUG    2025-02-24 07:14:01.327 | DEBUG    | nyord_vpn.network.vpn:connect:576 -   WRR2025-02-24 07:14:01 us=274529 AUTH: Received     vpn.py:576
                             control message: AUTH_FAILED                                                                                                             
Error: Failed to connect to VPN: Authentication failed - check your credentials



sudo -E nyord-vpn go fr --verbose

[02/24/25 07:14:20] DEBUG    2025-02-24 07:14:20.377 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:156 - Found OpenVPN at                   vpn.py:156
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 07:14:20.383 | DEBUG    | nyord_vpn.network.vpn:status:894 - Connection status: process=False, initialized=False    vpn.py:894
                    DEBUG    2025-02-24 07:14:20.387 | DEBUG    | nyord_vpn.network.server:get_servers_cache:289 - Using cached server list with 100     server.py:289
                             valid servers                                                                                                                            
                    DEBUG    2025-02-24 07:14:20.390 | DEBUG    | nyord_vpn.network.server:get_servers_cache:289 - Using cached server list with 100     server.py:289
                             valid servers                                                                                                                            
                    INFO     2025-02-24 07:14:20.391 | INFO     | nyord_vpn.core.client:go:275 - Selected server: fr439.nordvpn.com                      client.py:275
                    DEBUG    2025-02-24 07:14:20.605 | DEBUG    | nyord_vpn.network.vpn:disconnect:736 - Cleaned up OpenVPN log file                        vpn.py:736
                    DEBUG    2025-02-24 07:14:20.606 | DEBUG    | nyord_vpn.network.vpn:_invalidate_ip_cache:979 - IP cache invalidated                     vpn.py:979
                    INFO     2025-02-24 07:14:20.609 | INFO     | nyord_vpn.network.vpn:disconnect:760 - Disconnected from VPN                              vpn.py:760
                    DEBUG    2025-02-24 07:14:20.610 | DEBUG    | nyord_vpn.network.vpn:connect:421 - Connecting to fr439.nordvpn.com                       vpn.py:421
                    DEBUG    2025-02-24 07:14:20.612 | DEBUG    | nyord_vpn.utils.templates:log_debug:50 - Looking for config file at:                 templates.py:50
                             /Users/adam/.cache/nyord-vpn/configs/fr439.nordvpn.com.tcp.ovpn                                                                          
                    DEBUG    2025-02-24 07:14:20.613 | DEBUG    | nyord_vpn.utils.templates:log_debug:50 - Fixed config file permissions for           templates.py:50
                             /Users/adam/.cache/nyord-vpn/configs/fr439.nordvpn.com.tcp.ovpn                                                                          
                    DEBUG    2025-02-24 07:14:20.616 | DEBUG    | nyord_vpn.network.vpn:connect:432 - OpenVPN config for fr439.nordvpn.com:                 vpn.py:432
                    DEBUG    2025-02-24 07:14:20.617 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   client                                              vpn.py:435
                    DEBUG    2025-02-24 07:14:20.618 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   dev tun                                             vpn.py:435
                    DEBUG    2025-02-24 07:14:20.620 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   proto tcp                                           vpn.py:435
                    DEBUG    2025-02-24 07:14:20.621 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote 185.93.2.199 443                             vpn.py:435
                    DEBUG    2025-02-24 07:14:20.622 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   resolv-retry infinite                               vpn.py:435
                    DEBUG    2025-02-24 07:14:20.624 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote-random                                       vpn.py:435
                    DEBUG    2025-02-24 07:14:20.625 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   nobind                                              vpn.py:435
                    DEBUG    2025-02-24 07:14:20.626 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   tun-mtu 1500                                        vpn.py:435
                    DEBUG    2025-02-24 07:14:20.627 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   tun-mtu-extra 32                                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.629 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   mssfix 1450                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:20.630 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   persist-key                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:20.631 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   persist-tun                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:20.633 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping 15                                             vpn.py:435
                    DEBUG    2025-02-24 07:14:20.634 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping-restart 0                                      vpn.py:435
                    DEBUG    2025-02-24 07:14:20.635 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping-timer-rem                                      vpn.py:435
                    DEBUG    2025-02-24 07:14:20.637 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   reneg-sec 0                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:20.638 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   comp-lzo no                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:20.639 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   verify-x509-name CN=fr439.nordvpn.com               vpn.py:435
                    DEBUG    2025-02-24 07:14:20.641 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                    DEBUG    2025-02-24 07:14:20.642 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote-cert-tls server                              vpn.py:435
                    DEBUG    2025-02-24 07:14:20.643 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                    DEBUG    2025-02-24 07:14:20.645 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   auth-user-pass                                      vpn.py:435
                    DEBUG    2025-02-24 07:14:20.646 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   verb 3                                              vpn.py:435
                    DEBUG    2025-02-24 07:14:20.647 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   pull                                                vpn.py:435
                    DEBUG    2025-02-24 07:14:20.648 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   fast-io                                             vpn.py:435
                    DEBUG    2025-02-24 07:14:20.649 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   cipher AES-256-CBC                                  vpn.py:435
                    DEBUG    2025-02-24 07:14:20.650 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   auth SHA512                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:20.652 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   <ca>                                                vpn.py:435
                    DEBUG    2025-02-24 07:14:20.654 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----BEGIN CERTIFICATE-----                         vpn.py:435
                    DEBUG    2025-02-24 07:14:20.655 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MIIFCjCCAvKgAwIBAgIBATANBgkqhkiG9w0BAQ0FADA5MQswCQYDVQQGEwJQQTEQ                                                                         
                    DEBUG    2025-02-24 07:14:20.656 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MA4GA1UEChMHTm9yZFZQTjEYMBYGA1UEAxMPTm9yZFZQTiBSb290IENBMB4XDTE2                                                                         
                    DEBUG    2025-02-24 07:14:20.658 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MDEwMTAwMDAwMFoXDTM1MTIzMTIzNTk1OVowOTELMAkGA1UEBhMCUEExEDAOBgNV                                                                         
                    DEBUG    2025-02-24 07:14:20.659 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             BAoTB05vcmRWUE4xGDAWBgNVBAMTD05vcmRWUE4gUm9vdCBDQTCCAiIwDQYJKoZI                                                                         
                    DEBUG    2025-02-24 07:14:20.661 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             hvcNAQEBBQADggIPADCCAgoCggIBAMkr/BYhyo0F2upsIMXwC6QvkZps3NN2/eQF                                                                         
                    DEBUG    2025-02-24 07:14:20.662 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             kfQIS1gql0aejsKsEnmY0Kaon8uZCTXPsRH1gQNgg5D2gixdd1mJUvV3dE3y9FJr                                                                         
                    DEBUG    2025-02-24 07:14:20.664 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             XMoDkXdCGBodvKJyU6lcfEVF6/UxHcbBguZK9UtRHS9eJYm3rpL/5huQMCppX7kU                                                                         
                    DEBUG    2025-02-24 07:14:20.665 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             eQ8dpCwd3iKITqwd1ZudDqsWaU0vqzC2H55IyaZ/5/TnCk31Q1UP6BksbbuRcwOV                                                                         
                    DEBUG    2025-02-24 07:14:20.666 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             skEDsm6YoWDnn/IIzGOYnFJRzQH5jTz3j1QBvRIuQuBuvUkfhx1FEwhwZigrcxXu                                                                         
                    DEBUG    2025-02-24 07:14:20.668 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MP+QgM54kezgziJUaZcOM2zF3lvrwMvXDMfNeIoJABv9ljw969xQ8czQCU5lMVmA                                                                         
                    DEBUG    2025-02-24 07:14:20.669 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             37ltv5Ec9U5hZuwk/9QO1Z+d/r6Jx0mlurS8gnCAKJgwa3kyZw6e4FZ8mYL4vpRR                                                                         
                    DEBUG    2025-02-24 07:14:20.671 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             hPdvRTWCMJkeB4yBHyhxUmTRgJHm6YR3D6hcFAc9cQcTEl/I60tMdz33G6m0O42s                                                                         
                    DEBUG    2025-02-24 07:14:20.672 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             Qt/+AR3YCY/RusWVBJB/qNS94EtNtj8iaebCQW1jHAhvGmFILVR9lzD0EzWKHkvy                                                                         
                    DEBUG    2025-02-24 07:14:20.674 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             WEjmUVRgCDd6Ne3eFRNS73gdv/C3l5boYySeu4exkEYVxVRn8DhCxs0MnkMHWFK6                                                                         
                    DEBUG    2025-02-24 07:14:20.675 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MyzXCCn+JnWFDYPfDKHvpff/kLDobtPBf+Lbch5wQy9quY27xaj0XwLyjOltpiST                                                                         
                    DEBUG    2025-02-24 07:14:20.677 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             LWae/Q4vAgMBAAGjHTAbMAwGA1UdEwQFMAMBAf8wCwYDVR0PBAQDAgEGMA0GCSqG                                                                         
                    DEBUG    2025-02-24 07:14:20.678 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             SIb3DQEBDQUAA4ICAQC9fUL2sZPxIN2mD32VeNySTgZlCEdVmlq471o/bDMP4B8g                                                                         
                    DEBUG    2025-02-24 07:14:20.680 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             nQesFRtXY2ZCjs50Jm73B2LViL9qlREmI6vE5IC8IsRBJSV4ce1WYxyXro5rmVg/                                                                         
                    DEBUG    2025-02-24 07:14:20.681 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             k6a10rlsbK/eg//GHoJxDdXDOokLUSnxt7gk3QKpX6eCdh67p0PuWm/7WUJQxH2S                                                                         
                    DEBUG    2025-02-24 07:14:20.683 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             DxsT9vB/iZriTIEe/ILoOQF0Aqp7AgNCcLcLAmbxXQkXYCCSB35Vp06u+eTWjG0/                                                                         
                    DEBUG    2025-02-24 07:14:20.684 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             pyS5V14stGtw+fA0DJp5ZJV4eqJ5LqxMlYvEZ/qKTEdoCeaXv2QEmN6dVqjDoTAo                                                                         
                    DEBUG    2025-02-24 07:14:20.686 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             k0t5u4YRXzEVCfXAC3ocplNdtCA72wjFJcSbfif4BSC8bDACTXtnPC7nD0VndZLp                                                                         
                    DEBUG    2025-02-24 07:14:20.687 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             +RiNLeiENhk0oTC+UVdSc+n2nJOzkCK0vYu0Ads4JGIB7g8IB3z2t9ICmsWrgnhd                                                                         
                    DEBUG    2025-02-24 07:14:20.689 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             NdcOe15BincrGA8avQ1cWXsfIKEjbrnEuEk9b5jel6NfHtPKoHc9mDpRdNPISeVa                                                                         
                    DEBUG    2025-02-24 07:14:20.690 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             wDBM1mJChneHt59Nh8Gah74+TM1jBsw4fhJPvoc7Atcg740JErb904mZfkIEmojC                                                                         
                    DEBUG    2025-02-24 07:14:20.692 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             VPhBHVQ9LHBAdM8qFI2kRK0IynOmAZhexlP/aT/kpEsEPyaZQlnBn3An1CRz8h0S                                                                         
                    DEBUG    2025-02-24 07:14:20.693 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             PApL8PytggYKeQmRhl499+6jLxcZ2IegLfqq41dzIjwHwTMplg+1pKIOVojpWA==                                                                         
                    DEBUG    2025-02-24 07:14:20.695 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----END CERTIFICATE-----                           vpn.py:435
                    DEBUG    2025-02-24 07:14:20.696 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   </ca>                                               vpn.py:435
                    DEBUG    2025-02-24 07:14:20.697 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   key-direction 1                                     vpn.py:435
                    DEBUG    2025-02-24 07:14:20.699 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   <tls-auth>                                          vpn.py:435
                    DEBUG    2025-02-24 07:14:20.700 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----BEGIN OpenVPN Static key V1-----               vpn.py:435
                    DEBUG    2025-02-24 07:14:20.701 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   e685bdaf659a25a200e2b9e39e51ff03                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.703 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   0fc72cf1ce07232bd8b2be5e6c670143                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.704 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   f51e937e670eee09d4f2ea5a6e4e6996                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.705 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   5db852c275351b86fc4ca892d78ae002                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.707 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   d6f70d029bd79c4d1c26cf14e9588033                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.708 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   cf639f8a74809f29f72b9d58f9b8f5fe                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.709 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   fc7938eade40e9fed6cb92184abb2cc1                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.711 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   0eb1a296df243b251df0643d53724cdb                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.712 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   5a92a1d6cb817804c4a9319b57d53be5                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.713 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   80815bcfcb2df55018cc83fc43bc7ff8                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.715 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   2d51f9b88364776ee9d12fc85cc7ea5b                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.716 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   9741c4f598c485316db066d52db4540e                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.717 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   212e1518a9bd4828219e24b20d88f598                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.718 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   a196c9de96012090e333519ae18d3509                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.720 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   9427e7b372d348d352dc4c85e18cd4b9                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.721 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   3f8a56ddb2e64eb67adfc9b337157ff4                    vpn.py:435
                    DEBUG    2025-02-24 07:14:20.722 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----END OpenVPN Static key V1-----                 vpn.py:435
                    DEBUG    2025-02-24 07:14:20.724 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   </tls-auth>                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:20.725 | DEBUG    | nyord_vpn.network.vpn:connect:449 - Auth file exists and has correct format               vpn.py:449
                    DEBUG    2025-02-24 07:14:20.726 | DEBUG    | nyord_vpn.network.vpn:connect:464 - Running OpenVPN command:                              vpn.py:464
                    DEBUG    2025-02-24 07:14:20.727 | DEBUG    | nyord_vpn.network.vpn:connect:465 - openvpn --config                                      vpn.py:465
                             /Users/adam/.cache/nyord-vpn/configs/fr439.nordvpn.com.tcp.ovpn --auth-user-pass /Users/adam/.cache/nyord-vpn/openvpn.auth               
                             --verb 5 --connect-retry 2 --connect-timeout 10 --resolv-retry infinite --ping 10 --ping-restart 60 --script-security 2                  
                             --persist-tun --persist-key --nobind --fast-io --data-ciphers AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305:AES-256-CBC                      
                             --data-ciphers-fallback AES-256-CBC --auth-retry nointeract --auth-nocache --pull-filter ignore auth-token --tls-version-min             
                             1.2 --tls-cipher TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384:TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256 --redirect-gateway def1                     
                             --dhcp-option DNS 103.86.96.100 --dhcp-option DNS 103.86.99.100 --log /Users/adam/.cache/nyord-vpn/openvpn.log                           
[02/24/25 07:14:22] DEBUG    2025-02-24 07:14:22.470 | DEBUG    | nyord_vpn.network.vpn:connect:574 - Auth progress:                                        vpn.py:574
                    DEBUG    2025-02-24 07:14:22.473 | DEBUG    | nyord_vpn.network.vpn:connect:576 -   WRR2025-02-24 07:14:22 us=372430 AUTH: Received     vpn.py:576
                             control message: AUTH_FAILED                                                                                                             
Error: Failed to connect to VPN: Authentication failed - check your credentials



[02/24/25 07:14:35] DEBUG    2025-02-24 07:14:35.549 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:156 - Found OpenVPN at                   vpn.py:156
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 07:14:35.555 | DEBUG    | nyord_vpn.network.vpn:status:894 - Connection status: process=False, initialized=False    vpn.py:894
                    DEBUG    2025-02-24 07:14:35.559 | DEBUG    | nyord_vpn.network.server:get_servers_cache:289 - Using cached server list with 100     server.py:289
                             valid servers                                                                                                                            
                    DEBUG    2025-02-24 07:14:35.562 | DEBUG    | nyord_vpn.network.server:get_servers_cache:289 - Using cached server list with 100     server.py:289
                             valid servers                                                                                                                            
                    INFO     2025-02-24 07:14:35.564 | INFO     | nyord_vpn.core.client:go:275 - Selected server: pl122.nordvpn.com                      client.py:275
                    DEBUG    2025-02-24 07:14:35.763 | DEBUG    | nyord_vpn.network.vpn:disconnect:736 - Cleaned up OpenVPN log file                        vpn.py:736
                    DEBUG    2025-02-24 07:14:35.764 | DEBUG    | nyord_vpn.network.vpn:_invalidate_ip_cache:979 - IP cache invalidated                     vpn.py:979
                    INFO     2025-02-24 07:14:35.767 | INFO     | nyord_vpn.network.vpn:disconnect:760 - Disconnected from VPN                              vpn.py:760
                    DEBUG    2025-02-24 07:14:35.768 | DEBUG    | nyord_vpn.network.vpn:connect:421 - Connecting to pl122.nordvpn.com                       vpn.py:421
                    DEBUG    2025-02-24 07:14:35.770 | DEBUG    | nyord_vpn.utils.templates:log_debug:50 - Looking for config file at:                 templates.py:50
                             /Users/adam/.cache/nyord-vpn/configs/pl122.nordvpn.com.tcp.ovpn                                                                          
                    DEBUG    2025-02-24 07:14:35.772 | DEBUG    | nyord_vpn.network.vpn:connect:432 - OpenVPN config for pl122.nordvpn.com:                 vpn.py:432
                    DEBUG    2025-02-24 07:14:35.773 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   client                                              vpn.py:435
                    DEBUG    2025-02-24 07:14:35.775 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   dev tun                                             vpn.py:435
                    DEBUG    2025-02-24 07:14:35.776 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   proto tcp                                           vpn.py:435
                    DEBUG    2025-02-24 07:14:35.777 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote 37.120.211.171 443                           vpn.py:435
                    DEBUG    2025-02-24 07:14:35.779 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   resolv-retry infinite                               vpn.py:435
                    DEBUG    2025-02-24 07:14:35.780 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote-random                                       vpn.py:435
                    DEBUG    2025-02-24 07:14:35.781 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   nobind                                              vpn.py:435
                    DEBUG    2025-02-24 07:14:35.782 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   tun-mtu 1500                                        vpn.py:435
                    DEBUG    2025-02-24 07:14:35.784 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   tun-mtu-extra 32                                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.785 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   mssfix 1450                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:35.786 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   persist-key                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:35.787 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   persist-tun                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:35.789 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping 15                                             vpn.py:435
                    DEBUG    2025-02-24 07:14:35.790 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping-restart 0                                      vpn.py:435
                    DEBUG    2025-02-24 07:14:35.791 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping-timer-rem                                      vpn.py:435
                    DEBUG    2025-02-24 07:14:35.792 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   reneg-sec 0                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:35.793 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   comp-lzo no                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:35.794 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   verify-x509-name CN=pl122.nordvpn.com               vpn.py:435
                    DEBUG    2025-02-24 07:14:35.795 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                    DEBUG    2025-02-24 07:14:35.796 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote-cert-tls server                              vpn.py:435
                    DEBUG    2025-02-24 07:14:35.797 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                    DEBUG    2025-02-24 07:14:35.799 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   auth-user-pass                                      vpn.py:435
                    DEBUG    2025-02-24 07:14:35.800 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   verb 3                                              vpn.py:435
                    DEBUG    2025-02-24 07:14:35.801 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   pull                                                vpn.py:435
                    DEBUG    2025-02-24 07:14:35.802 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   fast-io                                             vpn.py:435
                    DEBUG    2025-02-24 07:14:35.803 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   cipher AES-256-CBC                                  vpn.py:435
                    DEBUG    2025-02-24 07:14:35.804 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   auth SHA512                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:35.805 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   <ca>                                                vpn.py:435
                    DEBUG    2025-02-24 07:14:35.806 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----BEGIN CERTIFICATE-----                         vpn.py:435
                    DEBUG    2025-02-24 07:14:35.807 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MIIFCjCCAvKgAwIBAgIBATANBgkqhkiG9w0BAQ0FADA5MQswCQYDVQQGEwJQQTEQ                                                                         
                    DEBUG    2025-02-24 07:14:35.809 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MA4GA1UEChMHTm9yZFZQTjEYMBYGA1UEAxMPTm9yZFZQTiBSb290IENBMB4XDTE2                                                                         
                    DEBUG    2025-02-24 07:14:35.811 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MDEwMTAwMDAwMFoXDTM1MTIzMTIzNTk1OVowOTELMAkGA1UEBhMCUEExEDAOBgNV                                                                         
                    DEBUG    2025-02-24 07:14:35.812 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             BAoTB05vcmRWUE4xGDAWBgNVBAMTD05vcmRWUE4gUm9vdCBDQTCCAiIwDQYJKoZI                                                                         
                    DEBUG    2025-02-24 07:14:35.813 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             hvcNAQEBBQADggIPADCCAgoCggIBAMkr/BYhyo0F2upsIMXwC6QvkZps3NN2/eQF                                                                         
                    DEBUG    2025-02-24 07:14:35.814 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             kfQIS1gql0aejsKsEnmY0Kaon8uZCTXPsRH1gQNgg5D2gixdd1mJUvV3dE3y9FJr                                                                         
                    DEBUG    2025-02-24 07:14:35.816 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             XMoDkXdCGBodvKJyU6lcfEVF6/UxHcbBguZK9UtRHS9eJYm3rpL/5huQMCppX7kU                                                                         
                    DEBUG    2025-02-24 07:14:35.818 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             eQ8dpCwd3iKITqwd1ZudDqsWaU0vqzC2H55IyaZ/5/TnCk31Q1UP6BksbbuRcwOV                                                                         
                    DEBUG    2025-02-24 07:14:35.820 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             skEDsm6YoWDnn/IIzGOYnFJRzQH5jTz3j1QBvRIuQuBuvUkfhx1FEwhwZigrcxXu                                                                         
                    DEBUG    2025-02-24 07:14:35.821 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MP+QgM54kezgziJUaZcOM2zF3lvrwMvXDMfNeIoJABv9ljw969xQ8czQCU5lMVmA                                                                         
                    DEBUG    2025-02-24 07:14:35.823 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             37ltv5Ec9U5hZuwk/9QO1Z+d/r6Jx0mlurS8gnCAKJgwa3kyZw6e4FZ8mYL4vpRR                                                                         
                    DEBUG    2025-02-24 07:14:35.824 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             hPdvRTWCMJkeB4yBHyhxUmTRgJHm6YR3D6hcFAc9cQcTEl/I60tMdz33G6m0O42s                                                                         
                    DEBUG    2025-02-24 07:14:35.826 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             Qt/+AR3YCY/RusWVBJB/qNS94EtNtj8iaebCQW1jHAhvGmFILVR9lzD0EzWKHkvy                                                                         
                    DEBUG    2025-02-24 07:14:35.827 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             WEjmUVRgCDd6Ne3eFRNS73gdv/C3l5boYySeu4exkEYVxVRn8DhCxs0MnkMHWFK6                                                                         
                    DEBUG    2025-02-24 07:14:35.828 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MyzXCCn+JnWFDYPfDKHvpff/kLDobtPBf+Lbch5wQy9quY27xaj0XwLyjOltpiST                                                                         
                    DEBUG    2025-02-24 07:14:35.830 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             LWae/Q4vAgMBAAGjHTAbMAwGA1UdEwQFMAMBAf8wCwYDVR0PBAQDAgEGMA0GCSqG                                                                         
                    DEBUG    2025-02-24 07:14:35.831 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             SIb3DQEBDQUAA4ICAQC9fUL2sZPxIN2mD32VeNySTgZlCEdVmlq471o/bDMP4B8g                                                                         
                    DEBUG    2025-02-24 07:14:35.833 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             nQesFRtXY2ZCjs50Jm73B2LViL9qlREmI6vE5IC8IsRBJSV4ce1WYxyXro5rmVg/                                                                         
                    DEBUG    2025-02-24 07:14:35.834 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             k6a10rlsbK/eg//GHoJxDdXDOokLUSnxt7gk3QKpX6eCdh67p0PuWm/7WUJQxH2S                                                                         
                    DEBUG    2025-02-24 07:14:35.836 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             DxsT9vB/iZriTIEe/ILoOQF0Aqp7AgNCcLcLAmbxXQkXYCCSB35Vp06u+eTWjG0/                                                                         
                    DEBUG    2025-02-24 07:14:35.837 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             pyS5V14stGtw+fA0DJp5ZJV4eqJ5LqxMlYvEZ/qKTEdoCeaXv2QEmN6dVqjDoTAo                                                                         
                    DEBUG    2025-02-24 07:14:35.838 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             k0t5u4YRXzEVCfXAC3ocplNdtCA72wjFJcSbfif4BSC8bDACTXtnPC7nD0VndZLp                                                                         
                    DEBUG    2025-02-24 07:14:35.840 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             +RiNLeiENhk0oTC+UVdSc+n2nJOzkCK0vYu0Ads4JGIB7g8IB3z2t9ICmsWrgnhd                                                                         
                    DEBUG    2025-02-24 07:14:35.841 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             NdcOe15BincrGA8avQ1cWXsfIKEjbrnEuEk9b5jel6NfHtPKoHc9mDpRdNPISeVa                                                                         
                    DEBUG    2025-02-24 07:14:35.842 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             wDBM1mJChneHt59Nh8Gah74+TM1jBsw4fhJPvoc7Atcg740JErb904mZfkIEmojC                                                                         
                    DEBUG    2025-02-24 07:14:35.844 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             VPhBHVQ9LHBAdM8qFI2kRK0IynOmAZhexlP/aT/kpEsEPyaZQlnBn3An1CRz8h0S                                                                         
                    DEBUG    2025-02-24 07:14:35.845 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             PApL8PytggYKeQmRhl499+6jLxcZ2IegLfqq41dzIjwHwTMplg+1pKIOVojpWA==                                                                         
                    DEBUG    2025-02-24 07:14:35.846 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----END CERTIFICATE-----                           vpn.py:435
                    DEBUG    2025-02-24 07:14:35.847 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   </ca>                                               vpn.py:435
                    DEBUG    2025-02-24 07:14:35.849 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   key-direction 1                                     vpn.py:435
                    DEBUG    2025-02-24 07:14:35.850 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   <tls-auth>                                          vpn.py:435
                    DEBUG    2025-02-24 07:14:35.851 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----BEGIN OpenVPN Static key V1-----               vpn.py:435
                    DEBUG    2025-02-24 07:14:35.853 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   e685bdaf659a25a200e2b9e39e51ff03                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.854 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   0fc72cf1ce07232bd8b2be5e6c670143                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.855 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   f51e937e670eee09d4f2ea5a6e4e6996                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.857 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   5db852c275351b86fc4ca892d78ae002                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.858 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   d6f70d029bd79c4d1c26cf14e9588033                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.859 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   cf639f8a74809f29f72b9d58f9b8f5fe                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.861 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   fc7938eade40e9fed6cb92184abb2cc1                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.862 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   0eb1a296df243b251df0643d53724cdb                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.864 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   5a92a1d6cb817804c4a9319b57d53be5                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.865 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   80815bcfcb2df55018cc83fc43bc7ff8                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.866 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   2d51f9b88364776ee9d12fc85cc7ea5b                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.868 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   9741c4f598c485316db066d52db4540e                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.869 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   212e1518a9bd4828219e24b20d88f598                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.870 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   a196c9de96012090e333519ae18d3509                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.872 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   9427e7b372d348d352dc4c85e18cd4b9                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.873 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   3f8a56ddb2e64eb67adfc9b337157ff4                    vpn.py:435
                    DEBUG    2025-02-24 07:14:35.874 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----END OpenVPN Static key V1-----                 vpn.py:435
                    DEBUG    2025-02-24 07:14:35.876 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   </tls-auth>                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:35.877 | DEBUG    | nyord_vpn.network.vpn:connect:449 - Auth file exists and has correct format               vpn.py:449
                    DEBUG    2025-02-24 07:14:35.879 | DEBUG    | nyord_vpn.network.vpn:connect:464 - Running OpenVPN command:                              vpn.py:464
                    DEBUG    2025-02-24 07:14:35.880 | DEBUG    | nyord_vpn.network.vpn:connect:465 - openvpn --config                                      vpn.py:465
                             /Users/adam/.cache/nyord-vpn/configs/pl122.nordvpn.com.tcp.ovpn --auth-user-pass /Users/adam/.cache/nyord-vpn/openvpn.auth               
                             --verb 5 --connect-retry 2 --connect-timeout 10 --resolv-retry infinite --ping 10 --ping-restart 60 --script-security 2                  
                             --persist-tun --persist-key --nobind --fast-io --data-ciphers AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305:AES-256-CBC                      
                             --data-ciphers-fallback AES-256-CBC --auth-retry nointeract --auth-nocache --pull-filter ignore auth-token --tls-version-min             
                             1.2 --tls-cipher TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384:TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256 --redirect-gateway def1                     
                             --dhcp-option DNS 103.86.96.100 --dhcp-option DNS 103.86.99.100 --log /Users/adam/.cache/nyord-vpn/openvpn.log                           
[02/24/25 07:14:37] DEBUG    2025-02-24 07:14:37.431 | DEBUG    | nyord_vpn.network.vpn:get_current_ip:302 - Checking IP with api.ipify.org (attempt 1)     vpn.py:302
                    DEBUG    2025-02-24 07:14:37.777 | DEBUG    | nyord_vpn.network.vpn:get_current_ip:309 - Got valid IP 95.214.217.211 from api.ipify.org vpn.py:309
                    INFO     2025-02-24 07:14:37.780 | INFO     | nyord_vpn.network.vpn:connect:638 - Connected to pl122.nordvpn.com                        vpn.py:638



[02/24/25 07:14:51] DEBUG    2025-02-24 07:14:51.124 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:156 - Found OpenVPN at                   vpn.py:156
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 07:14:51.131 | DEBUG    | nyord_vpn.network.vpn:status:894 - Connection status: process=True, initialized=True      vpn.py:894
                    INFO     2025-02-24 07:14:51.132 | INFO     | nyord_vpn.core.client:go:246 - Already connected to VPN, disconnecting first...        client.py:246
                    DEBUG    2025-02-24 07:14:51.134 | DEBUG    | nyord_vpn.network.vpn:get_current_ip:302 - Checking IP with api.ipify.org (attempt 1)     vpn.py:302
                    DEBUG    2025-02-24 07:14:51.502 | DEBUG    | nyord_vpn.network.vpn:get_current_ip:309 - Got valid IP 95.214.217.211 from api.ipify.org vpn.py:309
                    INFO     2025-02-24 07:14:51.505 | INFO     | nyord_vpn.core.client:bye:317 - Checking current connection status...                  client.py:317
                    INFO     2025-02-24 07:14:51.507 | INFO     | nyord_vpn.core.client:bye:327 - No active VPN connection found                         client.py:327
Not connected to VPN
                    DEBUG    2025-02-24 07:14:51.509 | DEBUG    | nyord_vpn.network.vpn:get_current_ip:302 - Checking IP with api.ipify.org (attempt 1)     vpn.py:302
                    DEBUG    2025-02-24 07:14:51.844 | DEBUG    | nyord_vpn.network.vpn:get_current_ip:309 - Got valid IP 95.214.217.211 from api.ipify.org vpn.py:309
                    DEBUG    2025-02-24 07:14:51.847 | DEBUG    | nyord_vpn.utils.utils:save_vpn_state:263 - Saved state to                               utils.py:263
                             /Users/adam/Library/Caches/nyord-vpn/state.json: {                                                                                       
                               "connected": false,                                                                                                                    
                               "current_ip": "95.214.217.211",                                                                                                        
                               "server": null,                                                                                                                        
                               "country": null,                                                                                                                       
                               "timestamp": 1740377691.847007,                                                                                                        
                               "normal_ip": "95.214.217.211",                                                                                                         
                               "connected_ip": null                                                                                                                   
                             }                                                                                                                                        
Public IP: 95.214.217.211
                    DEBUG    2025-02-24 07:14:51.852 | DEBUG    | nyord_vpn.network.server:get_servers_cache:289 - Using cached server list with 100     server.py:289
                             valid servers                                                                                                                            
                    DEBUG    2025-02-24 07:14:51.855 | DEBUG    | nyord_vpn.network.server:get_servers_cache:289 - Using cached server list with 100     server.py:289
                             valid servers                                                                                                                            
                    INFO     2025-02-24 07:14:51.857 | INFO     | nyord_vpn.core.client:go:275 - Selected server: fr544.nordvpn.com                      client.py:275
                    DEBUG    2025-02-24 07:14:51.957 | DEBUG    | nyord_vpn.network.vpn:disconnect:695 - Found OpenVPN process 32602                        vpn.py:695
[02/24/25 07:14:52] DEBUG    2025-02-24 07:14:52.159 | DEBUG    | nyord_vpn.network.vpn:disconnect:736 - Cleaned up OpenVPN log file                        vpn.py:736
                    DEBUG    2025-02-24 07:14:52.160 | DEBUG    | nyord_vpn.network.vpn:_invalidate_ip_cache:979 - IP cache invalidated                     vpn.py:979
                    INFO     2025-02-24 07:14:52.163 | INFO     | nyord_vpn.network.vpn:disconnect:760 - Disconnected from VPN                              vpn.py:760
                    DEBUG    2025-02-24 07:14:52.164 | DEBUG    | nyord_vpn.network.vpn:connect:421 - Connecting to fr544.nordvpn.com                       vpn.py:421
                    DEBUG    2025-02-24 07:14:52.166 | DEBUG    | nyord_vpn.utils.templates:log_debug:50 - Looking for config file at:                 templates.py:50
                             /Users/adam/.cache/nyord-vpn/configs/fr544.nordvpn.com.tcp.ovpn                                                                          
                    DEBUG    2025-02-24 07:14:52.167 | DEBUG    | nyord_vpn.network.vpn:connect:432 - OpenVPN config for fr544.nordvpn.com:                 vpn.py:432
                    DEBUG    2025-02-24 07:14:52.169 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   client                                              vpn.py:435
                    DEBUG    2025-02-24 07:14:52.171 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   dev tun                                             vpn.py:435
                    DEBUG    2025-02-24 07:14:52.173 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   proto tcp                                           vpn.py:435
                    DEBUG    2025-02-24 07:14:52.175 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote 217.138.207.187 443                          vpn.py:435
                    DEBUG    2025-02-24 07:14:52.176 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   resolv-retry infinite                               vpn.py:435
                    DEBUG    2025-02-24 07:14:52.177 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote-random                                       vpn.py:435
                    DEBUG    2025-02-24 07:14:52.178 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   nobind                                              vpn.py:435
                    DEBUG    2025-02-24 07:14:52.180 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   tun-mtu 1500                                        vpn.py:435
                    DEBUG    2025-02-24 07:14:52.181 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   tun-mtu-extra 32                                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.182 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   mssfix 1450                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:52.183 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   persist-key                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:52.185 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   persist-tun                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:52.186 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping 15                                             vpn.py:435
                    DEBUG    2025-02-24 07:14:52.187 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping-restart 0                                      vpn.py:435
                    DEBUG    2025-02-24 07:14:52.189 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   ping-timer-rem                                      vpn.py:435
                    DEBUG    2025-02-24 07:14:52.190 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   reneg-sec 0                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:52.191 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   comp-lzo no                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:52.192 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   verify-x509-name CN=fr544.nordvpn.com               vpn.py:435
                    DEBUG    2025-02-24 07:14:52.194 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                    DEBUG    2025-02-24 07:14:52.195 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   remote-cert-tls server                              vpn.py:435
                    DEBUG    2025-02-24 07:14:52.196 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                    DEBUG    2025-02-24 07:14:52.197 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   auth-user-pass                                      vpn.py:435
                    DEBUG    2025-02-24 07:14:52.199 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   verb 3                                              vpn.py:435
                    DEBUG    2025-02-24 07:14:52.200 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   pull                                                vpn.py:435
                    DEBUG    2025-02-24 07:14:52.201 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   fast-io                                             vpn.py:435
                    DEBUG    2025-02-24 07:14:52.203 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   cipher AES-256-CBC                                  vpn.py:435
                    DEBUG    2025-02-24 07:14:52.204 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   auth SHA512                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:52.205 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   <ca>                                                vpn.py:435
                    DEBUG    2025-02-24 07:14:52.206 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----BEGIN CERTIFICATE-----                         vpn.py:435
                    DEBUG    2025-02-24 07:14:52.208 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MIIFCjCCAvKgAwIBAgIBATANBgkqhkiG9w0BAQ0FADA5MQswCQYDVQQGEwJQQTEQ                                                                         
                    DEBUG    2025-02-24 07:14:52.209 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MA4GA1UEChMHTm9yZFZQTjEYMBYGA1UEAxMPTm9yZFZQTiBSb290IENBMB4XDTE2                                                                         
                    DEBUG    2025-02-24 07:14:52.211 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MDEwMTAwMDAwMFoXDTM1MTIzMTIzNTk1OVowOTELMAkGA1UEBhMCUEExEDAOBgNV                                                                         
                    DEBUG    2025-02-24 07:14:52.212 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             BAoTB05vcmRWUE4xGDAWBgNVBAMTD05vcmRWUE4gUm9vdCBDQTCCAiIwDQYJKoZI                                                                         
                    DEBUG    2025-02-24 07:14:52.213 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             hvcNAQEBBQADggIPADCCAgoCggIBAMkr/BYhyo0F2upsIMXwC6QvkZps3NN2/eQF                                                                         
                    DEBUG    2025-02-24 07:14:52.215 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             kfQIS1gql0aejsKsEnmY0Kaon8uZCTXPsRH1gQNgg5D2gixdd1mJUvV3dE3y9FJr                                                                         
                    DEBUG    2025-02-24 07:14:52.216 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             XMoDkXdCGBodvKJyU6lcfEVF6/UxHcbBguZK9UtRHS9eJYm3rpL/5huQMCppX7kU                                                                         
                    DEBUG    2025-02-24 07:14:52.218 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             eQ8dpCwd3iKITqwd1ZudDqsWaU0vqzC2H55IyaZ/5/TnCk31Q1UP6BksbbuRcwOV                                                                         
                    DEBUG    2025-02-24 07:14:52.219 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             skEDsm6YoWDnn/IIzGOYnFJRzQH5jTz3j1QBvRIuQuBuvUkfhx1FEwhwZigrcxXu                                                                         
                    DEBUG    2025-02-24 07:14:52.222 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MP+QgM54kezgziJUaZcOM2zF3lvrwMvXDMfNeIoJABv9ljw969xQ8czQCU5lMVmA                                                                         
                    DEBUG    2025-02-24 07:14:52.224 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             37ltv5Ec9U5hZuwk/9QO1Z+d/r6Jx0mlurS8gnCAKJgwa3kyZw6e4FZ8mYL4vpRR                                                                         
                    DEBUG    2025-02-24 07:14:52.225 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             hPdvRTWCMJkeB4yBHyhxUmTRgJHm6YR3D6hcFAc9cQcTEl/I60tMdz33G6m0O42s                                                                         
                    DEBUG    2025-02-24 07:14:52.227 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             Qt/+AR3YCY/RusWVBJB/qNS94EtNtj8iaebCQW1jHAhvGmFILVR9lzD0EzWKHkvy                                                                         
                    DEBUG    2025-02-24 07:14:52.228 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             WEjmUVRgCDd6Ne3eFRNS73gdv/C3l5boYySeu4exkEYVxVRn8DhCxs0MnkMHWFK6                                                                         
                    DEBUG    2025-02-24 07:14:52.230 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             MyzXCCn+JnWFDYPfDKHvpff/kLDobtPBf+Lbch5wQy9quY27xaj0XwLyjOltpiST                                                                         
                    DEBUG    2025-02-24 07:14:52.231 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             LWae/Q4vAgMBAAGjHTAbMAwGA1UdEwQFMAMBAf8wCwYDVR0PBAQDAgEGMA0GCSqG                                                                         
                    DEBUG    2025-02-24 07:14:52.233 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             SIb3DQEBDQUAA4ICAQC9fUL2sZPxIN2mD32VeNySTgZlCEdVmlq471o/bDMP4B8g                                                                         
                    DEBUG    2025-02-24 07:14:52.234 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             nQesFRtXY2ZCjs50Jm73B2LViL9qlREmI6vE5IC8IsRBJSV4ce1WYxyXro5rmVg/                                                                         
                    DEBUG    2025-02-24 07:14:52.236 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             k6a10rlsbK/eg//GHoJxDdXDOokLUSnxt7gk3QKpX6eCdh67p0PuWm/7WUJQxH2S                                                                         
                    DEBUG    2025-02-24 07:14:52.237 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             DxsT9vB/iZriTIEe/ILoOQF0Aqp7AgNCcLcLAmbxXQkXYCCSB35Vp06u+eTWjG0/                                                                         
                    DEBUG    2025-02-24 07:14:52.239 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             pyS5V14stGtw+fA0DJp5ZJV4eqJ5LqxMlYvEZ/qKTEdoCeaXv2QEmN6dVqjDoTAo                                                                         
                    DEBUG    2025-02-24 07:14:52.240 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             k0t5u4YRXzEVCfXAC3ocplNdtCA72wjFJcSbfif4BSC8bDACTXtnPC7nD0VndZLp                                                                         
                    DEBUG    2025-02-24 07:14:52.242 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             +RiNLeiENhk0oTC+UVdSc+n2nJOzkCK0vYu0Ads4JGIB7g8IB3z2t9ICmsWrgnhd                                                                         
                    DEBUG    2025-02-24 07:14:52.243 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             NdcOe15BincrGA8avQ1cWXsfIKEjbrnEuEk9b5jel6NfHtPKoHc9mDpRdNPISeVa                                                                         
                    DEBUG    2025-02-24 07:14:52.245 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             wDBM1mJChneHt59Nh8Gah74+TM1jBsw4fhJPvoc7Atcg740JErb904mZfkIEmojC                                                                         
                    DEBUG    2025-02-24 07:14:52.246 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             VPhBHVQ9LHBAdM8qFI2kRK0IynOmAZhexlP/aT/kpEsEPyaZQlnBn3An1CRz8h0S                                                                         
                    DEBUG    2025-02-24 07:14:52.248 | DEBUG    | nyord_vpn.network.vpn:connect:435 -                                                       vpn.py:435
                             PApL8PytggYKeQmRhl499+6jLxcZ2IegLfqq41dzIjwHwTMplg+1pKIOVojpWA==                                                                         
                    DEBUG    2025-02-24 07:14:52.249 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----END CERTIFICATE-----                           vpn.py:435
                    DEBUG    2025-02-24 07:14:52.250 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   </ca>                                               vpn.py:435
                    DEBUG    2025-02-24 07:14:52.252 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   key-direction 1                                     vpn.py:435
                    DEBUG    2025-02-24 07:14:52.253 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   <tls-auth>                                          vpn.py:435
                    DEBUG    2025-02-24 07:14:52.255 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----BEGIN OpenVPN Static key V1-----               vpn.py:435
                    DEBUG    2025-02-24 07:14:52.256 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   e685bdaf659a25a200e2b9e39e51ff03                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.257 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   0fc72cf1ce07232bd8b2be5e6c670143                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.258 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   f51e937e670eee09d4f2ea5a6e4e6996                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.260 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   5db852c275351b86fc4ca892d78ae002                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.261 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   d6f70d029bd79c4d1c26cf14e9588033                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.262 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   cf639f8a74809f29f72b9d58f9b8f5fe                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.264 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   fc7938eade40e9fed6cb92184abb2cc1                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.265 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   0eb1a296df243b251df0643d53724cdb                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.266 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   5a92a1d6cb817804c4a9319b57d53be5                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.268 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   80815bcfcb2df55018cc83fc43bc7ff8                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.269 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   2d51f9b88364776ee9d12fc85cc7ea5b                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.271 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   9741c4f598c485316db066d52db4540e                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.272 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   212e1518a9bd4828219e24b20d88f598                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.273 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   a196c9de96012090e333519ae18d3509                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.274 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   9427e7b372d348d352dc4c85e18cd4b9                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.276 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   3f8a56ddb2e64eb67adfc9b337157ff4                    vpn.py:435
                    DEBUG    2025-02-24 07:14:52.277 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   -----END OpenVPN Static key V1-----                 vpn.py:435
                    DEBUG    2025-02-24 07:14:52.278 | DEBUG    | nyord_vpn.network.vpn:connect:435 -   </tls-auth>                                         vpn.py:435
                    DEBUG    2025-02-24 07:14:52.280 | DEBUG    | nyord_vpn.network.vpn:connect:449 - Auth file exists and has correct format               vpn.py:449
                    DEBUG    2025-02-24 07:14:52.281 | DEBUG    | nyord_vpn.network.vpn:connect:464 - Running OpenVPN command:                              vpn.py:464
                    DEBUG    2025-02-24 07:14:52.282 | DEBUG    | nyord_vpn.network.vpn:connect:465 - openvpn --config                                      vpn.py:465
                             /Users/adam/.cache/nyord-vpn/configs/fr544.nordvpn.com.tcp.ovpn --auth-user-pass /Users/adam/.cache/nyord-vpn/openvpn.auth               
                             --verb 5 --connect-retry 2 --connect-timeout 10 --resolv-retry infinite --ping 10 --ping-restart 60 --script-security 2                  
                             --persist-tun --persist-key --nobind --fast-io --data-ciphers AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305:AES-256-CBC                      
                             --data-ciphers-fallback AES-256-CBC --auth-retry nointeract --auth-nocache --pull-filter ignore auth-token --tls-version-min             
                             1.2 --tls-cipher TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384:TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256 --redirect-gateway def1                     
                             --dhcp-option DNS 103.86.96.100 --dhcp-option DNS 103.86.99.100 --log /Users/adam/.cache/nyord-vpn/openvpn.log                           
[02/24/25 07:14:56] DEBUG    2025-02-24 07:14:56.179 | DEBUG    | nyord_vpn.network.vpn:get_current_ip:302 - Checking IP with api.ipify.org (attempt 1)     vpn.py:302
                    DEBUG    2025-02-24 07:14:56.540 | DEBUG    | nyord_vpn.network.vpn:get_current_ip:309 - Got valid IP 45.84.137.246 from api.ipify.org  vpn.py:309
                    INFO     2025-02-24 07:14:56.543 | INFO     | nyord_vpn.network.vpn:connect:638 - Connected to fr544.nordvpn.com                        vpn.py:638                    





JUST IMPLEMENT ATTEMPTING WITH ANOTHER SERVER IF CONNECTION FAILS FOR ANY REASON. DON’T OVER THINK

---

_**Assistant**_

Okay, I will modify the `connect` method in `src/nyord_vpn/network/vpn.py` to retry with a different server if the initial connection attempt fails. I'll add a loop that tries a limited number of servers before giving up.

```python:src/nyord_vpn/network/vpn.py
# ...
from nyord_vpn.storage.state import save_vpn_state, load_vpn_state
from nyord_vpn.network.server import select_server

# Constants
OPENVPN_AUTH = Path.home() / ".cache" / "nyord-vpn" / "openvpn.auth"
OPENVPN_LOG = Path.home() / ".cache" / "nyord-vpn" / "openvpn.log"
MAX_CONNECT_RETRIES = 3  # Maximum number of servers to try


class VPNConnectionManager:
    # ...

    def connect(self, server: dict[str, Any]) -> None:
        """Connect to a VPN server, retrying with different servers on failure.

        Args:
            server: Initial server information dictionary.

        Raises:
            VPNError: If connection fails after multiple retries.
        """
        max_attempts = MAX_CONNECT_RETRIES
        attempt = 0
        original_country = server.get("country")  # Keep track of original country

        while attempt < max_attempts:
            attempt += 1
            try:
                hostname = server.get("hostname")
                if not hostname:
                    raise VPNError("Invalid server info - missing hostname")

                # Force cleanup of any existing connections
                try:
                    self.disconnect()
                except Exception as e:
                    if self.verbose:
                        self.logger.warning(
                            f"Error during disconnect: {e}, attempting force cleanup"
                        )

                    # Ensure no OpenVPN processes are running
                    for proc in psutil.process_iter(["name", "pid", "cmdline"]):
                        try:
                            if proc.info["name"] == "openvpn":
                                cmdline = proc.info.get("cmdline", [])
                                if any("nordvpn.com" in arg for arg in cmdline):
                                    try:
                                        os.kill(proc.info["pid"], signal.SIGKILL)
                                        time.sleep(0.1)  # Brief pause after kill
                                    except Exception:
                                        pass
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            continue

                # Store server info
                self._server = hostname
                self._country_name = server.get("country")

                # Ensure OpenVPN is available
                if not self.openvpn_path:
                    self.openvpn_path = self.check_openvpn_installation()

                if self.verbose:
                    self.logger.debug(f"Connecting to {hostname} (attempt {attempt})")

                # Get OpenVPN config
                config_path = get_config_path(hostname)
                if not config_path:
                    raise VPNConfigError(f"Failed to get OpenVPN config for {hostname}")

                # Log config file contents for debugging
                if self.verbose:
                    try:
                        config_content = config_path.read_text()
                        self.logger.debug(f"OpenVPN config for {hostname}:")
                        for line in config_content.splitlines():
                            if not line.strip().startswith("#"):  # Skip comments
                                self.logger.debug(f"  {line}")
                    except Exception as e:
                        self.logger.warning(f"Failed to read config file: {e}")

                # Verify auth file exists and has correct format
                if not OPENVPN_AUTH.exists():
                    raise VPNError("Auth file not found - please run setup first")
                try:
                    auth_content = OPENVPN_AUTH.read_text().strip().split("\n")
                    if len(auth_content) != 2:
                        raise VPNError(
                            "Auth file is corrupted - please run setup again"
                        )
                    if not auth_content[0] or not auth_content[1]:
                        raise VPNError(
                            "Auth file contains empty username or password - please run setup again"
                        )
                    if self.verbose:
                        self.logger.debug(f"Auth file exists and has correct format")
                except Exception as e:
                    if isinstance(e, VPNError):
                        raise
                    raise VPNError(f"Failed to read auth file: {e}")

                # Start OpenVPN process
                cmd = get_openvpn_command(
                    config_path=config_path,
                    auth_path=OPENVPN_AUTH,
                    log_path=OPENVPN_LOG if self.verbose else None,
                    verbosity=5 if self.verbose else 3,
                )

                if self.verbose:
                    self.logger.debug("Running OpenVPN command:")
                    self.logger.debug(" ".join(cmd))

                try:
                    # Clear any existing log file
                    if OPENVPN_LOG and OPENVPN_LOG.exists():
                        OPENVPN_LOG.unlink()

                    # Start OpenVPN process
                    self.process = subprocess.Popen(
                        cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        bufsize=1,
                    )

                    # Give process a moment to start
                    time.sleep(0.5)

                    # Check if process died immediately
                    if self.process.poll() is not None:
                        stdout, stderr = self.process.communicate()
                        raise VPNError(
                            f"OpenVPN process failed to start:\n"
                            f"Exit code: {self.process.returncode}\n"
                            f"Output: {stdout}\n"
                            f"Error: {stderr}"
                        )

                except subprocess.SubprocessError as e:
                    raise VPNError(f"Failed to start OpenVPN process: {e}")

                # Monitor OpenVPN output
                start_time = time.time()
                success = False
                error_msg = None
                log_content = ""

                while time.time() - start_time < 30:  # 30 second timeout
                    # Check if process died
                    if self.process.poll() is not None:
                        stdout, stderr = self.process.communicate()

                        # Try to get log content for better error reporting
                        try:
                            if OPENVPN_LOG and OPENVPN_LOG.exists():
                                log_content = OPENVPN_LOG.read_text()
                                if self.verbose:
                                    self.logger.debug("OpenVPN log content:")
                                    for line in log_content.splitlines():
                                        self.logger.debug(f"  {line}")
                        except Exception as e:
                            if self.verbose:
                                self.logger.warning(f"Failed to read OpenVPN log: {e}")

                        # If we have log content, check for known errors
                        if log_content:
                            if "AUTH_FAILED" in log_content:
                                # Get more context around the auth failure
                                auth_lines = [
                                    line
                                    for line in log_content.splitlines()
                                    if "AUTH" in line
                                ]
                                if auth_lines and self.verbose:
                                    self.logger.debug("Auth-related log lines:")
                                    for line in auth_lines:
                                        self.logger.debug(f"  {line}")
                                error_msg = (
                                    "Authentication failed - check your credentials"
                                )
                                if "AUTH_FAILED,SESSION" in log_content:
                                    error_msg = "Session authentication failed - server may require re-login"
                                elif "AUTH_FAILED,CERTIFICATE" in log_content:
                                    error_msg = "Certificate authentication failed - server config may be invalid"
                            elif "Cannot load certificate file" in log_content:
                                error_msg = (
                                    "Certificate error - server config may be invalid"
                                )
                            elif "Cannot load private key file" in log_content:
                                error_msg = (
                                    "Private key error - server config may be invalid"
                                )
                            elif (
                                "All TAP-Windows adapters on this system are currently in use"
                                in log_content
                            ):
                                error_msg = "All VPN adapters are in use"
                            elif "TLS Error" in log_content:
                                error_msg = (
                                    "TLS handshake failed - server may be down"
                                )
                            elif "TLS key negotiation failed" in log_content:
                                error_msg = "TLS key negotiation failed - server may require different TLS settings"
                            elif "Connection timed out" in log_content:
                                error_msg = (
                                    "Connection timed out - server may be unreachable"
                                )
                            elif "Cannot resolve host address" in log_content:
                                error_msg = "Cannot resolve server hostname - DNS issue"

                        # If no specific error found, use a generic message
                        if not error_msg:
                            error_msg = (
                                f"OpenVPN process terminated unexpectedly:\n"
                                f"Exit code: {self.process.returncode}\n"
                                f"Output: {stdout}\n"
                                f"Error: {stderr}\n"
                                f"Log: {log_content if log_content else 'No log available'}"
                            )
                        break

                    # Check log file for status
                    if OPENVPN_LOG and OPENVPN_LOG.exists():
                        try:
                            log_content = OPENVPN_LOG.read_text()

                            # Check for success
                            if "Initialization Sequence Completed" in log_content:
                                success = True
                                break

                            # Check for auth progress
                            if self.verbose and "AUTH" in log_content:
                                auth_lines = [
                                    line
                                    for line in log_content.splitlines()
                                    if "AUTH" in line
                                ]
                                if auth_lines:
                                    self.logger.debug("Auth progress:")
                                    for line in auth_lines:
                                        self.logger.debug(f"  {line}")

                            # Check for common errors
                            if "AUTH_FAILED" in log_content:
                                error_msg = (
                                    "Authentication failed - check your credentials"
                                )
                                break
                            if "TLS Error" in log_content:
                                error_msg = (
                                    "TLS handshake failed - server may be down"
                                )
                                break
                            if "Connection timed out" in log_content:
                                error_msg = (
                                    "Connection timed out - server may be unreachable"
                                )
                                break
                            if "Cannot resolve host address" in log_content:
                                error_msg = "Cannot resolve server hostname - DNS issue"
                                break
                            if (
                                "All TAP-Windows adapters on this system are currently in use"
                                in log_content
                            ):
                                error_msg = "All VPN adapters are in use"
                                break
                            if "Cannot load certificate file" in log_content:
                                error_msg = (
                                    "Certificate error - server config may be invalid"
                                )
                                break
                            if "Cannot load private key file" in log_content:
                                error_msg = (
                                    "Private key error - server config may be invalid"
                                )
                                break
                        except Exception as e:
                            if self.verbose:
                                self.logger.warning(f"Failed to read OpenVPN log: {e}")

                    time.sleep(0.1)

                # Handle timeout or error
                if not success:
                    # Kill the process if it's still running
                    if self.process and self.process.poll() is None:
                        try:
                            self.process.terminate()
                            time.sleep(0.1)
                            if self.process.poll() is None:
                                self.process.kill()
                        except Exception:
                            pass

                    if error_msg:
                        if self.verbose:
                            self.logger.warning(
                                f"Connection to {hostname} failed: {error_msg}"
                            )
                    else:
                        if self.verbose:
                            self.logger.warning(

---

_**User**_

We already make a random subset and then check the pings, right? We don't we just sort them and then use that list to work through as fallbacks

---

_**Assistant**_

You

---



---

