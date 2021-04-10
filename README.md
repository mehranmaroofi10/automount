**To mount the Storage units automatically for Linux(Debian) servers**

**First step:**
Choose a permanent directory for placing the Automount.py
For example: ```/etc/automount/ ```


Go to ```/lib/sysstemd/system``` Directory.


**Step 2:**
We are going to make a system service.


Make a file named : ```automount.service```
Write the code bellow down in **automount.service**:


```
[Unit]
Description= automount service.
After=network-online.target
Wants=network-online.target systemd-networkd-wait-online.service

StartLimitIntervalSec=500
StartLimitBurst=5

[Service]
Type=simple
ExecStart=python3 /etc/automount/automount.py
Restart=on-failure
RestartSec=5s



[Install]
WantedBy=multi-user.target
```

```cp automount.service /etc/systemd/system/automount.service```
```chmod 644 /etc/systemd/system/automount.service```
```chhmod +x /etc/automount/automount.py```


**Step3:**
Now you can start and make the mounter restartable with codes bellow:


``` sudo systemctl deamon-reaload```
``` sudo systemctl start automount```
``` sudo systemctl enable automount```
```sudo systemctl restart automount```
