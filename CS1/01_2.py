# clases
from items import item
CrimsonGuard = item("Crimson Guard", 3725, "For 8 seconds, grant nearby allied heroes and buildings a 100% chance " +
                    "to block 70 + 50% of caster's strength as damage from each incoming attack",
                    ["+250 Health", "+12 health Regenation", "+8 armor"])

SkullBasher = item("Skull Basher", 2875, "Grants melee heroes a 25% chance on hit to stun the target for 1.2 seconds" +
                   "and deal 100 bonus physical damage. Bash chance for ranged heroes is 10%.",
                   ["+10 strengh", "+30 damage"])

GhostScepter = item("Ghost Scepter", 1500, "You enter ghost form for 4 seconds, becoming immune to physical damage," +
                    "but are unable to attack and 40% more vulnerable to magic damage.",
                    ["+5 strengh", "+5 agility", "+5 intelligence"])

CrimsonGuard.mostrar_informacion()
print()
SkullBasher.mostrar_informacion()
print()
GhostScepter.mostrar_informacion()
