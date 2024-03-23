import kicktippbb

def test_can_parse_if_odd_string_has_prefix():
    oddstring = kicktippbb.split_odds('Quote: 1.40 / 5 / 7.25')
    assert oddstring == ['1.40', '5', '7.25']

def test_can_parse_if_split_character_is_pipe():
    oddstring = kicktippbb.split_odds('1.40 | 5 | 7.25')
    assert oddstring == ['1.40', '5', '7.25']

def test_can_parse_if_split_character_is_slash():
    oddstring = kicktippbb.split_odds('1.40 / 5 / 7.25')
    assert oddstring == ['1.40', '5', '7.25']
