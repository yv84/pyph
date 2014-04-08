pyph
====

receiver/transmitter for lineage 2 packets

Requirement: python3, numpy, lxml.

client l2 -> route -> pyph -> server l2

example, server: rpg-club.

client side - routing:

os.system('route add 91.238.84.215 mask 255.255.255.255 192.168.100.10')
os.system('route add 213.59.44.50 mask 255.255.255.255 192.168.100.10')
os.system('route add 95.211.47.188 mask 255.255.255.255 192.168.100.10')
os.system('route add 95.211.196.17 mask 255.255.255.255 192.168.100.10')
os.system('route add 95.211.196.15 mask 255.255.255.255 192.168.100.10')
os.system('route PRINT') # ,where 192.168.100.10 - ip pyph

pyph side:

$ sudo iptables -t nat -A PREROUTING -p tcp --dst 213.59.44.50 --dport 7777 -j REDIRECT
$ sudo iptables -t nat -A PREROUTING -p tcp --dst 91.238.84.215 --dport 7777 -j REDIRECT --to-ports 7778
$ sudo iptables -t nat -A PREROUTING -p tcp --dst 95.211.47.188 --dport 8081 -j REDIRECT
$ sudo iptables -t nat -A PREROUTING -p tcp --dst 95.211.196.17 --dport 8081 -j REDIRECT --to-ports 8082
$ sudo iptables -t nat -A PREROUTING -p tcp --dst 95.211.196.15 --dport 8081 -j REDIRECT --to-ports 8083

run it, looks like: 
https://lh6.googleusercontent.com/--El2OfnpnqY/UQfQPDrfjQI/AAAAAAAADTg/mVOsDFi6FIM/s836/run.jpg
https://lh6.googleusercontent.com/-pDy0LN3h7VY/UQfQO-jaLPI/AAAAAAAADTc/kOl4Yn-wG38/s1103/helloWorld.jpg
