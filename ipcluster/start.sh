export conjson=`echo ${HOME}/.config/ipython/profile_default/security/ipcontroller-engine.json`
export engjson=`echo ${USER}@10.100.20.201:${HOME}/.ipython/profile_default/security`
screen -ls | grep ipc | cut -d. -f1 | awk '{print $1}' | xargs kill
screen -S ipc -d -m ./controller.sh
./engine.sh
scp $conjson $engjson 
scp engine.sh ${USER}@10.100.20.201:${HOME}
ssh wasit@10.100.20.201 ${HOME}/engine.sh
