c.ServerProxy.servers = {
    'streamlit': {
        'command': [
            'streamlit',
            'run',
            'hello',
            '--server.port', '8501',
            '--browser.serverAddress', '0.0.0.0',
        ],
        'port': 8501,
        'timeout': 60
    }
}
