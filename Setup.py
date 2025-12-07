from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="AliensonEarth",
    version="1.0",
    description="jogo projeto final Linguagem Prog. Aplicada",
    executables=executables
)