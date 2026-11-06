
package move;

import ru.ifmo.se.pokemon.*;

public final class RockSlide extends PhysicalMove {
    private static final double FLINCH_CHANCE = 0.30;
    private static final int FLINCH_TURNS = 1;

    public RockSlide() {
        super(Type.ROCK, 75, 0.9);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        if (p.isAlive() && Math.random() < FLINCH_CHANCE) {
            p.addEffect(
                    new Effect().attack(0).turns(FLINCH_TURNS)
            );
            p.prepareMove();
        }
    }

    @Override
    protected String describe() {
        return "обрушивает камни (Rock Slide)";
    }
}
