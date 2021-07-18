#!/bin/bash

wykonaj_robote () {
	systemctl start tor;
	echo "uruchomiono TOR";
	sleep $[ ( $RANDOM % 3 )  + 1 ]s;
	proxychains python3 vote_bankier.py;
	systemctl stop tor;
	echo "zatrzymano TOR";
}

    for (( i=1; $i <= 100 ; i++ ));
    do
        wykonaj_robote;
    done

echo "Gotowe!";
