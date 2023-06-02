from config import settings
from xmlrpc.client import ServerProxy
from flask import (request, jsonify, render_template, make_response,
                   redirect, url_for, session, Response)
from .program import get_program_info


def get_group_list():
    group_list = []
    for k in settings.GROUPS.keys():
        program_list = settings.GROUPS[k]['program_list']
        tmp = {}
        tmp['name'] = k
        tmp['desc'] = settings.GROUPS[k]['group_desc']
        program_info_list = []
        for item in program_list:
            server = item.split(".")[0]
            program = item.split(".")[1]
            program_info = get_program_info(server, program)
            if program_info:
                program_info['server'] = server
                program_info['group'] = [k]
                program_info_list.append(program_info)
        tmp['program_list'] = program_info_list
        group_list.append(tmp)

    res = {"code": 0, "info": group_list}
    return jsonify(res)


def get_group_of_program(server, program):
    group_list = []
    server_program = server + "." + program
    for k in settings.GROUPS.keys():
        program_list = settings.GROUPS[k]['program_list']
        if server_program in program_list:
            group_list.append(k)
    return group_list


def g_restart_all():
    group = request.args.get('group', '')
    program_list = settings.GROUPS[group]['program_list']
    for item in program_list:
        server = item.split(".")[0]
        program = item.split(".")[1]
        api = settings.SERVERS[server]['api']
        ppr_test = ServerProxy(api)
        ppr_test.supervisor.stopProcess(program)
        ppr_test.supervisor.startProcess(program)

    return jsonify({"code": 0, "msg": "success"})


def g_start_all():
    group = request.args.get('group', '')

    program_list = settings.GROUPS[group]['program_list']
    for item in program_list:
        server = item.split(".")[0]
        program = item.split(".")[1]
        api = settings.SERVERS[server]['api']
        ppr_test = ServerProxy(api)
        ppr_test.supervisor.startProcess(program)

    return jsonify({"code": 0, "msg": "success"})


def g_stop_all():
    group = request.args.get('group', '')
    program_list = settings.GROUPS[group]['program_list']

    for item in program_list:
        server = item.split(".")[0]
        program = item.split(".")[1]
        api = settings.SERVERS[server]['api']
        ppr_test = ServerProxy(api)
        ppr_test.supervisor.stopProcess(program)

    return jsonify({"code": 0, "msg": "success"})
