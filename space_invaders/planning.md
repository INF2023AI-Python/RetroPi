
0. Bsp gameplay
    https://www.youtube.com/watch?v=MU4psw3ccUI
    https://www.youtube.com/watch?v=uGjgxwiemms

1. player logik
    1. Movement
        a. MS
    2. HP Coloring
        a. standard farbe
    3. Shooting
        a. attack speed

2. gegner logik
    1. Movement
        a. X>X => Y+1 => X<X =>...
    2. Mob Level System
        a. Score Values
        b. designs
    3. HP Coloring
        a. standard farben
        b. farbverlauf bei hits
    4. Shooting
        a. attack speed
        b. wer kann schießen? (e.g. reihe 2 schießt nicht reihe 1 an)

3. Neutrals
    1. Rocks
        a. HP
    2. Special Ship
        a. Score
        b. maybe on-kill extra player / base hp?

4. Base
    1. Hp
    -> Komplette leißte ist HP-Balken, dort wo Bullet hittet wird hp weniger
    -> 8 segmente a 4 Pixel, jedes Segment 2 Hits, dann weg

5. interaktion und punkte logik
    1. Bullets
        a. shooting
    2. Collisions
        a. bullet/player -> player dmg
        b. bullet/mob ->  mob dmg
        c. bullet/base -> base dmg
        d. bullet/rock -> rock dmg
        e. bullet/bullet -> both bullets are destroyed
        f. mob/rock -> maybe: massive rock dmg
        g. mob/base -> loose
    3. Lose Conditions
        a. Player dead
        b. Base dead
        c. Mob berührt Base 
    4. Basis-HP system (Hp-Strich der unten im Bild ist)
    5. Level bzw. Wave System
    6. Score speichern



Game Design:

Player:
Player mit mehreren HP
Bewegt sich auf X achse

Gegner
Gegner eigentlich one Hit-> besser mehr HP und dafür weniger
Reihen an gegnern
bewegen sich leicht auf X achse, dann am rand eins runter, y achse vor und andre richtung x achse

Neutral Rocks:
Hindernisse mit mehreren HP, wenn gehittet verlieren sie Hp

Hp anstelle mit kleiner werdenden models mit Farbe darstellen
e.g. 
Plyer Hp Grün->Gelb->Rot->dead
Gegner HP 
Weiß->(Orange->)Rot->Tot

Neutrals HP:
Grün->Gelb->Rot->dead
Bei neutrals 1Hit != 1Farb Stufe weiter
e.g. 3 Hits zum wechsel

Neues Level (eigentlich kein level sonder alles außer score resettet)
=> neue gegner, ggf. mehr gegner / Gegner mehr HP /
Gegner schießen öfter
=> Neutral elemente respawnen

Score steigt pro gekilltem gegner

Wegem begrenzten Platz > nach erfolgreichem clearen einer wave, vor dem spawn der nächsten einen wave-counter einblenden?

Unterschiedlichen Gegner Typen vlt in minmal anderer Form darstellen und dafür aber auch noch die Farbe ändern
-> bei hit wird die farbe immer rötlicher
maybe so: 
Tier3 Mob>2Hits> Farbe von Tier2 Mob>1Hit> Farbe von Tier1 Mob>1Hit> dead
Wenn es Tier 2 farbe hat, dann stirbt es nach genauso vielen Hits wie das tier2 mob
Erst beim kill gibts punkte


Kein Pause Button:
bei einer neuen wave muss iwas bewegt werden, damit es weiter geht.



Mobs:
Farben zeigen HP an

- unterschiedliche formen + größen

jeder mob für 5x5 ausgelegt:
keine abstände zwischen den mobs
-> mobs können +-1y Pixel plaziert werden, um unterschied klar zu machen
-> mobs abwechselnd plazieren e.g. kleinere, neben größeren

-> kleinere mobs können in ihrem 5x5 hin und her fliegen

Größen(X*Y - Dimensionen)
- klein: 2X
- normal: 3X
- groß: 4x
- riesig 5x

AS (AttackSpeed): Schussraten in Anzahl der Schüsse/Vorwärtsbewegte Reihen
- langsam 1/3
- normal: 1/2
- schnell: 1/1
- sehr schnell: 2/1

HP:
1 Hp = 1 Bullet nötig

Special Points Ship:
- 1Hp
- normal groß
- Score: 200

Typ1:
- normal groß
- 1HP
- normal AS
- Score: 25

Typ2: 
- klein
- 1HP
- schnell AS
- Score: 30

Typ3:
- groß
- 2HP
- langsam AS
- Score: 30

Typ4:
- groß
- 1HP
- sehr schnell AS
- Score: 30

Typ...




Maybe Bullets machen 2 Dmg 
-> ermöglicht piercing
-> interessanteres game
