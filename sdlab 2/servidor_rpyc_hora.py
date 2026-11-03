import rpyc
from rpyc.utils.server import ThreadedServer
from datetime import datetime

class HorarioService(rpyc.Service):
    def on_connect(self, conn):
        print('[-] Cliente conectado ao serviço RPyC')

    def on_disconnect(self, conn):
        print('[-] Cliente desconectado do serviço RPyC')

    def exposed_get_horario(self):
        horario = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f'[*] Invocação remota recebida. Retornando: {horario}')
        return horario

if __name__ == '__main__':
    PORTA = 18861
    servidor = ThreadedServer(HorarioService, port=PORTA)
    print(f'[*] Servidor RPyC de Horário aguardando conexões na porta {PORTA}...')
    servidor.start()
