import looper


def test_looper_main():
    example_db_table = 'data/looper_db_example.csv'

    message_text = looper.main(example_db_table)
    
    expected_message_text = "Hello"
    assert('David' in message_text)
    assert('Ewing Sarcoma' in message_text)
    assert(message_text.count('doi: ') == 7)
    assert('Divergent HLA variations and heterogeneous expression' in message_text)