---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "stackoverflow",
  "question_id": 61403438,
  "link": "https://stackoverflow.com/questions/61403438/docker-tcp-retransmission-in-docker-network",
  "score": 3,
  "views": 2508,
  "answer_id": 67516035,
  "tags": [
    "docker",
    "docker-network"
  ],
  "query_label": "docker-tcp-retransmissions",
  "description": "TCP retransmissions in Docker networking; useful for troubleshooting RTT/jitter/retrans in containers",
  "collected_at": "2025-12-13T15:57:42.185331+00:00"
}
            ---
            # docker tcp retransmission in docker network

            ## Question
            TCP rentransmission occurs on any docker network.
simple test: create VM in Azure, centos 7,7
```
```
yum update
yum install docker
systemctl start docker
docker run --name mynginx1 -P -d nginx
tshark -tad -i any -Y "tcp.analysis.retransmission"
curl localhost:32768
```
```
this results in occurence of TCP Retransmission.
```
```
[root@vm1 ~]#  tshark -tad -i any -Y "tcp.analysis.retransmission"
Running as user "root" and group "root". This could be dangerous.
Capturing on 'any'
121 2020-04-24 07:26:55.504210673 109.81.211.189 -> 10.0.0.4     SSH 92 [TCP Retransmission] Encrypted request packet len=36
418 2020-04-24 07:27:04.982215355 109.81.211.189 -> 10.0.0.4     SSH 92 [TCP Retransmission] Encrypted request packet len=36
572 2020-04-24 07:27:10.746826933   172.17.0.1 -> 172.17.0.2   HTTP 147 [TCP Retransmission] GET / HTTP/1.1
576 2020-04-24 07:27:10.747858244   172.17.0.2 -> 172.17.0.1   TCP 307 [TCP Retransmission] http > 40514 [PSH, ACK] Seq=1 Ack=80 Win=29056 Len=239 TSval=1217913 TSecr=1217912
580 2020-04-24 07:27:10.747930345   172.17.0.2 -> 172.17.0.1   TCP 680 [TCP Retransmission] http > 40514 [PSH, ACK] Seq=240 Ack=80 Win=29056 Len=612 TSval=1217914 TSecr=1217913[Reassembly error, protocol TCP: New fragment overlaps old data (retransmission?)]
```
```
the same problem on Kubernetes (tested with flannel plugin)
this issue significantly reduce the performance of container, in our case high performance message parser inside docker has 4x less results. Using docker host network resolves the issue. But using bridge network causes this issue.
Please any advice/help?
for reference - the reason of retransmission is seen from wireshark as outoforder/duplicate
enter image wireshark trace detail

            ## Accepted Answer
            Finally we identified the problem in used image based on Alpine. After we moved the docker base image into debian/ubuntu retransmission problem gone.
