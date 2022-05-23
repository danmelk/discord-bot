from dataclasses import dataclass

@dataclass
class Auth:
    client_id: str
    client_secret: str
    user_agent: str