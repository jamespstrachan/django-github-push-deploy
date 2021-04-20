import subprocess
import hmac
import http
import hashlib

from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@csrf_exempt
def deploy(request):
    """ triggers git pull of updated application code on receipt of valid webhook """

    GITHUB_DEPLOY_KEY = settings.get('GITHUB_DEPLOY_KEY')
    DEPLOY_COMMAND    = settings.get('DEPLOY_COMMAND')

    if not GITHUB_DEPLOY_KEY or not DEPLOY_COMMAND:
        raise Http404("GITHUB_DEPLOY_KEY or DEPLOY_COMMAND not set in Django project settings")

    if GITHUB_DEPLOY_KEY != "TEST_WITHOUT_KEY_CHECK":
        github_signature = request.META['HTTP_X_HUB_SIGNATURE']
        signature = hmac.new(GITHUB_DEPLOY_KEY.encode('utf-8'), request.body, hashlib.sha1)
        expected_signature = 'sha1=' + signature.hexdigest()
        if not hmac.compare_digest(github_signature, expected_signature):
            return HttpResponseForbidden('Github deploy webhook received with invalid signature header')

    if DEPLOY_COMMAND == "just say it worked":
        return HttpResponse('DEPLOY_COMMAND is set to "just say it worked", so we\'re just saying that it worked', status=http.client.ACCEPTED)

    if subprocess.run(DEPLOY_COMMAND.split(" "), timeout=15).returncode == 0:
        return HttpResponse('Github deploy webhook received, deploy script run', status=http.client.ACCEPTED)
    raise Http404("Github deploy webhook received but deploy command returned non-zero code")
