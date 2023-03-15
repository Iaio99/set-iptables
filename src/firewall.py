from .utils import execute_rule


def basic_firewall():
    execute_rule("-N TCP")
    execute_rule("-N UDP")
    execute_rule("-P FORWARD DROP")
    execute_rule("-P OUTPUT ACCEPT")
    execute_rule("-P INPUT DROP")
    execute_rule("-A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT")
    execute_rule("-A INPUT -i lo -j ACCEPT")
    execute_rule("-A INPUT -m conntrack --ctstate INVALID -j DROP")
    execute_rule("-A INPUT -p icmp --icmp-type 8 -m conntrack --ctstate NEW -j ACCEPT")
    execute_rule("-A INPUT -p udp -m conntrack --ctstate NEW -j UDP")
    execute_rule("-A INPUT -p tcp --syn -m conntrack --ctstate NEW -j TCP")
    execute_rule("-A INPUT -p udp -j REJECT --reject-with icmp-port-unreachable")
    execute_rule("-A INPUT -p tcp -j REJECT --reject-with tcp-reset")
    execute_rule("-A INPUT -j REJECT --reject-with icmp-proto-unreachable")
