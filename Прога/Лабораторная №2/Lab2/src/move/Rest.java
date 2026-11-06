
package move;

import ru.ifmo.se.pokemon.*;

public final class Rest extends StatusMove {
    private static final int SLEEP_TURNS = 3;

    public Rest() {
        super(Type.PSYCHIC, 0, 1.0);
    }

    @Override
    protected boolean checkAccuracy(Pokemon a, Pokemon d) {
        return true;
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        if (!p.isAlive() ||
                p.getCondition() == Status.SLEEP ||
                p.getHP() >= p.getStat(Stat.HP)) {
            return;
        }

        double missingHp = p.getStat(Stat.HP) - p.getHP();
        int missing = (int) Math.ceil(missingHp);

        p.setMod(Stat.HP, -missing);

        p.setCondition(
                new Effect()
                        .condition(Status.SLEEP)
                        .attack(0)
                        .turns(SLEEP_TURNS)
        );
    }

    @Override
    protected String describe() {
        return "использует Rest";
    }
}
