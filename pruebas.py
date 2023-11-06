
##### ALGORITMOS DE PRUEBA #####

## Johnny Santiago Rodriguez Salinas

def vars_declaration():
    return '''
            var cadena string      
            var numero int
            var numero1 float32
            var numero2 float64
            var bool1 bool
            '''

def for_body():
    return '''
           for i := 0; i < 5; i++ {
           
           }
           '''

def if_sin_else():
    return '''
           if (-8 == .9){
        
           }
           '''

def if_con_else():
    return '''
           if(-.7>.23){
                return true
           }else{
                return false
           }
           '''

def func_declaration():
    return '''
           func main(a int,b int){
                return a + b 
           }
           '''

def switch_declaration():
    return '''
           switch valor {
                case 1:
                    // codigo
                case 2:
                    // codigo
                case 3:
                    // codigo
                default:
                    // codigo
            }
           '''

##  Jeremy Martinez
def test_suma_expression():
    return '''
        resultado = x + y
        a = b + c
        '''

def test_resta_expression():
    return '''
        resultado = x - y
        a = b - c
        '''

def test_multiplicacion_expression():
    return '''
        resultado = x * y
        a = b * c
        '''

def test_division_expression():
    return '''
        resultado = x / y
        a = b / c
        '''

def test_incremento_expression():
    return '''
        b = c++
        x++
        '''

def test_decremento_expression():
    return '''
        b = c--
        x--
        '''
