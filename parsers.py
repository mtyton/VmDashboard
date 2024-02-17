from adapters import VBoxManage


def parse_vm_list(vm_list):
    vm_list = vm_list.splitlines()

    return vm_list

vbox = VBoxManage()

vm_list = vbox.list_virtual_machines()

print(vm_list)

parsed_list = parse_vm_list(vm_list)

print(parsed_list)
