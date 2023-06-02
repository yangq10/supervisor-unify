

from .import server
from .import program
from .import group


def init_official(app):
    app.add_url_rule('/server/list', view_func=server.get_server_list)
    app.add_url_rule('/server/restartall', view_func=server.restart_all)
    app.add_url_rule('/server/startall', view_func=server.start_all)
    app.add_url_rule('/server/stopall', view_func=server.stop_all)

    app.add_url_rule('/group/list', view_func=group.get_group_list)
    app.add_url_rule('/group/restartall', view_func=group.g_restart_all)
    app.add_url_rule('/group/startall', view_func=group.g_start_all)
    app.add_url_rule('/group/stopall', view_func=group.g_stop_all)

    app.add_url_rule('/program/start', view_func=program.start)
    app.add_url_rule('/program/stop', view_func=program.stop)
    app.add_url_rule('/program/restart', view_func=program.restart)
    app.add_url_rule('/program/tailstdoutlog', view_func=program.tail_process_stdout_log)
    app.add_url_rule('/program/tailstderrlog', view_func=program.tail_process_stderr_log)
