from r2r import R2RClient
import os

# get client for r2r
def get_client():
    try:
        client_r2r = R2RClient(base_url=os.environ.get("SCIPHI_CLOUD_URL"))
        status_server = client_r2r.health()
        
        if status_server['response'] == "ok":
            return client_r2r
        else:
            return 'Error de servidor R2R'
    except Exception as e:
        return 'Error de servicio'

# login    
def login():
    try:
        cli = get_client()
        cli.login(os.environ.get("SCIPHI_CLOUD_USERNAME"), os.environ.get("SCIPHI_CLOUD_PASSWORD"))
        return cli.access_token
    except:
        return 'Usuario o contraseña incorrectos'


