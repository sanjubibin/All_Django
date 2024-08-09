class Employee:
    def __init__(self, name='NA', age='NA', no='NA', intro='NA') -> None:
        self.name = name
        self.first_name = name.split(' ')[0] if name != 'NA' else 'NA-NND'
        mid_name_list = [x.capitalize() for x in name.split(' ')[1:-1]]
        self.middle_name = ' '.join(mid_name_list) if name != 'NA' and len(mid_name_list) != 0 else 'NA-NMN'
        self.last_name = name.split(' ')[-1] if name != 'NA' else 'NA-NND'
        self.age = age
        self.no = no
        self.intro = intro

    def set_intro(self) -> None:
        self.name: str
        self.first_name: str

        if not self.name.startswith('NA'):
            self.intro = f'The Great {self.first_name.capitalize()}'
        else:
            print('inorder to set_intro name has to be updated already until that name will be "NA"')