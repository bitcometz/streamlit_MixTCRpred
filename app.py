import streamlit as st
import subprocess
import os

python_path = subprocess.run(["which", "python"], stdout=subprocess.PIPE, text=True).stdout.strip()
cmd_line     = " ".join([python_path, "aa.py"])
return_code  = os.system(cmd_line)
