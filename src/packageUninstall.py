import os

def check_dependents(module_name):
    """
    查看一个模块的依赖
    :param module_name: 模块名
    :return: module_name 所依赖的模块的列表
    """
    with os.popen('python3 -m pip show %s' % module_name) as p:
        dependents = p.readlines()

        if not len(dependents):
            return None
        dependents = dependents[-2]
        dependents = dependents.split(':')[-1].replace(' ', '').strip()
        if dependents:
            dependents = dependents.split(',')
        else:
            dependents = None
        return dependents


def remove(module_name):
    """
    递归地卸载一个模块
    :param module_name: 模块名称
    :return: None
    """
    dependents = check_dependents(module_name)
    if dependents:
        for package in dependents:
            remove(package)

    print("开始卸载依赖包:", module_name)
    os.system('python3 -m pip uninstall -y %s' % module_name)
    print("依赖包卸载完成:", module_name)


if __name__ == '__main__':
    pkg_name = input('请输入要卸载的第三方模块包: ')
    remove(pkg_name)