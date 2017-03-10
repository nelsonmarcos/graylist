from database import Database


def query_servers(query_dict):
    query_result = [server for server in Database.find('servers', query_dict)]
    return query_result


def query_result_to_str(query_result):
    server_list = []
    for server in query_result:
        server_list.append(server['server'])

    server_list_in_str = '\n'.join(server_list)
    return server_list_in_str