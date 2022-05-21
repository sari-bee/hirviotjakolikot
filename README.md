# Hirviöt ja kolikot -peli

Peli on yksi Helsingin yliopiston Ohjelmoinnin jatkokurssin (v. 2021) tehtävistä.

### Asennus ja käynnistys

1. Siirry terminaalissa kansioon jossa tiedostot ovat.
2. Avaa virtuaaliympäristö: "python3 -m venv venv" ja "source venv/bin/activate".
3. Asenna pygame: "pip install pygame".
4. Avaa sovellus: "python3 main.py". Samalla komennolla saat käynnistettyä sovelluksen uudestaan.
5. Pelattuasi tarpeeksi poistu virtuaaliympäristöstä komennolla "deactivate".

### Peli

Peli on varsin suoraviivainen: robottia ohjaillaan vasemmalla ja oikealla nuolinäppäimellä ja sen tulee estää kolikon katoaminen näytön alareunaan ja samalla väistellä hirviötä. Pisteitä kertyy sitä mukaa, kun robotti osuu kolikkoon.

### In english

The game features a robot, a monster and a coin. The aim is to avoid losing the coin to the void that is the lower bound of the screen while avoiding the monster. The more times you save the coin, the more points you get.

You can start the game by opening the virtual environment with  "python3 -m venv venv" and "source venv/bin/activate", installing pygame with "pip install pygame" and then typing "python3 main.py". When you're done playing, you can leave the virtual environment by typing "deactivate".
