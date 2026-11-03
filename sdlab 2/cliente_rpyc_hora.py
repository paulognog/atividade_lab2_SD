import rpyc

def solicitar_horario():
    HOST = 'localhost'
    PORTA = 18861
    
    print(f'[*] Conectando ao servidor RPyC em {HOST}:{PORTA}...')
    
    conexao = rpyc.connect(HOST, PORTA)      
    horario = conexao.root.get_horario()
    print(f'[+] Horário recebido do servidor via RPC: {horario}')
    
    conexao.close()
    print('[-] Conexão encerrada.')

if __name__ == '__main__':
    solicitar_horario()
