import subprocess as sub
import optparse as opt

def get_arguments():
    parser=opt.OptionParser()
    parser.add_option("-i", "--interface",dest="interface",help="Interface to change its mac adress")
    parser.add_option("-m","--mac",dest="new_mac",help="New mac adress")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[-]Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-]Please specify a new mac, use --help for more info.")
    return options

def change_mac(interface,new_mac):
    print("[+]Changing Mac Adress for "+interface+" to "+new_mac)
    sub.call(["ifconfig",interface,"down"])
    sub.call(["ifconfig",interface,"hw","ether",new_mac])
    sub.call(["ifconfig",interface,"up"])
    
options=get_arguments()
change_mac(options.interface,options.new_mac)
