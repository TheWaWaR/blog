
############################################################
#  1. Install debian 7 by live CD
############################################################ 
# grub> ls /
# grub> linux /vmlinuz
# grub> initrd /initrd.gz
# grub> boot





LOGIN='weet'
HOME=/home/${LOGIN}
DOWNLOADS=${HOME}/Downloads
mkdir -p $HOME/local/opt
############################################################
#  2. Dependencies
############################################################


su root
adduser ${LOGIN} sudo              # Then reboot

# >> a. edit sources.list

# deb http://mirrors.163.com/debian wheezy main non-free contrib
# deb http://mirrors.163.com/debian wheezy-proposed-updates main contrib non-free
# deb-src http://mirrors.163.com/debian wheezy main non-free contrib
# deb-src http://mirrors.163.com/debian wheezy-proposed-updates main contrib non-free
# 
# deb http://mirrors.163.com/debian-security wheezy/updates main contrib non-free 
# deb-src http://mirrors.163.com/debian-security wheezy/updates main contrib non-free

# sudo vi /etc/apt/sources.list
sudo apt-get update

sudo apt-get install build-essential python-dev libncurses-dev
# Configure required: proxychains
sudo apt-get install curl htop tree tmux proxychains python-pip
sudo pip install ipython



cd ${DOWNLOADS}
############################################################
#  3. Download & Build tools
############################################################
# a. Emacs24
sudo pip install jedi epc pyflakes pep8
wget http://ftp.gnu.org/gnu/emacs/emacs-24.3.tar.xz
tar Jxf emacs-24.3.tar.xz
cd emacs-24.3
./configure --with-x=no --with-x-toolkit=no --with-xpm=no --with-jpeg=no --with-png=no --with-gif=no --with-tiff=no
make
sudo make install

# b. Vim74
wget ftp://ftp.vim.org/pub/vim/unix/vim-7.4.tar.bz2
tar xf vim-7.4.tar.bz2
cd vim74
./configure --enable-pythoninterp=yes
make
sudo make install

# c. zsh
wget http://sourceforge.net/projects/zsh/files/zsh/5.0.2/zsh-5.0.2.tar.bz2
wget http://sourceforge.net/projects/zsh/files/zsh-doc/5.0.2/zsh-5.0.2-doc.tar.bz2
tar xf zsh-5.0.2.tar.bz2
tar xf zsh-5.0.2-doc.tar.bz2
cd zsh-5.0.2
./configure && make
sudo make install

# Config zsh
curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | sh
curl https://gist.github.com/TheWaWaR/28291f8fb326bbdfe714/raw/87a8f1bddec42d94f93e2d851e39ad6cf4e0ef48/.zshrc > ~/.zshrc

# bash
# >> export TMUX_SHELL='/usr/local/bin/zsh'
# tmux
curl https://gist.githubusercontent.com/TheWaWaR/5889519/raw/96d183211a899462a923a2dc1532b3490bbdd056/tmux.conf > ~/.tmux.conf




############################################################
#  4. Other Install
############################################################
# a. Mozilla Thunderbird
wget http://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/latest/linux-x86_64/en-US/thunderbird-24.5.0.tar.bz2
tar -xf thunderbird-24.5.0.tar.bz2
mv thunderbird ${HOME}/local/opt
sudo ln -s ${HOME}/local/opt/thunderbird/thunderbird /usr/bin/

# b. Skype  >> https://wiki.debian.org/zh_CN/skype
sudo dpkg --add-architecture i386
sudo apt-get update
wget -O skype-install.deb http://www.skype.com/go/getskype-linux-deb
sudo dpkg -i skype-install.deb
sudo apt-get install -f

# c. Fontconfig-infinality ==> http://www.neowin.net/forum/topic/1153268-installing-infinality-freetypefontconfig-in-debian-7/
git clone https://github.com/chenxiaolong/Debian-Packages.git
cd Debian-Packages/
## Deps
sudo apt-get install pdebuild-cross docbook-to-man quilt # Get deps
cd freetype-infinality/
dpkg-checkbuilddeps
cd ../fontconfig-infinality/
dpkg-checkbuilddeps
## Build
cd ../freetype-infinality/
./build.sh
cd ../fontconfig-infinality/
./build.sh
## Install
cd ..
sudo dpkg -i freetype-infinality/*.deb fontconfig-infinality/*.deb
## Config
cd /etc/fonts/infinality
sudo ./infctl.sh setstyle [yourpreferredstyle]
