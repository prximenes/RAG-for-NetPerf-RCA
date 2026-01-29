---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 1047365,
  "link": "https://serverfault.com/questions/1047365/no-network-connectivity-in-the-lxc-container-set-up-in-the-routed-mode",
  "score": 6,
  "views": 11863,
  "answer_id": 1051267,
  "answer_kind": "accepted",
  "tags": [
    "networking",
    "linux-networking",
    "lxc",
    "lxd"
  ],
  "query_label": "tcp-bufferbloat-fq_codel",
  "description": "Bufferbloat and fq_codel/codel tuning (scenario_02)",
  "collected_at": "2025-12-13T16:07:01.025668+00:00"
}
            ---
            # No network connectivity in the LXC container set up in the &quot;routed&quot; mode

            ## Question
            I'm experimenting with lxc/lxd in Vagrant, but i'm quite new to it. I managed to create running container, but I cannot ping anything (including 8.8.8.8) from inside of it. I can ping its IP from my top-level non-virtual system, but it refuses SSH connections. I can enter the container only directly from the direct container's host (Vagrant) by using
```
lxc exec my-container /bin/bash
```
.
I tried to setup my container in the
```
routed
```
 mode, and I still want it, for the learning purposes. The LXD/LXC documentation seems to be somewhat lacking though.
I tried to follow this instruction: https://blog.simos.info/how-to-get-lxd-containers-get-ip-from-the-lan-with-routed-network/ but it didn't work for me in the end. I could miss something, because I'm not well versed in the linux networking yet.
My Vagrant host is running on
```
Ubuntu 20.04
```
.
My LXC container is running on
```
Debian 10
```
.
LXC configuration on my Vagrant host:
```
```
config:
  core.https_address: '[::]:8443'
  core.trust_password: true
networks: []
storage_pools:
- config:
    source: /home/luken/lxd-storage-pools
  description: ""
  name: default
  driver: dir
profiles:
- name: default
  config: {}
  description: ""
  devices:
    root:
      path: /
      pool: default
      type: disk
- name: mail-server
  config:
    user.network-config: |
      version: 2
      ethernets:
        eth0:
          addresses:
          - 192.168.33.11/32
          nameservers:
            addresses:
            - 8.8.8.8
            search: []
          routes:
          -   to: 0.0.0.0/0
            via: 169.254.0.1
  description: Mail Server LXD profile
  devices:
    eth0:
      ipv4.address: 192.168.33.11
      nictype: routed
      parent: eth1
      type: nic
cluster: null
```
```
```
ip addr
```
 in my Vagrant host:
```
```
luken@luken-tech-test:~$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:be:4a:e8 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic eth0
       valid_lft 76347sec preferred_lft 76347sec
    inet6 fe80::a00:27ff:febe:4ae8/64 scope link
       valid_lft forever preferred_lft forever
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:65:e6:28 brd ff:ff:ff:ff:ff:ff
    inet 192.168.33.2/24 brd 192.168.33.255 scope global eth1
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe65:e628/64 scope link
       valid_lft forever preferred_lft forever
6: vetha8400046@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether fe:48:28:3e:e4:fa brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 169.254.0.1/32 scope global vetha8400046
       valid_lft forever preferred_lft forever
    inet6 fe80::fc48:28ff:fe3e:e4fa/64 scope link
       valid_lft forever preferred_lft forever
```
```
```
ip addr
```
 in my container:
```
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0@if6: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 9a:14:96:30:67:43 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.33.11/32 brd 255.255.255.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::9814:96ff:fe30:6743/64 scope link
       valid_lft forever preferred_lft forever
```
```
```
ip r
```
 in my Vagrant host:
```
```
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15
10.0.2.2 dev eth0 proto dhcp scope link src 10.0.2.15 metric 100
192.168.33.0/24 dev eth1 proto kernel scope link src 192.168.33.2
192.168.33.11 dev vetha8400046 scope link
```
```
```
ip r
```
 in my container:
```
```
default via 169.254.0.1 dev eth0
169.254.0.1 dev eth0 scope link
```
```
Is there anything I missed (probably a lot)?

            ## Accepted Answer
            This is the correct setup for having Debian 10 containers accessible in our local network by their own static IPs, and them having access to the internet.
Our
```
Vagrantfile
```
:
```
```
Vagrant.configure("2") do |config|
  config.vm.define "main" do |main|
    main.vm.box = "bento/ubuntu-20.04"
    main.vm.box_version = "202010.24.0"
    main.vm.hostname = "lxc-host"
    main.vm.network "public_network", auto_config: false
    main.vm.provision "shell",
      run: "always",
      inline: "ip address add **192.168.1.200**/24 dev eth1"
    main.vm.provision "shell",
      run: "always",
      inline: "ip link set eth1 up"
    main.vm.provider :virtualbox do |vb|
        vb.memory = 1024
    end
  end
end
```
```
Notice that we are setting up "public" network, it means that when starting up Vagrant, you will be asked to choose interface to use, choose the one that you are using to connect to your local network.
Notice also that we are setting up only a single IP for now, this (192.168.1.200) will be our host's IP. We are not setting up container's IP here.
After starting up our host, enable IP forwarding in its configuration, by uncommenting:
```
net.ipv4.ip_forward=1
```
 in
```
/etc/sysctl.conf
```
 and restarting sysctl by executing
```
systemctl restart systemd-sysctl
```
 .
Now, assuming that you installed and set up
```
LXD
```
 correctly on the host, you can init
```
lxd
```
 with the following configuration:
```
```
config:
  core.https_address: '[::]:8443'
  core.trust_password: true
networks: []
storage_pools:
- config:
    source: [path-to-storage-pools-directory]
  description: ""
  name: default
  driver: dir
profiles:
- name: default
  config:
  description: ""
  devices:
    root:
      path: /
      pool: default
      type: disk
- name: test-container
  config:
    user.user-data: |
      #cloud-config
      bootcmd:
        - echo 'nameserver 8.8.8.8' > /etc/resolvconf/resolv.conf.d/tail
        - systemctl restart resolvconf
  description: Mail Server LXD profile
  devices:
    eth0:
      ipv4.address: 192.168.1.201
      nictype: routed
      parent: eth1
      type: nic
cluster: null
```
```
Change [path-to-storage-pools-directory] into actual path to the directory where you are going to store your pools.
Note that we are not using cloud-init to set up networking, as it would collide with Debian's networking service making it fail to start.
Note also that we are using cloud-init to set up nameserver to use by our guest.
192.168.1.201 will be our guest's IP. This setup assumes that the local network is 192.168.1.0, if your network is different, change IPs accordingly. Also make sure that the IPs used here are not used by anything else in the network already.
We are using two profiles here but it's up to you how you organize your configuration.
Now let's run our container:
```
```
lxc launch images:debian/10/cloud our-actual-test-container --profile default --profile test-container
```
```
It should be running, and be available in the local network, but it won't have access to the internet, and that's the tricky part. This is caused by routing set up by the
```
lxd
```
 based on the assumption that default gateway is the one to the vagrant/virtualbox network. We need to fix that.
When executing
```
ip r
```
 on the host, you should see the list of routes - something like that:
```
```
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15
10.0.2.2 dev eth0 proto dhcp scope link src 10.0.2.15 metric 100
192.168.1.0/24 dev eth1 proto kernel scope link src 192.168.1.200
192.168.1.201 dev vethc5cebe03 scope link
```
```
The issue is with the default one, which is routing traffic into the vagrant/virtualbox network instead of our actual gateway. Let's remove it:
```
```
ip route del default via 10.0.2.2
```
```
And let's add the rule that will forward packets to the actual gateway of our local network:
```
```
ip route add default via 192.168.1.1
```
```
(assuming that 192.168.1.1 is IP of our local gateway)
Now the traffic from the container will be going to the correct gateway, and we are done!
