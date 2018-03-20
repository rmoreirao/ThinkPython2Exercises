If problems running push: https://stackoverflow.com/questions/31672796/git-clone-couldnt-resolve-fqdn-thus-cloning-fails

Using Git Bash:

env|grep -i proxy
unset  HTTP_PROXY HTTPS_PROXY http_proxy https_proxy
git push origin master