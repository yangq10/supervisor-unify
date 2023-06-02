from config import settings
from xmlrpc.client import ServerProxy
from flask import (request, jsonify, render_template, make_response,
                   redirect, url_for, session, Response)
from .group import get_group_of_program


def get_server_list():
    server_list = []
    for k in settings.SERVERS.keys():
        item = settings.SERVERS[k]
        tmp = {}
        tmp['name'] = k
        tmp['desc'] = item['server_desc']
        api = item['api']
        ppr_test = ServerProxy(api)
        p_list = ppr_test.supervisor.getAllProcessInfo()
        for p_info in p_list:
            p_info['server'] = k
            p_info['group'] = get_group_of_program(k, p_info['name'])
        tmp['program_list'] = p_list

        server_list.append(tmp)
    res = {"code": 0, "info": server_list}
    return jsonify(res)


def restart_all():
    server = request.args.get('server', '')
    api = settings.SERVERS[server]['api']
    ppr_test = ServerProxy(api)
    ppr_test.supervisor.stopAllProcesses()
    ppr_test.supervisor.startAllProcesses()
    return jsonify({"code": 0, "msg": "success"})


def start_all():
    server = request.args.get('server', '')
    api = settings.SERVERS[server]['api']
    ppr_test = ServerProxy(api)
    ppr_test.supervisor.startAllProcesses()
    return jsonify({"code": 0, "msg": "success"})


def stop_all():
    server = request.args.get('server', '')
    api = settings.SERVERS[server]['api']
    ppr_test = ServerProxy(api)
    ppr_test.supervisor.stopAllProcesses()
    return jsonify({"code": 0, "msg": "success"})
