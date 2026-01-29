---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 518862,
  "link": "https://serverfault.com/questions/518862/will-increasing-net-core-somaxconn-make-a-difference",
  "score": 53,
  "views": 164304,
  "answer_id": 519152,
  "answer_kind": "accepted",
  "tags": [
    "linux",
    "networking",
    "kernel"
  ],
  "query_label": "tcp-listen-queue-backlog",
  "description": "Listen queue / backlog / SYN backlog troubleshooting (scenario_04)",
  "collected_at": "2025-12-13T16:07:02.431387+00:00"
}
            ---
            # Will increasing net.core.somaxconn make a difference?

            ## Question
            I got into an argument on the net.core.somaxconn parameter: I was told that it will not make any difference if we change the default 128.
I believed this might be enough proof:
"If the backlog argument is greater than the value in /proc/sys/net/core/somaxconn, then it is silently truncated to that value" http://linux.die.net/man/2/listen
but it's not.
Does anyone know a method to testify this with two machines, sitting on a Gbit network?
The best would be against MySQL, LVS, apache2 ( 2.2 ), memcached.

            ## Accepted Answer
            Setting
```
net.core.somaxconn
```
 to higher values is only needed on highloaded servers where new connection rate is so high/bursty that having 128 (50% more in BSD's: 128
```
backlog
```
 + 64
```
half-open
```
) not-yet-accepted connections is considered normal. Or when you need to delegate definition of "normal" to an applications itself.
Some administrators use high
```
net.core.somaxconn
```
 to hide problems with their services, so from user's point of view process it'll look like a latency spike instead of connection interrupted/timeout (controlled by
```
net.ipv4.tcp_abort_on_overflow
```
 in Linux).
```
listen(2)
```
 manual says -
```
net.core.somaxconn
```
 acts only upper boundary for an application which is free to choose something smaller (usually set in app's config). Though some apps just use
```
listen(fd, -1)
```
 which means set backlog to the max value allowed by system.
Real cause is either low processing rate (e.g. a single threaded blocking server) or insufficient number of worker threads/processes (e.g. multi- process/threaded blocking software like
```
apache
```
/
```
tomcat
```
)
PS. Sometimes it's preferable to fail fast and let the load-balancer to do it's job(retry) than to make user wait - for that purpose we set
```
net.core.somaxconn
```
 any value, and limit application backlog to e.g.
```
10
```
 and set
```
net.ipv4.tcp_abort_on_overflow
```
 to 1.
PPS. Old versions of Linux kernel have nasty bug of truncating
```
somaxcon
```
 value to it's 16 lower bits (i.e. casting value to
```
uint16_t
```
), so raising that value to more than
```
65535
```
 can even be dangerous. For more information see: http://patchwork.ozlabs.org/patch/255460/
If you want to go into more details about all backlog internals in Linux, feel free to read:
How TCP backlog works in Linux.
