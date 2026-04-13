#!/usr/bin/env python3
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import Node

class LinuxRouter(Node):
    """Um Node no Mininet que atua como Roteador (habilita IP Forwarding)"""
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class LabTopo(Topo):
    def build(self, **_opts):
        # Adiciona Roteadores
        r1 = self.addHost('r1', cls=LinuxRouter, ip='10.0.0.1/24')
        r2 = self.addHost('r2', cls=LinuxRouter, ip='10.0.0.2/24')
        
        # Cria a conexão r1 --- r2
        self.addLink(r1, r2, intfName1='r1-eth0', intfName2='r2-eth0')

if __name__ == '__main__':
    setLogLevel('info')
    topo = LabTopo()
    net = Mininet(topo=topo)
    net.start()
    print("\n*** Topologia iniciada. Abra xterms para r1 e r2 e inicie o FRRouting. ***\n")
    CLI(net)
    net.stop()