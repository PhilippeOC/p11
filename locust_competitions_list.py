from locust import HttpUser, SequentialTaskSet, task, constant


class CompetitionsList(SequentialTaskSet):

    @task
    def login_user(self):
        exepected_response = "Competitions:"
        result = "fail"
        with self.client.post("showSummary", {"email": "john@simplylift.co"},
                              catch_response=True, name="login") as response:
            if response.status_code == 200 and exepected_response in response.text:
                result = "success"
                response.success()
            else:
                response.failure("post failed")
        print(self.login_user.__name__, result)


class GetCompetitionslist(HttpUser):
    """ Performences pour l'affiche de la liste des compétitions """
    host = "http://127.0.0.1:5000/"
    tasks = [CompetitionsList]
    wait_time = constant(1)
