import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Roaming In Space",
    options={"build_exe": {"packages":["pygame"], 
    "include_files":["rocket.jpeg", "space.jpeg", "ARIALUNI.TTF"]}},
    executables = executables
)