
title: 我的Vim 配置清单
created: 2014-04-03 15:34
category: Programming
**********

# 试图解决的问题
  总得来说就是尽可能模仿IDE中的特性，同时又保证编辑器不至于太复杂。
  
## 项目文件管理(目录树)
## Outline(Class browser)
## Python 编程:
   + 代码检查: flymake, pylint, pep8
   + 智能代码提示
   + Go to definition


# 配置步骤   
1. 安装基础配置集合
  项目主页：https://github.com/fisadev/fisa-vim-config
  安装过程：
``` bash
    sudo apt-get install vim exuberant-ctags git
    sudo pip install dbgp vim-debug pep8 flake8 pyflakes isort
    # 注意备份自己的旧配置
    curl -L https://raw.githubusercontent.com/fisadev/fisa-vim-config/master/.vimrc > ~/.vimrc
    # 然后打开vim克隆相应的插件
    vim
```

2. 打开 rope 强化Python编程
``let g:pymode_rope = 1``
