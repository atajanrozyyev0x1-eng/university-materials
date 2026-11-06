package move;

import ru.ifmo.se.pokemon.*;

public final class Growl extends StatusMove {

    public Growl() {
        super(Type.NORMAL, 0, 1.0);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        p.setMod(Stat.ATTACK, -1);
    }

    @Override
    protected String describe() {
        return "использует Growl";
    }
}
