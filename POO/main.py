from account import Account
from car import Car
from uberx import UberX


def run():
    mycar = Car('FUQ862',Account('Jorge Guevara', '1067838070'))
    myuberx = UberX('FUQ868',Account('Alis Menco','33655874'), 'Ford','Fiesta')
    
    
    # print(vars(mycar))
    # print(vars(mycar.driver))
    
    print(vars(myuberx))
    print(vars(myuberx.driver))
    
    # mycar.driver = 'Leo Perez'
    # mycar.license = 'FUQ987'
    # mycar.passenger = 5
       
    
    


if __name__ == '__main__':
    run()
    
