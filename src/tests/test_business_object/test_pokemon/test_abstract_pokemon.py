from business_object.pokemon.abstract_pokemon import AbstractPokemon


class TestAbstractPokemon(AbstractPokemon):
    def test_level_up():
        pokemon = AbstractPokemon()
        pokemon.level_up()
        assert pokemon._level == 1
