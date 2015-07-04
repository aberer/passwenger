#! /bin/bash

if [ $# != 1 ] && [ $# != 2 ] ; then
    echo $0 lang
    exit 
fi

if [ "$(which aspell)" == "" ]; then
    echo "aspell not found. Please install the package!"
    exit 
fi

excl_expr=""
if [ $# == 2 ]; then
    excl_expr=" | "
fi

lang=$1
aspell -d $lang dump master > /dev/null

if [ $? != 0 ]; then
    echo "languge \"$lang\" not found. Please install the respective aspell package"
fi

cmd="aspell -d $lang dump master \
     | aspell -l $lang expand \
    | tr ' ' '\n'  \
    | sed -e  's/ä/ae/g' -e 's/ö/oe/g' -e 's/ü/ue/g' -e 's/ß/ss/g' \
          -e 's/Ä/Ae/g' -e 's/Ö/Oe/g' -e 's/Ü/Ue/g' \
    | tr '[:upper:]' '[:lower:]' \
    | sort -u"

if [ $# == 2 ]; then
    cmd="$cmd | tr -d  '$2' | grep -v '^$' | sort -u " 
fi
eval $cmd
