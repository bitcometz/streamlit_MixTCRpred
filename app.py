import streamlit as st
import subprocess
import os

import sys

python_path = sys.executable
st.write("Python Interpreter Path:", python_path)

python_path = subprocess.run(["which", "python"], stdout=subprocess.PIPE, text=True).stdout.strip()
cmd_line     = " ".join([python_path, "aa.py"])
return_code  = os.system(cmd_line)
