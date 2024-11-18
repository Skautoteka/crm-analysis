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


example_reports_to_sort = """
[
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12f6",
        "name": "a",
        "status": "IN_PROGRESS",
        "createdAt": "2024-11-12T20:02:37.000Z",
        "updatedAt": "2024-11-12T20:02:37.000Z",
        "playerId": "18228bad-4d09-4773-8aeb-73938a2456c1",
        "createdById": "9b1e9a92-404c-44e5-bea3-1724d00f1db6",
        "player": {
            "name": "Cristiano Ronaldo",
            "id": "18228bad-4d09-4773-8aeb-73938a2456c1",
            "firstName": "Cristiano",
            "lastName": "Ronaldo",
            "sex": "MALE",
            "age": 24,
            "position": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                "name": "Refleks",
                "value": 5,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            },
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b9",
                "name": "Szybkość",
                "value": 9,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            }
        ]
    },
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12f6",
        "name": "a",
        "status": "IN_PROGRESS",
        "createdAt": "2024-11-12T20:02:37.000Z",
        "updatedAt": "2024-11-12T20:02:37.000Z",
        "playerId": "18228bad-4d09-4773-8aeb-73938a2456c1",
        "createdById": "9b1e9a92-404c-44e5-bea3-1724d00f1db6",
        "player": {
            "name": "Cristiano Ronaldo",
            "id": "18228bad-4d09-4773-8aeb-73938a2456c1",
            "firstName": "Cristiano",
            "lastName": "Ronaldo",
            "sex": "MALE",
            "age": 24,
            "position": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                "name": "Refleks",
                "value": 5,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            },
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b9",
                "name": "Szybkość",
                "value": 9,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            }
        ]
    },
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12f6",
        "name": "a",
        "status": "IN_PROGRESS",
        "createdAt": "2024-11-12T20:02:37.000Z",
        "updatedAt": "2024-11-12T20:02:37.000Z",
        "playerId": "18228bad-4d09-4773-8aeb-73938a2456c1",
        "createdById": "9b1e9a92-404c-44e5-bea3-1724d00f1db6",
        "player": {
            "name": "Cristiano Ronaldo",
            "id": "18228bad-4d09-4773-8aeb-73938a2456c1",
            "firstName": "Cristiano",
            "lastName": "Ronaldo",
            "sex": "MALE",
            "age": 24,
            "position": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                "name": "Refleks",
                "value": 5,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            },
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b9",
                "name": "Szybkość",
                "value": 10,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            }
        ]
    },
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12f7",
        "name": "a",
        "status": "IN_PROGRESS",
        "createdAt": "2024-11-12T20:02:37.000Z",
        "updatedAt": "2024-11-12T20:02:37.000Z",
        "playerId": "28228bad-4d09-4773-8aeb-73938a2456c2",
        "createdById": "9b1e9a92-404c-44e5-bea3-1724d00f1db6",
        "player": {
            "name": "Robert Lewandowski",
            "id": "28228bad-4d09-4773-8aeb-73938a2456c2",
            "firstName": "Robert",
            "lastName": "Lewandowski",
            "sex": "MALE",
            "age": 36,
            "position": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                "name": "Refleks",
                "value": 6,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            },
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b9",
                "name": "Szybkość",
                "value": 8,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            }
        ]
    },
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12f7",
        "name": "a",
        "status": "IN_PROGRESS",
        "createdAt": "2024-11-12T20:02:37.000Z",
        "updatedAt": "2024-11-12T20:02:37.000Z",
        "playerId": "28228bad-4d09-4773-8aeb-73938a2456c2",
        "createdById": "9b1e9a92-404c-44e5-bea3-1724d00f1db6",
        "player": {
            "name": "Robert Lewandowski",
            "id": "28228bad-4d09-4773-8aeb-73938a2456c2",
            "firstName": "Robert",
            "lastName": "Lewandowski",
            "sex": "MALE",
            "age": 36,
            "position": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                "name": "Refleks",
                "value": 6,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            },
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b9",
                "name": "Szybkość",
                "value": 8,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            }
        ]
    },
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12f7",
        "name": "a",
        "status": "IN_PROGRESS",
        "createdAt": "2024-11-12T20:02:37.000Z",
        "updatedAt": "2024-11-12T20:02:37.000Z",
        "playerId": "28228bad-4d09-4773-8aeb-73938a2456c2",
        "createdById": "9b1e9a92-404c-44e5-bea3-1724d00f1db6",
        "player": {
            "name": "Robert Lewandowski",
            "id": "28228bad-4d09-4773-8aeb-73938a2456c2",
            "firstName": "Robert",
            "lastName": "Lewandowski",
            "sex": "MALE",
            "age": 36,
            "position": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                "name": "Refleks",
                "value": 6,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            },
            {
                "id": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b9",
                "name": "Szybkość",
                "value": 9,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z",
                "ReportTrait": {
                    "traitId": "e0a6b3f5-1234-4f3b-912d-b44a63a1e2b8",
                    "reportId": "ba50b02f-def9-4141-9668-156a37be12f6",
                    "createdAt": "2024-11-12T20:02:37.000Z",
                    "updatedAt": "2024-11-12T20:02:37.000Z"
                }
            }
        ]
    }
]
"""


def test_mean():
    with mock.patch("requests.get") as mocked_get:
        get = mock.MagicMock()
        get.text = example_reports_to_sort
        get.status_code = 200
        mocked_get.return_value = get

        response = client.post(
            "/mean/",
            json={
                "trait": {
                    "name": "Szybkość",
                }
            },
        )
        assert response.status_code == 200
        assert (
            response.text
            == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334},{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        )

        response = client.post(
            "/mean/",
            json={
                "trait": {
                    "name": "Szybkość",
                    "descending": True,
                }
            },
        )
        assert response.status_code == 200
        assert (
            response.text
            == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334},{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        )

        response = client.post(
            "/mean/",
            json={
                "trait": {
                    "name": "Szybkość",
                    "descending": False,
                }
            },
        )
        assert response.status_code == 200
        assert (
            response.text
            == '[{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334},{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334}]'
        )

        response = client.post(
            "/mean/",
            json={
                "trait": {
                    "name": "Szybkość",
                    "minValue": 8,
                }
            },
        )
        assert response.status_code == 200
        assert (
            response.text
            == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334},{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        )

        response = client.post(
            "/mean/",
            json={
                "trait": {
                    "name": "Szybkość",
                    "minValue": 8,
                    "maxValue": 10,
                }
            },
        )
        assert response.status_code == 200
        assert (
            response.text
            == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334},{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        )

        response = client.post(
            "/mean/",
            json={
                "trait": {
                    "name": "Szybkość",
                    "minValue": 9,
                }
            },
        )
        assert response.status_code == 200
        assert (
            response.text
            == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334}]'
        )

        response = client.post(
            "/mean/",
            json={
                "trait": {
                    "name": "Szybkość",
                    "maxValue": 9,
                }
            },
        )
        assert response.status_code == 200
        assert (
            response.text
            == '[{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        )

        response = client.post(
            "/mean/",
            json={
                "trait": {
                    "name": "Szybkość",
                    "minValue": 8,
                    "maxValue": 10,
                },
                "report": {
                    "playerId": "18228bad-4d09-4773-8aeb-73938a2456c1",
                },
            },
        )
        assert response.status_code == 200
        assert (
            response.text
            == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334}]'
        )

        response = client.post(
            "/mean/",
            json={
                "trait": {
                    "name": "Szybkość",
                    "minValue": 8,
                    "maxValue": 10,
                },
                "report": {
                    "playerId": "28228bad-4d09-4773-8aeb-73938a2456c2",
                },
            },
        )
        assert response.status_code == 200
        assert (
            response.text
            == '[{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        )

        response = client.post(
            "/mean/",
            json={
                "trait": {
                    "name": "Szybkość",
                    "minValue": 9,
                    "maxValue": 10,
                },
                "report": {
                    "playerId": "28228bad-4d09-4773-8aeb-73938a2456c2",
                },
            },
        )
        assert response.status_code == 200
        assert response.text == "[]"
