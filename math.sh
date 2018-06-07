#!/bin/bash
#initial value of counter is set to 3
car=10

while  [ $car -le 100 ]

do
echo 
    echo $car
        ((car= $car +10))
done

echo "All done"

