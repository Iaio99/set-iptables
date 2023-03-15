from . import execute_rule


def reset_rules():
    execute_rule("-F")
    execute_rule("-X")
    execute_rule("-F -t nat")
    execute_rule("-X -t nat")
    execute_rule("-F -t security")
    execute_rule("-X -t security")
    execute_rule("-F -t mangle")
    execute_rule("-X -t mangle")
    execute_rule("-F -t raw")
    execute_rule("-X -t raw")
    execute_rule("-P INPUT ACCEPT")
    execute_rule("-P OUTPUT ACCEPT")
    execute_rule("-P FORWARD ACCEPT")