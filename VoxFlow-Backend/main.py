import app
import socket

def find_free_port(start_port=5000, max_attempts=10):
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    raise RuntimeError("Nenhuma porta disponível encontrada!")

if __name__ == '__main__':
    try:
        port = find_free_port(3000)
        print(f"Executando na porta {port -1}")
        app.app.run(host='127.0.0.1', port=port, debug=True)
    except RuntimeError as e:
        print(e)