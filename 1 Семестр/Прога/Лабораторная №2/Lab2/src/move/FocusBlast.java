
package move;

import ru.ifmo.se.pokemon.*;

public final class FocusBlast extends SpecialMove {
    private static final double DEFENSE_DROP_CHANCE = 0.10;

    public FocusBlast() {
        super(Type.FIGHTING, 120, 0.70);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() < DEFENSE_DROP_CHANCE) {
            p.setMod(Stat.SPECIAL_DEFENSE, -1);
        }
    }

    @Override
    protected String describe() {
        return "использует Focus Blast";
    }
}
