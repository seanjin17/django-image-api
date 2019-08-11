#!/bin/sh
apt-get update -yq                                                    && \
apt-get install -yq git make curl                                     && \
curl -L https://git.io/n-install | N_PREFIX=~/.n bash -s -- -y latest && \
source /root/.bashrc                                                  && \
npm install -g pm2 yarn                                               && \
cd ~                                                                  && \
git clone https://github.com/frk1/steamhourboostv2.git                && \
cd steamhourboostv2                                                   && \
yarn install --production                                             && \
clear                                                                 && \
echo "Done. Run 'npm run user' to add users!"
