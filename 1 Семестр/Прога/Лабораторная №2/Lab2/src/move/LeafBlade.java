package move;

import ru.ifmo.se.pokemon.*;

public final class LeafBlade extends PhysicalMove {
    private static final double CRITICAL_HIT_CHANCE = 0.125;
    private static final double CRITICAL_DAMAGE_MULTIPLIER = 1.5;

    public LeafBlade() {
        super(Type.GRASS, 90, 1.0);
    }

    @Override
    protected double calcCriticalHit(Pokemon attacker, Pokemon defender) {
        if (Math.random() < CRITICAL_HIT_CHANCE) {
            System.out.println("Критический удар!");
            return CRITICAL_DAMAGE_MULTIPLIER;
        }

        return 1.0;
    }

    @Override
    protected String describe() {
        return "использует Leaf Blade";
    }
}
