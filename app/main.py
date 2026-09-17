from app.config import KNIGHTS
from app.knight import prepare_knights
# -------------------------------------------------------------------------------
# BATTLE:
# 1 Lancelot vs Mordred:


def battle(knights: dict) -> dict:
    knights = prepare_knights(KNIGHTS)

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection
    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0
        # return battle results:
    return {
        lancelot.name : lancelot.hp,
        arthur.name : arthur.hp,
        mordred.name : mordred.hp,
        red_knight.name : red_knight.hp,
    }


print(battle(KNIGHTS))
