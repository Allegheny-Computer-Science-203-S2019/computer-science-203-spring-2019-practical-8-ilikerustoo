# NOTE: You should run this script from the plugins-src/ directory
python3 -m compileall .
mkdir -p ../plugins
cp __pycache__/*.pyc ../plugins
mv ../plugins/frequencies1.cpython-36.pyc ../plugins/frequencies1.pyc
mv ../plugins/frequencies2.cpython-36.pyc ../plugins/frequencies2.pyc
mv ../plugins/words1.cpython-36.pyc ../plugins/words1.pyc
mv ../plugins/words2.cpython-36.pyc ../plugins/words2.pyc
