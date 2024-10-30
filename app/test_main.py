from unittest import mock

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

example_reports = (
    '[{"id":"276232af-8b64-414f-b574-d4bb5ff10358","name":"Raport #1","status":"IN_PROGRESS",'
    '"createdAt":"2024-10-30T07:46:03.000Z","updatedAt":"2024-10-30T07:46:03.000Z","playerId":'
    '"4b4b4076-c6aa-4601-841e-ba51f7e60c32","player":{"name":"Damian Kowalski",'
    '"id":"4b4b4076-c6aa-4601-841e-ba51f7e60c32","firstName":"Damian","lastName":"Kowalski",'
    '"sex":"MALE","age":30,"position":"WINGER","teamId":null,"createdAt":"2024-10-30T07:46:03.000Z",'
    '"updatedAt":"2024-10-30T07:46:03.000Z"}},{"id":"89bca610-c842-42d6-892c-e9ecfea85760",'
    '"name":"Raport #2","status":"COMPLETED","createdAt":"2024-10-30T07:46:03.000Z",'
    '"updatedAt":"2024-10-30T07:46:03.000Z","playerId":"bfaee0f7-2e44-4182-a78f-a03253eee601",'
    '"player":{"name":"Jakub Prus","id":"bfaee0f7-2e44-4182-a78f-a03253eee601","firstName":'
    '"Jakub","lastName":"Prus","sex":"MALE","age":35,"position":"DEFENSE","teamId":null,'
    '"createdAt":"2024-10-30T07:46:03.000Z","updatedAt":"2024-10-30T07:46:03.000Z"}},'
    '{"id":"8dc3f345-7f02-44de-a0d7-466bbf3a4ac1","name":"Raport #3","status":"IN_PROGRESS",'
    '"createdAt":"2024-10-30T07:46:03.000Z","updatedAt":"2024-10-30T07:46:03.000Z","playerId":'
    '"18228bad-4d09-4773-8aeb-73938a2456c1","player":{"name":"Cristiano Ronaldo",'
    '"id":"18228bad-4d09-4773-8aeb-73938a2456c1","firstName":"Cristiano","lastName":"Ronaldo",'
    '"sex":"MALE","age":24,"position":"FORWARD","teamId":null,"createdAt":"2024-10-30T07:46:03.000Z",'
    '"updatedAt":"2024-10-30T07:46:03.000Z"}}]'
)

damian_report = (
    '[{"id":"276232af-8b64-414f-b574-d4bb5ff10358","name":"Raport #1","status":'
    '"IN_PROGRESS","createdAt":"2024-10-30T07:46:03.000Z","updatedAt":'
    '"2024-10-30T07:46:03.000Z","playerId":"4b4b4076-c6aa-4601-841e-ba51f7e60c32",'
    '"player":{"name":"Damian Kowalski","id":"4b4b4076-c6aa-4601-841e-ba51f7e60c32",'
    '"firstName":"Damian","lastName":"Kowalski","sex":"MALE","age":30,"position":'
    '"WINGER","teamId":null,"createdAt":"2024-10-30T07:46:03.000Z",'
    '"updatedAt":"2024-10-30T07:46:03.000Z"}}]'
)


def test_filter_reports():
    with mock.patch("requests.get") as mocked_get:
        get = mock.MagicMock()
        get.text = example_reports
        get.status_code = 200
        mocked_get.return_value = get

        response = client.post("/filter-reports/", json={})
        assert response.status_code == 200
        assert response.text == example_reports

        response = client.post(
            "/filter-reports/", json={"player": {"position": "WINGER"}}
        )
        assert response.status_code == 200
        assert response.text == damian_report

        response = client.post(
            "/filter-reports/", json={"player": {"sex": "MALE"}}
        )
        assert response.status_code == 200
        assert response.text == example_reports

        response = client.post(
            "/filter-reports/", json={"player": {"sex": "FEMALE"}}
        )
        assert response.status_code == 200
        assert response.text == "[]"

        response = client.post("/filter-reports/", json={"name": "Raport #1"})
        assert response.status_code == 200
        assert response.text == damian_report

        response = client.post(
            "/filter-reports/",
            json={"name": "Raport #1", "player": {"sex": "MALE"}},
        )
        assert response.status_code == 200
        assert response.text == damian_report

        response = client.post(
            "/filter-reports/",
            json={
                "player": {
                    "sex": "MALE",
                    "firstName": "Damian",
                    "lastName": "Kowalski",
                }
            },
        )
        assert response.status_code == 200
        assert response.text == damian_report
