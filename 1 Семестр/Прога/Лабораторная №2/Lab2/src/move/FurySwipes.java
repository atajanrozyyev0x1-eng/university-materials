
package move;

import ru.ifmo.se.pokemon.*;

public final class FurySwipes extends PhysicalMove {
    private static final double TWO_HITS_CHANCE = 0.35;
    private static final double UP_TO_THREE_HITS_CHANCE = 0.70;
    private static final double UP_TO_FOUR_HITS_CHANCE = 0.85;

    private int completedHits = 0;

    public FurySwipes() {
        super(Type.NORMAL, 18, 0.8);
    }

    @Override
    protected boolean checkAccuracy(Pokemon attacker, Pokemon defender) {
        if (completedHits == 0) {
            hits = 1;

            if (!super.checkAccuracy(attacker, defender)) {
                return false;
            }

            double roll = Math.random();

            if (roll < TWO_HITS_CHANCE) {
                hits = 2;
            } else if (roll < UP_TO_THREE_HITS_CHANCE) {
                hits = 3;
            } else if (roll < UP_TO_FOUR_HITS_CHANCE) {
                hits = 4;
            } else {
                hits = 5;
            }
        }

        return true;
    }

    @Override
    protected void applyOppDamage(Pokemon opponent, double damage) {
        super.applyOppDamage(opponent, damage);
        completedHits++;

        if (!opponent.isAlive() || completedHits == hits) {
            hits = completedHits;
            completedHits = 0;
        }
    }

    @Override
    protected String describe() {
        return "использует Fury Swipes";
    }
}
