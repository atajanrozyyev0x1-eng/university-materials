package move;

import ru.ifmo.se.pokemon.*;

public final class HealPulse extends StatusMove {
    private static final double HEALING_RATIO = 0.5;
    private static final int MIN_HEALING = 1;

    public HealPulse() {
        super(Type.PSYCHIC, 0, 1.0);
    }

    @Override
    protected boolean checkAccuracy(Pokemon a, Pokemon d) {
        return true;
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        double missingHp = p.getStat(Stat.HP) - p.getHP();
        int missing = (int) Math.ceil(missingHp);

        double halfHp = p.getStat(Stat.HP) * HEALING_RATIO;
        int roundedHealing = (int) Math.round(halfHp);
        int healingAmount = Math.max(MIN_HEALING, roundedHealing);
        int healing = Math.min(missing, healingAmount);

        if (healing > 0) {
            p.setMod(Stat.HP, -healing);
        }
    }

    @Override
    protected String describe() {
        return "использует Heal Pulse";
    }
}
