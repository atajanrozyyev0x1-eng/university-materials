
package pokemon;

import ru.ifmo.se.pokemon.Type;
import move.FocusBlast;

public final class Simisage extends Pansage {

    public Simisage(String name, int level) {
        super(name, level);

        setType(Type.GRASS);

        setStats(75, 98, 63, 98, 63, 101);

        addMove(new FocusBlast());
    }
}
