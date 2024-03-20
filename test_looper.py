import looper


def test_looper_main():
    example_db_table = 'data/looper_db.csv'

    message_text = looper.main(example_db_table)
    
    expected_message_text = "Hello"
    assert('Dr. Beyonce' in message_text)
    assert('Proteomics' in message_text)
    assert('Assessing the risk to develop a growing teratoma syndrome' in message_text)
    assert(message_text.count('doi: ') == 7)