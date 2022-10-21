my_app_path=$( dirname $(readlink -f "$0"))
echo $my_app_path
source "$my_app_path/pyenv/Scripts/activate"
cd "$my_app_path/main"
python codeEditor.py