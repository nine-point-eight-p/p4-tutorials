#!/usr/bin/env python3
import sys
import time

from probe_hdrs import *

socket = conf.L2socket(iface='eth0')

def main():

    probe_pkt = Ether(dst='ff:ff:ff:ff:ff:ff', src=get_if_hwaddr('eth0')) / \
                Probe(hop_cnt=0) / \
                ProbeFwd(egress_spec=4) / \
                ProbeFwd(egress_spec=1) / \
                ProbeFwd(egress_spec=4) / \
                ProbeFwd(egress_spec=1) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=2) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=2) / \
                ProbeFwd(egress_spec=1)
    probe_pkt = bytes(probe_pkt)

    while True:
        try:
            socket.send(probe_pkt)
            time.sleep(1 / 1_000_000) # 1 us
        except KeyboardInterrupt:
            sys.exit()

if __name__ == '__main__':
    main()
