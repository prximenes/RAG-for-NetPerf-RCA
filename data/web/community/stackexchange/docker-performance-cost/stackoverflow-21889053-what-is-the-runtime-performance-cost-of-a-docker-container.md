---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "stackoverflow",
  "question_id": 21889053,
  "link": "https://stackoverflow.com/questions/21889053/what-is-the-runtime-performance-cost-of-a-docker-container",
  "score": 813,
  "views": 310842,
  "answer_id": 26149994,
  "tags": [
    "linux",
    "docker",
    "performance",
    "virtual-machine",
    "containerd"
  ],
  "query_label": "docker-performance-cost",
  "description": "Runtime performance costs of containers; sets expectations for overhead vs root cause",
  "collected_at": "2025-12-13T15:57:43.144286+00:00"
}
            ---
            # What is the runtime performance cost of a Docker container?

            ## Question
            I'd like to comprehensively understand the run-time performance cost of a Docker container. I've found references to networking anecdotally being ~100µs slower.
I've also found references to the run-time cost being "negligible" and "close to zero" but I'd like to know more precisely what those costs are. Ideally I'd like to know what Docker is abstracting with a performance cost and things that are abstracted without a performance cost. Networking, CPU, memory, etc.
Furthermore, if there are abstraction costs, are there ways to get around the abstraction cost. For example, perhaps I can mount a disk directly vs. virtually in Docker.

            ## Accepted Answer
            An excellent 2014 IBM research paper “An Updated Performance Comparison of Virtual Machines and Linux Containers” by Felter et al. provides a comparison between bare metal, KVM, and Docker containers. The general result is: Docker is nearly identical to native performance and faster than KVM in every category.
The exception to this is Docker’s NAT — if you use port mapping (e.g.,
```
docker run -p 8080:8080
```
), then you can expect a minor hit in latency, as shown below. However, you can now use the host network stack (e.g.,
```
docker run --net=host
```
) when launching a Docker container, which will perform identically to the Native column (as shown in the Redis latency results lower down).
They also ran latency tests on a few specific services, such as Redis. You can see that above 20 client threads, highest latency overhead goes Docker NAT, then KVM, then a rough tie between Docker host/native.
Just because it’s a really useful paper, here are some other figures. Please download it for full access.
Taking a look at Disk I/O:
Now looking at CPU overhead:
Now some examples of memory (read the paper for details, memory can be extra tricky):
