#!/bin/bash

read -p "Enter first number : " num1
read -p "Enter second number : " num2

addition=$((num1 + num2))
subtraction=$((num1 - num2))
multiplication=$((num1 * num2))

if [ $num2 -ne 0 ]; then
  division=$((num1 / num2))
else
  division="undefined"
fi

echo "Addition : $addition"
echo "Subtraction : $subtraction"
echo "Multiplication : $multiplication"
echo "Division : $division"
