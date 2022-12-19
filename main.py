from django.conf import settings
import json
from gidconnect.APIs import ExtensionAPI
import datetime

user = settings.ENVIRONMENT_VARIABLES.get("USER")


class Greeting(RunnerView):
    def get_response():
        text = f"""*Gideon wants to initiate convertation with {user} for flirting, write a message to start conversation (small message)*"""
        generated = ExtensionAPI(extension_name="MegaTextGen", command=text, extra_kwargs={
            "max_tokens": 100,
            "engine": "text-davinci-002",
        })
        jsonified = json.loads(generated)
        error = jsonified.get("error")
        if error:
            return error

        resp = jsonified.get("response", {})
        ai_response = resp.get("response", {}).get(
            "choices", [{}])[0].get("text")
        return ai_response


RUNNER_STORE_VALUES_LIST = [
    {
        "name": "greeting",
        "variable": Greeting,
    }
]
