wget https://www.python.org/ftp/python/3.13.14/python-3.13.14-amd64.exe

./python-3.13.14-amd64.exe

echo "python installiert - weiter"
pacman -S git nano vim

wget -O ~/.vim/autoload/plug.vim https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

cp ./.vimrc ~/

vim +'PlugInstall --sync' +qa

echo "alias python='/C/Users/maikt/AppData/Local/Programs/Python/Python313/python'" >> ~/.bashrc
echo "alias pip='/C/Users/maikt/AppData/Local/Programs/Python/Python313/Lib/site-packages/pip'" >> ~/.bashrc
echo "export PATH=$PATH:/C/Users/maikt/AppData/Local/Programs/Python/Python313/" >> ~/.bashrc 

source ~/.bashrc
