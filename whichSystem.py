import re, sys, subprocess

if len(sys.argv) != 2:
    print("\n[!] Usage: python3 %s <ip>\n" % sys.argv[0])
    sys.exit(1)

def get_ttl(ip):
    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    out = out.split()
    out = out[12].decode('utf-8')

    ttl_value = re.findall(r"\d{1,3}", out)[0]
    return ttl_value

def get_os(ttl):
    ttl = int(ttl)

    if ttl >= 0 and ttl <= 64:
        return "Linux"
    elif ttl >= 65 and ttl <= 128:
        return "Windows"
    else:
        return "Not found"

if __name__ == "__main__":
    ip = sys.argv[1]
    ttl = get_ttl(ip)
    os_name = get_os(ttl)
    print("\n%s (ttl -> %s): %s\n" % (ip, ttl, os_name))