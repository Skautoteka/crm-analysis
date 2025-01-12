from unittest import mock

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

example_reports = """[
    {
        "id": "276232af-8b64-414f-b574-d4bb5ff10358",
        "name": "Raport #1",
        "status": "IN_PROGRESS",
        "taskId": "b7a42c1e-6d97-4f84-a1fa-5a1e9c7a7c74",
        "createdAt": "2025-01-10T09:07:19.000Z",
        "updatedAt": "2025-01-10T09:07:19.000Z",
        "playerId": "4b4b4076-c6aa-4601-841e-ba51f7e60c32",
        "regionId": null,
        "createdById": null,
        "player": {
            "name": "Damian Kowalski",
            "id": "4b4b4076-c6aa-4601-841e-ba51f7e60c32",
            "masterPlayerId": null,
            "version": 1,
            "firstName": "Damian",
            "lastName": "Kowalski",
            "sex": "Mężczyzna",
            "nationality": "Polska",
            "birthYear": 1994,
            "height": 185,
            "weight": 74,
            "physique": "Atletyczna",
            "positionId": "DEFENSE",
            "teamId": "806f4fbe-2f92-4b33-a99c-ef6e64951af1",
            "createdAt": "2025-01-10T09:07:19.000Z",
            "updatedAt": "2025-01-10T09:07:19.000Z"
        },
        "traits": [
            {
                "traitId": "STAMINA",
                "traitLabel": "Kondycja",
                "reportId": "276232af-8b64-414f-b574-d4bb5ff10358",
                "value": 2,
                "createdAt": "2025-01-10T09:07:19.000Z",
                "updatedAt": "2025-01-10T09:07:19.000Z"
            },
            {
                "traitId": "SPEED",
                "traitLabel": "Szybkość",
                "reportId": "276232af-8b64-414f-b574-d4bb5ff10358",
                "value": 2,
                "createdAt": "2025-01-10T09:07:19.000Z",
                "updatedAt": "2025-01-10T09:07:19.000Z"
            },
            {
                "traitId": "REFLEX",
                "traitLabel": "Refleks",
                "reportId": "276232af-8b64-414f-b574-d4bb5ff10358",
                "value": 9,
                "createdAt": "2025-01-10T09:07:19.000Z",
                "updatedAt": "2025-01-10T09:07:19.000Z"
            },
            {
                "traitId": "INTERCEPTIONS",
                "traitLabel": "Parady",
                "reportId": "276232af-8b64-414f-b574-d4bb5ff10358",
                "value": 5,
                "createdAt": "2025-01-10T09:07:19.000Z",
                "updatedAt": "2025-01-10T09:07:19.000Z"
            },
            {
                "traitId": "HEADING",
                "traitLabel": "Strzał głową",
                "reportId": "276232af-8b64-414f-b574-d4bb5ff10358",
                "value": 5,
                "createdAt": "2025-01-10T09:07:19.000Z",
                "updatedAt": "2025-01-10T09:07:19.000Z"
            },
            {
                "traitId": "FINISHING",
                "traitLabel": "Wykończenie",
                "reportId": "276232af-8b64-414f-b574-d4bb5ff10358",
                "value": 9,
                "createdAt": "2025-01-10T09:07:19.000Z",
                "updatedAt": "2025-01-10T09:07:19.000Z"
            }
        ],
        "positions": [
            {
                "id": 5,
                "reportId": "276232af-8b64-414f-b574-d4bb5ff10358",
                "positionId": "WINGER",
                "isOptional": true,
                "createdAt": "2025-01-10T09:07:19.000Z",
                "updatedAt": "2025-01-10T09:07:19.000Z"
            },
            {
                "id": 4,
                "reportId": "276232af-8b64-414f-b574-d4bb5ff10358",
                "positionId": "DEFENSE",
                "isOptional": false,
                "createdAt": "2025-01-10T09:07:19.000Z",
                "updatedAt": "2025-01-10T09:07:19.000Z"
            }
        ],
        "description": {
            "id": 3,
            "reportId": "276232af-8b64-414f-b574-d4bb5ff10358",
            "evaluation": null,
            "potential": null,
            "physicalDescription": "Strong and agile player",
            "mentalDescription": "Highly focused and motivated",
            "technicalDescription": "Excellent ball control and dribbling",
            "opponentId": null,
            "formationId": null,
            "timePlayed": null,
            "goalsScored": null,
            "assists": null,
            "summary": null,
            "createdAt": "2025-01-10T09:07:19.000Z",
            "updatedAt": "2025-01-10T09:07:19.000Z"
        }
    },
    {
        "id": "692b678d-ba81-4b7d-8d17-5aac71aee80e",
        "name": "Raport #5",
        "status": "IN_PROGRESS",
        "taskId": "8f4d3d5f-71cf-4b7e-8f53-7e09c8d6c73f",
        "createdAt": "2025-01-10T09:07:19.000Z",
        "updatedAt": "2025-01-10T09:07:19.000Z",
        "playerId": "18228bad-4d09-4773-8aeb-73938a2456c1",
        "regionId": null,
        "createdById": null,
        "player": {
            "name": "Cristiano Ronaldo",
            "id": "18228bad-4d09-4773-8aeb-73938a2456c1",
            "masterPlayerId": null,
            "version": 1,
            "firstName": "Cristiano",
            "lastName": "Ronaldo",
            "sex": "Mężczyzna",
            "nationality": "Portugalska",
            "birthYear": 1984,
            "height": 187,
            "weight": 83,
            "physique": "Atletyczna",
            "positionId": "FORWARD",
            "teamId": "002e573c-3a98-4ed8-8bb6-e3a178b9731f",
            "createdAt": "2025-01-10T09:07:19.000Z",
            "updatedAt": "2025-01-10T09:07:19.000Z"
        },
        "traits": [],
        "positions": [],
        "description": null
    },
    {
        "id": "89bca610-c842-42d6-892c-e9ecfea85760",
        "name": "Raport #2",
        "status": "COMPLETED",
        "taskId": "b7a42c1e-6d97-4f84-a1fa-5a1e9c7a7c74",
        "createdAt": "2025-01-10T09:07:19.000Z",
        "updatedAt": "2025-01-10T09:07:19.000Z",
        "playerId": "bfaee0f7-2e44-4182-a78f-a03253eee601",
        "regionId": null,
        "createdById": null,
        "player": {
            "name": "Jakub Prus",
            "id": "bfaee0f7-2e44-4182-a78f-a03253eee601",
            "masterPlayerId": null,
            "version": 1,
            "firstName": "Jakub",
            "lastName": "Prus",
            "sex": "Mężczyzna",
            "nationality": "Polska",
            "birthYear": 1998,
            "height": 192,
            "weight": 80,
            "physique": "Atletyczna",
            "positionId": "WINGER",
            "teamId": "c4bc4290-f729-48e5-81d7-cd612d8afea0",
            "createdAt": "2025-01-10T09:07:19.000Z",
            "updatedAt": "2025-01-10T09:07:19.000Z"
        },
        "traits": [
            {
                "traitId": "PHYSICAL_STRENGTH",
                "traitLabel": "Siła fizyczna",
                "reportId": "89bca610-c842-42d6-892c-e9ecfea85760",
                "value": 7,
                "createdAt": "2025-01-10T09:07:19.000Z",
                "updatedAt": "2025-01-10T09:07:19.000Z"
            }
        ],
        "positions": [
            {
                "id": 6,
                "reportId": "89bca610-c842-42d6-892c-e9ecfea85760",
                "positionId": "FORWARD",
                "isOptional": true,
                "createdAt": "2025-01-10T09:07:19.000Z",
                "updatedAt": "2025-01-10T09:07:19.000Z"
            }
        ],
        "description": {
            "id": 4,
            "reportId": "89bca610-c842-42d6-892c-e9ecfea85760",
            "evaluation": null,
            "potential": null,
            "physicalDescription": "Quick and light on feet",
            "mentalDescription": "Tactical awareness",
            "technicalDescription": "Precise passing and positioning",
            "opponentId": null,
            "formationId": null,
            "timePlayed": null,
            "goalsScored": null,
            "assists": null,
            "summary": null,
            "createdAt": "2025-01-10T09:07:19.000Z",
            "updatedAt": "2025-01-10T09:07:19.000Z"
        }
    },
    {
        "id": "8dc3f345-7f02-44de-a0d7-466bbf3a4ac1",
        "name": "Raport #4",
        "status": "COMPLETED",
        "taskId": "8f4d3d5f-71cf-4b7e-8f53-7e09c8d6c73f",
        "createdAt": "2025-01-10T09:07:19.000Z",
        "updatedAt": "2025-01-10T09:07:19.000Z",
        "playerId": "18228bad-4d09-4773-8aeb-73938a2456c1",
        "regionId": null,
        "createdById": null,
        "player": {
            "name": "Cristiano Ronaldo",
            "id": "18228bad-4d09-4773-8aeb-73938a2456c1",
            "masterPlayerId": null,
            "version": 1,
            "firstName": "Cristiano",
            "lastName": "Ronaldo",
            "sex": "Mężczyzna",
            "nationality": "Portugalska",
            "birthYear": 1984,
            "height": 187,
            "weight": 83,
            "physique": "Atletyczna",
            "positionId": "FORWARD",
            "teamId": "002e573c-3a98-4ed8-8bb6-e3a178b9731f",
            "createdAt": "2025-01-10T09:07:19.000Z",
            "updatedAt": "2025-01-10T09:07:19.000Z"
        },
        "traits": [],
        "positions": [],
        "description": null
    },
    {
        "id": "ee918037-4d57-4552-86d6-16701011fd43",
        "name": "Raport #3",
        "status": "IN_PROGRESS",
        "taskId": "d2b3c8e4-8c9e-4e84-a7de-3c0a8d07c72e",
        "createdAt": "2025-01-10T09:07:19.000Z",
        "updatedAt": "2025-01-10T09:07:19.000Z",
        "playerId": "bfaee0f7-2e44-4182-a78f-a03253eee601",
        "regionId": null,
        "createdById": null,
        "player": {
            "name": "Jakub Prus",
            "id": "bfaee0f7-2e44-4182-a78f-a03253eee601",
            "masterPlayerId": null,
            "version": 1,
            "firstName": "Jakub",
            "lastName": "Prus",
            "sex": "Mężczyzna",
            "nationality": "Polska",
            "birthYear": 1998,
            "height": 192,
            "weight": 80,
            "physique": "Atletyczna",
            "positionId": "WINGER",
            "teamId": "c4bc4290-f729-48e5-81d7-cd612d8afea0",
            "createdAt": "2025-01-10T09:07:19.000Z",
            "updatedAt": "2025-01-10T09:07:19.000Z"
        },
        "traits": [],
        "positions": [],
        "description": null
    }
]
"""

# damian_report = (
#     '[{"id":"276232af-8b64-414f-b574-d4bb5ff10358","name":"Raport #1","status":'
#     '"IN_PROGRESS","createdAt":"2024-10-30T07:46:03.000Z","updatedAt":'
#     '"2024-10-30T07:46:03.000Z","playerId":"4b4b4076-c6aa-4601-841e-ba51f7e60c32",'
#     '"player":{"name":"Damian Kowalski","id":"4b4b4076-c6aa-4601-841e-ba51f7e60c32",'
#     '"firstName":"Damian","lastName":"Kowalski","sex":"MALE","age":30,"position":'
#     '"WINGER","teamId":null,"createdAt":"2024-10-30T07:46:03.000Z",'
#     '"updatedAt":"2024-10-30T07:46:03.000Z"}}]'
# )

example_notes = """
[
    {
        "id": "4853f3dc-39f5-44dd-aeed-f06f1f485b26",
        "name": "Notatka 6",
        "status": "IN_PROGRESS",
        "taskId": "8f4d3d5f-71cf-4b7e-8f53-7e09c8d6c73f",
        "evaluation": 10,
        "content": "Jakas notatka",
        "playerNumber": 222,
        "teamId": "002e573c-3a98-4ed8-8bb6-e3a178b9731f",
        "createdAt": "2025-01-06T17:01:36.000Z",
        "updatedAt": "2025-01-08T16:28:41.000Z",
        "createdById": "0a1868a7-cc98-4b57-8807-2c7f8e556c1b",
        "team": {
            "id": "002e573c-3a98-4ed8-8bb6-e3a178b9731f",
            "name": "Lech Poznan",
            "league": null,
            "city": null,
            "country": null,
            "createdAt": "2025-01-06T16:58:12.000Z",
            "updatedAt": "2025-01-06T16:58:12.000Z"
        }
    },
    {
        "id": "53621606-0e30-4b27-ae77-ec0445e454b1",
        "name": "Notatka 7",
        "status": "COMPLETED",
        "taskId": "8f4d3d5f-71cf-4b7e-8f53-7e09c8d6c73f",
        "evaluation": 10,
        "content": null,
        "playerNumber": 333,
        "teamId": null,
        "createdAt": "2025-01-08T15:54:10.000Z",
        "updatedAt": "2025-01-08T15:54:15.000Z",
        "createdById": "0a1868a7-cc98-4b57-8807-2c7f8e556c1b",
        "team": null
    },
    {
        "id": "692b678d-ba81-4b7d-8d17-5aac71aee80e",
        "name": "Notatka #5",
        "status": "COMPLETED",
        "taskId": "8f4d3d5f-71cf-4b7e-8f53-7e09c8d6c73f",
        "evaluation": 2,
        "content": "To jest notatka #5",
        "playerNumber": 222,
        "teamId": "002e573c-3a98-4ed8-8bb6-e3a178b9731f",
        "createdAt": "2025-01-06T16:58:13.000Z",
        "updatedAt": "2025-01-06T16:58:13.000Z",
        "createdById": null,
        "team": {
            "id": "002e573c-3a98-4ed8-8bb6-e3a178b9731f",
            "name": "Lech Poznan",
            "league": null,
            "city": null,
            "country": null,
            "createdAt": "2025-01-06T16:58:12.000Z",
            "updatedAt": "2025-01-06T16:58:12.000Z"
        }
    },
    {
        "id": "89bca610-c842-42d6-892c-e9ecfea85760",
        "name": "Notatka #2",
        "status": "COMPLETED",
        "taskId": "8f4d3d5f-71cf-4b7e-8f53-7e09c8d6c73f",
        "evaluation": 9,
        "content": "To jest notatka #2",
        "playerNumber": 333,
        "teamId": "de81af74-1f4a-4b87-9b90-e975af472577",
        "createdAt": "2025-01-06T16:58:13.000Z",
        "updatedAt": "2025-01-06T16:58:13.000Z",
        "createdById": null,
        "team": {
            "id": "de81af74-1f4a-4b87-9b90-e975af472577",
            "name": "Barcelona",
            "league": null,
            "city": null,
            "country": null,
            "createdAt": "2025-01-06T16:58:12.000Z",
            "updatedAt": "2025-01-06T16:58:12.000Z"
        }
    }
]
"""


# def test_filter_reports():
#     with mock.patch("requests.get") as mocked_get:
#         get = mock.MagicMock()
#         get.text = example_reports
#         get.status_code = 200
#         mocked_get.return_value = get
#
#         response = client.post("/filter-reports/", json={})
#         assert response.status_code == 200
#         assert response.text == example_reports
#
#         response = client.post(
#             "/filter-reports/", json={"player": {"position": "WINGER"}}
#         )
#         assert response.status_code == 200
#         assert response.text == damian_report
#
#         response = client.post(
#             "/filter-reports/", json={"player": {"sex": "MALE"}}
#         )
#         assert response.status_code == 200
#         assert response.text == example_reports
#
#         response = client.post(
#             "/filter-reports/", json={"player": {"sex": "FEMALE"}}
#         )
#         assert response.status_code == 200
#         assert response.text == "[]"
#
#         response = client.post("/filter-reports/", json={"name": "Raport #1"})
#         assert response.status_code == 200
#         assert response.text == damian_report
#
#         response = client.post(
#             "/filter-reports/",
#             json={"name": "Raport #1", "player": {"sex": "MALE"}},
#         )
#         assert response.status_code == 200
#         assert response.text == damian_report
#
#         response = client.post(
#             "/filter-reports/",
#             json={
#                 "player": {
#                     "sex": "MALE",
#                     "firstName": "Damian",
#                     "lastName": "Kowalski",
#                 }
#             },
#         )
#         assert response.status_code == 200
#         assert response.text == damian_report

example_reports_for_avg = """
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
            "positionId": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "traitId": "REFLEX",
                "traitLabel": "Refleks",
                "value": 5,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z"            
            },
            {
                "traitId": "SPEED",
                "traitLabel": "Szybkość",
                "value": 9,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z"
            }
        ],
        "positions": [],
        "description": null
    },
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12f7",
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
            "positionId": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "traitId": "REFLEX",
                "traitLabel": "Refleks",
                "value": 5,
                "createdAt": "2024-11-13T20:00:28.000Z",
                "updatedAt": "2024-11-13T20:00:28.000Z"
            },
            {
                "traitId": "SPEED",
                "traitLabel": "Szybkość",
                "value": 9,
                "createdAt": "2024-11-13T20:00:28.000Z",
                "updatedAt": "2024-11-13T20:00:28.000Z"
            }
        ],
        "positions": [],
        "description": null
    },
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12f8",
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
            "positionId": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "traitId": "REFLEX",
                "traitLabel": "Refleks",
                "value": 5,
                "createdAt": "2024-11-14T20:00:28.000Z",
                "updatedAt": "2024-11-14T20:00:28.000Z"
            },
            {
                "traitId": "SPEED",
                "traitLabel": "Szybkość",
                "value": 10,
                "createdAt": "2024-11-14T20:00:28.000Z",
                "updatedAt": "2024-11-14T20:00:28.000Z"
            }
        ],
        "positions": [],
        "description": null
    },
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12f9",
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
            "positionId": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "traitId": "REFLEX",
                "traitLabel": "Refleks",
                "value": 6,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z"
            },
            {
                "traitId": "SPEED",
                "traitLabel": "Szybkość",
                "value": 8,
                "createdAt": "2024-11-12T20:00:28.000Z",
                "updatedAt": "2024-11-12T20:00:28.000Z"
            }
        ],
        "positions": [],
        "description": null
    },
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12fa",
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
            "positionId": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "traitId": "REFLEX",
                "traitLabel": "Refleks",
                "value": 6,
                "createdAt": "2024-11-13T20:00:28.000Z",
                "updatedAt": "2024-11-13T20:00:28.000Z"
            },
            {
                "traitId": "SPEED",
                "traitLabel": "Szybkość",
                "value": 8,
                "createdAt": "2024-11-13T20:00:28.000Z",
                "updatedAt": "2024-11-13T20:00:28.000Z"
            }
        ],
        "positions": [],
        "description": null
    },
    {
        "id": "ba50b02f-def9-4141-9668-156a37be12fb",
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
            "positionId": "FORWARD",
            "teamId": null,
            "createdAt": "2024-11-12T20:00:28.000Z",
            "updatedAt": "2024-11-12T20:00:28.000Z"
        },
        "traits": [
            {
                "traitId": "REFLEX",
                "traitLabel": "Refleks",
                "value": 6,
                "createdAt": "2024-11-14T20:00:28.000Z",
                "updatedAt": "2024-11-14T20:00:28.000Z"
            },
            {
                "traitId": "SPEED",
                "traitLabel": "Szybkość",
                "value": 9,
                "createdAt": "2024-11-14T20:00:28.000Z",
                "updatedAt": "2024-11-14T20:00:28.000Z"
            }
        ],
        "positions": [],
        "description": null
    }
]
"""


def test_analyze_filters():
    with mock.patch("requests.get") as mocked_get:
        get = mock.MagicMock()
        get.text = example_reports
        get.status_code = 200
        mocked_get.return_value = get

        response = client.post(
            "/analyze/",
            json={},
        )
        assert response.status_code == 422

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == {
            "4b4b4076-c6aa-4601-841e-ba51f7e60c32",
            "bfaee0f7-2e44-4182-a78f-a03253eee601",
            "18228bad-4d09-4773-8aeb-73938a2456c1",
        }

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == {
            "4b4b4076-c6aa-4601-841e-ba51f7e60c32",
            "bfaee0f7-2e44-4182-a78f-a03253eee601",
            "18228bad-4d09-4773-8aeb-73938a2456c1",
        }

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {
                        "key": "position",
                        "predicate": "eq",
                        "value": "WINGER",
                    }
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == {
            # "4b4b4076-c6aa-4601-841e-ba51f7e60c32",  # TODO
            "bfaee0f7-2e44-4182-a78f-a03253eee601",
        }

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {
                        "key": "sex",
                        "predicate": "eq",
                        "value": "Mężczyzna",
                    },
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == {
            "4b4b4076-c6aa-4601-841e-ba51f7e60c32",
            "bfaee0f7-2e44-4182-a78f-a03253eee601",
            "18228bad-4d09-4773-8aeb-73938a2456c1",
        }

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {
                        "key": "sex",
                        "predicate": "eq",
                        "value": "Kobieta",
                    },
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == set([])

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {
                        "key": "report_name",
                        "predicate": "eq",
                        "value": "Raport #1",
                    },
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == {
            "4b4b4076-c6aa-4601-841e-ba51f7e60c32",
        }

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {
                        "key": "report_name",
                        "predicate": "eq",
                        "value": "Raport #1",
                    },
                    {
                        "key": "sex",
                        "predicate": "eq",
                        "value": "Mężczyzna",
                    },
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == {
            "4b4b4076-c6aa-4601-841e-ba51f7e60c32",
        }

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {
                        "key": "sex",
                        "predicate": "eq",
                        "value": "Mężczyzna",
                    },
                    {
                        "key": "firstName",
                        "predicate": "eq",
                        "value": "Damian",
                    },
                    {
                        "key": "lastName",
                        "predicate": "eq",
                        "value": "Kowalski",
                    },
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == {
            "4b4b4076-c6aa-4601-841e-ba51f7e60c32",
        }

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {
                        "key": "playerId",
                        "predicate": "eq",
                        "value": "4b4b4076-c6aa-4601-841e-ba51f7e60c32",
                    },
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == {
            "4b4b4076-c6aa-4601-841e-ba51f7e60c32",
        }


def test_analyze_with_avg():
    with mock.patch("requests.get") as mocked_get:
        get = mock.MagicMock()
        get.text = example_reports_for_avg
        get.status_code = 200
        mocked_get.return_value = get

        # response = client.post(
        #     "/mean/",
        #     json={
        #         "trait": {
        #             "name": "Szybkość",
        #         }
        #     },
        # )
        # assert response.status_code == 200
        # assert (
        #     response.text
        #     == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334},{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        # )
        #
        # response = client.post(
        #     "/mean/",
        #     json={
        #         "trait": {
        #             "name": "Szybkość",
        #             "descending": True,
        #         }
        #     },
        # )
        # assert response.status_code == 200
        # assert (
        #     response.text
        #     == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334},{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        # )
        #
        # response = client.post(
        #     "/mean/",
        #     json={
        #         "trait": {
        #             "name": "Szybkość",
        #             "descending": False,
        #         }
        #     },
        # )
        # assert response.status_code == 200
        # assert (
        #     response.text
        #     == '[{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334},{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334}]'
        # )
        #
        # response = client.post(
        #     "/mean/",
        #     json={
        #         "trait": {
        #             "name": "Szybkość",
        #             "minValue": 8,
        #         }
        #     },
        # )
        # assert response.status_code == 200
        # assert (
        #     response.text
        #     == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334},{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        # )
        #
        # response = client.post(
        #     "/mean/",
        #     json={
        #         "trait": {
        #             "name": "Szybkość",
        #             "minValue": 8,
        #             "maxValue": 10,
        #         }
        #     },
        # )
        # assert response.status_code == 200
        # assert (
        #     response.text
        #     == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334},{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        # )
        #
        # response = client.post(
        #     "/mean/",
        #     json={
        #         "trait": {
        #             "name": "Szybkość",
        #             "minValue": 9,
        #         }
        #     },
        # )
        # assert response.status_code == 200
        # assert (
        #     response.text
        #     == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334}]'
        # )

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {
                        "key": "speed",
                        "predicate": "avg_gt",
                        "value": "9",
                    }
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == {
            "18228bad-4d09-4773-8aeb-73938a2456c1",
        }

        #
        # response = client.post(
        #     "/mean/",
        #     json={
        #         "trait": {
        #             "name": "Szybkość",
        #             "maxValue": 9,
        #         }
        #     },
        # )
        # assert response.status_code == 200
        # assert (
        #     response.text
        #     == '[{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        # )

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {
                        "key": "speed",
                        "predicate": "avg_lt",
                        "value": "9",
                    }
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == {
            "28228bad-4d09-4773-8aeb-73938a2456c2",
        }

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {"key": "finishing", "predicate": "eq", "value": "twenty"}
                ],
            },
        )
        assert response.status_code == 502

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {"key": "finishing", "predicate": "eq", "value": "20"}
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == set([])

        response = client.post(
            "/analyze/",
            json={
                "type": "report",
                "filters": [
                    {"key": "finishing", "predicate": "lt", "value": "20"}
                ],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(report["playerId"] for report in answer)
        assert players == set([])

        #
        # response = client.post(
        #     "/mean/",
        #     json={
        #         "trait": {
        #             "name": "Szybkość",
        #             "minValue": 8,
        #             "maxValue": 10,
        #         },
        #         "report": {
        #             "playerId": "18228bad-4d09-4773-8aeb-73938a2456c1",
        #         },
        #     },
        # )
        # assert response.status_code == 200
        # assert (
        #     response.text
        #     == '[{"playerId":"18228bad-4d09-4773-8aeb-73938a2456c1","value":9.333333333333334}]'
        # )
        #
        # response = client.post(
        #     "/mean/",
        #     json={
        #         "trait": {
        #             "name": "Szybkość",
        #             "minValue": 8,
        #             "maxValue": 10,
        #         },
        #         "report": {
        #             "playerId": "28228bad-4d09-4773-8aeb-73938a2456c2",
        #         },
        #     },
        # )
        # assert response.status_code == 200
        # assert (
        #     response.text
        #     == '[{"playerId":"28228bad-4d09-4773-8aeb-73938a2456c2","value":8.333333333333334}]'
        # )
        #
        # response = client.post(
        #     "/mean/",
        #     json={
        #         "trait": {
        #             "name": "Szybkość",
        #             "minValue": 9,
        #             "maxValue": 10,
        #         },
        #         "report": {
        #             "playerId": "28228bad-4d09-4773-8aeb-73938a2456c2",
        #         },
        #     },
        # )
        # assert response.status_code == 200
        # assert response.text == "[]"


def test_analyze_notes():
    with mock.patch("requests.get") as mocked_get:
        get = mock.MagicMock()
        get.text = example_notes
        get.status_code = 200
        mocked_get.return_value = get

        response = client.post(
            "/analyze/",
            json={
                "type": "note",
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(note["playerNumber"] for note in answer)
        assert players == {
            222,
            333,
        }

        response = client.post(
            "/analyze/",
            json={
                "type": "note",
                "filters": [],
            },
        )
        assert response.status_code == 200
        answer = response.json()
        players = set(note["playerNumber"] for note in answer)
        assert players == {
            222,
            333,
        }


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
