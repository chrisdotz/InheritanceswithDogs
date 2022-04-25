class FatherDog:
    eyes = 'brown'
    breed = 'husky'
    
    def bark(self):
        if self.breed == 'husky':
            print('rooff...')
        else:
            print('ROOF')

        
class SonDog(FatherDog):
    eyes = 'black'
    breed = 'husky mixed with pit'
    
husky = SonDog()

husky.bark()