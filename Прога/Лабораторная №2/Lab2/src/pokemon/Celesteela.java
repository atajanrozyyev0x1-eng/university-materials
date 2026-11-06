package pokemon;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;
import move.RockSlide;
import move.DoubleTeam;
import move.Absorb;
import move.MegaDrain;

public final class Celesteela extends Pokemon {

    public Celesteela(String name, int level) {
        super(name, level);

        setType(Type.STEEL, Type.FLYING);

        setStats(97, 101, 103, 107, 101, 61);
        setMove(
                new RockSlide(),
                new DoubleTeam(),
                new Absorb(),
                new MegaDrain()
        );
    }
}

