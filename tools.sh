#!/bin/bash
#用来检查工程里的python文件的第一行有没有指定编码为 utf-8,因为代码里有汉字注释。
x=$(find . -name '*.py')
add_utf8(){
    sed -i '1 i #encoding: utf-8' $1
}
for item in ${x[*]}
do
    head -n 1 "$item"| grep utf-8
    if [[ "$?" -ne 0 ]]; then
        # 添加
        lines=$(cat ./mysite/__init__.py | wc -l)
        # 如果py文件为空
        echo "---------------$lines"
        if [[ $lines -eq 0 ]]; then
            echo "#encoding: utf-8" >> "$item"
        else
            add_utf8 "$item"
        fi
    fi
done

