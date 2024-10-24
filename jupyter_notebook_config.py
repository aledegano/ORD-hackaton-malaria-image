c.ServerProxy.servers = {
    'streamlit': {
        'command': [
            'streamlit',
            'run',
            '../work/hackathon_SDSC_2024/code/streamlit_app.py',
            '--server.port', '8501',
            '--browser.serverAddress', '0.0.0.0',
        ],
        'port': 8501,
        'timeout': 60
    }
}
