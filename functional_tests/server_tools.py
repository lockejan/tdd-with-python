from fabric.api import run
from fabric.context_managers import settings, shell_env


def _get_manage_dot_py(host: str) -> str:
    return f'~/sites/{host}/venv/bin/python ~/sites/{host}/manage.py'


def reset_database(host: str):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'vagrant@{host}:2222'):
        run(f'{manage_dot_py} flush --noinput')


def _get_server_env_vars(host: str) -> dict:
    env_lines = run(f'cat ~/sites/{host}/.env').splitlines()
    return dict(line.split('=') for line in env_lines if line)


def create_session_on_server(host: str, email: str) -> str:
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'vagrant@{host}:2222'):
        env_vars = _get_server_env_vars(host)
        with shell_env(**env_vars):
            session_key = run(f'{manage_dot_py} create_session {email}')
            return session_key.strip()
