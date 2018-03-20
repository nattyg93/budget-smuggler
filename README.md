# Budget Smuggler API


## Running

- This app is built on top of [dj-core](https://github.com/ionata/dj-core)
  and is intended to be deployed using
  [deployment-django](https://github.com/ionata/deployment-django).
- Ensure the web server (e.g. NGINX) and any proxies (e.g. HAProxy) are
  configured to:
  - forward `/backend/` to the Django server (e.g. Gunicorn);
  - alias `/backend/api/v1/` to `/api/v1/` so that the front-end can run in
    Internet Explorer 11 and issue GETs to `/api/v1/` without sending the
    cookie set by Django, which is valid on the path `/backend/`.

