Foo = type('Foo', (), dict(i=4))

Bar = type('Bar', (Foo,), dict(get_i = lambda self: self.i))
