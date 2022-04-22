# BotAlertas
Monitoramento da caixa de entrada de um e-mail para emitir alertas via ligação telefônica no caso de e-mails que atendam aos parâmetros pré definidos.

### Fluxo básico: 
  Será feita uma varredura pela caixa de entrada do e-mail a cada x segundos, buscando e-mails a partir de parâmetros de busca, como por exemplo: emails não lidos ou lidos, e/ou um texto ou substring específica dentro do campo assunto ou do próprio corpo do email. 
  
  Ao encontrar, o robô iniciará a chamada para o primeiro número da lista de destinatários do arquivo de configuração, e para cada destinatário será feita x tentativas caso a chamada falhe ou não seja atendida, quando atendida é registrado o id da chamada no arquivo de log e o monitoramento da caixa de entrada continua.
  
Observação: Para identificar que a chamada foi atendida e a mensagem entregue, é necessário apertar qualquer número do teclado númerico durante a ligação ou recusá-la.

### Parâmetros no arquivo de configuração

#### Seção APP:
- interval: define o intervalo entre cada verificação da caixa de entrada do email

#### Seção CALL:
- phone1: Número de destino da ligação. obs: outros números poderão ser adicionados seguindo o padrão 'phone1, phone2, phone3'
- message: mensagem que será lida na chamada
- token: token da zenvia para enviar chamadas
- attempts: Número de tentativas para realizar a chamada em caso de falha ao enviar, ou chamada não atendida
- interval: Intervalo entre a chamada e a verificação do status da chamada. obs: deve-se levar em consideração o tempo para que seja atendida

#### Seção EMAIL:
- user: email de origem
- password: senha do email
- server: servidor do email que será utilizado
- flag: flag de busca dos e-mails, padrão: Unseen(e-mails não lidos)
- parameters: parâmetros para filtrar os e-mails pelo conteúdo

## Requerimentos:
- python 3.8.10+
- totalvoice api
- imaplib
.
