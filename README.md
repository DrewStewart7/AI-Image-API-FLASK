# AI-Image-API-FLASK
Server for an AI image generation website. All of this was developed for learning purposes.



Requires https://github.com/lllyasviel/Fooocus to be running on the local machine.


Also requires a header sent with requests, "auth" = "bop123!"

This is used to ensure that the request is coming from a verified source. Could be modified to check that the request is coming from a certain IP, API key, or something else. For my use, the client would never see the outgoing request made by the site so it was safe to include a simple "password" as the auth value.
