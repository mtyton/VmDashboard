import subprocess


class mainManager():
    def run_command(self, command):
        raise NotImplementedError("Subclasses must implement this method")

    def list_virtual_machines(self):
        raise NotImplementedError("Subclasses must implement this method")

    def get_vm_info(self, vm_name):
        raise NotImplementedError("Subclasses must implement this method")

    def get_all_vm_status(self):
        raise NotImplementedError("Subclasses must implement this method")

    def start_vm(self, vm_name):
        raise NotImplementedError("Subclasses must implement this method")

    def stop_vm(self, vm_name):
        raise NotImplementedError("Subclasses must implement this method")


class VBoxManage(mainManager):
    def __init__(self):
        self.vboxmanage = 'D:/vbox/vboxmanage.exe '

    def run_command(self, command):
        result = subprocess.run(self.vboxmanage + command, shell=True,
                                stdout=subprocess.PIPE, text=True)
        return result.stdout

    def list_virtual_machines(self):
        command = "list vms"
        return self.run_command(command)

    def get_vm_info(self, vm_name):
        command = "showvminfo " + vm_name
        return self.run_command(command)

    def get_all_vm_status(self):
        running_vms = self.get_running_vms()
        all_vms = self.list_virtual_machines()
        running_vms = running_vms.splitlines()
        all_vms = all_vms.splitlines()
        status_list = []
        for vm in all_vms:
            if vm in running_vms:
                status_list.append('running')  # TODO: this will be better yes
            else:
                status_list.append('not running')
        return status_list

    def get_running_vms(self):
        command = "list runningvms"
        return self.run_command(command=command)

    def start_vm(self, vm_name):
        command = "startvm " + vm_name
        return self.run_command(command)

    def stop_vm(self, vm_name):
        command = "controlvm " + vm_name + " poweroff"
        return self.run_command(command)
