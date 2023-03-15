import os


save_rules = os.system("iptables-save -f /etc/iptables/iptables.rules")
restore_rules = os.system("iptables-restore /etc/iptables/iptables.rules")


def execute_rule(rule):
    os.system(f"iptables {rule}")
