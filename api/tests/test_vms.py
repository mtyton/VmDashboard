from fastapi import testclient
from api.main import app


client = testclient.TestClient(app)


def test_list_vms():
    response = client.get("/list-vms/")
    assert response.status_code == 200
    assert response.json() == [
        {"uuid": "vm1", "name": "VM1", "state": "running"},
        {"uuid": "vm2", "name": "VM2", "state": "stopped"},
    ]
