---
            {
  "source": "stackexchange",
  "license": "CC BY-SA 4.0 (Stack Exchange)",
  "site": "serverfault",
  "question_id": 806014,
  "link": "https://serverfault.com/questions/806014/need-explanation-of-option-ethtool-k",
  "score": 1,
  "views": 1038,
  "answer_id": 806017,
  "tags": [
    "linux",
    "ubuntu",
    "networking",
    "debian",
    "linux-networking"
  ],
  "query_label": "linux-offloads-ethtool",
  "description": "ethtool -k / offload flags explained; useful for offload-disabled, CPU/softirq scenarios",
  "collected_at": "2025-12-13T15:57:32.674065+00:00"
}
            ---
            # Need explanation of option ethtool -K

            ## Question
            I did
rsync -av --rsh=ssh ...
and catch error
Corrupted MAC on input. Packet Corrupt
I found solution here
ethtool -K eth0 tx off rx off
This option disabled TCP checksum of ethernet adapter. But what does it mean, processor is responsible of TCP checksum now?
If I off TCP checksum permanently for ethernet adapter, it is normal or I will have bad consequences?

            ## Accepted Answer
            If you disable TCP checksum offloading, it will need to be carried out at a higher level. This will put put additional load on the higher level processor. As to it's consequence, that depends upon the spec of the system and the work it it doing, I don't think we can give any reasonable assurances here.
- I would make the change and attempt to test it in a lab.
- I would also check to see if there are driver/firmware updates for the NIC which I could apply and test.
- Changing the NIC may be a solution too.
