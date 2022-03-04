from locust import HttpUser, SequentialTaskSet, task, constant


class UpdatePoints(SequentialTaskSet):

    @task
    def login_user(self):
        exepected_response = "Summary | GUDLFT Registration"
        with self.client.post("showSummary", {"email": "john@simplylift.co"},
                              catch_response=True, name="login") as response:
            if response.status_code == 200 and exepected_response in response.text:
                response.success()
            else:
                response.failure("post failed")

    @task
    def buy_places(self):
        exepected_response = "Great-booking complete!"
        with self.client.post("/purchasePlaces", {"competition": "Spring Festival", "club": "Simply Lift", "places": 1},
                              catch_response=True, name="places") as response:
            if response.status_code == 200 and exepected_response in response.text:
                response.success()
            else:
                response.failure("buy places failed")


class GetUpdatePoints(HttpUser):
    """ performences pour la mise à jour des points """
    host = "http://127.0.0.1:5000/"
    tasks = [UpdatePoints]
    wait_time = constant(2)
