
package pokemon;

import ru.ifmo.se.pokemon.*;
import move.*;

public class Pansage extends Pokemon {

    public Pansage(String name, int level) {
        super(name, level);

        setType(Type.GRASS);

        setStats(50, 53, 48, 53, 48, 64);

        setMove(
                new Confide(),
                new FurySwipes(),
                new Rest()
        );
    }
}
