'''
def es_ip_valida (cadena):
    # Verificación del prefijo de subred
    try:
        ip,m=cadena.split("/")
        m_num=int(m)
        ipl=ip.split(".")
    except:
        return False
    
    if m_num<0 or m_num>32: return False
    
    for octeto in ipl:
        if int(octeto)<0 or int(octeto) >255: return False 
    
    return True
    
    print (m)
    print (ip)
    print(a,b,c,d)
    
'''

def es_ip_valida(cadena):
    try:
        ip, m = cadena.split("/")
        octetos = ip.split(".")
        
        return (
            0 <= int(m) <= 32
            and len(octetos) == 4
            and all(o.isdigit() and 0 <= int(o) <= 255 for o in octetos)
        )
    except:
        return False

print(es_ip_valida("192.168.10.4/24"))