from collections import defaultdict
import time

# rate limiting
class RateLimiter:
    def __init__(self, max_requests, per_seconds):
        self.max_requests = max_requests
        self.per_seconds = per_seconds
        self.requests = defaultdict(list)
    
    def allow_request(self, client_id):
        now = time.time()
        if client_id not in self.requests:
            self.requests[client_id] = [now]
            return True
        self.requests[client_id] = [timestamp for timestamp in self.requests[client_id] if now - timestamp < self.per_seconds]
        if len(self.requests[client_id]) < self.max_requests:
            self.requests[client_id].append(now)
            return True
        return False


# ip blocking
blocked_ips = set()

def is_ip_blocked(ip_address):
    return ip_address in blocked_ips


# heartbeat
import threading

def send_heartbeat(client_socket):
    while True:
        try:
            client_socket.sendall(b'HEARTBEAT')
            response = client_socket.recv(1024)
            if response != b'ACK':
                print("Heartbeat failed")
                break
            time.sleep(10)
        except:
            break

