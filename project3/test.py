import pytest

#####Imports

def test_imports():
    import hashers
    import hashtable
    import plots
    import timer

##### Hashers

def test_kr():
    from hashers import HasherKR
    assert HasherKR().hash_key('INFO-F103') == 0x00000233

def test_crc32():
    from hashers import HasherCrc32
    assert HasherCrc32().hash_key('INFO-F103') == 0xB3EBBDC1

def test_djb2():
    from hashers import HasherDjb2
    assert HasherDjb2().hash_key('INFO-F103') == 0xEDB14EF8

##### HashTableChaining

def test_ht_chaining_is_empty():
    from hashers import HasherKR
    from hashtable import HashTableChaining
    assert HashTableChaining(1, HasherKR()).size() == 0

def test_ht_chaining_size_is_correct_after_insert():
    from hashers import HasherKR
    from hashtable import HashTableChaining
    ht = HashTableChaining(16, HasherKR())
    ht.insert('Jack', 'O\'Neill')
    assert ht.size() == 1

def test_ht_chaining_size_is_correct_after_replace():
    from hashers import HasherKR
    from hashtable import HashTableChaining
    ht = HashTableChaining(16, HasherKR())
    ht.insert('Jack', '?')
    ht.insert('Jack', 'O\'Neill')
    assert ht.size() == 1

def test_ht_chaining_get():
    from hashers import HasherKR
    from hashtable import HashTableChaining
    ht = HashTableChaining(16, HasherKR())
    ht.insert('Jack', 'O\'Neill')
    assert ht.get('Jack') == 'O\'Neill'

def test_ht_chaining_get_after_replace():
    from hashers import HasherKR
    from hashtable import HashTableChaining
    ht = HashTableChaining(16, HasherKR())
    ht.insert('Jack', 'O\'Neil')
    ht.insert('Jack', 'O\'Neill')
    assert ht.get('Jack') == 'O\'Neill'

def test_ht_chaining_get_raises_KeyError():
    from hashers import HasherKR
    from hashtable import HashTableChaining
    ht = HashTableChaining(16, HasherKR())
    ht.insert('Jack', 'O\'Neill')
    with pytest.raises(KeyError):
        ht.get('Daniel')

def test_ht_chaining_insert_same_hash():
    from hashers import HasherKR
    from hashtable import HashTableChaining
    ht = HashTableChaining(16, HasherKR())
    ht.insert('a', 'a')
    ht.insert('A', 'A')
    assert ht.size() == 2

def test_ht_chaining_delete():
    from hashers import HasherKR
    from hashtable import HashTableChaining
    ht = HashTableChaining(16, HasherKR())
    ht.insert('Jack', 'O\'Neill')
    ht.delete('Jack')
    assert ht.size() == 0

def test_ht_chaining_delete_raises_KeyError():
    from hashers import HasherKR
    from hashtable import HashTableChaining
    ht = HashTableChaining(16, HasherKR())
    with pytest.raises(KeyError):
        ht.delete('Jack')

def test_ht_chaining_delete_same_hash():
    from hashers import HasherKR
    from hashtable import HashTableChaining
    ht = HashTableChaining(16, HasherKR())
    ht.insert('a', 'a')
    ht.insert('A', 'A')
    ht.delete('a')
    assert ht.size() == 1

##### HashTableDouble

def test_ht_double_is_empty():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    assert HashTableDouble(1, DoubleHasher(HasherKR(), HasherKR())).size() == 0

def test_ht_double_size_is_correct_after_insert():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(16, DoubleHasher(HasherKR(), HasherKR()))
    ht.insert('Daniel', 'Jackson')
    assert ht.size() == 1

def test_ht_double_size_is_correct_after_replace():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(16, DoubleHasher(HasherKR(), HasherKR()))
    ht.insert('Daniel', '?')
    ht.insert('Daniel', 'Jackson')
    assert ht.size() == 1

def test_ht_double_get():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(16, DoubleHasher(HasherKR(), HasherKR()))
    ht.insert('Daniel', 'Jackson')
    assert ht.get('Daniel') == 'Jackson'

def test_ht_double_get_after_replace():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(16, DoubleHasher(HasherKR(), HasherKR()))
    ht.insert('Daniel', '?')
    ht.insert('Daniel', 'Jackson')
    assert ht.get('Daniel') == 'Jackson'

def test_ht_double_get_raises_KeyError():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(16, DoubleHasher(HasherKR(), HasherKR()))
    ht.insert('Daniel', 'Jackson')
    with pytest.raises(KeyError):
        ht.get('Jack')

def test_ht_double_insert_same_hash():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(16, DoubleHasher(HasherKR(), HasherKR()))
    ht.insert('a', 'a')
    ht.insert('A', 'A')
    assert ht.size() == 2

def test_ht_double_delete():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(16, DoubleHasher(HasherKR(), HasherKR()))
    ht.insert('Daniel', 'Jackson')
    ht.delete('Daniel')
    assert ht.size() == 0

def test_ht_double_delete_raises_KeyError():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(16, DoubleHasher(HasherKR(), HasherKR()))
    with pytest.raises(KeyError):
        ht.delete('Daniel')

def test_ht_double_delete_same_hash():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(16, DoubleHasher(HasherKR(), HasherKR()))
    ht.insert('a', 'a')
    ht.insert('A', 'A')
    ht.delete('a')
    assert ht.size() == 1

def test_ht_double_delete_reorganises_container():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(16, DoubleHasher(HasherKR(), HasherKR()))
    ht.insert('a', 'a')
    ht.insert('A', 'A')
    ht.delete('a')
    assert ht.get('A') == 'A'

def test_ht_double_insert_raises_OverflowError():
    from hashers import HasherKR, DoubleHasher
    from hashtable import HashTableDouble
    ht = HashTableDouble(1, DoubleHasher(HasherKR(), HasherKR()))
    ht.insert('Jack', 'O\'Neill')
    with pytest.raises(OverflowError):
        ht.insert('Daniel', 'Jackson')
