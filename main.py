from services import CharacterFactory, GameEngine, ConsoleLogger

def main():
    logger = ConsoleLogger()
    engine = GameEngine(logger)
    factory = CharacterFactory()

    p1 = factory.create_character("warrior", "Arthur")
    p2 = factory.create_character("mage", "Merlin")

    engine.add_player(p1)
    engine.add_player(p2)

    print("\n--- Battle Starts ---")
    actions = engine.run_battle_round()
    for action in actions:
        print(action)

if __name__ == "__main__":
    main()
