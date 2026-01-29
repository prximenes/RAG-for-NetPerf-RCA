---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 715861,
  "link": "https://serverfault.com/questions/715861/how-do-i-tell-how-close-im-getting-to-somaxconn",
  "score": 26,
  "views": 16262,
  "answer_id": 715873,
  "answer_kind": "accepted",
  "tags": [
    "linux",
    "performance-tuning"
  ],
  "query_label": "tcp-listen-queue-backlog",
  "description": "Listen queue / backlog / SYN backlog troubleshooting (scenario_04)",
  "collected_at": "2025-12-13T16:07:02.847393+00:00"
}
            ---
            # How do I tell how close I&#39;m getting to somaxconn?

            ## Question
            The sysctl option
```
net.core.somaxconn
```
 defaults to 128 (on our systems) but can be raised.
- What exactly is this limit measuring and capping?
- How do I find out how close I am to the limit?
Context: I had a problem recently that appeared to be corrected by raising this limit. The problem was intermittent, so I don't trust that it is really fixed. I would like to find out if the current number of [whatever this setting caps] is greater than the previous maximum limit of 128.

            ## Accepted Answer
            ```
somaxconn
```
 determines the maximum number of backlogged connections allowed for each TCP port on the system. Increasing it (recommended for servers) can prevent "connection refused" messages, but it can result in slow connections if the server can't handle the increased load.
You can check the current backlog with
```
netstat -ant | grep -c SYN_REC
```
 according to this page. It will count how many connections are in the "SYN received" state, meaning the system has received a SYN packet (connection request) but hasn't acknowledged it yet.
If your system has
```
ss
```
 installed, you can also use
```
ss -s
```
 to display a summary of connections. Look for
```
synrecv
```
 in the output, or
```
ss -s | grep -Po '(?<=synrecv )\d+(?=,)'
```
 to just print the number.
