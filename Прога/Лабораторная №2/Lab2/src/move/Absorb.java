package move;

import ru.ifmo.se.pokemon.*;

public final class Absorb extends SpecialMove {
    private static final double MIN_DAMAGE = 1.0;
    private static final double FALLBACK_DAMAGE_DIVISOR = 2.0;
    private static final double HEALING_RATIO = 0.5;
    private static final int MIN_HEALING = 1;
    private double actualDamage;

    public Absorb() {
        super(Type.GRASS, 20, 1.0);
    }



    @Override
    protected void applyOppDamage(Pokemon opponent, double damage) {

        double damageValue = Double.isFinite(damage)
                ? Math.abs(damage)
                : power / FALLBACK_DAMAGE_DIVISOR;
        double safeDamage = Math.max(MIN_DAMAGE, damageValue);

        double before = Math.max(0, opponent.getHP());
        super.applyOppDamage(opponent, safeDamage);
        double after = Math.max(0, opponent.getHP());

        double dealtDamage = before - after;
        actualDamage = Math.max(0, dealtDamage);
    }




    @Override
    protected void applySelfDamage(Pokemon p, double damage) {
        double missingHp = p.getStat(Stat.HP) - p.getHP();
        int missing = (int) Math.ceil(missingHp);

        double healingValue = actualDamage * HEALING_RATIO;
        int roundedHealing = (int) Math.round(healingValue);
        int healingAmount = Math.max(MIN_HEALING, roundedHealing);
        int healing = actualDamage > 0 ? Math.min(missing, healingAmount) : 0;

        if (healing > 0) {
            p.setMod(Stat.HP, -healing);
        }
    }


    @Override
    protected String describe() {
        return "использует Absorb";
    }
}