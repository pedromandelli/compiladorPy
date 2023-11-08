from lexer import Lexer


def main():
    content = """
    {
{
  float x;
  float z;
  int i;
  int max;
  x = 0;
  max = 10000;
  for (i = 1; i <= max; i = i + 1){
    print x;
    x = x + 0.001;
    z = x;
    if (z != x){
      print "Erro numérico na atribuição de números na notação ponto flutuante!";
      break;
    }
  }
}


{
  int y;
  int j;
  int i;
  y = new int[10];
  j = 0;
  for (i = 0; i < 20; i = i + 1) 
    if (i % 2 == 0){
      y[j] = i + 1;
      j = j + 1;
    }
    else
      print 0;

  for (i = 0; i < 10; i = i + 1)
    print y[i];

  return;
}
}
    """
    lexer = Lexer(content)
    token = lexer.get_next_token()
    while token.type != 'EOF':
        print(token)
        token = lexer.get_next_token()

if __name__ == "__main__":
    main()