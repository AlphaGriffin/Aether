#todo!!
# echo "Starting The Docker Build Process"
FROM gentoo/stage3-amd64

# echo "Installing Programs"
# install your apps
RUN emerge --sync
RUN emerge games-misc/cowsay
RUN emerge games-misc/fortune-mod
RUN emerge dev-vcs/git

CMD cd /
RUN git clone http://github.com/ruckusist/TF_Curses
CMD cd TF_Curses
RUN python3 setup.py install
CMD cd /

# echo "Final Output of program... might now show til run"
# do something...
CMD fortune | cowsay

CMD tf_curses
