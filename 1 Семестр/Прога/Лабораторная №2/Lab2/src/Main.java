import ru.ifmo.se.pokemon.*;
import pokemon.*;

public class Main {
    public static void main(String[] args) {

        Battle battle = new Battle();

        battle.addAlly(new Celesteela("Rocket", 30));
        battle.addAlly(new Simisage("Simisage", 30));
        battle.addAlly(new Gallade("Gallade", 30));

        battle.addFoe(new Pansage("Pansage", 13));
        battle.addFoe(new Ralts("Ralts", 19));
        battle.addFoe(new Kirlia("Kirlia", 20));

        battle.go();
    }
}