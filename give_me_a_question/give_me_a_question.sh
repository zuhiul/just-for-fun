if [ ! -n "$1" ] ;then
    echo '2000' > in
else
    echo $1 > in
fi
python3 give_me_a_question.py
