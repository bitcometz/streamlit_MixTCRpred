import pkg_resources
import subprocess



# 获取当前 Python 环境中已安装的所有包
installed_packages = pkg_resources.working_set

# 打印已安装的包名和版本信息
for package in installed_packages:
    print(package.key, package.version)

python_path    = subprocess.run(["which", "python"], stdout=subprocess.PIPE, text=True).stdout.strip()
print(python_path)
