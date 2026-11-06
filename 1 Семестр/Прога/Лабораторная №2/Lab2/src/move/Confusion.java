
package move;

import ru.ifmo.se.pokemon.*;

public final class Confusion extends SpecialMove {
    private static final double CONFUSION_CHANCE = 0.10;

    public Confusion() {
        super(Type.PSYCHIC, 50, 1.0);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() < CONFUSION_CHANCE) {
            p.confuse();
        }
    }

    @Override
    protected String describe() {
        return "использует Confusion";
    }
}
