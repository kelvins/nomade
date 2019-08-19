from nomade import utils


def test_slugify_with_slug():
    assert utils.slugify('my_migration_1') == 'my_migration_1'


def test_slugify_with_multiple_spaces():
    assert utils.slugify(' Ace  of  Spades ') == 'ace_of_spades'


def test_slugify_with_special_chars():
    assert utils.slugify('# Nomad _on the road!') == 'nomad_on_the_road'


def test_unique_id():
    assert utils.unique_id() != utils.unique_id()
