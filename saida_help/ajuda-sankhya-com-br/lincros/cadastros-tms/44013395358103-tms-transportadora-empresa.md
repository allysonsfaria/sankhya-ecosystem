---
id: "44013395358103"
titulo: "[TMS] - Transportadora (empresa)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013395358103--TMS-Transportadora-empresa"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:56:55Z"
rotulos: ["sync_hc", "lincros", "lincros_13432548", "sync_hash_4178f276bc86"]
---

# [TMS] - Transportadora (empresa)

**Menu:** Cadastros Gerais >Transportadoras >Transportadora (Empresa)

**Objetivo**: Esta tela permite realizar o vínculo de transportadora já cadastrada na base com a empresa, bem como desfazer o vínculo.

**Considerações**: 
        - Na cadastro da transportadora (empresa) é possível efetuar configurações referentes a transportadora de forma restritiva, apenas para a empresa a qual o cadastro está vinculado.
Por exemplo: se no cadastro geral da transportadora estiver configurado que a mesma utiliza o padrão EDI PROCEDA 3.0, porém para a operação da embarcadora for utilizado o EDI PROCEDA 5.0, no cadastro da transportadora (empresa) a embarcadora poderá configurar que essa transportadora utiliza o padrão EDI PROCEDA 5.0, sem interferir nos cadastros de demais clientes da base que operam com a mesma transportadora.
Trata-se de um cadastro compartilhado, porém cada embarcadora poderá aplicar suas configurações necessárias. 

**Informações sobre a tela**

Campos que podem ser habilitados/desabilitados:

- Permite o embarcador alterar os valores da transportadora na cotação;
- Permite exportar valor do frete calculado;
- Permitir calcular IST;
- Permite ordem de descarga sem documentos: permite a criação de uma ordem de descarga sem haver documentos informados;
- Considerar cubagem do CT-e: considera a cubagem do CT-e ao invés da cubagem da nota fiscal para os cálculos dos movimentos no conhecimento;
- Considerar peso do CT-e: considera o peso do CT-e ao invés do peso da nota fiscal para os cálculos dos movimentos no conhecimento;
- Considera ICMS reduzido para cotações:

- Cálculo de exemplo do ICMS: Valor total dos componentes que possuem a flag 'calcula icms' marcada na tabela de fretes: R$300

Percentual do ICMS: 12%

300 / 0,88 = 340,90

340,9 - 300 = 40,9

Valor do ICMS = R$40,90

- Quando a flag Considera ICMS Reduzido para cotações estiver marcada, na seleção de transportadora via cotação spot, o cálculo do ICMS será realizado da forma reduzida, sendo:

300 / 100 \* 12

Valor do ICMS = R$36,00

Não é válido para cotação em que foi realizada simulação de tabela, somente para valor total de frete informado;

- Permite usar a tolerância para divergência de imposto: Quando esta flag estiver marcada, será considerado o valor informado no campo Tolerância Frete para a divergência de imposto;
- Transportadora própria: quando a flag estiver ativa, a transportadora em questão se tornará própria da empresa corrente.
- Uma transportadora não poderá ser própria de duas empresas diferentes.
- Somente será possível fazer o vínculo da transportadora onde as filiais tenham os mesmos CNPJs que as unidades da empresa.

![Imagem 1: Somente será possível fazer o vínculo da transportadora onde as filiais tenham os mesmos CNPJs que as unidades da…](https://ajuda.sankhya.com.br/hc/article_attachments/44013404010007)

![Imagem 2: Somente será possível fazer o vínculo da transportadora onde as filiais tenham os mesmos CNPJs que as unidades da…](https://ajuda.sankhya.com.br/hc/article_attachments/44013412630295)

- Rateia ICMS por movimento;
- Emite nota fiscal de serviço no frete municipal: Ao desabilitar este parâmetro, quando entrar um Ct-e do tipo ‘Normal’ mas com a mesma origem e destino o sistema automaticamente considera como tipo ‘Eletrônico’ e não mais como ‘Serviço’;
- Retornar tabela com menor valor;
- Modal padrão;
- Modal de tributação;
- EDI padrão: é possível vincular padrões da Lincros e da empresa atual;
- Forma de pagamento padrão: utilizada em faturas, sendo necessário realizar o cadastro de formas de pagamento previamente;
- Cubagem padrão: utilizada para cálculo do peso cubado. Caso na tabela de fretes haja o componente cubagem utilizada, será buscado primeiramente o componente. Caso não haja, será buscado este campo. Caso o mesmo esteja vazio, será buscado o do cadastro da transportadora. E caso vazio, será utilizado o padrão 300;
- Tolerância frete;
- Percentual tolerância de frete;
- Km inicial padrão;
- Expressão leitura cubagem;
- Expressão leitura peso: utilizada caso a opção Considerar peso do CT-e estiver ativa. Por padrão o sistema lê a tag “PESO DECLARADO”, mas caso a transportadora utilize outro termo, pode ser inserido neste campo. Por exemplo: //\*/infCarga/infQ[tpMed='**PESO TAXADO**']/qCarga;
- Expressão leitura quantidade pallets;

- Tolerância de dias para vencimento fatura:

- Define se será gerado a pendência na fatura quando a data de emissão da fatura e a data de vencimento da fatura, não cumprem a quantidade de dias inserido no parâmetro. Pendência: “Prazo do vencimento é inferior ao prazo mínimo”.

- Tolerância de dias para faturamento:

- Ao inserir tolerância de dias para faturamento, o Lincros irá utilizar essa informação na geração da pré-fatura. Considerará a data atual + quantidade de dias inseridos, para calcular a data do vencimento.

- Observações para faturamento:

- Ao registrar as observações para faturamento, quando for gerada a pré-fatura, o Lincros irá levar a informação para o campo observações da pré-fatura automaticamente.

![Imagem 3: - Ao registrar as observações para faturamento, quando for gerada a pré-fatura, o Lincros irá levar a informação para o…](https://ajuda.sankhya.com.br/hc/article_attachments/44013389584023)

- Configuração de faturamento

Usar filial de faturamento da tabela de fretes na carga.

Sofre impacto pela configuração de empresa usarCNPJFaturamentoTabelaCarga.

![Imagem 4: Sofre impacto pela configuração de empresa usarCNPJFaturamentoTabelaCarga .](https://ajuda.sankhya.com.br/hc/article_attachments/44013412927511)

- Configuração de integração de CT-e:

- Permite integrar CT-e com pendências.
- Permite integrar CT-e com erro de importação.

- Configuração união de conhecimentos:

- Desconsiderar agrupamento: quando marcado, não permite realizar a união de conhecimentos.- Permite unir conhecimentos remetente distinto.
- Permite unir conhecimentos destinatário distinto.
- Permite unir conhecimentos origem distinta.
- Permite unir conhecimentos destino distinto.
- Permite unir conhecimentos com natureza de operação distintas.
- Permite unir conhecimentos com unidades distintas.

  ![Imagem 5: Permite unir conhecimentos com unidades distintas.](https://ajuda.sankhya.com.br/hc/article_attachments/44013389867031)

- Configuração dos anexos da ordem de coleta: define quais itens serão gerados ao clicar em Download e ao enviar via e-mail para a transportadora:

- Relatório espelho ordem de coleta.
  - NOTFIS.
- Relatório espelho de pré-conhecimento.
- Relatório agendamento de notas não entregues.
- Notas fiscais.
- Relatório minuta de despacho (somente com o módulo portaria).
- Danfe.
- Arquivos anexados.

  ![Imagem 6: Arquivos anexados.](https://ajuda.sankhya.com.br/hc/article_attachments/44013389955991)

É possível realizar a configuração via FTP para a transportadora, de forma que os arquivos como por exemplo EDIs sejam lidos no diretório informado, após a transportadora disponibilizá-los na determinada pasta, para realizar a importação do mesmo no TMS.

- Se for o caso da transportadora trabalhar com FTP, na seção Configuração FTP marcar a opção Sim em FTP ativo e preencher os dados:

- Host de acesso (ip do ftp da transportadora).
- Porta do FTP.
- Modo de acesso .- Diretório raiz (a pasta que será lida).
- Usuário do ftp **(o usuário precisa possuir permissão para exclusão do arquivo no ftp após efetuar a leitura e importação do mesmo para o Lincros).**- Senha para acesso ao ftp.
- Importar anexos.

  ![Imagem 7: Importar anexos.](https://ajuda.sankhya.com.br/hc/article_attachments/44013416356631)

- Feito isso, é necessário configurar um agendamento de processo (Sistema > Agendamento de Processos > Novo) com os seguintes parâmetros:

- Processo: LeituraFtpJob.
- Classe (caminho completo): com.transpobrasil.job.LeituraFtpJob.
- Cron (s m h dM M dW): 0 0/15 \* 1/1 \* ?

**Obs**: O Cron deve ser no mínimo de 10 em 10 Minutos.

![Imagem 8: Obs : O Cron deve ser no mínimo de 10 em 10 Minutos.](https://ajuda.sankhya.com.br/hc/article_attachments/44013427754647)

![Imagem 9: Obs : O Cron deve ser no mínimo de 10 em 10 Minutos.](https://ajuda.sankhya.com.br/hc/article_attachments/44013404897303)

- Tolerância de frete por moeda:

- Permite o cadastro de tolerância de frete (valor/percentual) por moeda. É utilizado no embarque internacional e fatura internacional.

**Conclusão**: Após a leitura do artigo fica evidente o cuidado e atenção que é necessário para o preenchimento correto das informações que por consequência vão diminuir a probabilidade de erros na operação. 

        "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
