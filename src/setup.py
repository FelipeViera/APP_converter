# setup.py
from cx_Freeze import setup, Executable

# Configurações do executável
executables = [
    Executable(
        'src/main.py',  # Substitua pelo nome do seu script Python
        base='Win32GUI',  # Use 'Win32GUI' para aplicação com interface gráfica
        icon='src/assets/moeda.ico'  # Substitua pelo caminho do seu ícone
    )
]

# Informações do projeto
setup(
    name='App_conveter',
    version='1.0',
    description='App capaz de converter valores financeiros.',
    executables=executables
)
