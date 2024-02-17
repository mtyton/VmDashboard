from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class VMBasicData(BaseModel):
    uuid: str
    name: str
    state: str


class VMDetailedData(BaseModel):
    uuid: str
    name: str
    state: str
    cpu: int
    memory: int
    disk: int
    network: int



@router.get("/list-vms/")
async def list_vms() -> list[VMBasicData]:
    data = [
        VMBasicData(**{"uuid": "vm1", "name": "VM1", "state": "running"}),
        VMBasicData(**{"uuid": "vm2", "name": "VM2", "state": "stopped"}),
    ]
    return data


@router.get("/get-vm/{vm_uuid}", response_model=VMDetailedData)
async def get_vm(vm_uuid: str) -> VMDetailedData:
    vm = VMDetailedData(
        uuid=vm_uuid,
        name="VM1",
        state="running",
        cpu=2,
        memory=2048,
        disk=20,
        network=100
    )
    return vm
