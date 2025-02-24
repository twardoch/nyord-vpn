## SpecStory

## VPN Connection Issue: No Servers in Germany (24/02/2025, 17:43:00)

_**User**_

[02/24/25 17:42:28] DEBUG    2025-02-24 17:42:28.252 | DEBUG    | nyord_vpn.network.vpn:check_openvpn_installation:172 - Found OpenVPN at                   vpn.py:172
                             /usr/local/sbin/openvpn                                                                                                                  
                    DEBUG    2025-02-24 17:42:28.259 | DEBUG    | nyord_vpn.network.vpn:setup_connection:250 - Created auth file at                         vpn.py:250
                             /Users/adam/.cache/nyord-vpn/openvpn.auth                                                                                                
                    DEBUG    2025-02-24 17:42:28.261 | DEBUG    | nyord_vpn.network.vpn:get_current_ip:321 - Checking IP with api.ipify.org (attempt 1)     vpn.py:321
                    DEBUG    2025-02-24 17:42:28.669 | DEBUG    | nyord_vpn.network.vpn:get_current_ip:330 - Got valid IP 45.130.105.8 from api.ipify.org   vpn.py:330
Error: Failed to connect: No servers available in DE. Available countries: 


@https://api.nordvpn.com/v2/servers

---

_**Assistant**_

Let me help investigate why there are no servers available in Germany (DE) despite attempting to connect to NordVPN's API. I'll check the server response and the code handling it.

First, let me search for relevant code that handles server retrieval:

---

_****_

Tool call timed out after 5000ms

---

_****_



Let me try a more targeted search:

---

_****_

<details>
            <summary>Grep search for "api.nordvpn.com/v2/servers" • **10** files</summary>
        
| File | Line | Match |
|------|------|-------|
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/TODO.md` | L38 | `- [ ] Switch to https://api.nordvpn.com/v2/servers for server data fetching (the local "cached" file should be made compatible with the v2 format)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L436 | `"https://api.nordvpn.com/v2/servers",` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/nyord_vpn.txt` | L11553 | `- [ ] Switch to https://api.nordvpn.com/v2/servers for server data fetching (the local "cached" file should be made compatible with the v2 format)` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-10-vpn-server-availability-issues.md` | L1741 | `1. READ THE SERVER JSON from @https://api.nordvpn.com/v2/servers  (not from @https://api.nordvpn.com/v1/servers/recommendations ).` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-10-vpn-server-availability-issues.md` | L1821 | `+                 "https://api.nordvpn.com/v2/servers",` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-10-vpn-server-availability-issues.md` | L2437 | `curl -s https://api.nordvpn.com/v2/servers | head -n 20` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_08-10-vpn-server-availability-issues.md` | L4197 | `curl -s https://api.nordvpn.com/v2/servers | head -n 20 | jq` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-09-improving-nyord-vpn-server-selection-and-setup.md` | L209 | `1. `https://api.nordvpn.com/v2/servers?limit=16384` - Gets all servers at once` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-09-improving-nyord-vpn-server-selection-and-setup.md` | L347 | `But @@https://api.nordvpn.com/v2/servers https://api.nordvpn.com/v2/servers is not very big compared to @https://api.nordvpn.com/v1/servers/recommendations  and @https://api.nordvpn.com/v1/servers/countries` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_17-19-vpn-country-resolution-issue.md` | L276 | `@https://api.nordvpn.com/v2/servers` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_17-19-vpn-country-resolution-issue.md` | L403 | `Why are we not caching https://api.nordvpn.com/v2/servers in ~/.cache/nyord-vpn ?` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_17-19-vpn-country-resolution-issue.md` | L544 | `"https://api.nordvpn.com/v2/servers",` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_17-19-vpn-country-resolution-issue.md` | L3013 | `-                 "https://api.nordvpn.com/v2/servers",` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_17-19-vpn-country-resolution-issue.md` | L3139 | `@https://api.nordvpn.com/v2/servers` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_17-19-vpn-country-resolution-issue.md` | L3157 | `+                 "https://api.nordvpn.com/v2/servers",` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-23_06-52-code-optimization-and-refactoring-discussion.md` | L2794 | `@https://api.nordvpn.com/v2/servers` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history/2025-02-24_05-33-vpn-connection-troubleshooting-and-debugging.md` | L36 | `—— The new servers are at https://api.nordvpn.com/v2/servers , you KNOW THAT, right?` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history.txt` | L79441 | `1. `https://api.nordvpn.com/v2/servers?limit=16384` - Gets all servers at once` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history.txt` | L79579 | `But @@https://api.nordvpn.com/v2/servers https://api.nordvpn.com/v2/servers is not very big compared to @https://api.nordvpn.com/v1/servers/recommendations  and @https://api.nordvpn.com/v1/servers/countries` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/.specstory/history.txt` | L83738 | `@https://api.nordvpn.com/v2/servers` |
| `file:///Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py` | L436 | `"https://api.nordvpn.com/v2/servers",` |

</details>

---

_****_



Let me check the server handling code:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



Let me check how the server data is processed:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



Let me check the country code validation:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



I see the issue. The code is trying to access the server data from the NordVPN v2 API, but there seems to be a problem with how the response is being processed. Let me check the actual API response structure:

---

_****_

```bash
curl -s https://api.nordvpn.com/v2/servers | head -n 20
```

```
adata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r
55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"name
":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,1
5],"service_ids":[1,5],"location_ids":[45]},{"id":945157,"created_
at":"2019-06-13 04:49:56","updated_at":"2025-02-24 16:36:21","name
":"United States #2939","station":"172.93.237.99","ipv6_station":"
","hostname":"us2939.nordvpn.com","status":"online","load":0,"ips"
:[{"id":138778,"created_at":"2019-07-09 14:15:11","updated_at":"20
19-07-09 14:15:11","server_id":945157,"ip_id":63127,"type":"entry"
,"ip":{"id":63127,"ip":"172.93.237.99","version":4}}],"specificati
ons":[{"id":8,"title":"Version","identifier":"version","values":[{
"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"onl
ine"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"pub
lic_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],
"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"
online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[1
9]},{"id":945160,"created_at":"2019-06-13 04:49:57","updated_at":"
2025-02-24 15:32:36","name":"United States #2940","station":"172.9
3.237.100","ipv6_station":"","hostname":"us2940.nordvpn.com","stat
us":"online","load":0,"ips":[{"id":139372,"created_at":"2019-07-09
 14:25:49","updated_at":"2019-07-09 14:25:49","server_id":945160,"
ip_id":63130,"type":"entry","ip":{"id":63130,"ip":"172.93.237.100"
,"version":4}}],"specifications":[{"id":8,"title":"Version","ident
ifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technolo
gies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id"
:35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEB
YAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"
online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_
ids":[1,5],"location_ids":[19]},{"id":945916,"created_at":"2019-06
-25 11:49:45","updated_at":"2025-02-24 16:36:21","name":"Germany #
655","station":"194.31.54.4","ipv6_station":"","hostname":"de655.n
ordvpn.com","status":"online","load":3,"ips":[{"id":1773885,"creat
ed_at":"2024-08-21 05:08:31","updated_at":"2024-08-21 05:08:31","s
erver_id":945916,"ip_id":65179,"type":"entry","ip":{"id":65179,"ip
":"194.31.54.4","version":4}}],"specifications":[{"id":8,"title":"
Version","identifier":"version","values":[{"id":200,"value":"2.0.0
"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":
"online"},{"id":35,"metadata":[{"name":"public_key","value":"m0tej
5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status":"online"},{"id
":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[
9,19],"service_ids":[1,5],"location_ids":[133]},{"id":946435,"crea
ted_at":"2019-07-12 07:51:12","updated_at":"2025-02-24 16:40:25","
name":"United Kingdom #892","station":"195.206.170.3","ipv6_statio
n":"","hostname":"uk892.nordvpn.com","status":"online","load":19,"
ips":[{"id":1855574,"created_at":"2024-09-27 08:48:09","updated_at
":"2024-09-27 08:48:09","server_id":946435,"ip_id":68866,"type":"e
ntry","ip":{"id":68866,"ip":"195.206.170.3","version":4}}],"specif
ications":[{"id":8,"title":"Version","identifier":"version","value
s":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status"
:"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{
"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"m
etadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt
4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"na
me":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11
,15],"service_ids":[1,5],"location_ids":[45]},{"id":946441,"create
d_at":"2019-07-12 07:51:13","updated_at":"2025-02-24 16:40:25","na
me":"United Kingdom #894","station":"195.206.170.131","ipv6_statio
n":"","hostname":"uk894.nordvpn.com","status":"online","load":27,"
ips":[{"id":1856397,"created_at":"2024-10-03 12:49:58","updated_at
":"2024-10-03 12:49:58","server_id":946441,"ip_id":68872,"type":"e
ntry","ip":{"id":68872,"ip":"195.206.170.131","version":4}}],"spec
ifications":[{"id":8,"title":"Version","identifier":"version","val
ues":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"statu
s":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"}
,{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,
"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvC
vt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"
name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,
11,15],"service_ids":[1,5],"location_ids":[45]},{"id":947116,"crea
ted_at":"2019-08-06 07:35:03","updated_at":"2025-02-24 16:40:25","
name":"United Kingdom #896","station":"178.239.164.3","ipv6_statio
n":"","hostname":"uk896.nordvpn.com","status":"online","load":24,"
ips":[{"id":1855544,"created_at":"2024-09-27 08:46:21","updated_at
":"2024-09-27 08:46:21","server_id":947116,"ip_id":72133,"type":"e
ntry","ip":{"id":72133,"ip":"178.239.164.3","version":4}}],"specif
ications":[{"id":8,"title":"Version","identifier":"version","value
s":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status"
:"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{
"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"m
etadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt
4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"na
me":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11
,15],"service_ids":[1,5],"location_ids":[45]},{"id":947122,"create
d_at":"2019-08-06 07:35:04","updated_at":"2025-02-24 16:40:25","na
me":"United Kingdom #898","station":"178.239.164.131","ipv6_statio
n":"","hostname":"uk898.nordvpn.com","status":"online","load":21,"
ips":[{"id":1855524,"created_at":"2024-09-27 08:44:47","updated_at
":"2024-09-27 08:44:47","server_id":947122,"ip_id":72139,"type":"e
ntry","ip":{"id":72139,"ip":"178.239.164.131","version":4}}],"spec
ifications":[{"id":8,"title":"Version","identifier":"version","val
ues":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"statu
s":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"}
,{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,
"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvC
vt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"
name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,
15,11],"service_ids":[1,5],"location_ids":[45]},{"id":947235,"crea
ted_at":"2019-08-23 12:48:22","updated_at":"2025-02-24 16:32:22","
name":"United States #2943","station":"89.187.175.97","ipv6_statio
n":"","hostname":"us2943.nordvpn.com","status":"online","load":4,"
ips":[{"id":1818610,"created_at":"2024-08-29 11:50:57","updated_at
":"2024-08-29 11:50:57","server_id":947235,"ip_id":72639,"type":"e
ntry","ip":{"id":72639,"ip":"89.187.175.97","version":4}}],"specif
ications":[{"id":8,"title":"Version","identifier":"version","value
s":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status"
:"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name"
:"public_key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI
="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"stat
us":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_id
s":[79]},{"id":947238,"created_at":"2019-08-23 12:48:22","updated_
at":"2025-02-24 16:40:25","name":"United States #2944","station":"
89.187.175.98","ipv6_station":"","hostname":"us2944.nordvpn.com","
status":"online","load":2,"ips":[{"id":1810823,"created_at":"2024-
08-28 11:12:32","updated_at":"2024-08-28 11:12:32","server_id":947
238,"ip_id":72645,"type":"entry","ip":{"id":72645,"ip":"89.187.175
.98","version":4}}],"specifications":[{"id":8,"title":"Version","i
dentifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"tech
nologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{
"id":35,"metadata":[{"name":"public_key","value":"8pRFH/FfMBs3eBJC
M2ABFoOs/13n78LYQvoovZVLdgI="}],"status":"online"},{"id":42,"statu
s":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"serv
ice_ids":[1,5],"location_ids":[79]},{"id":947280,"created_at":"201
9-08-28 06:59:11","updated_at":"2025-02-24 16:36:21","name":"Unite
d States #2945","station":"89.187.185.86","ipv6_station":"","hostn
ame":"us2945.nordvpn.com","status":"online","load":5,"ips":[{"id":
1821697,"created_at":"2024-08-30 04:42:38","updated_at":"2024-08-3
0 04:42:38","server_id":947280,"ip_id":73533,"type":"entry","ip":{
"id":73533,"ip":"89.187.185.86","version":4}}],"specifications":[{
"id":8,"title":"Version","identifier":"version","values":[{"id":20
0,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{
"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key
","value":"V1WC7wt34kcSDyqPuUhN56NJ0v+GlqY9TwZR5WlzzB4="}],"status
":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"
}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[51]},{"i
d":947283,"created_at":"2019-08-28 06:59:11","updated_at":"2025-02
-24 16:16:39","name":"United States #2946","station":"89.187.185.9
7","ipv6_station":"","hostname":"us2946.nordvpn.com","status":"onl
ine","load":2,"ips":[{"id":1807685,"created_at":"2024-08-28 06:22:
30","updated_at":"2024-08-28 06:22:30","server_id":947283,"ip_id":
73536,"type":"entry","ip":{"id":73536,"ip":"89.187.185.97","versio
n":4}}],"specifications":[{"id":8,"title":"Version","identifier":"
version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{
"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"met
adata":[{"name":"public_key","value":"V1WC7wt34kcSDyqPuUhN56NJ0v+G
lqY9TwZR5WlzzB4="}],"status":"online"},{"id":42,"status":"online"}
,{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,
5],"location_ids":[51]},{"id":947592,"created_at":"2019-09-18 09:5
1:34","updated_at":"2025-02-24 00:16:49","name":"Netherlands #408"
,"station":"185.229.58.3","ipv6_station":"","hostname":"nl408.nord
vpn.com","status":"online","load":0,"ips":[{"id":1751714,"created_
at":"2024-08-19 05:57:10","updated_at":"2024-08-19 05:57:10","serv
er_id":947592,"ip_id":74514,"type":"entry","ip":{"id":74514,"ip":"
185.229.58.3","version":4}}],"specifications":[{"id":8,"title":"Ve
rsion","identifier":"version","values":[{"id":200,"value":"2.0.0"}
]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"o
nline"},{"id":35,"metadata":[{"name":"public_key","value":"5p4Rkyb
dRU5uaDi90eu4KZPTFif0lKCg4Qp6t1c4F30="}],"status":"online"},{"id":
42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,
19],"service_ids":[1,5],"location_ids":[5]},{"id":947595,"created_
at":"2019-09-18 09:51:34","updated_at":"2025-02-24 16:32:22","name
":"Netherlands #409","station":"185.229.58.129","ipv6_station":"",
"hostname":"nl409.nordvpn.com","status":"online","load":1,"ips":[{
"id":1768144,"created_at":"2024-08-20 07:16:03","updated_at":"2024
-08-20 07:16:03","server_id":947595,"ip_id":74517,"type":"entry","
ip":{"id":74517,"ip":"185.229.58.129","version":4}}],"specificatio
ns":[{"id":8,"title":"Version","identifier":"version","values":[{"
id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"onli
ne"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"publ
ic_key","value":"5p4RkybdRU5uaDi90eu4KZPTFif0lKCg4Qp6t1c4F30="}],"
status":"online"},{"id":42,"status":"online"},{"id":45,"status":"o
nline"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[5]
},{"id":948099,"created_at":"2019-09-26 12:22:40","updated_at":"20
25-02-24 15:20:22","name":"Germany #676","station":"37.120.223.116
","ipv6_station":"","hostname":"de676.nordvpn.com","status":"onlin
e","load":0,"ips":[{"id":1791453,"created_at":"2024-08-26 11:14:49
","updated_at":"2024-08-26 11:14:49","server_id":948099,"ip_id":75
906,"type":"entry","ip":{"id":75906,"ip":"37.120.223.116","version
":4}}],"specifications":[{"id":8,"title":"Version","identifier":"v
ersion","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"
id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"meta
data":[{"name":"public_key","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM8
1AChLlzlsOSjSs="}],"status":"online"},{"id":42,"status":"online"},
{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5
],"location_ids":[133]},{"id":948810,"created_at":"2019-10-11 09:0
6:37","updated_at":"2025-02-24 16:40:25","name":"United States #50
55","station":"89.187.175.2","ipv6_station":"","hostname":"us5055.
nordvpn.com","status":"online","load":13,"ips":[{"id":795035,"crea
ted_at":"2023-01-16 13:35:10","updated_at":"2023-01-16 13:35:10","
server_id":948810,"ip_id":78471,"type":"entry","ip":{"id":78471,"i
p":"89.187.175.2","version":4}}],"specifications":[{"id":8,"title"
:"Version","identifier":"version","values":[{"id":257,"value":"2.1
.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status
":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"}
,{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_
key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI="}],"sta
tus":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}
],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"
location_ids":[79]},{"id":949095,"created_at":"2019-10-29 07:51:33
","updated_at":"2025-02-24 16:16:22","name":"United States #2949",
"station":"64.44.32.75","ipv6_station":"","hostname":"us2949.nordv
pn.com","status":"online","load":0,"ips":[{"id":155328,"created_at
":"2019-10-30 08:32:23","updated_at":"2019-10-30 08:32:23","server
_id":949095,"ip_id":80337,"type":"entry","ip":{"id":80337,"ip":"64
.44.32.75","version":4}}],"specifications":[{"id":8,"title":"Versi
on","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}]
,"technologies":[{"id":3,"status":"online"},{"id":5,"status":"onli
ne"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4
Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,
"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21]
,"service_ids":[1,5],"location_ids":[19]},{"id":949098,"created_at
":"2019-10-29 07:51:33","updated_at":"2025-02-24 16:32:22","name":
"United States #2950","station":"64.44.32.76","ipv6_station":"","h
ostname":"us2950.nordvpn.com","status":"online","load":0,"ips":[{"
id":193733,"created_at":"2020-04-28 07:18:59","updated_at":"2020-0
4-28 07:18:59","server_id":949098,"ip_id":80340,"type":"entry","ip
":{"id":80340,"ip":"64.44.32.76","version":4}}],"specifications":[
{"id":8,"title":"Version","identifier":"version","values":[{"id":2
00,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},
{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_ke
y","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"statu
s":"online"},{"id":42,"status":"online"},{"id":45,"status":"online
"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"
id":949581,"created_at":"2019-11-20 07:55:10","updated_at":"2025-0
2-24 16:40:25","name":"France #439","station":"185.93.2.199","ipv6
_station":"","hostname":"fr439.nordvpn.com","status":"online","loa
d":5,"ips":[{"id":1803435,"created_at":"2024-08-27 13:14:39","upda
ted_at":"2024-08-27 13:14:39","server_id":949581,"ip_id":82254,"ty
pe":"entry","ip":{"id":82254,"ip":"185.93.2.199","version":4}}],"s
pecifications":[{"id":8,"title":"Version","identifier":"version","
values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"st
atus":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"
name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlL
ZLDBM="}],"status":"online"},{"id":42,"status":"online"},{"id":45,
"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"locati
on_ids":[87]},{"id":949584,"created_at":"2019-11-20 07:55:10","upd
ated_at":"2025-02-24 16:36:21","name":"France #440","station":"185
.93.2.206","ipv6_station":"","hostname":"fr440.nordvpn.com","statu
s":"online","load":6,"ips":[{"id":1779073,"created_at":"2024-08-22
 08:12:09","updated_at":"2024-08-22 08:12:09","server_id":949584,"
ip_id":82257,"type":"entry","ip":{"id":82257,"ip":"185.93.2.206","
version":4}}],"specifications":[{"id":8,"title":"Version","identif
ier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologi
es":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":3
5,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j
/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":42,"status":"on
line"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_id
s":[1,5],"location_ids":[87]},{"id":950271,"created_at":"2019-12-0
2 10:45:18","updated_at":"2025-02-24 16:40:25","name":"Japan #429"
,"station":"37.120.210.107","ipv6_station":"","hostname":"jp429.no
rdvpn.com","status":"online","load":29,"ips":[{"id":723494,"create
d_at":"2022-11-17 10:58:24","updated_at":"2022-11-17 10:58:24","se
rver_id":950271,"ip_id":85143,"type":"entry","ip":{"id":85143,"ip"
:"37.120.210.107","version":4}}],"specifications":[{"id":8,"title"
:"Version","identifier":"version","values":[{"id":257,"value":"2.1
.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status
":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"}
,{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_
key","value":"SAio0Z0suFlRfmydzPdcn6MamqS7Mq4pSOm2YmJkLSs="}],"sta
tus":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}
],"status":"online"}],"group_ids":[11,15,23],"service_ids":[1,5],"
location_ids":[3984]},{"id":950346,"created_at":"2019-12-03 07:26:
00","updated_at":"2025-02-24 16:40:25","name":"Spain #114","statio
n":"37.120.199.243","ipv6_station":"","hostname":"es114.nordvpn.co
m","status":"online","load":50,"ips":[{"id":1022015,"created_at":"
2023-07-14 12:08:53","updated_at":"2023-07-14 12:08:53","server_id
":950346,"ip_id":85356,"type":"entry","ip":{"id":85356,"ip":"37.12
0.199.243","version":4}}],"specifications":[{"id":8,"title":"Versi
on","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}]
,"technologies":[{"id":1,"status":"online"},{"id":3,"status":"onli
ne"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":
23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","v
alue":"IF1FGVSzrUznFVZ+dymIz+6bdlCgsuiT/d6cyapN8lw="}],"status":"o
nline"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"stat
us":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"locatio
n_ids":[113]},{"id":950361,"created_at":"2019-12-03 07:52:53","upd
ated_at":"2025-02-24 16:40:25","name":"Italy #132","station":"217.
138.197.75","ipv6_station":"","hostname":"it132.nordvpn.com","stat
us":"online","load":23,"ips":[{"id":939377,"created_at":"2023-06-2
0 06:54:02","updated_at":"2023-06-20 06:54:02","server_id":950361,
"ip_id":85416,"type":"entry","ip":{"id":85416,"ip":"217.138.197.75
","version":4}}],"specifications":[{"id":8,"title":"Version","iden
tifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technol
ogies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id
":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"statu
s":"online"},{"id":35,"metadata":[{"name":"public_key","value":"Fg
xaycYZ4t1kp4x7LDv60sczNTAl0h/d4pyyUNHhgBc="}],"status":"online"},{
"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"onli
ne"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[3
978]},{"id":950406,"created_at":"2019-12-03 09:17:57","updated_at"
:"2025-02-24 16:36:21","name":"United States #4735","station":"217
.138.198.235","ipv6_station":"","hostname":"us4735.nordvpn.com","s
tatus":"online","load":23,"ips":[{"id":438578,"created_at":"2021-1
2-08 11:11:25","updated_at":"2021-12-08 11:11:25","server_id":9504
06,"ip_id":85596,"type":"entry","ip":{"id":85596,"ip":"217.138.198
.235","version":4}}],"specifications":[{"id":8,"title":"Version","
identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"tec
hnologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},
{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"s
tatus":"online"},{"id":35,"metadata":[{"name":"public_key","value"
:"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"online
"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"
online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_ids
":[305]},{"id":950436,"created_at":"2019-12-03 09:54:36","updated_
at":"2025-02-24 16:40:26","name":"Poland #122","station":"37.120.2
11.171","ipv6_station":"","hostname":"pl122.nordvpn.com","status":
"online","load":37,"ips":[{"id":1020326,"created_at":"2023-07-14 0
7:43:43","updated_at":"2023-07-14 07:43:43","server_id":950436,"ip
_id":85716,"type":"entry","ip":{"id":85716,"ip":"37.120.211.171","
version":4}}],"specifications":[{"id":8,"title":"Version","identif
ier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologi
es":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5
,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":
"online"},{"id":35,"metadata":[{"name":"public_key","value":"kjAOz
XQRVGpmQdqE2zPsITH8QHmFK83AAPktqWed9wM="}],"status":"online"},{"id
":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"
}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[367]
},{"id":950481,"created_at":"2019-12-03 12:01:58","updated_at":"20
25-02-24 16:40:26","name":"Czech Republic #93","station":"217.138.
199.27","ipv6_station":"","hostname":"cz93.nordvpn.com","status":"
online","load":15,"ips":[{"id":1042049,"created_at":"2023-07-19 10
:40:00","updated_at":"2023-07-19 10:40:00","server_id":950481,"ip_
id":85899,"type":"entry","ip":{"id":85899,"ip":"217.138.199.27","v
ersion":4}}],"specifications":[{"id":8,"title":"Version","identifi
er":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologie
s":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,
"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"
online"},{"id":35,"metadata":[{"name":"public_key","value":"apEe1p
4IQvCQxexoxoUTXsm2p582FtbDAboPwThFYEs="}],"status":"online"},{"id"
:51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}
],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[143]}
,{"id":950538,"created_at":"2019-12-03 12:56:46","updated_at":"202
5-02-24 16:40:26","name":"Austria #80","station":"5.253.207.203","
ipv6_station":"","hostname":"at80.nordvpn.com","status":"online","
load":14,"ips":[{"id":1012112,"created_at":"2023-07-12 10:42:31","
updated_at":"2023-07-12 10:42:31","server_id":950538,"ip_id":86127
,"type":"entry","ip":{"id":86127,"ip":"5.253.207.203","version":4}
}],"specifications":[{"id":8,"title":"Version","identifier":"versi
on","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":
1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"
online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{
"id":35,"metadata":[{"name":"public_key","value":"F6b2ac9H7hEvt03E
onY1bS4FzNAabEmURDTB8wIIPXc="}],"status":"online"},{"id":51,"metad
ata":[{"name":"port","value":"8443"}],"status":"online"}],"group_i
ds":[11,15,19],"service_ids":[1,5],"location_ids":[205]},{"id":950
568,"created_at":"2019-12-03 13:48:18","updated_at":"2025-02-24 16
:40:26","name":"Romania #59","station":"86.106.137.187","ipv6_stat
ion":"","hostname":"ro59.nordvpn.com","status":"online","load":23,
"ips":[{"id":1043009,"created_at":"2023-07-19 11:39:41","updated_a
t":"2023-07-19 11:39:41","server_id":950568,"ip_id":86247,"type":"
entry","ip":{"id":86247,"ip":"86.106.137.187","version":4}}],"spec
ifications":[{"id":8,"title":"Version","identifier":"version","val
ues":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"statu
s":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"}
,{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,
"metadata":[{"name":"public_key","value":"o3Dj1qKYmzBBOBaD9JAhK9cg
/8nfYxWg6GADL09DPHE="}],"status":"online"},{"id":51,"metadata":[{"
name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,
15,19],"service_ids":[1,5],"location_ids":[65]},{"id":950598,"crea
ted_at":"2019-12-03 14:06:40","updated_at":"2025-02-24 16:36:22","
name":"Switzerland #198","station":"37.120.213.131","ipv6_station"
:"","hostname":"ch198.nordvpn.com","status":"online","load":19,"ip
s":[{"id":938273,"created_at":"2023-06-19 10:48:10","updated_at":"
2023-06-19 10:48:10","server_id":950598,"ip_id":86367,"type":"entr
y","ip":{"id":86367,"ip":"37.120.213.131","version":4}}],"specific
ations":[{"id":8,"title":"Version","identifier":"version","values"
:[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"
online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"i
d":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"met
adata":[{"name":"public_key","value":"SqAWBSVdnUJ859Bz2Nyt82rlSebM
wPgvwQxIb1DzyF8="}],"status":"online"},{"id":51,"metadata":[{"name
":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,1
9],"service_ids":[1,5],"location_ids":[107]},{"id":950628,"created
_at":"2019-12-03 14:25:53","updated_at":"2025-02-24 16:40:26","nam
e":"Bulgaria #38","station":"217.138.202.147","ipv6_station":"","h
ostname":"bg38.nordvpn.com","status":"online","load":7,"ips":[{"id
":1030013,"created_at":"2023-07-19 06:14:34","updated_at":"2023-07
-19 06:14:34","server_id":950628,"ip_id":86487,"type":"entry","ip"
:{"id":86487,"ip":"217.138.202.147","version":4}}],"specifications
":[{"id":8,"title":"Version","identifier":"version","values":[{"id
":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online
"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,
"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata"
:[{"name":"public_key","value":"xqa+kDsDeYLQAnVDUQaFun9Djfo3c1ESTM
wfNArHw10="}],"status":"online"},{"id":51,"metadata":[{"name":"por
t","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"se
rvice_ids":[1,5],"location_ids":[259]},{"id":950658,"created_at":"
2019-12-03 14:43:02","updated_at":"2025-02-24 16:36:22","name":"Hu
ngary #47","station":"217.138.192.99","ipv6_station":"","hostname"
:"hu47.nordvpn.com","status":"online","load":19,"ips":[{"id":10386
86,"created_at":"2023-07-19 09:30:15","updated_at":"2023-07-19 09:
30:15","server_id":950658,"ip_id":86607,"type":"entry","ip":{"id":
86607,"ip":"217.138.192.99","version":4}}],"specifications":[{"id"
:8,"title":"Version","identifier":"version","values":[{"id":257,"v
alue":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id"
:3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status"
:"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name
":"public_key","value":"3KWTCjpHlmXD3BroyAIFMN8ajr+ibShIl8OSUGgejX
Y="}],"status":"online"},{"id":51,"metadata":[{"name":"port","valu
e":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_id
s":[1,5],"location_ids":[247]},{"id":951120,"created_at":"2019-12-
09 11:56:08","updated_at":"2025-02-24 16:36:22","name":"France #45
2","station":"45.152.181.219","ipv6_station":"","hostname":"fr452.
nordvpn.com","status":"online","load":27,"ips":[{"id":965984,"crea
ted_at":"2023-06-27 13:02:08","updated_at":"2023-06-27 13:02:08","
server_id":951120,"ip_id":87555,"type":"entry","ip":{"id":87555,"i
p":"45.152.181.219","version":4}}],"specifications":[{"id":8,"titl
e":"Version","identifier":"version","values":[{"id":257,"value":"2
.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"stat
us":"online"},{"id":5,"status":"online"},{"id":21,"status":"online
"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"publi
c_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"s
tatus":"online"},{"id":51,"metadata":[{"name":"port","value":"8443
"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5]
,"location_ids":[87]},{"id":951123,"created_at":"2019-12-09 15:34:
59","updated_at":"2025-02-24 16:40:26","name":"Japan #454","statio
n":"89.187.161.54","ipv6_station":"","hostname":"jp454.nordvpn.com
","status":"online","load":22,"ips":[{"id":596243,"created_at":"20
22-07-08 07:48:04","updated_at":"2022-07-08 07:48:04","server_id":
951123,"ip_id":87579,"type":"entry","ip":{"id":87579,"ip":"89.187.
161.54","version":4}}],"specifications":[{"id":8,"title":"Version"
,"identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"t
echnologies":[{"id":1,"status":"online"},{"id":3,"status":"online"
},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,
"status":"online"},{"id":35,"metadata":[{"name":"public_key","valu
e":"SAio0Z0suFlRfmydzPdcn6MamqS7Mq4pSOm2YmJkLSs="}],"status":"onli
ne"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status"
:"online"}],"group_ids":[11,15,23],"service_ids":[1,5],"location_i
ds":[3984]},{"id":952599,"created_at":"2019-12-18 11:06:55","updat
ed_at":"2025-02-24 16:24:23","name":"United States #4951","station
":"84.17.44.122","ipv6_station":"","hostname":"us4951.nordvpn.com"
,"status":"online","load":1,"ips":[{"id":1809916,"created_at":"202
4-08-28 10:54:56","updated_at":"2024-08-28 10:54:56","server_id":9
52599,"ip_id":88899,"type":"entry","ip":{"id":88899,"ip":"84.17.44
.122","version":4}}],"specifications":[{"id":8,"title":"Version","
identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"tec
hnologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},
{"id":35,"metadata":[{"name":"public_key","value":"V1WC7wt34kcSDyq
PuUhN56NJ0v+GlqY9TwZR5WlzzB4="}],"status":"online"},{"id":42,"stat
us":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"ser
vice_ids":[1,5],"location_ids":[51]},{"id":956138,"created_at":"20
20-02-17 09:36:29","updated_at":"2025-02-24 16:40:26","name":"Denm
ark #150","station":"37.120.194.3","ipv6_station":"","hostname":"d
k150.nordvpn.com","status":"online","load":20,"ips":[{"id":1010432
,"created_at":"2023-07-12 09:16:23","updated_at":"2023-07-12 09:16
:23","server_id":956138,"ip_id":98828,"type":"entry","ip":{"id":98
828,"ip":"37.120.194.3","version":4}}],"specifications":[{"id":8,"
title":"Version","identifier":"version","values":[{"id":257,"value
":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"
status":"online"},{"id":5,"status":"online"},{"id":21,"status":"on
line"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"p
ublic_key","value":"EHL1zeXjZEJlqtFA8qaRVuvl0zR4skbC/AjiG66CLCc="}
],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"
8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[
1,5],"location_ids":[169]},{"id":956471,"created_at":"2020-02-25 0
8:28:44","updated_at":"2025-02-24 16:40:26","name":"Germany #750",
"station":"5.180.62.120","ipv6_station":"","hostname":"de750.nordv
pn.com","status":"online","load":17,"ips":[{"id":979883,"created_a
t":"2023-06-30 07:46:11","updated_at":"2023-06-30 07:46:11","serve
r_id":956471,"ip_id":102428,"type":"entry","ip":{"id":102428,"ip":
"5.180.62.120","version":4}}],"specifications":[{"id":8,"title":"V
ersion","identifier":"version","values":[{"id":257,"value":"2.1.0"
}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"
online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"
id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key
","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status
":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"
status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"loc
ation_ids":[133]},{"id":956477,"created_at":"2020-02-25 11:14:12",
"updated_at":"2025-02-24 16:40:26","name":"United States #4953","s
tation":"89.187.175.53","ipv6_station":"","hostname":"us4953.nordv
pn.com","status":"online","load":1,"ips":[{"id":1850299,"created_a
t":"2024-09-12 13:39:49","updated_at":"2024-09-12 13:39:49","serve
r_id":956477,"ip_id":102437,"type":"entry","ip":{"id":102437,"ip":
"89.187.175.53","version":4}}],"specifications":[{"id":8,"title":"
Version","identifier":"version","values":[{"id":200,"value":"2.0.0
"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":
"online"},{"id":35,"metadata":[{"name":"public_key","value":"8pRFH
/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI="}],"status":"online"},{"id
":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[
9,21],"service_ids":[1,5],"location_ids":[79]},{"id":956480,"creat
ed_at":"2020-02-25 11:14:13","updated_at":"2025-02-24 16:40:26","n
ame":"United States #4954","station":"89.187.175.54","ipv6_station
":"","hostname":"us4954.nordvpn.com","status":"online","load":5,"i
ps":[{"id":1812651,"created_at":"2024-08-28 12:13:26","updated_at"
:"2024-08-28 12:13:26","server_id":956480,"ip_id":102440,"type":"e
ntry","ip":{"id":102440,"ip":"89.187.175.54","version":4}}],"speci
fications":[{"id":8,"title":"Version","identifier":"version","valu
es":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status
":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name
":"public_key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdg
I="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"sta
tus":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_i
ds":[79]},{"id":956489,"created_at":"2020-02-25 12:24:48","updated
_at":"2025-02-24 16:40:26","name":"Poland #125","station":"217.138
.209.67","ipv6_station":"","hostname":"pl125.nordvpn.com","status"
:"online","load":25,"ips":[{"id":1020452,"created_at":"2023-07-14 
07:44:07","updated_at":"2023-07-14 07:44:07","server_id":956489,"i
p_id":102491,"type":"entry","ip":{"id":102491,"ip":"217.138.209.67
","version":4}}],"specifications":[{"id":8,"title":"Version","iden
tifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technol
ogies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id
":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"statu
s":"online"},{"id":35,"metadata":[{"name":"public_key","value":"kj
AOzXQRVGpmQdqE2zPsITH8QHmFK83AAPktqWed9wM="}],"status":"online"},{
"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"onli
ne"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[3
67]},{"id":956522,"created_at":"2020-02-28 10:10:05","updated_at":
"2025-02-24 16:36:22","name":"United States #5057","station":"217.
138.208.211","ipv6_station":"","hostname":"us5057.nordvpn.com","st
atus":"online","load":21,"ips":[{"id":438611,"created_at":"2021-12
-08 11:11:42","updated_at":"2021-12-08 11:11:42","server_id":95652
2,"ip_id":102632,"type":"entry","ip":{"id":102632,"ip":"217.138.20
8.211","version":4}}],"specifications":[{"id":8,"title":"Version",
"identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"te
chnologies":[{"id":1,"status":"online"},{"id":3,"status":"online"}
,{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"
status":"online"},{"id":35,"metadata":[{"name":"public_key","value
":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"onlin
e"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":
"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_id
s":[305]},{"id":956525,"created_at":"2020-02-28 10:10:06","updated
_at":"2025-02-24 16:40:26","name":"United States #5058","station":
"217.138.208.219","ipv6_station":"","hostname":"us5058.nordvpn.com
","status":"online","load":23,"ips":[{"id":438644,"created_at":"20
21-12-08 11:11:57","updated_at":"2021-12-08 11:11:57","server_id":
956525,"ip_id":102638,"type":"entry","ip":{"id":102638,"ip":"217.1
38.208.219","version":4}}],"specifications":[{"id":8,"title":"Vers
ion","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}
],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"onl
ine"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id"
:23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","
value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"
online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"sta
tus":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"locati
on_ids":[305]},{"id":956528,"created_at":"2020-02-28 10:10:06","up
dated_at":"2025-02-24 16:36:22","name":"United States #5059","stat
ion":"217.138.208.139","ipv6_station":"","hostname":"us5059.nordvp
n.com","status":"online","load":25,"ips":[{"id":438677,"created_at
":"2021-12-08 11:12:16","updated_at":"2021-12-08 11:12:16","server
_id":956528,"ip_id":102644,"type":"entry","ip":{"id":102644,"ip":"
217.138.208.139","version":4}}],"specifications":[{"id":8,"title":
"Version","identifier":"version","values":[{"id":257,"value":"2.1.
0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status"
:"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},
{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_k
ey","value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"stat
us":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}]
,"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"l
ocation_ids":[305]},{"id":956531,"created_at":"2020-02-28 10:10:07
","updated_at":"2025-02-24 16:40:26","name":"United States #5060",
"station":"217.138.208.147","ipv6_station":"","hostname":"us5060.n
ordvpn.com","status":"online","load":18,"ips":[{"id":438710,"creat
ed_at":"2021-12-08 11:12:34","updated_at":"2021-12-08 11:12:34","s
erver_id":956531,"ip_id":102650,"type":"entry","ip":{"id":102650,"
ip":"217.138.208.147","version":4}}],"specifications":[{"id":8,"ti
tle":"Version","identifier":"version","values":[{"id":257,"value":
"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"st
atus":"online"},{"id":5,"status":"online"},{"id":21,"status":"onli
ne"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"pub
lic_key","value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],
"status":"online"},{"id":51,"metadata":[{"name":"port","value":"84
43"}],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,
5],"location_ids":[305]},{"id":956603,"created_at":"2020-03-05 13:
10:47","updated_at":"2025-02-24 16:40:26","name":"Norway #141","st
ation":"37.120.203.163","ipv6_station":"","hostname":"no141.nordvp
n.com","status":"online","load":28,"ips":[{"id":924911,"created_at
":"2023-06-14 11:24:03","updated_at":"2023-06-14 11:24:03","server
_id":956603,"ip_id":106556,"type":"entry","ip":{"id":106556,"ip":"
37.120.203.163","version":4}}],"specifications":[{"id":8,"title":"
Version","identifier":"version","values":[{"id":257,"value":"2.1.0
"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":
"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{
"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_ke
y","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"statu
s":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],
"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"lo
cation_ids":[97]},{"id":956606,"created_at":"2020-03-05 13:10:47",
"updated_at":"2025-02-24 16:40:26","name":"Norway #142","station":
"37.120.203.171","ipv6_station":"","hostname":"no142.nordvpn.com",
"status":"online","load":10,"ips":[{"id":924866,"created_at":"2023
-06-14 11:23:43","updated_at":"2023-06-14 11:23:43","server_id":95
6606,"ip_id":106562,"type":"entry","ip":{"id":106562,"ip":"37.120.
203.171","version":4}}],"specifications":[{"id":8,"title":"Version
","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"
technologies":[{"id":1,"status":"online"},{"id":3,"status":"online
"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23
,"status":"online"},{"id":35,"metadata":[{"name":"public_key","val
ue":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"onl
ine"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status
":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_
ids":[97]},{"id":956609,"created_at":"2020-03-05 13:10:48","update
d_at":"2025-02-24 16:32:23","name":"Norway #143","station":"37.120
.203.179","ipv6_station":"","hostname":"no143.nordvpn.com","status
":"online","load":17,"ips":[{"id":917294,"created_at":"2023-06-06 
12:12:15","updated_at":"2023-06-06 12:12:15","server_id":956609,"i
p_id":106568,"type":"entry","ip":{"id":106568,"ip":"37.120.203.179
","version":4}}],"specifications":[{"id":8,"title":"Version","iden
tifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technol
ogies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id
":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"statu
s":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24
IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{
"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"onli
ne"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[9
7]},{"id":956612,"created_at":"2020-03-05 13:10:48","updated_at":"
2025-02-24 16:40:26","name":"Norway #144","station":"37.120.203.18
7","ipv6_station":"","hostname":"no144.nordvpn.com","status":"onli
ne","load":10,"ips":[{"id":917252,"created_at":"2023-06-06 12:11:2
7","updated_at":"2023-06-06 12:11:27","server_id":956612,"ip_id":1
06574,"type":"entry","ip":{"id":106574,"ip":"37.120.203.187","vers
ion":4}}],"specifications":[{"id":8,"title":"Version","identifier"
:"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":
[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"st
atus":"online"},{"id":21,"status":"online"},{"id":23,"status":"onl
ine"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN
0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51
,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"
group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"i
d":956615,"created_at":"2020-03-05 13:10:48","updated_at":"2025-02
-24 16:32:23","name":"Norway #145","station":"37.120.203.195","ipv
6_station":"","hostname":"no145.nordvpn.com","status":"online","lo
ad":13,"ips":[{"id":917210,"created_at":"2023-06-06 12:10:06","upd
ated_at":"2023-06-06 12:10:06","server_id":956615,"ip_id":106580,"
type":"entry","ip":{"id":106580,"ip":"37.120.203.195","version":4}
}],"specifications":[{"id":8,"title":"Version","identifier":"versi
on","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":
1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"
online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{
"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLp
FpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metad
ata":[{"name":"port","value":"8443"}],"status":"online"}],"group_i
ds":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":9566
18,"created_at":"2020-03-05 13:10:49","updated_at":"2025-02-24 16:
40:26","name":"Norway #146","station":"37.120.203.203","ipv6_stati
on":"","hostname":"no146.nordvpn.com","status":"online","load":12,
"ips":[{"id":917168,"created_at":"2023-06-06 12:09:17","updated_at
":"2023-06-06 12:09:17","server_id":956618,"ip_id":106586,"type":"
entry","ip":{"id":106586,"ip":"37.120.203.203","version":4}}],"spe
cifications":[{"id":8,"title":"Version","identifier":"version","va
lues":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"stat
us":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"
},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35
,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjc
I2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{
"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11
,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956621,"cre
ated_at":"2020-03-05 13:10:49","updated_at":"2025-02-24 16:40:26",
"name":"Norway #147","station":"37.120.203.211","ipv6_station":"",
"hostname":"no147.nordvpn.com","status":"online","load":14,"ips":[
{"id":917126,"created_at":"2023-06-06 12:08:21","updated_at":"2023
-06-06 12:08:21","server_id":956621,"ip_id":106592,"type":"entry",
"ip":{"id":106592,"ip":"37.120.203.211","version":4}}],"specificat
ions":[{"id":8,"title":"Version","identifier":"version","values":[
{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"on
line"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id"
:21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metad
ata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6
JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":
"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19]
,"service_ids":[1,5],"location_ids":[97]},{"id":956624,"created_at
":"2020-03-05 13:10:50","updated_at":"2025-02-24 16:40:26","name":
"Norway #148","station":"37.120.203.219","ipv6_station":"","hostna
me":"no148.nordvpn.com","status":"online","load":13,"ips":[{"id":9
17084,"created_at":"2023-06-06 12:07:34","updated_at":"2023-06-06 
12:07:34","server_id":956624,"ip_id":106598,"type":"entry","ip":{"
id":106598,"ip":"37.120.203.219","version":4}}],"specifications":[
{"id":8,"title":"Version","identifier":"version","values":[{"id":2
57,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},
{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"st
atus":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{
"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZSh
KjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port",
"value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"servi
ce_ids":[1,5],"location_ids":[97]},{"id":956627,"created_at":"2020
-03-05 13:10:50","updated_at":"2025-02-24 16:40:26","name":"Norway
 #149","station":"95.174.66.27","ipv6_station":"","hostname":"no14
9.nordvpn.com","status":"online","load":40,"ips":[{"id":917042,"cr
eated_at":"2023-06-06 12:07:05","updated_at":"2023-06-06 12:07:05"
,"server_id":956627,"ip_id":106604,"type":"entry","ip":{"id":10660
4,"ip":"95.174.66.27","version":4}}],"specifications":[{"id":8,"ti
tle":"Version","identifier":"version","values":[{"id":257,"value":
"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"st
atus":"online"},{"id":5,"status":"online"},{"id":21,"status":"onli
ne"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"pub
lic_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],
"status":"online"},{"id":51,"metadata":[{"name":"port","value":"84
43"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,
5],"location_ids":[97]},{"id":956636,"created_at":"2020-03-06 10:5
0:34","updated_at":"2025-02-24 16:40:26","name":"United Kingdom #1
785","station":"194.35.233.75","ipv6_station":"","hostname":"uk178
5.nordvpn.com","status":"online","load":16,"ips":[{"id":1031597,"c
reated_at":"2023-07-19 06:16:16","updated_at":"2023-07-19 06:16:16
","server_id":956636,"ip_id":70750,"type":"entry","ip":{"id":70750
,"ip":"194.35.233.75","version":4}}],"specifications":[{"id":8,"ti
tle":"Version","identifier":"version","values":[{"id":257,"value":
"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"st
atus":"online"},{"id":5,"status":"online"},{"id":21,"status":"onli
ne"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"pub
lic_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],
"status":"online"},{"id":51,"metadata":[{"name":"port","value":"84
43"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,
5],"location_ids":[45]},{"id":956693,"created_at":"2020-03-10 11:0
7:25","updated_at":"2025-02-24 16:40:26","name":"Hungary #49","sta
tion":"217.138.192.83","ipv6_station":"","hostname":"hu49.nordvpn.
com","status":"online","load":17,"ips":[{"id":1038770,"created_at"
:"2023-07-19 09:30:35","updated_at":"2023-07-19 09:30:35","server_
id":956693,"ip_id":86595,"type":"entry","ip":{"id":86595,"ip":"217
.138.192.83","version":4}}],"specifications":[{"id":8,"title":"Ver
sion","identifier":"version","values":[{"id":257,"value":"2.1.0"}]
}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"on
line"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id
":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key",
"value":"3KWTCjpHlmXD3BroyAIFMN8ajr+ibShIl8OSUGgejXY="}],"status":
"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"st
atus":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"locat
ion_ids":[247]},{"id":956696,"created_at":"2020-03-10 12:25:51","u
pdated_at":"2025-02-24 16:40:26","name":"France #536","station":"2
17.138.207.139","ipv6_station":"","hostname":"fr536.nordvpn.com","
status":"online","load":36,"ips":[{"id":966083,"created_at":"2023-
06-27 13:02:36","updated_at":"2023-06-27 13:02:36","server_id":956
696,"ip_id":107162,"type":"entry","ip":{"id":107162,"ip":"217.138.
207.139","version":4}}],"specifications":[{"id":8,"title":"Version
","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"
technologies":[{"id":1,"status":"online"},{"id":3,"status":"online
"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23
,"status":"online"},{"id":35,"metadata":[{"name":"public_key","val
ue":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"onl
ine"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status
":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_
ids":[87]},{"id":956699,"created_at":"2020-03-10 12:25:51","update
d_at":"2025-02-24 16:36:22","name":"France #537","station":"217.13
8.207.147","ipv6_station":"","hostname":"fr537.nordvpn.com","statu
s":"online","load":28,"ips":[{"id":966116,"created_at":"2023-06-27
 13:02:44","updated_at":"2023-06-27 13:02:44","server_id":956699,"
ip_id":107168,"type":"entry","ip":{"id":107168,"ip":"217.138.207.1
47","version":4}}],"specifications":[{"id":8,"title":"Version","id
entifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"techn
ologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"
id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"sta
tus":"online"},{"id":35,"metadata":[{"name":"public_key","value":"
FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"}
,{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"on
line"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":
[87]},{"id":956702,"created_at":"2020-03-10 12:25:51","updated_at"
:"2025-02-24 16:36:22","name":"France #538","station":"217.138.207
.155","ipv6_station":"","hostname":"fr538.nordvpn.com","status":"o
nline","load":49,"ips":[{"id":966149,"created_at":"2023-06-27 13:0
2:52","updated_at":"2023-06-27 13:02:52","server_id":956702,"ip_id
":107174,"type":"entry","ip":{"id":107174,"ip":"217.138.207.155","
version":4}}],"specifications":[{"id":8,"title":"Version","identif
ier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologi
es":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5
,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":
"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M
53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id
":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"
}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]}
,{"id":956705,"created_at":"2020-03-10 12:25:52","updated_at":"202
5-02-24 16:40:26","name":"France #539","station":"217.138.207.163"
,"ipv6_station":"","hostname":"fr539.nordvpn.com","status":"online
","load":19,"ips":[{"id":966182,"created_at":"2023-06-27 13:02:59"
,"updated_at":"2023-06-27 13:02:59","server_id":956705,"ip_id":107
180,"type":"entry","ip":{"id":107180,"ip":"217.138.207.163","versi
on":4}}],"specifications":[{"id":8,"title":"Version","identifier":
"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[
{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"sta
tus":"online"},{"id":21,"status":"online"},{"id":23,"status":"onli
ne"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4d
hBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,
"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"g
roup_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id
":956708,"created_at":"2020-03-10 12:25:52","updated_at":"2025-02-
24 16:40:26","name":"France #540","station":"217.138.207.195","ipv
6_station":"","hostname":"fr540.nordvpn.com","status":"online","lo
ad":27,"ips":[{"id":966215,"created_at":"2023-06-27 13:03:07","upd
ated_at":"2023-06-27 13:03:07","server_id":956708,"ip_id":107186,"
type":"entry","ip":{"id":107186,"ip":"217.138.207.195","version":4
}}],"specifications":[{"id":8,"title":"Version","identifier":"vers
ion","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id"
:1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":
"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},
{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/
2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"meta
data":[{"name":"port","value":"8443"}],"status":"online"}],"group_
ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956
711,"created_at":"2020-03-10 12:25:53","updated_at":"2025-02-24 16
:40:26","name":"France #541","station":"217.138.207.203","ipv6_sta
tion":"","hostname":"fr541.nordvpn.com","status":"online","load":2
7,"ips":[{"id":966248,"created_at":"2023-06-27 13:03:16","updated_
at":"2023-06-27 13:03:16","server_id":956711,"ip_id":107192,"type"
:"entry","ip":{"id":107192,"ip":"217.138.207.203","version":4}}],"
specifications":[{"id":8,"title":"Version","identifier":"version",
"values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"s
tatus":"online"},{"id":3,"status":"online"},{"id":5,"status":"onli
ne"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id"
:35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW
1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata"
:[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":
[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956714,"
created_at":"2020-03-10 12:25:53","updated_at":"2025-02-24 16:40:2
6","name":"France #542","station":"217.138.207.171","ipv6_station"
:"","hostname":"fr542.nordvpn.com","status":"online","load":25,"ip
s":[{"id":966281,"created_at":"2023-06-27 13:03:24","updated_at":"
2023-06-27 13:03:24","server_id":956714,"ip_id":107198,"type":"ent
ry","ip":{"id":107198,"ip":"217.138.207.171","version":4}}],"speci
fications":[{"id":8,"title":"Version","identifier":"version","valu
es":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status
":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},
{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"
metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/Eo
ZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"n
ame":"port","value":"8443"}],"status":"online"}],"group_ids":[11,1
5,19],"service_ids":[1,5],"location_ids":[87]},{"id":956717,"creat
ed_at":"2020-03-10 12:25:54","updated_at":"2025-02-24 16:40:26","n
ame":"France #543","station":"217.138.207.179","ipv6_station":"","
hostname":"fr543.nordvpn.com","status":"online","load":46,"ips":[{
"id":966314,"created_at":"2023-06-27 13:03:35","updated_at":"2023-
06-27 13:03:35","server_id":956717,"ip_id":107204,"type":"entry","
ip":{"id":107204,"ip":"217.138.207.179","version":4}}],"specificat
ions":[{"id":8,"title":"Version","identifier":"version","values":[
{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"on
line"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id"
:21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metad
ata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBg
zvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":
"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19]
,"service_ids":[1,5],"location_ids":[87]},{"id":956720,"created_at
":"2020-03-10 12:25:54","updated_at":"2025-02-24 16:40:26","name":
"France #544","station":"217.138.207.187","ipv6_station":"","hostn
ame":"fr544.nordvpn.com","status":"online","load":25,"ips":[{"id":
966347,"created_at":"2023-06-27 13:03:42","updated_at":"2023-06-27
 13:03:42","server_id":956720,"ip_id":107210,"type":"entry","ip":{
"id":107210,"ip":"217.138.207.187","version":4}}],"specifications"
:[{"id":8,"title":"Version","identifier":"version","values":[{"id"
:257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"
},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"
status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":
[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71
FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port
","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"ser
vice_ids":[1,5],"location_ids":[87]},{"id":956732,"created_at":"20
20-03-12 13:04:17","updated_at":"2025-02-24 16:40:26","name":"Swit
zerland #221","station":"91.132.136.235","ipv6_station":"","hostna
me":"ch221.nordvpn.com","status":"online","load":32,"ips":[{"id":9
38321,"created_at":"2023-06-19 10:48:33","updated_at":"2023-06-19 
10:48:33","server_id":956732,"ip_id":107477,"type":"entry","ip":{"
id":107477,"ip":"91.132.136.235","version":4}}],"specifications":[
{"id":8,"title":"Version","identifier":"version","values":[{"id":2
57,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},
{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"st
atus":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{
"name":"public_key","value":"SqAWBSVdnUJ859Bz2Nyt82rlSebMwPgvwQxIb
1DzyF8="}],"status":"online"},{"id":51,"metadata":[{"name":"port",
"value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"servi
ce_ids":[1,5],"location_ids":[107]}],"groups":[{"id":11,"created_a
t":"2017-06-13 13:43:00","updated_at":"2017-06-13 13:43:00","title
":"Standard VPN servers","identifier":"legacy_standard","type":{"i
d":3,"created_at":"2017-06-13 13:40:17","updated_at":"2017-06-13 1
3:40:23","title":"Legacy category","identifier":"legacy_group_cate
gory"}},{"id":15,"created_at":"2017-06-13 13:43:38","updated_at":"
2017-06-13 13:43:38","title":"P2P","identifier":"legacy_p2p","type
":{"id":3,"created_at":"2017-06-13 13:40:17","updated_at":"2017-06
-13 13:40:23","title":"Legacy category","identifier":"legacy_group
_category"}},{"id":19,"created_at":"2017-10-27 14:17:17","updated_
at":"2017-10-27 14:17:17","title":"Europe","identifier":"europe","
type":{"id":5,"created_at":"2017-10-27 14:16:30","updated_at":"201
7-10-27 14:16:30","title":"Regions","identifier":"regions"}},{"id"
:21,"created_at":"2017-10-27 14:23:03","updated_at":"2017-10-30 08
:09:48","title":"The Americas","identifier":"the_americas","type":
{"id":5,"created_at":"2017-10-27 14:16:30","updated_at":"2017-10-2
7 14:16:30","title":"Regions","identifier":"regions"}},{"id":9,"cr
eated_at":"2017-06-13 13:42:36","updated_at":"2018-08-22 12:54:48"
,"title":"Dedicated IP","identifier":"legacy_dedicated_ip","type":
{"id":3,"created_at":"2017-06-13 13:40:17","updated_at":"2017-06-1
3 13:40:23","title":"Legacy category","identifier":"legacy_group_c
ategory"}},{"id":23,"created_at":"2017-10-27 14:23:51","updated_at
":"2017-10-30 08:09:57","title":"Asia Pacific","identifier":"asia_
pacific","type":{"id":5,"created_at":"2017-10-27 14:16:30","update
d_at":"2017-10-27 14:16:30","title":"Regions","identifier":"region
s"}}],"services":[{"id":1,"name":"VPN","identifier":"vpn","created
_at":"2017-03-21 12:00:45","updated_at":"2017-05-25 13:12:31"},{"i
d":5,"name":"Proxy","identifier":"proxy","created_at":"2017-05-29 
19:38:30","updated_at":"2017-05-29 19:38:30"}],"locations":[{"id":
367,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14
:06:47","latitude":52.25,"longitude":21,"country":{"id":174,"name"
:"Poland","code":"PL","city":{"id":6863429,"name":"Warsaw","latitu
de":52.25,"longitude":21,"dns_name":"warsaw","hub_score":0}}},{"id
":247,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 
14:06:47","latitude":47.5,"longitude":19.083333,"country":{"id":98
,"name":"Hungary","code":"HU","city":{"id":3348344,"name":"Budapes
t","latitude":47.5,"longitude":19.083333,"dns_name":"budapest","hu
b_score":0}}},{"id":51,"created_at":"2017-06-15 14:06:47","updated
_at":"2017-06-15 14:06:47","latitude":34.0522222,"longitude":-118.
2427778,"country":{"id":228,"name":"United States","code":"US","ci
ty":{"id":8761958,"name":"Los Angeles","latitude":34.052222,"longi
tude":-118.242778,"dns_name":"los-angeles","hub_score":0}}},{"id":
205,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14
:06:47","latitude":48.2,"longitude":16.366667,"country":{"id":14,"
name":"Austria","code":"AT","city":{"id":448799,"name":"Vienna","l
atitude":48.2,"longitude":16.366667,"dns_name":"vienna","hub_score
":0}}},{"id":107,"created_at":"2017-06-15 14:06:47","updated_at":"
2017-06-15 14:06:47","latitude":47.366667,"longitude":8.55,"countr
y":{"id":209,"name":"Switzerland","code":"CH","city":{"id":1171814
,"name":"Zurich","latitude":47.366667,"longitude":8.55,"dns_name":
"zurich","hub_score":0}}},{"id":169,"created_at":"2017-06-15 14:06
:47","updated_at":"2017-06-15 14:06:47","latitude":55.666667,"long
itude":12.583333,"country":{"id":58,"name":"Denmark","code":"DK","
city":{"id":2382515,"name":"Copenhagen","latitude":55.666667,"long
itude":12.583333,"dns_name":"copenhagen","hub_score":0}}},{"id":97
,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06
:47","latitude":59.916667,"longitude":10.75,"country":{"id":163,"n
ame":"Norway","code":"NO","city":{"id":6127364,"name":"Oslo","lati
tude":59.916667,"longitude":10.75,"dns_name":"oslo","hub_score":0}
}},{"id":45,"created_at":"2017-06-15 14:06:47","updated_at":"2017-
06-15 14:06:47","latitude":51.514125,"longitude":-0.093689,"countr
y":{"id":227,"name":"United Kingdom","code":"GB","city":{"id":2989
907,"name":"London","latitude":51.514125,"longitude":-0.093689,"dn
s_name":"london","hub_score":0}}},{"id":87,"created_at":"2017-06-1
5 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":48.86666
7,"longitude":2.333333,"country":{"id":74,"name":"France","code":"
FR","city":{"id":2886284,"name":"Paris","latitude":48.866667,"long
itude":2.333333,"dns_name":"paris","hub_score":0}}},{"id":133,"cre
ated_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47",
"latitude":50.116667,"longitude":8.683333,"country":{"id":81,"name
":"Germany","code":"DE","city":{"id":2215709,"name":"Frankfurt","l
atitude":50.116667,"longitude":8.683333,"dns_name":"frankfurt","hu
b_score":0}}},{"id":19,"created_at":"2017-06-15 14:06:47","updated
_at":"2017-06-15 14:06:47","latitude":42.8863889,"longitude":-78.8
786111,"country":{"id":228,"name":"United States","code":"US","cit
y":{"id":8963153,"name":"Buffalo","latitude":42.886389,"longitude"
:-78.878611,"dns_name":"buffalo","hub_score":0}}},{"id":3990,"crea
ted_at":"2018-06-18 14:58:07","updated_at":"2018-06-18 14:58:07","
latitude":50.833333,"longitude":4.333333,"country":{"id":21,"name"
:"Belgium","code":"BE","city":{"id":654293,"name":"Brussels","lati
tude":50.833333,"longitude":4.333333,"dns_name":"brussels","hub_sc
ore":0}}},{"id":79,"created_at":"2017-06-15 14:06:47","updated_at"
:"2017-06-15 14:06:47","latitude":32.7833333,"longitude":-96.8,"co
untry":{"id":228,"name":"United States","code":"US","city":{"id":9
080300,"name":"Dallas","latitude":32.783333,"longitude":-96.8,"dns
_name":"dallas","hub_score":0}}},{"id":5,"created_at":"2017-06-15 
14:06:47","updated_at":"2017-06-15 14:06:47","latitude":52.35,"lon
gitude":4.916667,"country":{"id":153,"name":"Netherlands","code":"
NL","city":{"id":6076868,"name":"Amsterdam","latitude":52.35,"long
itude":4.916667,"dns_name":"amsterdam","hub_score":0}}},{"id":3984
,"created_at":"2018-06-18 14:45:14","updated_at":"2018-06-18 14:45
:14","latitude":35.685,"longitude":139.751389,"country":{"id":108,
"name":"Japan","code":"JP","city":{"id":4633349,"name":"Tokyo","la
titude":35.685,"longitude":139.751389,"dns_name":"tokyo","hub_scor
e":0}}},{"id":113,"created_at":"2017-06-15 14:06:47","updated_at":
"2017-06-15 14:06:47","latitude":40.408566,"longitude":-3.69222,"c
ountry":{"id":202,"name":"Spain","code":"ES","city":{"id":2619989,
"name":"Madrid","latitude":40.408566,"longitude":-3.69222,"dns_nam
e":"madrid","hub_score":0}}},{"id":3978,"created_at":"2018-06-18 1
1:48:51","updated_at":"2018-06-18 11:48:51","latitude":45.466667,"
longitude":9.2,"country":{"id":106,"name":"Italy","code":"IT","cit
y":{"id":4542737,"name":"Milan","latitude":45.466667,"longitude":9
.2,"dns_name":"milan","hub_score":0}}},{"id":305,"created_at":"201
7-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":40
.7141667,"longitude":-74.0063889,"country":{"id":228,"name":"Unite
d States","code":"US","city":{"id":8971718,"name":"New York","lati
tude":40.714167,"longitude":-74.006389,"dns_name":"new-york","hub_
score":0}}},{"id":143,"created_at":"2017-06-15 14:06:47","updated_
at":"2017-06-15 14:06:47","latitude":50.083333,"longitude":14.4666
67,"country":{"id":57,"name":"Czech Republic","code":"CZ","city":{
"id":2144945,"name":"Prague","latitude":50.083333,"longitude":14.4
66667,"dns_name":"prague","hub_score":0}}},{"id":65,"created_at":"
2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude"
:44.433333,"longitude":26.1,"country":{"id":179,"name":"Romania","
code":"RO","city":{"id":6953096,"name":"Bucharest","latitude":44.4
33333,"longitude":26.1,"dns_name":"bucharest","hub_score":0}}},{"i
d":259,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15
 14:06:47","latitude":42.6833333,"longitude":23.3166667,"country":
{"id":33,"name":"Bulgaria","code":"BG","city":{"id":777368,"name":
"Sofia","latitude":42.683333,"longitude":23.316667,"dns_name":"sof
ia","hub_score":0}}}],"technologies":[{"id":1,"name":"IKEv2/IPSec"
,"identifier":"ikev2","created_at":"2017-03-21 12:00:24","updated_
at":"2017-09-05 14:20:16","metadata":null,"pivot":{"technology_id"
:0,"server_id":0,"status":""}},{"id":3,"name":"OpenVPN UDP","ident
ifier":"openvpn_udp","created_at":"2017-05-04 08:03:24","updated_a
t":"2017-05-09 19:27:37","metadata":null,"pivot":{"technology_id":
0,"server_id":0,"status":""}},{"id":5,"name":"OpenVPN TCP","identi
fier":"openvpn_tcp","created_at":"2017-05-09 19:28:14","updated_at
":"2017-05-09 19:28:14","metadata":null,"pivot":{"technology_id":0
,"server_id":0,"status":""}},{"id":21,"name":"HTTP Proxy (SSL)","i
dentifier":"proxy_ssl","created_at":"2017-10-02 12:45:14","updated
_at":"2017-10-02 12:45:14","metadata":null,"pivot":{"technology_id
":0,"server_id":0,"status":""}},{"id":23,"name":"HTTP CyberSec Pro
xy (SSL)","identifier":"proxy_ssl_cybersec","created_at":"2017-10-
02 12:50:49","updated_at":"2017-10-02 12:50:49","metadata":null,"p
ivot":{"technology_id":0,"server_id":0,"status":""}},{"id":35,"nam
e":"Wireguard","identifier":"wireguard_udp","created_at":"2019-02-
14 14:08:43","updated_at":"2019-02-14 14:08:43","metadata":null,"p
ivot":{"technology_id":0,"server_id":0,"status":""}},{"id":51,"nam
e":"NordWhisper","identifier":"nordwhisper","created_at":"2024-10-
07 10:17:17","updated_at":"2024-10-07 10:17:17","metadata":null,"p
ivot":{"technology_id":0,"server_id":0,"status":""}},{"id":42,"nam
e":"OpenVPN UDP Dedicated","identifier":"openvpn_dedicated_udp","c
reated_at":"2019-09-19 14:49:18","updated_at":"2019-09-19 14:49:18
","metadata":null,"pivot":{"technology_id":0,"server_id":0,"status
":""}},{"id":45,"name":"OpenVPN TCP Dedicated","identifier":"openv
pn_dedicated_tcp","created_at":"2019-09-19 14:49:54","updated_at":
"2019-09-19 14:49:54","metadata":null,"pivot":{"technology_id":0,"
server_id":0,"status":""}}]}%                                     
(nyord_vpn) adam@Hamlet nyord_vpn %
```

---

_****_



Let me check the server handling code more closely:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



I see the issue. The code is trying to validate the country code against the locations in the cache, but the API response format has changed. The v2 API response has a different structure than what the code expects.

Let me check how the cache is being populated:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



I see the issue now. The code is expecting the API response to have a specific structure with "servers" and "locations" keys, but the actual API response is a list of server objects. Let me fix this by updating the server cache handling code:

---

_****_

```diff
              api_data = response.json()
  
+             # Process API response (v2 API returns a list of servers)
+             if not isinstance(api_data, list):
+                 self.logger.warning("Invalid API response format - expected list of servers")
+                 return None
+ 
              # Initialize cache data structure
              new_cache: ServerCache = {
              }
  
-             # Process API response (v2 API returns a dict with servers and locations)
-             if not isinstance(api_data, dict):
-                 self.logger.warning("Invalid API response format")
-                 return None
- 
-             # Extract servers
+             # Extract servers and build locations map
              servers: List[ServerInfo] = []
-             server_list = api_data.get("servers", [])
-             if isinstance(server_list, list):
-                 for item in server_list:
-                     if not isinstance(item, dict):
-                         continue
+             locations: Dict[str, ServerLocation] = {}
+ 
+             for item in api_data:
+                 if not isinstance(item, dict):
+                     continue
  
-                         # Get technologies
-                         technologies: List[Technology] = []
-                         for tech in item.get("technologies", []):
-                             if not isinstance(tech, dict):
-                                 continue
-                             tech_id = tech.get("id")
-                             if tech_id is None:
-                                 continue
-                             technology: Technology = {
-                                 "id": int(tech_id),
-                                 "status": str(tech.get("status", ""))
-                             }
-                             if tech.get("metadata"):
-                                 technology["metadata"] = cast(List[Dict[str, str]], tech["metadata"])
-                             technologies.append(technology)
+                 # Get technologies
+                 technologies: List[Technology] = []
+                 for tech in item.get("technologies", []):
+                     if not isinstance(tech, dict):
+                         continue
+                     tech_id = tech.get("id")
+                     if tech_id is None:
+                         continue
+                     technology: Technology = {
+                         "id": int(tech_id),
+                         "status": str(tech.get("status", ""))
+                     }
+                     if tech.get("metadata"):
+                         technology["metadata"] = cast(List[Dict[str, str]], tech["metadata"])
+                     technologies.append(technology)
  
-                         server_info: ServerInfo = {
-                             "hostname": str(item.get("hostname", "")),
-                             "location_ids": [str(lid) for lid in item.get("location_ids", [])],
-                             "status": str(item.get("status", "")),
-                             "load": int(item.get("load", 0)),
-                             "technologies": technologies
-                         }
-                         servers.append(server_info)
+                 # Create server info
+                 server_info: ServerInfo = {
+                     "hostname": str(item.get("hostname", "")),
+                     "location_ids": [str(lid) for lid in item.get("location_ids", [])],
+                     "status": str(item.get("status", "")),
+                     "load": int(item.get("load", 0)),
+                     "technologies": technologies
+                 }
+                 servers.append(server_info)
  
-             # Extract locations
-             locations: Dict[str, ServerLocation] = {}
-             locations_dict = api_data.get("locations", {})
-             if isinstance(locations_dict, dict):
-                 for loc_id, location_data in locations_dict.items():
-                     if not isinstance(location_data, dict):
-                         continue
-                     country_data = location_data.get("country", {})
-                     if isinstance(country_data, dict):
-                         country: Country = {
-                             "name": str(country_data.get("name", "")),
-                             "code": str(country_data.get("code", ""))
-                         }
-                         location: ServerLocation = {
-                             "id": str(loc_id),
-                             "country": country
-                         }
-                         locations[str(loc_id)] = location
+                 # Process locations
+                 for location_id in item.get("location_ids", []):
+                     if location_id not in locations:
+                         # Find location info in the API response
+                         location_data = next(
+                             (loc for loc in api_data.get("locations", [])
+                             if str(loc.get("id")) == str(location_id)),
+                             None
+                         )
+                         if location_data and isinstance(location_data, dict):
+                             country_data = location_data.get("country", {})
+                             if isinstance(country_data, dict):
+                                 country: Country = {
+                                     "name": str(country_data.get("name", "")),
+                                     "code": str(country_data.get("code", ""))
+                                 }
+                                 locations[str(location_id)] = {
+                                     "id": str(location_id),
+                                     "country": country
+                                 }
  
              new_cache["servers"] = servers
              new_cache["locations"] = locations
  
-             # Cache the data
-             cache_servers(cast(Dict[str, Any], new_cache))
-             
+             # Cache the results
              self._servers_cache = new_cache
              self._last_cache_update = time.time()
+             cache_servers(new_cache)
+ 
              return new_cache
  
```

---

_****_



Let me fix the linter errors:

---

_****_

```diff
                          # Find location info in the API response
                          location_data = next(
-                             (loc for loc in api_data.get("locations", [])
+                             (loc for loc in api_data
                              if str(loc.get("id")) == str(location_id)),
                              None
              self._servers_cache = new_cache
              self._last_cache_update = time.time()
-             cache_servers(new_cache)
+             cache_servers(cast(Dict[str, Any], new_cache))
  
              return new_cache
```

---

_****_



Now let me check the country code validation to ensure it works with the new cache structure:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



The country code validation looks correct - it's already using the cache structure we're maintaining. The issue was with how we were building the cache from the API response.

Let me check how we're filtering servers by country:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_





The server filtering code looks correct as well. The issue was with how we were building the cache from the API response. Let me check the API response structure more carefully:

---

_****_

```bash
curl -s https://api.nordvpn.com/v2/servers | jq '.[] | select(.location_ids[0] == 133) | {hostname, location_ids, country: .country.code}' | head -n 5
```

```
jq: error (at <stdin>:0): Cannot index array with string "location
_ids"

```

---

_****_



Let me try a different approach:

---

_****_

```bash
curl -s https://api.nordvpn.com/v2/servers | jq '.[0]' | head -n 20
```

```
jq: error (at <stdin>:0): Cannot index object with number

```

---

_****_





Let me try one more time:

---

_****_

```bash
curl -s https://api.nordvpn.com/v2/servers | head -n 20
```

```
(nyord_vpn) adam@Hamlet nyord_vpn % 
":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11,1
5],"service_ids":[1,5],"location_ids":[45]},{"id":945157,"created_
at":"2019-06-13 04:49:56","updated_at":"2025-02-24 16:36:21","name
":"United States #2939","station":"172.93.237.99","ipv6_station":"
","hostname":"us2939.nordvpn.com","status":"online","load":0,"ips"
:[{"id":138778,"created_at":"2019-07-09 14:15:11","updated_at":"20
19-07-09 14:15:11","server_id":945157,"ip_id":63127,"type":"entry"
,"ip":{"id":63127,"ip":"172.93.237.99","version":4}}],"specificati
ons":[{"id":8,"title":"Version","identifier":"version","values":[{
"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"onl
ine"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"pub
lic_key","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],
"status":"online"},{"id":42,"status":"online"},{"id":45,"status":"
online"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[1
9]},{"id":945160,"created_at":"2019-06-13 04:49:57","updated_at":"
2025-02-24 15:32:36","name":"United States #2940","station":"172.9
3.237.100","ipv6_station":"","hostname":"us2940.nordvpn.com","stat
us":"online","load":0,"ips":[{"id":139372,"created_at":"2019-07-09
 14:25:49","updated_at":"2019-07-09 14:25:49","server_id":945160,"
ip_id":63130,"type":"entry","ip":{"id":63130,"ip":"172.93.237.100"
,"version":4}}],"specifications":[{"id":8,"title":"Version","ident
ifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technolo
gies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id"
:35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4Q95ayR8TEB
YAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,"status":"
online"},{"id":45,"status":"online"}],"group_ids":[9,21],"service_
ids":[1,5],"location_ids":[19]},{"id":945916,"created_at":"2019-06
-25 11:49:45","updated_at":"2025-02-24 16:36:21","name":"Germany #
655","station":"194.31.54.4","ipv6_station":"","hostname":"de655.n
ordvpn.com","status":"online","load":3,"ips":[{"id":1773885,"creat
ed_at":"2024-08-21 05:08:31","updated_at":"2024-08-21 05:08:31","s
erver_id":945916,"ip_id":65179,"type":"entry","ip":{"id":65179,"ip
":"194.31.54.4","version":4}}],"specifications":[{"id":8,"title":"
Version","identifier":"version","values":[{"id":200,"value":"2.0.0
"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":
"online"},{"id":35,"metadata":[{"name":"public_key","value":"m0tej
5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status":"online"},{"id
":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[
9,19],"service_ids":[1,5],"location_ids":[133]},{"id":946435,"crea
ted_at":"2019-07-12 07:51:12","updated_at":"2025-02-24 16:40:25","
name":"United Kingdom #892","station":"195.206.170.3","ipv6_statio
n":"","hostname":"uk892.nordvpn.com","status":"online","load":19,"
ips":[{"id":1855574,"created_at":"2024-09-27 08:48:09","updated_at
":"2024-09-27 08:48:09","server_id":946435,"ip_id":68866,"type":"e
ntry","ip":{"id":68866,"ip":"195.206.170.3","version":4}}],"specif
ications":[{"id":8,"title":"Version","identifier":"version","value
s":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status"
:"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{
"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"m
etadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt
4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"na
me":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11
,15],"service_ids":[1,5],"location_ids":[45]},{"id":946441,"create
d_at":"2019-07-12 07:51:13","updated_at":"2025-02-24 16:40:25","na
me":"United Kingdom #894","station":"195.206.170.131","ipv6_statio
n":"","hostname":"uk894.nordvpn.com","status":"online","load":27,"
ips":[{"id":1856397,"created_at":"2024-10-03 12:49:58","updated_at
":"2024-10-03 12:49:58","server_id":946441,"ip_id":68872,"type":"e
ntry","ip":{"id":68872,"ip":"195.206.170.131","version":4}}],"spec
ifications":[{"id":8,"title":"Version","identifier":"version","val
ues":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"statu
s":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"}
,{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,
"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvC
vt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"
name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,
11,15],"service_ids":[1,5],"location_ids":[45]},{"id":947116,"crea
ted_at":"2019-08-06 07:35:03","updated_at":"2025-02-24 16:40:25","
name":"United Kingdom #896","station":"178.239.164.3","ipv6_statio
n":"","hostname":"uk896.nordvpn.com","status":"online","load":24,"
ips":[{"id":1855544,"created_at":"2024-09-27 08:46:21","updated_at
":"2024-09-27 08:46:21","server_id":947116,"ip_id":72133,"type":"e
ntry","ip":{"id":72133,"ip":"178.239.164.3","version":4}}],"specif
ications":[{"id":8,"title":"Version","identifier":"version","value
s":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status"
:"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{
"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"m
etadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvCvt
4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"na
me":"port","value":"8443"}],"status":"online"}],"group_ids":[19,11
,15],"service_ids":[1,5],"location_ids":[45]},{"id":947122,"create
d_at":"2019-08-06 07:35:04","updated_at":"2025-02-24 16:40:25","na
me":"United Kingdom #898","station":"178.239.164.131","ipv6_statio
n":"","hostname":"uk898.nordvpn.com","status":"online","load":21,"
ips":[{"id":1855524,"created_at":"2024-09-27 08:44:47","updated_at
":"2024-09-27 08:44:47","server_id":947122,"ip_id":72139,"type":"e
ntry","ip":{"id":72139,"ip":"178.239.164.131","version":4}}],"spec
ifications":[{"id":8,"title":"Version","identifier":"version","val
ues":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"statu
s":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"}
,{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,
"metadata":[{"name":"public_key","value":"K53l2wOIHU3262sX5N/5kAvC
vt4r55lNui30EbvaDlE="}],"status":"online"},{"id":51,"metadata":[{"
name":"port","value":"8443"}],"status":"online"}],"group_ids":[19,
15,11],"service_ids":[1,5],"location_ids":[45]},{"id":947235,"crea
ted_at":"2019-08-23 12:48:22","updated_at":"2025-02-24 16:32:22","
name":"United States #2943","station":"89.187.175.97","ipv6_statio
n":"","hostname":"us2943.nordvpn.com","status":"online","load":4,"
ips":[{"id":1818610,"created_at":"2024-08-29 11:50:57","updated_at
":"2024-08-29 11:50:57","server_id":947235,"ip_id":72639,"type":"e
ntry","ip":{"id":72639,"ip":"89.187.175.97","version":4}}],"specif
ications":[{"id":8,"title":"Version","identifier":"version","value
s":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status"
:"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name"
:"public_key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI
="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"stat
us":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_id
s":[79]},{"id":947238,"created_at":"2019-08-23 12:48:22","updated_
at":"2025-02-24 16:40:25","name":"United States #2944","station":"
89.187.175.98","ipv6_station":"","hostname":"us2944.nordvpn.com","
status":"online","load":2,"ips":[{"id":1810823,"created_at":"2024-
08-28 11:12:32","updated_at":"2024-08-28 11:12:32","server_id":947
238,"ip_id":72645,"type":"entry","ip":{"id":72645,"ip":"89.187.175
.98","version":4}}],"specifications":[{"id":8,"title":"Version","i
dentifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"tech
nologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},{
"id":35,"metadata":[{"name":"public_key","value":"8pRFH/FfMBs3eBJC
M2ABFoOs/13n78LYQvoovZVLdgI="}],"status":"online"},{"id":42,"statu
s":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"serv
ice_ids":[1,5],"location_ids":[79]},{"id":947280,"created_at":"201
9-08-28 06:59:11","updated_at":"2025-02-24 16:36:21","name":"Unite
d States #2945","station":"89.187.185.86","ipv6_station":"","hostn
ame":"us2945.nordvpn.com","status":"online","load":5,"ips":[{"id":
1821697,"created_at":"2024-08-30 04:42:38","updated_at":"2024-08-3
0 04:42:38","server_id":947280,"ip_id":73533,"type":"entry","ip":{
"id":73533,"ip":"89.187.185.86","version":4}}],"specifications":[{
"id":8,"title":"Version","identifier":"version","values":[{"id":20
0,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},{
"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_key
","value":"V1WC7wt34kcSDyqPuUhN56NJ0v+GlqY9TwZR5WlzzB4="}],"status
":"online"},{"id":42,"status":"online"},{"id":45,"status":"online"
}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[51]},{"i
d":947283,"created_at":"2019-08-28 06:59:11","updated_at":"2025-02
-24 16:16:39","name":"United States #2946","station":"89.187.185.9
7","ipv6_station":"","hostname":"us2946.nordvpn.com","status":"onl
ine","load":2,"ips":[{"id":1807685,"created_at":"2024-08-28 06:22:
30","updated_at":"2024-08-28 06:22:30","server_id":947283,"ip_id":
73536,"type":"entry","ip":{"id":73536,"ip":"89.187.185.97","versio
n":4}}],"specifications":[{"id":8,"title":"Version","identifier":"
version","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{
"id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"met
adata":[{"name":"public_key","value":"V1WC7wt34kcSDyqPuUhN56NJ0v+G
lqY9TwZR5WlzzB4="}],"status":"online"},{"id":42,"status":"online"}
,{"id":45,"status":"online"}],"group_ids":[9,21],"service_ids":[1,
5],"location_ids":[51]},{"id":947592,"created_at":"2019-09-18 09:5
1:34","updated_at":"2025-02-24 00:16:49","name":"Netherlands #408"
,"station":"185.229.58.3","ipv6_station":"","hostname":"nl408.nord
vpn.com","status":"online","load":0,"ips":[{"id":1751714,"created_
at":"2024-08-19 05:57:10","updated_at":"2024-08-19 05:57:10","serv
er_id":947592,"ip_id":74514,"type":"entry","ip":{"id":74514,"ip":"
185.229.58.3","version":4}}],"specifications":[{"id":8,"title":"Ve
rsion","identifier":"version","values":[{"id":200,"value":"2.0.0"}
]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":"o
nline"},{"id":35,"metadata":[{"name":"public_key","value":"5p4Rkyb
dRU5uaDi90eu4KZPTFif0lKCg4Qp6t1c4F30="}],"status":"online"},{"id":
42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,
19],"service_ids":[1,5],"location_ids":[5]},{"id":947595,"created_
at":"2019-09-18 09:51:34","updated_at":"2025-02-24 16:32:22","name
":"Netherlands #409","station":"185.229.58.129","ipv6_station":"",
"hostname":"nl409.nordvpn.com","status":"online","load":1,"ips":[{
"id":1768144,"created_at":"2024-08-20 07:16:03","updated_at":"2024
-08-20 07:16:03","server_id":947595,"ip_id":74517,"type":"entry","
ip":{"id":74517,"ip":"185.229.58.129","version":4}}],"specificatio
ns":[{"id":8,"title":"Version","identifier":"version","values":[{"
id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"onli
ne"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"publ
ic_key","value":"5p4RkybdRU5uaDi90eu4KZPTFif0lKCg4Qp6t1c4F30="}],"
status":"online"},{"id":42,"status":"online"},{"id":45,"status":"o
nline"}],"group_ids":[9,19],"service_ids":[1,5],"location_ids":[5]
},{"id":948099,"created_at":"2019-09-26 12:22:40","updated_at":"20
25-02-24 15:20:22","name":"Germany #676","station":"37.120.223.116
","ipv6_station":"","hostname":"de676.nordvpn.com","status":"onlin
e","load":0,"ips":[{"id":1791453,"created_at":"2024-08-26 11:14:49
","updated_at":"2024-08-26 11:14:49","server_id":948099,"ip_id":75
906,"type":"entry","ip":{"id":75906,"ip":"37.120.223.116","version
":4}}],"specifications":[{"id":8,"title":"Version","identifier":"v
ersion","values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"
id":3,"status":"online"},{"id":5,"status":"online"},{"id":35,"meta
data":[{"name":"public_key","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM8
1AChLlzlsOSjSs="}],"status":"online"},{"id":42,"status":"online"},
{"id":45,"status":"online"}],"group_ids":[9,19],"service_ids":[1,5
],"location_ids":[133]},{"id":948810,"created_at":"2019-10-11 09:0
6:37","updated_at":"2025-02-24 16:40:25","name":"United States #50
55","station":"89.187.175.2","ipv6_station":"","hostname":"us5055.
nordvpn.com","status":"online","load":13,"ips":[{"id":795035,"crea
ted_at":"2023-01-16 13:35:10","updated_at":"2023-01-16 13:35:10","
server_id":948810,"ip_id":78471,"type":"entry","ip":{"id":78471,"i
p":"89.187.175.2","version":4}}],"specifications":[{"id":8,"title"
:"Version","identifier":"version","values":[{"id":257,"value":"2.1
.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status
":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"}
,{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_
key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI="}],"sta
tus":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}
],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"
location_ids":[79]},{"id":949095,"created_at":"2019-10-29 07:51:33
","updated_at":"2025-02-24 16:16:22","name":"United States #2949",
"station":"64.44.32.75","ipv6_station":"","hostname":"us2949.nordv
pn.com","status":"online","load":0,"ips":[{"id":155328,"created_at
":"2019-10-30 08:32:23","updated_at":"2019-10-30 08:32:23","server
_id":949095,"ip_id":80337,"type":"entry","ip":{"id":80337,"ip":"64
.44.32.75","version":4}}],"specifications":[{"id":8,"title":"Versi
on","identifier":"version","values":[{"id":200,"value":"2.0.0"}]}]
,"technologies":[{"id":3,"status":"online"},{"id":5,"status":"onli
ne"},{"id":35,"metadata":[{"name":"public_key","value":"dzMgdcXyF4
Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"status":"online"},{"id":42,
"status":"online"},{"id":45,"status":"online"}],"group_ids":[9,21]
,"service_ids":[1,5],"location_ids":[19]},{"id":949098,"created_at
":"2019-10-29 07:51:33","updated_at":"2025-02-24 16:32:22","name":
"United States #2950","station":"64.44.32.76","ipv6_station":"","h
ostname":"us2950.nordvpn.com","status":"online","load":0,"ips":[{"
id":193733,"created_at":"2020-04-28 07:18:59","updated_at":"2020-0
4-28 07:18:59","server_id":949098,"ip_id":80340,"type":"entry","ip
":{"id":80340,"ip":"64.44.32.76","version":4}}],"specifications":[
{"id":8,"title":"Version","identifier":"version","values":[{"id":2
00,"value":"2.0.0"}]}],"technologies":[{"id":3,"status":"online"},
{"id":5,"status":"online"},{"id":35,"metadata":[{"name":"public_ke
y","value":"dzMgdcXyF4Q95ayR8TEBYAL5Op+RuFEB/WGq2usxkFA="}],"statu
s":"online"},{"id":42,"status":"online"},{"id":45,"status":"online
"}],"group_ids":[9,21],"service_ids":[1,5],"location_ids":[19]},{"
id":949581,"created_at":"2019-11-20 07:55:10","updated_at":"2025-0
2-24 16:40:25","name":"France #439","station":"185.93.2.199","ipv6
_station":"","hostname":"fr439.nordvpn.com","status":"online","loa
d":5,"ips":[{"id":1803435,"created_at":"2024-08-27 13:14:39","upda
ted_at":"2024-08-27 13:14:39","server_id":949581,"ip_id":82254,"ty
pe":"entry","ip":{"id":82254,"ip":"185.93.2.199","version":4}}],"s
pecifications":[{"id":8,"title":"Version","identifier":"version","
values":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"st
atus":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"
name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlL
ZLDBM="}],"status":"online"},{"id":42,"status":"online"},{"id":45,
"status":"online"}],"group_ids":[9,19],"service_ids":[1,5],"locati
on_ids":[87]},{"id":949584,"created_at":"2019-11-20 07:55:10","upd
ated_at":"2025-02-24 16:36:21","name":"France #440","station":"185
.93.2.206","ipv6_station":"","hostname":"fr440.nordvpn.com","statu
s":"online","load":6,"ips":[{"id":1779073,"created_at":"2024-08-22
 08:12:09","updated_at":"2024-08-22 08:12:09","server_id":949584,"
ip_id":82257,"type":"entry","ip":{"id":82257,"ip":"185.93.2.206","
version":4}}],"specifications":[{"id":8,"title":"Version","identif
ier":"version","values":[{"id":200,"value":"2.0.0"}]}],"technologi
es":[{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":3
5,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j
/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":42,"status":"on
line"},{"id":45,"status":"online"}],"group_ids":[9,19],"service_id
s":[1,5],"location_ids":[87]},{"id":950271,"created_at":"2019-12-0
2 10:45:18","updated_at":"2025-02-24 16:40:25","name":"Japan #429"
,"station":"37.120.210.107","ipv6_station":"","hostname":"jp429.no
rdvpn.com","status":"online","load":29,"ips":[{"id":723494,"create
d_at":"2022-11-17 10:58:24","updated_at":"2022-11-17 10:58:24","se
rver_id":950271,"ip_id":85143,"type":"entry","ip":{"id":85143,"ip"
:"37.120.210.107","version":4}}],"specifications":[{"id":8,"title"
:"Version","identifier":"version","values":[{"id":257,"value":"2.1
.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status
":"online"},{"id":5,"status":"online"},{"id":21,"status":"online"}
,{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_
key","value":"SAio0Z0suFlRfmydzPdcn6MamqS7Mq4pSOm2YmJkLSs="}],"sta
tus":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}
],"status":"online"}],"group_ids":[11,15,23],"service_ids":[1,5],"
location_ids":[3984]},{"id":950346,"created_at":"2019-12-03 07:26:
00","updated_at":"2025-02-24 16:40:25","name":"Spain #114","statio
n":"37.120.199.243","ipv6_station":"","hostname":"es114.nordvpn.co
m","status":"online","load":50,"ips":[{"id":1022015,"created_at":"
2023-07-14 12:08:53","updated_at":"2023-07-14 12:08:53","server_id
":950346,"ip_id":85356,"type":"entry","ip":{"id":85356,"ip":"37.12
0.199.243","version":4}}],"specifications":[{"id":8,"title":"Versi
on","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}]
,"technologies":[{"id":1,"status":"online"},{"id":3,"status":"onli
ne"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":
23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","v
alue":"IF1FGVSzrUznFVZ+dymIz+6bdlCgsuiT/d6cyapN8lw="}],"status":"o
nline"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"stat
us":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"locatio
n_ids":[113]},{"id":950361,"created_at":"2019-12-03 07:52:53","upd
ated_at":"2025-02-24 16:40:25","name":"Italy #132","station":"217.
138.197.75","ipv6_station":"","hostname":"it132.nordvpn.com","stat
us":"online","load":23,"ips":[{"id":939377,"created_at":"2023-06-2
0 06:54:02","updated_at":"2023-06-20 06:54:02","server_id":950361,
"ip_id":85416,"type":"entry","ip":{"id":85416,"ip":"217.138.197.75
","version":4}}],"specifications":[{"id":8,"title":"Version","iden
tifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technol
ogies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id
":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"statu
s":"online"},{"id":35,"metadata":[{"name":"public_key","value":"Fg
xaycYZ4t1kp4x7LDv60sczNTAl0h/d4pyyUNHhgBc="}],"status":"online"},{
"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"onli
ne"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[3
978]},{"id":950406,"created_at":"2019-12-03 09:17:57","updated_at"
:"2025-02-24 16:36:21","name":"United States #4735","station":"217
.138.198.235","ipv6_station":"","hostname":"us4735.nordvpn.com","s
tatus":"online","load":23,"ips":[{"id":438578,"created_at":"2021-1
2-08 11:11:25","updated_at":"2021-12-08 11:11:25","server_id":9504
06,"ip_id":85596,"type":"entry","ip":{"id":85596,"ip":"217.138.198
.235","version":4}}],"specifications":[{"id":8,"title":"Version","
identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"tec
hnologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},
{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"s
tatus":"online"},{"id":35,"metadata":[{"name":"public_key","value"
:"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"online
"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"
online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_ids
":[305]},{"id":950436,"created_at":"2019-12-03 09:54:36","updated_
at":"2025-02-24 16:40:26","name":"Poland #122","station":"37.120.2
11.171","ipv6_station":"","hostname":"pl122.nordvpn.com","status":
"online","load":37,"ips":[{"id":1020326,"created_at":"2023-07-14 0
7:43:43","updated_at":"2023-07-14 07:43:43","server_id":950436,"ip
_id":85716,"type":"entry","ip":{"id":85716,"ip":"37.120.211.171","
version":4}}],"specifications":[{"id":8,"title":"Version","identif
ier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologi
es":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5
,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":
"online"},{"id":35,"metadata":[{"name":"public_key","value":"kjAOz
XQRVGpmQdqE2zPsITH8QHmFK83AAPktqWed9wM="}],"status":"online"},{"id
":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"
}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[367]
},{"id":950481,"created_at":"2019-12-03 12:01:58","updated_at":"20
25-02-24 16:40:26","name":"Czech Republic #93","station":"217.138.
199.27","ipv6_station":"","hostname":"cz93.nordvpn.com","status":"
online","load":15,"ips":[{"id":1042049,"created_at":"2023-07-19 10
:40:00","updated_at":"2023-07-19 10:40:00","server_id":950481,"ip_
id":85899,"type":"entry","ip":{"id":85899,"ip":"217.138.199.27","v
ersion":4}}],"specifications":[{"id":8,"title":"Version","identifi
er":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologie
s":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,
"status":"online"},{"id":21,"status":"online"},{"id":23,"status":"
online"},{"id":35,"metadata":[{"name":"public_key","value":"apEe1p
4IQvCQxexoxoUTXsm2p582FtbDAboPwThFYEs="}],"status":"online"},{"id"
:51,"metadata":[{"name":"port","value":"8443"}],"status":"online"}
],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[143]}
,{"id":950538,"created_at":"2019-12-03 12:56:46","updated_at":"202
5-02-24 16:40:26","name":"Austria #80","station":"5.253.207.203","
ipv6_station":"","hostname":"at80.nordvpn.com","status":"online","
load":14,"ips":[{"id":1012112,"created_at":"2023-07-12 10:42:31","
updated_at":"2023-07-12 10:42:31","server_id":950538,"ip_id":86127
,"type":"entry","ip":{"id":86127,"ip":"5.253.207.203","version":4}
}],"specifications":[{"id":8,"title":"Version","identifier":"versi
on","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":
1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"
online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{
"id":35,"metadata":[{"name":"public_key","value":"F6b2ac9H7hEvt03E
onY1bS4FzNAabEmURDTB8wIIPXc="}],"status":"online"},{"id":51,"metad
ata":[{"name":"port","value":"8443"}],"status":"online"}],"group_i
ds":[11,15,19],"service_ids":[1,5],"location_ids":[205]},{"id":950
568,"created_at":"2019-12-03 13:48:18","updated_at":"2025-02-24 16
:40:26","name":"Romania #59","station":"86.106.137.187","ipv6_stat
ion":"","hostname":"ro59.nordvpn.com","status":"online","load":23,
"ips":[{"id":1043009,"created_at":"2023-07-19 11:39:41","updated_a
t":"2023-07-19 11:39:41","server_id":950568,"ip_id":86247,"type":"
entry","ip":{"id":86247,"ip":"86.106.137.187","version":4}}],"spec
ifications":[{"id":8,"title":"Version","identifier":"version","val
ues":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"statu
s":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"}
,{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,
"metadata":[{"name":"public_key","value":"o3Dj1qKYmzBBOBaD9JAhK9cg
/8nfYxWg6GADL09DPHE="}],"status":"online"},{"id":51,"metadata":[{"
name":"port","value":"8443"}],"status":"online"}],"group_ids":[11,
15,19],"service_ids":[1,5],"location_ids":[65]},{"id":950598,"crea
ted_at":"2019-12-03 14:06:40","updated_at":"2025-02-24 16:36:22","
name":"Switzerland #198","station":"37.120.213.131","ipv6_station"
:"","hostname":"ch198.nordvpn.com","status":"online","load":19,"ip
s":[{"id":938273,"created_at":"2023-06-19 10:48:10","updated_at":"
2023-06-19 10:48:10","server_id":950598,"ip_id":86367,"type":"entr
y","ip":{"id":86367,"ip":"37.120.213.131","version":4}}],"specific
ations":[{"id":8,"title":"Version","identifier":"version","values"
:[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"
online"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"i
d":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"met
adata":[{"name":"public_key","value":"SqAWBSVdnUJ859Bz2Nyt82rlSebM
wPgvwQxIb1DzyF8="}],"status":"online"},{"id":51,"metadata":[{"name
":"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,1
9],"service_ids":[1,5],"location_ids":[107]},{"id":950628,"created
_at":"2019-12-03 14:25:53","updated_at":"2025-02-24 16:40:26","nam
e":"Bulgaria #38","station":"217.138.202.147","ipv6_station":"","h
ostname":"bg38.nordvpn.com","status":"online","load":7,"ips":[{"id
":1030013,"created_at":"2023-07-19 06:14:34","updated_at":"2023-07
-19 06:14:34","server_id":950628,"ip_id":86487,"type":"entry","ip"
:{"id":86487,"ip":"217.138.202.147","version":4}}],"specifications
":[{"id":8,"title":"Version","identifier":"version","values":[{"id
":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online
"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,
"status":"online"},{"id":23,"status":"online"},{"id":35,"metadata"
:[{"name":"public_key","value":"xqa+kDsDeYLQAnVDUQaFun9Djfo3c1ESTM
wfNArHw10="}],"status":"online"},{"id":51,"metadata":[{"name":"por
t","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"se
rvice_ids":[1,5],"location_ids":[259]},{"id":950658,"created_at":"
2019-12-03 14:43:02","updated_at":"2025-02-24 16:36:22","name":"Hu
ngary #47","station":"217.138.192.99","ipv6_station":"","hostname"
:"hu47.nordvpn.com","status":"online","load":19,"ips":[{"id":10386
86,"created_at":"2023-07-19 09:30:15","updated_at":"2023-07-19 09:
30:15","server_id":950658,"ip_id":86607,"type":"entry","ip":{"id":
86607,"ip":"217.138.192.99","version":4}}],"specifications":[{"id"
:8,"title":"Version","identifier":"version","values":[{"id":257,"v
alue":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id"
:3,"status":"online"},{"id":5,"status":"online"},{"id":21,"status"
:"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name
":"public_key","value":"3KWTCjpHlmXD3BroyAIFMN8ajr+ibShIl8OSUGgejX
Y="}],"status":"online"},{"id":51,"metadata":[{"name":"port","valu
e":"8443"}],"status":"online"}],"group_ids":[11,15,19],"service_id
s":[1,5],"location_ids":[247]},{"id":951120,"created_at":"2019-12-
09 11:56:08","updated_at":"2025-02-24 16:36:22","name":"France #45
2","station":"45.152.181.219","ipv6_station":"","hostname":"fr452.
nordvpn.com","status":"online","load":27,"ips":[{"id":965984,"crea
ted_at":"2023-06-27 13:02:08","updated_at":"2023-06-27 13:02:08","
server_id":951120,"ip_id":87555,"type":"entry","ip":{"id":87555,"i
p":"45.152.181.219","version":4}}],"specifications":[{"id":8,"titl
e":"Version","identifier":"version","values":[{"id":257,"value":"2
.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"stat
us":"online"},{"id":5,"status":"online"},{"id":21,"status":"online
"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"publi
c_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"s
tatus":"online"},{"id":51,"metadata":[{"name":"port","value":"8443
"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5]
,"location_ids":[87]},{"id":951123,"created_at":"2019-12-09 15:34:
59","updated_at":"2025-02-24 16:40:26","name":"Japan #454","statio
n":"89.187.161.54","ipv6_station":"","hostname":"jp454.nordvpn.com
","status":"online","load":22,"ips":[{"id":596243,"created_at":"20
22-07-08 07:48:04","updated_at":"2022-07-08 07:48:04","server_id":
951123,"ip_id":87579,"type":"entry","ip":{"id":87579,"ip":"89.187.
161.54","version":4}}],"specifications":[{"id":8,"title":"Version"
,"identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"t
echnologies":[{"id":1,"status":"online"},{"id":3,"status":"online"
},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,
"status":"online"},{"id":35,"metadata":[{"name":"public_key","valu
e":"SAio0Z0suFlRfmydzPdcn6MamqS7Mq4pSOm2YmJkLSs="}],"status":"onli
ne"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status"
:"online"}],"group_ids":[11,15,23],"service_ids":[1,5],"location_i
ds":[3984]},{"id":952599,"created_at":"2019-12-18 11:06:55","updat
ed_at":"2025-02-24 16:24:23","name":"United States #4951","station
":"84.17.44.122","ipv6_station":"","hostname":"us4951.nordvpn.com"
,"status":"online","load":1,"ips":[{"id":1809916,"created_at":"202
4-08-28 10:54:56","updated_at":"2024-08-28 10:54:56","server_id":9
52599,"ip_id":88899,"type":"entry","ip":{"id":88899,"ip":"84.17.44
.122","version":4}}],"specifications":[{"id":8,"title":"Version","
identifier":"version","values":[{"id":200,"value":"2.0.0"}]}],"tec
hnologies":[{"id":3,"status":"online"},{"id":5,"status":"online"},
{"id":35,"metadata":[{"name":"public_key","value":"V1WC7wt34kcSDyq
PuUhN56NJ0v+GlqY9TwZR5WlzzB4="}],"status":"online"},{"id":42,"stat
us":"online"},{"id":45,"status":"online"}],"group_ids":[9,21],"ser
vice_ids":[1,5],"location_ids":[51]},{"id":956138,"created_at":"20
20-02-17 09:36:29","updated_at":"2025-02-24 16:40:26","name":"Denm
ark #150","station":"37.120.194.3","ipv6_station":"","hostname":"d
k150.nordvpn.com","status":"online","load":20,"ips":[{"id":1010432
,"created_at":"2023-07-12 09:16:23","updated_at":"2023-07-12 09:16
:23","server_id":956138,"ip_id":98828,"type":"entry","ip":{"id":98
828,"ip":"37.120.194.3","version":4}}],"specifications":[{"id":8,"
title":"Version","identifier":"version","values":[{"id":257,"value
":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"
status":"online"},{"id":5,"status":"online"},{"id":21,"status":"on
line"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"p
ublic_key","value":"EHL1zeXjZEJlqtFA8qaRVuvl0zR4skbC/AjiG66CLCc="}
],"status":"online"},{"id":51,"metadata":[{"name":"port","value":"
8443"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[
1,5],"location_ids":[169]},{"id":956471,"created_at":"2020-02-25 0
8:28:44","updated_at":"2025-02-24 16:40:26","name":"Germany #750",
"station":"5.180.62.120","ipv6_station":"","hostname":"de750.nordv
pn.com","status":"online","load":17,"ips":[{"id":979883,"created_a
t":"2023-06-30 07:46:11","updated_at":"2023-06-30 07:46:11","serve
r_id":956471,"ip_id":102428,"type":"entry","ip":{"id":102428,"ip":
"5.180.62.120","version":4}}],"specifications":[{"id":8,"title":"V
ersion","identifier":"version","values":[{"id":257,"value":"2.1.0"
}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"
online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"
id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key
","value":"m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="}],"status
":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"
status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"loc
ation_ids":[133]},{"id":956477,"created_at":"2020-02-25 11:14:12",
"updated_at":"2025-02-24 16:40:26","name":"United States #4953","s
tation":"89.187.175.53","ipv6_station":"","hostname":"us4953.nordv
pn.com","status":"online","load":1,"ips":[{"id":1850299,"created_a
t":"2024-09-12 13:39:49","updated_at":"2024-09-12 13:39:49","serve
r_id":956477,"ip_id":102437,"type":"entry","ip":{"id":102437,"ip":
"89.187.175.53","version":4}}],"specifications":[{"id":8,"title":"
Version","identifier":"version","values":[{"id":200,"value":"2.0.0
"}]}],"technologies":[{"id":3,"status":"online"},{"id":5,"status":
"online"},{"id":35,"metadata":[{"name":"public_key","value":"8pRFH
/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdgI="}],"status":"online"},{"id
":42,"status":"online"},{"id":45,"status":"online"}],"group_ids":[
9,21],"service_ids":[1,5],"location_ids":[79]},{"id":956480,"creat
ed_at":"2020-02-25 11:14:13","updated_at":"2025-02-24 16:40:26","n
ame":"United States #4954","station":"89.187.175.54","ipv6_station
":"","hostname":"us4954.nordvpn.com","status":"online","load":5,"i
ps":[{"id":1812651,"created_at":"2024-08-28 12:13:26","updated_at"
:"2024-08-28 12:13:26","server_id":956480,"ip_id":102440,"type":"e
ntry","ip":{"id":102440,"ip":"89.187.175.54","version":4}}],"speci
fications":[{"id":8,"title":"Version","identifier":"version","valu
es":[{"id":200,"value":"2.0.0"}]}],"technologies":[{"id":3,"status
":"online"},{"id":5,"status":"online"},{"id":35,"metadata":[{"name
":"public_key","value":"8pRFH/FfMBs3eBJCM2ABFoOs/13n78LYQvoovZVLdg
I="}],"status":"online"},{"id":42,"status":"online"},{"id":45,"sta
tus":"online"}],"group_ids":[9,21],"service_ids":[1,5],"location_i
ds":[79]},{"id":956489,"created_at":"2020-02-25 12:24:48","updated
_at":"2025-02-24 16:40:26","name":"Poland #125","station":"217.138
.209.67","ipv6_station":"","hostname":"pl125.nordvpn.com","status"
:"online","load":25,"ips":[{"id":1020452,"created_at":"2023-07-14
07:44:07","updated_at":"2023-07-14 07:44:07","server_id":956489,"i
p_id":102491,"type":"entry","ip":{"id":102491,"ip":"217.138.209.67
","version":4}}],"specifications":[{"id":8,"title":"Version","iden
tifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technol
ogies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id
":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"statu
s":"online"},{"id":35,"metadata":[{"name":"public_key","value":"kj
AOzXQRVGpmQdqE2zPsITH8QHmFK83AAPktqWed9wM="}],"status":"online"},{
"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"onli
ne"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[3
67]},{"id":956522,"created_at":"2020-02-28 10:10:05","updated_at":
"2025-02-24 16:36:22","name":"United States #5057","station":"217.
138.208.211","ipv6_station":"","hostname":"us5057.nordvpn.com","st
atus":"online","load":21,"ips":[{"id":438611,"created_at":"2021-12
-08 11:11:42","updated_at":"2021-12-08 11:11:42","server_id":95652
2,"ip_id":102632,"type":"entry","ip":{"id":102632,"ip":"217.138.20
8.211","version":4}}],"specifications":[{"id":8,"title":"Version",
"identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"te
chnologies":[{"id":1,"status":"online"},{"id":3,"status":"online"}
,{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"
status":"online"},{"id":35,"metadata":[{"name":"public_key","value
":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"onlin
e"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":
"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"location_id
s":[305]},{"id":956525,"created_at":"2020-02-28 10:10:06","updated
_at":"2025-02-24 16:40:26","name":"United States #5058","station":
"217.138.208.219","ipv6_station":"","hostname":"us5058.nordvpn.com
","status":"online","load":23,"ips":[{"id":438644,"created_at":"20
21-12-08 11:11:57","updated_at":"2021-12-08 11:11:57","server_id":
956525,"ip_id":102638,"type":"entry","ip":{"id":102638,"ip":"217.1
38.208.219","version":4}}],"specifications":[{"id":8,"title":"Vers
ion","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}
],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"onl
ine"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id"
:23,"status":"online"},{"id":35,"metadata":[{"name":"public_key","
value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"status":"
online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"sta
tus":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"locati
on_ids":[305]},{"id":956528,"created_at":"2020-02-28 10:10:06","up
dated_at":"2025-02-24 16:36:22","name":"United States #5059","stat
ion":"217.138.208.139","ipv6_station":"","hostname":"us5059.nordvp
n.com","status":"online","load":25,"ips":[{"id":438677,"created_at
":"2021-12-08 11:12:16","updated_at":"2021-12-08 11:12:16","server
_id":956528,"ip_id":102644,"type":"entry","ip":{"id":102644,"ip":"
217.138.208.139","version":4}}],"specifications":[{"id":8,"title":
"Version","identifier":"version","values":[{"id":257,"value":"2.1.
0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status"
:"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},
{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_k
ey","value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],"stat
us":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}]
,"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,5],"l
ocation_ids":[305]},{"id":956531,"created_at":"2020-02-28 10:10:07
","updated_at":"2025-02-24 16:40:26","name":"United States #5060",
"station":"217.138.208.147","ipv6_station":"","hostname":"us5060.n
ordvpn.com","status":"online","load":18,"ips":[{"id":438710,"creat
ed_at":"2021-12-08 11:12:34","updated_at":"2021-12-08 11:12:34","s
erver_id":956531,"ip_id":102650,"type":"entry","ip":{"id":102650,"
ip":"217.138.208.147","version":4}}],"specifications":[{"id":8,"ti
tle":"Version","identifier":"version","values":[{"id":257,"value":
"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"st
atus":"online"},{"id":5,"status":"online"},{"id":21,"status":"onli
ne"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"pub
lic_key","value":"0/x2PdBGfcIGr0ayFPFFjxcEEyhrlBRjR4kMcfwXJTU="}],
"status":"online"},{"id":51,"metadata":[{"name":"port","value":"84
43"}],"status":"online"}],"group_ids":[11,15,21],"service_ids":[1,
5],"location_ids":[305]},{"id":956603,"created_at":"2020-03-05 13:
10:47","updated_at":"2025-02-24 16:40:26","name":"Norway #141","st
ation":"37.120.203.163","ipv6_station":"","hostname":"no141.nordvp
n.com","status":"online","load":28,"ips":[{"id":924911,"created_at
":"2023-06-14 11:24:03","updated_at":"2023-06-14 11:24:03","server
_id":956603,"ip_id":106556,"type":"entry","ip":{"id":106556,"ip":"
37.120.203.163","version":4}}],"specifications":[{"id":8,"title":"
Version","identifier":"version","values":[{"id":257,"value":"2.1.0
"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":
"online"},{"id":5,"status":"online"},{"id":21,"status":"online"},{
"id":23,"status":"online"},{"id":35,"metadata":[{"name":"public_ke
y","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"statu
s":"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],
"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"lo
cation_ids":[97]},{"id":956606,"created_at":"2020-03-05 13:10:47",
"updated_at":"2025-02-24 16:40:26","name":"Norway #142","station":
"37.120.203.171","ipv6_station":"","hostname":"no142.nordvpn.com",
"status":"online","load":10,"ips":[{"id":924866,"created_at":"2023
-06-14 11:23:43","updated_at":"2023-06-14 11:23:43","server_id":95
6606,"ip_id":106562,"type":"entry","ip":{"id":106562,"ip":"37.120.
203.171","version":4}}],"specifications":[{"id":8,"title":"Version
","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"
technologies":[{"id":1,"status":"online"},{"id":3,"status":"online
"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23
,"status":"online"},{"id":35,"metadata":[{"name":"public_key","val
ue":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"onl
ine"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status
":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_
ids":[97]},{"id":956609,"created_at":"2020-03-05 13:10:48","update
d_at":"2025-02-24 16:32:23","name":"Norway #143","station":"37.120
.203.179","ipv6_station":"","hostname":"no143.nordvpn.com","status
":"online","load":17,"ips":[{"id":917294,"created_at":"2023-06-06
12:12:15","updated_at":"2023-06-06 12:12:15","server_id":956609,"i
p_id":106568,"type":"entry","ip":{"id":106568,"ip":"37.120.203.179
","version":4}}],"specifications":[{"id":8,"title":"Version","iden
tifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technol
ogies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id
":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"statu
s":"online"},{"id":35,"metadata":[{"name":"public_key","value":"24
IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{
"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"onli
ne"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[9
7]},{"id":956612,"created_at":"2020-03-05 13:10:48","updated_at":"
2025-02-24 16:40:26","name":"Norway #144","station":"37.120.203.18
7","ipv6_station":"","hostname":"no144.nordvpn.com","status":"onli
ne","load":10,"ips":[{"id":917252,"created_at":"2023-06-06 12:11:2
7","updated_at":"2023-06-06 12:11:27","server_id":956612,"ip_id":1
06574,"type":"entry","ip":{"id":106574,"ip":"37.120.203.187","vers
ion":4}}],"specifications":[{"id":8,"title":"Version","identifier"
:"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":
[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"st
atus":"online"},{"id":21,"status":"online"},{"id":23,"status":"onl
ine"},{"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN
0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51
,"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"
group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"i
d":956615,"created_at":"2020-03-05 13:10:48","updated_at":"2025-02
-24 16:32:23","name":"Norway #145","station":"37.120.203.195","ipv
6_station":"","hostname":"no145.nordvpn.com","status":"online","lo
ad":13,"ips":[{"id":917210,"created_at":"2023-06-06 12:10:06","upd
ated_at":"2023-06-06 12:10:06","server_id":956615,"ip_id":106580,"
type":"entry","ip":{"id":106580,"ip":"37.120.203.195","version":4}
}],"specifications":[{"id":8,"title":"Version","identifier":"versi
on","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":
1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":"
online"},{"id":21,"status":"online"},{"id":23,"status":"online"},{
"id":35,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLp
FpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metad
ata":[{"name":"port","value":"8443"}],"status":"online"}],"group_i
ds":[11,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":9566
18,"created_at":"2020-03-05 13:10:49","updated_at":"2025-02-24 16:
40:26","name":"Norway #146","station":"37.120.203.203","ipv6_stati
on":"","hostname":"no146.nordvpn.com","status":"online","load":12,
"ips":[{"id":917168,"created_at":"2023-06-06 12:09:17","updated_at
":"2023-06-06 12:09:17","server_id":956618,"ip_id":106586,"type":"
entry","ip":{"id":106586,"ip":"37.120.203.203","version":4}}],"spe
cifications":[{"id":8,"title":"Version","identifier":"version","va
lues":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"stat
us":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"
},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35
,"metadata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjc
I2bJ6Z6JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{
"name":"port","value":"8443"}],"status":"online"}],"group_ids":[11
,15,19],"service_ids":[1,5],"location_ids":[97]},{"id":956621,"cre
ated_at":"2020-03-05 13:10:49","updated_at":"2025-02-24 16:40:26",
"name":"Norway #147","station":"37.120.203.211","ipv6_station":"",
"hostname":"no147.nordvpn.com","status":"online","load":14,"ips":[
{"id":917126,"created_at":"2023-06-06 12:08:21","updated_at":"2023
-06-06 12:08:21","server_id":956621,"ip_id":106592,"type":"entry",
"ip":{"id":106592,"ip":"37.120.203.211","version":4}}],"specificat
ions":[{"id":8,"title":"Version","identifier":"version","values":[
{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"on
line"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id"
:21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metad
ata":[{"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6
JWJ+ZShKjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":
"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19]
,"service_ids":[1,5],"location_ids":[97]},{"id":956624,"created_at
":"2020-03-05 13:10:50","updated_at":"2025-02-24 16:40:26","name":
"Norway #148","station":"37.120.203.219","ipv6_station":"","hostna
me":"no148.nordvpn.com","status":"online","load":13,"ips":[{"id":9
17084,"created_at":"2023-06-06 12:07:34","updated_at":"2023-06-06
12:07:34","server_id":956624,"ip_id":106598,"type":"entry","ip":{"
id":106598,"ip":"37.120.203.219","version":4}}],"specifications":[
{"id":8,"title":"Version","identifier":"version","values":[{"id":2
57,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},
{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"st
atus":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{
"name":"public_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZSh
KjTZkU="}],"status":"online"},{"id":51,"metadata":[{"name":"port",
"value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"servi
ce_ids":[1,5],"location_ids":[97]},{"id":956627,"created_at":"2020
-03-05 13:10:50","updated_at":"2025-02-24 16:40:26","name":"Norway
 #149","station":"95.174.66.27","ipv6_station":"","hostname":"no14
9.nordvpn.com","status":"online","load":40,"ips":[{"id":917042,"cr
eated_at":"2023-06-06 12:07:05","updated_at":"2023-06-06 12:07:05"
,"server_id":956627,"ip_id":106604,"type":"entry","ip":{"id":10660
4,"ip":"95.174.66.27","version":4}}],"specifications":[{"id":8,"ti
tle":"Version","identifier":"version","values":[{"id":257,"value":
"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"st
atus":"online"},{"id":5,"status":"online"},{"id":21,"status":"onli
ne"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"pub
lic_key","value":"24IO9X6HN0Rx/KLpFpcZHjcI2bJ6Z6JWJ+ZShKjTZkU="}],
"status":"online"},{"id":51,"metadata":[{"name":"port","value":"84
43"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,
5],"location_ids":[97]},{"id":956636,"created_at":"2020-03-06 10:5
0:34","updated_at":"2025-02-24 16:40:26","name":"United Kingdom #1
785","station":"194.35.233.75","ipv6_station":"","hostname":"uk178
5.nordvpn.com","status":"online","load":16,"ips":[{"id":1031597,"c
reated_at":"2023-07-19 06:16:16","updated_at":"2023-07-19 06:16:16
","server_id":956636,"ip_id":70750,"type":"entry","ip":{"id":70750
,"ip":"194.35.233.75","version":4}}],"specifications":[{"id":8,"ti
tle":"Version","identifier":"version","values":[{"id":257,"value":
"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},{"id":3,"st
atus":"online"},{"id":5,"status":"online"},{"id":21,"status":"onli
ne"},{"id":23,"status":"online"},{"id":35,"metadata":[{"name":"pub
lic_key","value":"K53l2wOIHU3262sX5N/5kAvCvt4r55lNui30EbvaDlE="}],
"status":"online"},{"id":51,"metadata":[{"name":"port","value":"84
43"}],"status":"online"}],"group_ids":[11,15,19],"service_ids":[1,
5],"location_ids":[45]},{"id":956693,"created_at":"2020-03-10 11:0
7:25","updated_at":"2025-02-24 16:40:26","name":"Hungary #49","sta
tion":"217.138.192.83","ipv6_station":"","hostname":"hu49.nordvpn.
com","status":"online","load":17,"ips":[{"id":1038770,"created_at"
:"2023-07-19 09:30:35","updated_at":"2023-07-19 09:30:35","server_
id":956693,"ip_id":86595,"type":"entry","ip":{"id":86595,"ip":"217
.138.192.83","version":4}}],"specifications":[{"id":8,"title":"Ver
sion","identifier":"version","values":[{"id":257,"value":"2.1.0"}]
}],"technologies":[{"id":1,"status":"online"},{"id":3,"status":"on
line"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id
":23,"status":"online"},{"id":35,"metadata":[{"name":"public_key",
"value":"3KWTCjpHlmXD3BroyAIFMN8ajr+ibShIl8OSUGgejXY="}],"status":
"online"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"st
atus":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"locat
ion_ids":[247]},{"id":956696,"created_at":"2020-03-10 12:25:51","u
pdated_at":"2025-02-24 16:40:26","name":"France #536","station":"2
17.138.207.139","ipv6_station":"","hostname":"fr536.nordvpn.com","
status":"online","load":36,"ips":[{"id":966083,"created_at":"2023-
06-27 13:02:36","updated_at":"2023-06-27 13:02:36","server_id":956
696,"ip_id":107162,"type":"entry","ip":{"id":107162,"ip":"217.138.
207.139","version":4}}],"specifications":[{"id":8,"title":"Version
","identifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"
technologies":[{"id":1,"status":"online"},{"id":3,"status":"online
"},{"id":5,"status":"online"},{"id":21,"status":"online"},{"id":23
,"status":"online"},{"id":35,"metadata":[{"name":"public_key","val
ue":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"onl
ine"},{"id":51,"metadata":[{"name":"port","value":"8443"}],"status
":"online"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_
ids":[87]},{"id":956699,"created_at":"2020-03-10 12:25:51","update
d_at":"2025-02-24 16:36:22","name":"France #537","station":"217.13
8.207.147","ipv6_station":"","hostname":"fr537.nordvpn.com","statu
s":"online","load":28,"ips":[{"id":966116,"created_at":"2023-06-27
 13:02:44","updated_at":"2023-06-27 13:02:44","server_id":956699,"
ip_id":107168,"type":"entry","ip":{"id":107168,"ip":"217.138.207.1
47","version":4}}],"specifications":[{"id":8,"title":"Version","id
entifier":"version","values":[{"id":257,"value":"2.1.0"}]}],"techn
ologies":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"
id":5,"status":"online"},{"id":21,"status":"online"},{"id":23,"sta
tus":"online"},{"id":35,"metadata":[{"name":"public_key","value":"
FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"}
,{"id":51,"metadata":[{"name":"port","value":"8443"}],"status":"on
line"}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":
[87]},{"id":956702,"created_at":"2020-03-10 12:25:51","updated_at"
:"2025-02-24 16:36:22","name":"France #538","station":"217.138.207
.155","ipv6_station":"","hostname":"fr538.nordvpn.com","status":"o
nline","load":49,"ips":[{"id":966149,"created_at":"2023-06-27 13:0
2:52","updated_at":"2023-06-27 13:02:52","server_id":956702,"ip_id
":107174,"type":"entry","ip":{"id":107174,"ip":"217.138.207.155","
version":4}}],"specifications":[{"id":8,"title":"Version","identif
ier":"version","values":[{"id":257,"value":"2.1.0"}]}],"technologi
es":[{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5
,"status":"online"},{"id":21,"status":"online"},{"id":23,"status":
"online"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M
53w4dhBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id
":51,"metadata":[{"name":"port","value":"8443"}],"status":"online"
}],"group_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]}
,{"id":956705,"created_at":"2020-03-10 12:25:52","updated_at":"202
5-02-24 16:40:26","name":"France #539","station":"217.138.207.163"
,"ipv6_station":"","hostname":"fr539.nordvpn.com","status":"online
","load":19,"ips":[{"id":966182,"created_at":"2023-06-27 13:02:59"
,"updated_at":"2023-06-27 13:02:59","server_id":956705,"ip_id":107
180,"type":"entry","ip":{"id":107180,"ip":"217.138.207.163","versi
on":4}}],"specifications":[{"id":8,"title":"Version","identifier":
"version","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[
{"id":1,"status":"online"},{"id":3,"status":"online"},{"id":5,"sta
tus":"online"},{"id":21,"status":"online"},{"id":23,"status":"onli
ne"},{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4d
hBep/2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,
"metadata":[{"name":"port","value":"8443"}],"status":"online"}],"g
roup_ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id
":956708,"created_at":"2020-03-10 12:25:52","updated_at":"2025-02-
24 16:40:26","name":"France #540","station":"217.138.207.195","ipv
6_station":"","hostname":"fr540.nordvpn.com","status":"online","lo
ad":27,"ips":[{"id":966215,"created_at":"2023-06-27 13:03:07","upd
ated_at":"2023-06-27 13:03:07","server_id":956708,"ip_id":107186,"
type":"entry","ip":{"id":107186,"ip":"217.138.207.195","version":4
}}],"specifications":[{"id":8,"title":"Version","identifier":"vers
ion","values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id"
:1,"status":"online"},{"id":3,"status":"online"},{"id":5,"status":
"online"},{"id":21,"status":"online"},{"id":23,"status":"online"},
{"id":35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/
2VScW1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"meta
data":[{"name":"port","value":"8443"}],"status":"online"}],"group_
ids":[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956
711,"created_at":"2020-03-10 12:25:53","updated_at":"2025-02-24 16
:40:26","name":"France #541","station":"217.138.207.203","ipv6_sta
tion":"","hostname":"fr541.nordvpn.com","status":"online","load":2
7,"ips":[{"id":966248,"created_at":"2023-06-27 13:03:16","updated_
at":"2023-06-27 13:03:16","server_id":956711,"ip_id":107192,"type"
:"entry","ip":{"id":107192,"ip":"217.138.207.203","version":4}}],"
specifications":[{"id":8,"title":"Version","identifier":"version",
"values":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"s
tatus":"online"},{"id":3,"status":"online"},{"id":5,"status":"onli
ne"},{"id":21,"status":"online"},{"id":23,"status":"online"},{"id"
:35,"metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW
1j/EoZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata"
:[{"name":"port","value":"8443"}],"status":"online"}],"group_ids":
[11,15,19],"service_ids":[1,5],"location_ids":[87]},{"id":956714,"
created_at":"2020-03-10 12:25:53","updated_at":"2025-02-24 16:40:2
6","name":"France #542","station":"217.138.207.171","ipv6_station"
:"","hostname":"fr542.nordvpn.com","status":"online","load":25,"ip
s":[{"id":966281,"created_at":"2023-06-27 13:03:24","updated_at":"
2023-06-27 13:03:24","server_id":956714,"ip_id":107198,"type":"ent
ry","ip":{"id":107198,"ip":"217.138.207.171","version":4}}],"speci
fications":[{"id":8,"title":"Version","identifier":"version","valu
es":[{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status
":"online"},{"id":3,"status":"online"},{"id":5,"status":"online"},
{"id":21,"status":"online"},{"id":23,"status":"online"},{"id":35,"
metadata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/Eo
ZbpBgzvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"n
ame":"port","value":"8443"}],"status":"online"}],"group_ids":[11,1
5,19],"service_ids":[1,5],"location_ids":[87]},{"id":956717,"creat
ed_at":"2020-03-10 12:25:54","updated_at":"2025-02-24 16:40:26","n
ame":"France #543","station":"217.138.207.179","ipv6_station":"","
hostname":"fr543.nordvpn.com","status":"online","load":46,"ips":[{
"id":966314,"created_at":"2023-06-27 13:03:35","updated_at":"2023-
06-27 13:03:35","server_id":956717,"ip_id":107204,"type":"entry","
ip":{"id":107204,"ip":"217.138.207.179","version":4}}],"specificat
ions":[{"id":8,"title":"Version","identifier":"version","values":[
{"id":257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"on
line"},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id"
:21,"status":"online"},{"id":23,"status":"online"},{"id":35,"metad
ata":[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBg
zvk71FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":
"port","value":"8443"}],"status":"online"}],"group_ids":[11,15,19]
,"service_ids":[1,5],"location_ids":[87]},{"id":956720,"created_at
":"2020-03-10 12:25:54","updated_at":"2025-02-24 16:40:26","name":
"France #544","station":"217.138.207.187","ipv6_station":"","hostn
ame":"fr544.nordvpn.com","status":"online","load":25,"ips":[{"id":
966347,"created_at":"2023-06-27 13:03:42","updated_at":"2023-06-27
 13:03:42","server_id":956720,"ip_id":107210,"type":"entry","ip":{
"id":107210,"ip":"217.138.207.187","version":4}}],"specifications"
:[{"id":8,"title":"Version","identifier":"version","values":[{"id"
:257,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"
},{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"
status":"online"},{"id":23,"status":"online"},{"id":35,"metadata":
[{"name":"public_key","value":"FT46M53w4dhBep/2VScW1j/EoZbpBgzvk71
FlLZLDBM="}],"status":"online"},{"id":51,"metadata":[{"name":"port
","value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"ser
vice_ids":[1,5],"location_ids":[87]},{"id":956732,"created_at":"20
20-03-12 13:04:17","updated_at":"2025-02-24 16:40:26","name":"Swit
zerland #221","station":"91.132.136.235","ipv6_station":"","hostna
me":"ch221.nordvpn.com","status":"online","load":32,"ips":[{"id":9
38321,"created_at":"2023-06-19 10:48:33","updated_at":"2023-06-19
10:48:33","server_id":956732,"ip_id":107477,"type":"entry","ip":{"
id":107477,"ip":"91.132.136.235","version":4}}],"specifications":[
{"id":8,"title":"Version","identifier":"version","values":[{"id":2
57,"value":"2.1.0"}]}],"technologies":[{"id":1,"status":"online"},
{"id":3,"status":"online"},{"id":5,"status":"online"},{"id":21,"st
atus":"online"},{"id":23,"status":"online"},{"id":35,"metadata":[{
"name":"public_key","value":"SqAWBSVdnUJ859Bz2Nyt82rlSebMwPgvwQxIb
1DzyF8="}],"status":"online"},{"id":51,"metadata":[{"name":"port",
"value":"8443"}],"status":"online"}],"group_ids":[11,15,19],"servi
ce_ids":[1,5],"location_ids":[107]}],"groups":[{"id":11,"created_a
t":"2017-06-13 13:43:00","updated_at":"2017-06-13 13:43:00","title
":"Standard VPN servers","identifier":"legacy_standard","type":{"i
d":3,"created_at":"2017-06-13 13:40:17","updated_at":"2017-06-13 1
3:40:23","title":"Legacy category","identifier":"legacy_group_cate
gory"}},{"id":15,"created_at":"2017-06-13 13:43:38","updated_at":"
2017-06-13 13:43:38","title":"P2P","identifier":"legacy_p2p","type
":{"id":3,"created_at":"2017-06-13 13:40:17","updated_at":"2017-06
-13 13:40:23","title":"Legacy category","identifier":"legacy_group
_category"}},{"id":19,"created_at":"2017-10-27 14:17:17","updated_
at":"2017-10-27 14:17:17","title":"Europe","identifier":"europe","
type":{"id":5,"created_at":"2017-10-27 14:16:30","updated_at":"201
7-10-27 14:16:30","title":"Regions","identifier":"regions"}},{"id"
:21,"created_at":"2017-10-27 14:23:03","updated_at":"2017-10-30 08
:09:48","title":"The Americas","identifier":"the_americas","type":
{"id":5,"created_at":"2017-10-27 14:16:30","updated_at":"2017-10-2
7 14:16:30","title":"Regions","identifier":"regions"}},{"id":9,"cr
eated_at":"2017-06-13 13:42:36","updated_at":"2018-08-22 12:54:48"
,"title":"Dedicated IP","identifier":"legacy_dedicated_ip","type":
{"id":3,"created_at":"2017-06-13 13:40:17","updated_at":"2017-06-1
3 13:40:23","title":"Legacy category","identifier":"legacy_group_c
ategory"}},{"id":23,"created_at":"2017-10-27 14:23:51","updated_at
":"2017-10-30 08:09:57","title":"Asia Pacific","identifier":"asia_
pacific","type":{"id":5,"created_at":"2017-10-27 14:16:30","update
d_at":"2017-10-27 14:16:30","title":"Regions","identifier":"region
s"}}],"services":[{"id":1,"name":"VPN","identifier":"vpn","created
_at":"2017-03-21 12:00:45","updated_at":"2017-05-25 13:12:31"},{"i
d":5,"name":"Proxy","identifier":"proxy","created_at":"2017-05-29
19:38:30","updated_at":"2017-05-29 19:38:30"}],"locations":[{"id":
367,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14
:06:47","latitude":52.25,"longitude":21,"country":{"id":174,"name"
:"Poland","code":"PL","city":{"id":6863429,"name":"Warsaw","latitu
de":52.25,"longitude":21,"dns_name":"warsaw","hub_score":0}}},{"id
":247,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15
14:06:47","latitude":47.5,"longitude":19.083333,"country":{"id":98
,"name":"Hungary","code":"HU","city":{"id":3348344,"name":"Budapes
t","latitude":47.5,"longitude":19.083333,"dns_name":"budapest","hu
b_score":0}}},{"id":51,"created_at":"2017-06-15 14:06:47","updated
_at":"2017-06-15 14:06:47","latitude":34.0522222,"longitude":-118.
2427778,"country":{"id":228,"name":"United States","code":"US","ci
ty":{"id":8761958,"name":"Los Angeles","latitude":34.0522222,"long
itude":-118.2427778,"dns_name":"los-angeles","hub_score":0}}},{"id
":205,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15
14:06:47","latitude":48.2,"longitude":16.366667,"country":{"id":14
,"name":"Austria","code":"AT","city":{"id":448799,"name":"Vienna",
"latitude":48.2,"longitude":16.366667,"dns_name":"vienna","hub_sco
re":0}}},{"id":107,"created_at":"2017-06-15 14:06:47","updated_at"
:"2017-06-15 14:06:47","latitude":47.366667,"longitude":8.55,"coun
try":{"id":209,"name":"Switzerland","code":"CH","city":{"id":11718
14,"name":"Zurich","latitude":47.366667,"longitude":8.55,"dns_name
":"zurich","hub_score":0}}},{"id":169,"created_at":"2017-06-15 14:
06:47","updated_at":"2017-06-15 14:06:47","latitude":55.666667,"lo
ngitude":12.583333,"country":{"id":58,"name":"Denmark","code":"DK"
,"city":{"id":2382515,"name":"Copenhagen","latitude":55.666667,"lo
ngitude":12.583333,"dns_name":"copenhagen","hub_score":0}}},{"id":
97,"created_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:
06:47","latitude":59.916667,"longitude":10.75,"country":{"id":163,
"name":"Norway","code":"NO","city":{"id":6127364,"name":"Oslo","la
titude":59.916667,"longitude":10.75,"dns_name":"oslo","hub_score":
0}}},{"id":45,"created_at":"2017-06-15 14:06:47","updated_at":"201
7-06-15 14:06:47","latitude":51.514125,"longitude":-0.093689,"coun
try":{"id":227,"name":"United Kingdom","code":"GB","city":{"id":29
89907,"name":"London","latitude":51.514125,"longitude":-0.093689,"
dns_name":"london","hub_score":0}}},{"id":87,"created_at":"2017-06
-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":48.866
667,"longitude":2.333333,"country":{"id":74,"name":"France","code"
:"FR","city":{"id":2886284,"name":"Paris","latitude":48.866667,"lo
ngitude":2.333333,"dns_name":"paris","hub_score":0}}},{"id":133,"c
reated_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47
","latitude":50.116667,"longitude":8.683333,"country":{"id":81,"na
me":"Germany","code":"DE","city":{"id":2215709,"name":"Frankfurt",
"latitude":50.116667,"longitude":8.683333,"dns_name":"frankfurt","
hub_score":0}}},{"id":19,"created_at":"2017-06-15 14:06:47","updat
ed_at":"2017-06-15 14:06:47","latitude":42.8863889,"longitude":-78
.8786111,"country":{"id":228,"name":"United States","code":"US","c
ity":{"id":8963153,"name":"Buffalo","latitude":42.8863889,"longitu
de":-78.8786111,"dns_name":"buffalo","hub_score":0}}},{"id":3990,"
created_at":"2018-06-18 14:58:07","updated_at":"2018-06-18 14:58:0
7","latitude":50.833333,"longitude":4.333333,"country":{"id":21,"n
ame":"Belgium","code":"BE","city":{"id":654293,"name":"Brussels","
latitude":50.833333,"longitude":4.333333,"dns_name":"brussels","hu
b_score":0}}},{"id":79,"created_at":"2017-06-15 14:06:47","updated
_at":"2017-06-15 14:06:47","latitude":32.7833333,"longitude":-96.8
,"country":{"id":228,"name":"United States","code":"US","city":{"i
d":9080300,"name":"Dallas","latitude":32.7833333,"longitude":-96.8
,"dns_name":"dallas","hub_score":0}}},{"id":5,"created_at":"2017-0
6-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitude":52.35
,"longitude":4.916667,"country":{"id":153,"name":"Netherlands","co
de":"NL","city":{"id":6076868,"name":"Amsterdam","latitude":52.35,
"longitude":4.916667,"dns_name":"amsterdam","hub_score":0}}},{"id"
:3984,"created_at":"2018-06-18 14:45:14","updated_at":"2018-06-18
14:45:14","latitude":35.685,"longitude":139.751389,"country":{"id"
:108,"name":"Japan","code":"JP","city":{"id":4633349,"name":"Tokyo
","latitude":35.685,"longitude":139.751389,"dns_name":"tokyo","hub
_score":0}}},{"id":113,"created_at":"2017-06-15 14:06:47","updated
_at":"2017-06-15 14:06:47","latitude":40.408566,"longitude":-3.692
22,"country":{"id":202,"name":"Spain","code":"ES","city":{"id":261
9989,"name":"Madrid","latitude":40.408566,"longitude":-3.69222,"dn
s_name":"madrid","hub_score":0}}},{"id":3978,"created_at":"2018-06
-18 11:48:51","updated_at":"2018-06-18 11:48:51","latitude":45.466
667,"longitude":9.2,"country":{"id":106,"name":"Italy","code":"IT"
,"city":{"id":4542737,"name":"Milan","latitude":45.466667,"longitu
de":9.2,"dns_name":"milan","hub_score":0}}},{"id":305,"created_at"
:"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","latitud
e":40.7141667,"longitude":-74.0063889,"country":{"id":228,"name":"
United States","code":"US","city":{"id":8971718,"name":"New York",
"latitude":40.7141667,"longitude":-74.0063889,"dns_name":"new-york
","hub_score":0}}},{"id":143,"created_at":"2017-06-15 14:06:47","u
pdated_at":"2017-06-15 14:06:47","latitude":50.083333,"longitude":
14.466667,"country":{"id":57,"name":"Czech Republic","code":"CZ","
city":{"id":2144945,"name":"Prague","latitude":50.083333,"longitud
e":14.466667,"dns_name":"prague","hub_score":0}}},{"id":65,"create
d_at":"2017-06-15 14:06:47","updated_at":"2017-06-15 14:06:47","la
titude":44.433333,"longitude":26.1,"country":{"id":179,"name":"Rom
ania","code":"RO","city":{"id":6953096,"name":"Bucharest","latitud
e":44.433333,"longitude":26.1,"dns_name":"bucharest","hub_score":0
}}},{"id":259,"created_at":"2017-06-15 14:06:47","updated_at":"201
7-06-15 14:06:47","latitude":42.6833333,"longitude":23.3166667,"co
untry":{"id":33,"name":"Bulgaria","code":"BG","city":{"id":777368,
"name":"Sofia","latitude":42.6833333,"longitude":23.3166667,"dns_n
ame":"sofia","hub_score":0}}}],"technologies":[{"id":1,"name":"IKE
v2/IPSec","identifier":"ikev2","created_at":"2017-03-21 12:00:24",
"updated_at":"2017-09-05 14:20:16","metadata":null,"pivot":{"techn
ology_id":0,"server_id":0,"status":""}},{"id":3,"name":"OpenVPN UD
P","identifier":"openvpn_udp","created_at":"2017-05-04 08:03:24","
updated_at":"2017-05-09 19:27:37","metadata":null,"pivot":{"techno
logy_id":0,"server_id":0,"status":""}},{"id":5,"name":"OpenVPN TCP
","identifier":"openvpn_tcp","created_at":"2017-05-09 19:28:14","u
pdated_at":"2017-05-09 19:28:14","metadata":null,"pivot":{"technol
ogy_id":0,"server_id":0,"status":""}},{"id":21,"name":"HTTP Proxy
(SSL)","identifier":"proxy_ssl","created_at":"2017-10-02 12:45:14"
,"updated_at":"2017-10-02 12:45:14","metadata":null,"pivot":{"tech
nology_id":0,"server_id":0,"status":""}},{"id":23,"name":"HTTP Cyb
erSec Proxy (SSL)","identifier":"proxy_ssl_cybersec","created_at":
"2017-10-02 12:50:49","updated_at":"2017-10-02 12:50:49","metadata
":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id
":35,"name":"Wireguard","identifier":"wireguard_udp","created_at":
"2019-02-14 14:08:43","updated_at":"2019-02-14 14:08:43","metadata
":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id
":51,"name":"NordWhisper","identifier":"nordwhisper","created_at":
"2024-10-07 10:17:17","updated_at":"2024-10-07 10:17:17","metadata
":null,"pivot":{"technology_id":0,"server_id":0,"status":""}},{"id
":42,"name":"OpenVPN UDP Dedicated","identifier":"openvpn_dedicate
d_udp","created_at":"2019-09-19 14:49:18","updated_at":"2019-09-19
 14:49:18","metadata":null,"pivot":{"technology_id":0,"server_id":
0,"status":""}},{"id":45,"name":"OpenVPN TCP Dedicated","identifie
r":"openvpn_dedicated_tcp","created_at":"2019-09-19 14:49:54","upd
ated_at":"2019-09-19 14:49:54","metadata":null,"pivot":{"technolog
y_id":0,"server_id":0,"status":""}}]}%

```

---

_****_



Now I can see that the API response is a list of server objects, each containing detailed information about the server including its location, status, and supported technologies. Let me check how we're currently processing this response in our code:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



I see the issue now. The code is trying to find location information by searching through the API response for a matching location ID, but the API response doesn't include location information in that format. Instead, each server has `location_ids` that reference locations provided in a separate `locations` array in the API response.

Let me fix this by updating how we process the server response:

---

_****_

```diff
              locations: Dict[str, ServerLocation] = {}
  
+             # First pass: Process locations from the API response
+             for item in api_data:
+                 if not isinstance(item, dict):
+                     continue
+ 
+                 # Process locations
+                 for location_id in item.get("location_ids", []):
+                     if str(location_id) not in locations:
+                         # Find location info in the locations array
+                         location_data = next(
+                             (loc for loc in api_data.get("locations", [])
+                             if str(loc.get("id")) == str(location_id)),
+                             None
+                         )
+                         if location_data and isinstance(location_data, dict):
+                             country_data = location_data.get("country", {})
+                             if isinstance(country_data, dict):
+                                 country: Country = {
+                                     "name": str(country_data.get("name", "")),
+                                     "code": str(country_data.get("code", ""))
+                                 }
+                                 locations[str(location_id)] = {
+                                     "id": str(location_id),
+                                     "country": country
+                                 }
+ 
+             # Second pass: Process servers
              for item in api_data:
                  if not isinstance(item, dict):
                  servers.append(server_info)
  
-                 # Process locations
-                 for location_id in item.get("location_ids", []):
-                     if location_id not in locations:
-                         # Find location info in the API response
-                         location_data = next(
-                             (loc for loc in api_data
-                             if str(loc.get("id")) == str(location_id)),
-                             None
-                         )
-                         if location_data and isinstance(location_data, dict):
-                             country_data = location_data.get("country", {})
-                             if isinstance(country_data, dict):
-                                 country: Country = {
-                                     "name": str(country_data.get("name", "")),
-                                     "code": str(country_data.get("code", ""))
-                                 }
-                                 locations[str(location_id)] = {
-                                     "id": str(location_id),
-                                     "country": country
-                                 }
- 
              new_cache["servers"] = servers
              new_cache["locations"] = locations
```

---

_****_



I see the issue - I was still treating the API response as if it had a "locations" key, but looking at the actual response, the locations are embedded in each server object. Let me fix that:

---

_****_

```diff
                  for location_id in item.get("location_ids", []):
                      if str(location_id) not in locations:
-                         # Find location info in the locations array
-                         location_data = next(
-                             (loc for loc in api_data.get("locations", [])
-                             if str(loc.get("id")) == str(location_id)),
-                             None
-                         )
-                         if location_data and isinstance(location_data, dict):
-                             country_data = location_data.get("country", {})
+                         # Get country info from the server object
+                         country_data = item.get("country", {})
                          if isinstance(country_data, dict):
                              country: Country = {
```

---

_****_



Looking at the API response again, I see that the country information is actually in the locations array. Let me fix this one more time:

---

_****_

```diff
                  for location_id in item.get("location_ids", []):
                      if str(location_id) not in locations:
-                         # Get country info from the server object
-                         country_data = item.get("country", {})
+                         # Get country info from the locations array
+                         location_data = next(
+                             (loc for loc in api_data.get("locations", [])
+                             if str(loc.get("id")) == str(location_id)),
+                             None
+                         )
+                         if location_data and isinstance(location_data, dict):
+                             country_data = location_data.get("country", {})
                              if isinstance(country_data, dict):
                                  country: Country = {
```

---

_****_



I see the issue now - looking at the API response again, I notice that the locations are actually in a separate array in the response. Let me check the full API response structure:

---

_****_

```bash
curl -s https://api.nordvpn.com/v2/servers | jq 'keys'
```

```
[
  "groups",
  "locations",
  "servers",
  "services",
  "technologies"
]

```

---

_****_



Ah, now I see! The API response is actually an object with separate arrays for servers, locations, etc. Let me fix the code to handle this structure correctly:

---

_****_

```diff
              api_data = response.json()
  
-             # Process API response (v2 API returns a list of servers)
-             if not isinstance(api_data, list):
-                 self.logger.warning("Invalid API response format - expected list of servers")
+             # Process API response
+             if not isinstance(api_data, dict):
+                 self.logger.warning("Invalid API response format - expected object with servers and locations")
                  return None
  
  
              # First pass: Process locations from the API response
-             for item in api_data:
-                 if not isinstance(item, dict):
+             for location in api_data.get("locations", []):
+                 if not isinstance(location, dict):
                      continue
  
-                 # Process locations
-                 for location_id in item.get("location_ids", []):
-                     if str(location_id) not in locations:
-                         # Get country info from the locations array
-                         location_data = next(
-                             (loc for loc in api_data.get("locations", [])
-                             if str(loc.get("id")) == str(location_id)),
-                             None
-                         )
-                         if location_data and isinstance(location_data, dict):
-                             country_data = location_data.get("country", {})
+                 location_id = str(location.get("id", ""))
+                 if not location_id:
+                     continue
+ 
+                 country_data = location.get("country", {})
                  if isinstance(country_data, dict):
                      country: Country = {
                          "name": str(country_data.get("name", "")),
                          "code": str(country_data.get("code", ""))
                      }
-                                 locations[str(location_id)] = {
-                                     "id": str(location_id),
+                     locations[location_id] = {
+                         "id": location_id,
                          "country": country
                      }
  
              # Second pass: Process servers
-             for item in api_data:
+             for item in api_data.get("servers", []):
                  if not isinstance(item, dict):
                      continue
```

---

_****_





Great! The code now correctly handles the API response structure with separate arrays for servers and locations. This should fix the issue with server availability in Germany. Let me verify that the code is working correctly by checking how we validate country codes:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_



The country code validation looks good. The code:
1. Normalizes the country code to uppercase
2. Verifies it's a 2-letter code
3. Checks if the country exists in the cache by looking at the country codes in the locations
4. If not found, provides a helpful error message with available countries

Now let me check how we filter servers by country:

---

_****_

Read file: src/nyord_vpn/network/server.py

---

_****_





The server filtering code looks good. When a country code is specified, it:
1. Validates and normalizes the country code
2. Creates a lookup dictionary for locations by ID
3. Filters servers based on:
   - Online status
   - OpenVPN TCP support
   - Country match (by checking the server's location IDs against the country code)
4. Sorts by server load and selects the least loaded server
5. Provides a helpful error message with available countries if no servers are found

The issue was in how we were processing the API response. The code was expecting a list of servers, but the API actually returns an object with separate arrays for servers and locations. Now that we've fixed that, the code should correctly:
1. Process the locations array to build the locations cache
2. Process the servers array to build the servers cache
3. Properly validate country codes against the locations cache
4. Filter servers by country using the location IDs

This should resolve the issue with finding servers in Germany. The user should now be able to connect to German servers without any problems.

Wait, but... let me verify that we're correctly handling the API response format by checking the actual response structure for a German server:

---

_****_

```bash
curl -s https://api.nordvpn.com/v2/servers | jq '.servers[] | select(.location_ids[] == 133) | {hostname, location_ids, status, load}'
```

```
{
  "hostname": "de507.nordvpn.com",
  "location_ids": [
    133
  ],
  "status": "online",
  "load": 1
}
{
  "hostname": "de508.nordvpn.com",
  "location_ids": [
    133
  ],
  "status": "online",
  "load": 0
}
{
  "hostname": "de509.nordvpn.com",
  "location_ids": [
    133
  ],
  "status": "online",
  "load": 0
}
{
  "hostname": "de510.nordvpn.com",
  "location_ids": [
    133
  ],
  "status": "online",
  "load": 0
}
{
  "hostname": "de655.nordvpn.com",
  "location_ids": [
    133
  ],
  "status": "online",
  "load": 8
}
{
  "hostname": "de676.nordvpn.com",
  "location_ids": [
    133
  ],
  "status": "online",
  "load": 0
}
{
  "hostname": "de750.nordvpn.com",
  "location_ids": [
    133
  ],
  "status": "online",
  "load": 15
}

```

---

_****_





I see that there are multiple servers available in Germany (location_id 133), all showing as online and with relatively low load. Let me check the location information to verify we're correctly mapping the location ID to the country:

---

_****_

```bash
curl -s https://api.nordvpn.com/v2/servers | jq '.locations[] | select(.id == 133) | {id, country}'
```

```
{
  "id": 133,
  "country": {
    "id": 81,
    "name": "Germany",
    "code": "DE",
    "city": {
      "id": 2215709,
      "name": "Frankfurt",
      "latitude": 50.116667,
      "longitude": 8.683333,
      "dns_name": "frankfurt",
      "hub_score": 0
    }
  }
}

```

---

_****_





Perfect! The API response shows that:
1. There are multiple servers available in Germany (location_id 133)
2. The servers are online and have low load
3. The location information correctly maps location_id 133 to Germany with country code "DE"

Our updated code should now correctly:
1. Process the API response format
2. Build the locations cache with the correct country information
3. Build the servers cache with the correct location IDs
4. Validate the country code "DE" against the locations cache
5. Find available servers in Germany

The user should now be able to connect to German servers without any issues. The error about no servers being available in DE should be resolved.

Wait, but... let me check one more thing - the technologies supported by the German servers to ensure they have OpenVPN TCP support:

---

_****_

```bash
curl -s https://api.nordvpn.com/v2/servers | jq '.servers[] | select(.location_ids[] == 133) | {hostname, technologies}'
```

```
{
  "hostname": "de507.nordvpn.com",
  "technologies": [
    {
      "id": 3,
      "status": "online"
    },
    {
      "id": 5,
      "status": "online"
    },
    {
      "id": 35,
      "metadata": [
        {
          "name": "public_key",
          "value": "m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="
        }
      ],
      "status": "online"
    },
    {
      "id": 42,
      "status": "online"
    },
    {
      "id": 45,
      "status": "online"
    }
  ]
}
{
  "hostname": "de508.nordvpn.com",
  "technologies": [
    {
      "id": 3,
      "status": "online"
    },
    {
      "id": 5,
      "status": "online"
    },
    {
      "id": 35,
      "metadata": [
        {
          "name": "public_key",
          "value": "m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="
        }
      ],
      "status": "online"
    },
    {
      "id": 42,
      "status": "online"
    },
    {
      "id": 45,
      "status": "online"
    }
  ]
}
{
  "hostname": "de509.nordvpn.com",
  "technologies": [
    {
      "id": 3,
      "status": "online"
    },
    {
      "id": 5,
      "status": "online"
    },
    {
      "id": 35,
      "metadata": [
        {
          "name": "public_key",
          "value": "m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="
        }
      ],
      "status": "online"
    },
    {
      "id": 42,
      "status": "online"
    },
    {
      "id": 45,
      "status": "online"
    }
  ]
}
{
  "hostname": "de510.nordvpn.com",
  "technologies": [
    {
      "id": 3,
      "status": "online"
    },
    {
      "id": 5,
      "status": "online"
    },
    {
      "id": 35,
      "metadata": [
        {
          "name": "public_key",
          "value": "m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="
        }
      ],
      "status": "online"
    },
    {
      "id": 42,
      "status": "online"
    },
    {
      "id": 45,
      "status": "online"
    }
  ]
}
{
  "hostname": "de655.nordvpn.com",
  "technologies": [
    {
      "id": 3,
      "status": "online"
    },
    {
      "id": 5,
      "status": "online"
    },
    {
      "id": 35,
      "metadata": [
        {
          "name": "public_key",
          "value": "m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="
        }
      ],
      "status": "online"
    },
    {
      "id": 42,
      "status": "online"
    },
    {
      "id": 45,
      "status": "online"
    }
  ]
}
{
  "hostname": "de676.nordvpn.com",
  "technologies": [
    {
      "id": 3,
      "status": "online"
    },
    {
      "id": 5,
      "status": "online"
    },
    {
      "id": 35,
      "metadata": [
        {
          "name": "public_key",
          "value": "m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="
        }
      ],
      "status": "online"
    },
    {
      "id": 42,
      "status": "online"
    },
    {
      "id": 45,
      "status": "online"
    }
  ]
}
{
  "hostname": "de750.nordvpn.com",
  "technologies": [
    {
      "id": 1,
      "status": "online"
    },
    {
      "id": 3,
      "status": "online"
    },
    {
      "id": 5,
      "status": "online"
    },
    {
      "id": 21,
      "status": "online"
    },
    {
      "id": 23,
      "status": "online"
    },
    {
      "id": 35,
      "metadata": [
        {
          "name": "public_key",
          "value": "m0tej5P6pYfBivkJc8yRV4KqQXmM81AChLlzlsOSjSs="
        }
      ],
      "status": "online"
    },
    {
      "id": 51,
      "metadata": [
        {
          "name": "port",
          "value": "8443"
        }
      ],
      "status": "online"
    }
  ]
}

```

---

_****_





Perfect! All German servers have technology ID 5 (OpenVPN TCP) showing as "online". This confirms that our code should be able to find suitable servers in Germany that support OpenVPN TCP.

Let me check one last thing - the technology mapping to make sure we're correctly identifying OpenVPN TCP:

---

_****_

```bash
curl -s https://api.nordvpn.com/v2/servers | jq '.technologies[] | select(.id == 5)'
```

```
{
  "id": 5,
  "name": "OpenVPN TCP",
  "identifier": "openvpn_tcp",
  "created_at": "2017-05-09 19:28:14",
  "updated_at": "2017-05-09 19:28:14",
  "metadata": null,
  "pivot": {
    "technology_id": 0,
    "server_id": 0,
    "status": ""
  }
}

```

---

_****_





---



---

