from config import settings
from xmlrpc.client import ServerProxy
from flask import (request, jsonify, render_template, make_response,
                   redirect, url_for, session, Response)


def start():
    server = request.args.get('server', '')
    program = request.args.get('program', '')
    api = settings.SERVERS[server]['api']
    ppr_test = ServerProxy(api)
    resp = ppr_test.supervisor.startProcess(program)

    return jsonify({"code": 0, "msg": "success"})


def stop():
    server = request.args.get('server', '')
    program = request.args.get('program', '')
    api = settings.SERVERS[server]['api']
    ppr_test = ServerProxy(api)
    resp = ppr_test.supervisor.stopProcess(program)

    return jsonify({"code": 0, "msg": "success"})


def restart():
    server = request.args.get('server', '')
    program = request.args.get('program', '')
    api = settings.SERVERS[server]['api']
    ppr_test = ServerProxy(api)
    ppr_test.supervisor.stopProcess(program)
    ppr_test.supervisor.startProcess(program)

    return jsonify({"code": 0, "msg": "success"})


def get_program_info(server, program):
    api = settings.SERVERS[server]['api']
    ppr_test = ServerProxy(api)
    try:
        info = ppr_test.supervisor.getProcessInfo(program)
        return info
    except Exception as e:
        return None


def tail_process_stdout_log():
    log_len = 10000
    server = request.args.get('server', '')
    program = request.args.get('program', '')
    offset = int(request.args.get('offset', '0'))
    api = settings.SERVERS[server]['api']
    ppr_test = ServerProxy(api)
    if(offset == 0):
        log_info = ppr_test.supervisor.tailProcessStdoutLog(program, offset, log_len)
        end = True
        offset_next = log_info[1]
        log_str = log_info[0]
    else:
        log_info = ppr_test.supervisor.readProcessStdoutLog(program, offset, log_len)
        if len(log_info) < log_len:
            end = True
        else:
            end = False
        log_str = log_info
        offset_next = offset + len(log_info)
    info = dict(
        detail=log_str,
        end=end,
        offset=offset_next
    )
    res = {"code": 0, "info": info}
    return jsonify(res)


def tail_process_stderr_log():
    log_len = 10000
    server = request.args.get('server', '')
    program = request.args.get('program', '')
    offset = int(request.args.get('offset', '0'))
    api = settings.SERVERS[server]['api']
    ppr_test = ServerProxy(api)
    if(offset == 0):
        log_info = ppr_test.supervisor.tailProcessStderrLog(program, offset, log_len)
        end = True
        offset_next = log_info[1]
        log_str = log_info[0]
    else:
        log_info = ppr_test.supervisor.readProcessStderrLog(program, offset, log_len)
        if len(log_info) < log_len:
            end = True
        else:
            end = False
        log_str = log_info
        offset_next = offset + len(log_info)
    info = dict(
        detail=log_str,
        end=end,
        offset=offset_next
    )
    res = {"code": 0, "info": info}
    return jsonify(res)
