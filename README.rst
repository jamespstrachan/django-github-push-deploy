=====
Django Github Push Deploy
=====

A little Django app which listens for Github webhook calls, checks their key
and triggers a local deploy script of the user's choosing.

Quick start
-----------

1. Add "django_github_push_deploy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_github_push_deploy',
    ]

2. Include the polls URLconf in your project urls.py like this:

    path('django-github-push-deploy/', include('django_github_push_deploy.urls')),

3. Add GITHUB_DEPLOY_KEY and DEPLOY_SCRIPT_PATH (relative to BASE_DIR) to your project settings like this:

    GITHUB_DEPLOY_KEY  = "BIG-LONG-GITHUB-HASH"
    DEPLOY_SCRIPT_PATH = "./deploy.sh"

4. GITHUB_DEPLOY_KEY can be set to "TEST_WITHOUT_KEY_CHECK" to skip the key check (useful for checking initial
   setup, shouldn't be left in this state)

5. DEPLOY_COMMAND can be set to "just say it worked" to return a 200 if we get to the script-running step (useful
   for checking initial Github setup, but nothing will happen if you leave it in this state)
