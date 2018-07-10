class BaseEntry:
    def display(self):
        for att in dir(self):
            if not att.startswith('__') and att != 'display':
                val = getattr(self, att)
                if isinstance(val, (int, float, complex, str)):
                    print(att, ":", val)
                elif isinstance(val, (list, tuple, dict)):
                    print(att, ":")
                    print('[')
                    for item in val:
                        if hasattr(item, 'display'):
                            item.display()
                            print()
                    print(']')
                elif hasattr(val, 'display'):
                    val.display()
                    print()
                else:
                    print(att, ":", val)
