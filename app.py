import streamlit as st
import pkg_resources

# 获取当前 Python 环境中已安装的所有包
installed_packages = pkg_resources.working_set

# 打印已安装的包名和版本信息
for package in installed_packages:
    st.write(package.key, package.version)
    
from tabulate import tabulate
