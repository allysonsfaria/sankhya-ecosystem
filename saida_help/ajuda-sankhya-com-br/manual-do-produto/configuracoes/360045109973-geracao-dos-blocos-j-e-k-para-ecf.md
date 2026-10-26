---
id: "360045109973"
titulo: "Geração dos Blocos J e K para ECF "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109973-Gera%C3%A7%C3%A3o-dos-Blocos-J-e-K-para-ECF"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:56:12Z"
rotulos: ["Configuração", "Relatórios", "ECD", "ECF", "Bloco J", "Bloco K", "Geração dos Blocos J e K para ECF  manual", "Contabilidade", "Plano de Contas", "Geração de Registros da ECF: Plano de Contas e Saldos"]
---

# Geração dos Blocos J e K para ECF 

O objetivo dessa documentação é demonstrar como o sistema irá trabalhar a geração destes registros na ECF referentes ao Plano de Contas e aos saldos das contas contábeis. Além disso, será possível visualizar as melhorias de usabilidade disponibilizadas nas rotinas de geração da [ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116493-Configurador-de-Blocos-e-Registros-ECF)/[ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607454-Configura%C3%A7%C3%A3o-para-Raz%C3%A3o-Auxiliar-ECD) e em outras rotinas relacionadas.

Na estrutura do arquivo da ECF, existem os blocos:

J - Plano de Contas da empresa;

K - Saldos das Contas.

[Relação de registros dos Blocos J e K](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109973-Gera%C3%A7%C3%A3o-dos-Blocos-J-e-K-para-ECF#relaoderegistrosdosblocosjek)               [Informações Adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109973-Gera%C3%A7%C3%A3o-dos-Blocos-J-e-K-para-ECF#informaesadicionais)

[Rotinas de Geração da ECD e ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109973-Gera%C3%A7%C3%A3o-dos-Blocos-J-e-K-para-ECF#rotinasdegeraodaecdeecf)

## Relação de registros dos Blocos J e K

![Imagem 1: Relação de registros dos Blocos J e K](https://ajuda.sankhya.com.br/hc/article_attachments/6272068907031)

Informações sobre a geração dos blocos J e K:

Os blocos apenas serão gerados caso a empresa da geração do arquivo, tenha nas suas Preferências de Contabilidade a configuração para geração dos blocos (aba ECF - Escrituração Contábil Fiscal - sub-aba Blocos).

As informações sobre o plano de contas, plano de contas referencial e os valores dos saldos das contas será baseado nas configurações existentes para e empresa, conforme o tipo de cada registro. Vejamos:

![Imagem 2: As informações sobre o plano de contas, plano de contas referencial e os valores dos saldos das contas será baseado nas…](https://ajuda.sankhya.com.br/hc/article_attachments/6272594474391)

---

![Imagem 3: As informações sobre o plano de contas, plano de contas referencial e os valores dos saldos das contas será baseado nas…](https://ajuda.sankhya.com.br/hc/article_attachments/6273278316951)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109973-Gera%C3%A7%C3%A3o-dos-Blocos-J-e-K-para-ECF#top)

## Informações Adicionais

Tem-se abaixo os passos para realização da importação dos arquivos no PGE, para que posteriormente os Blocos J e K sejam importados corretamente.

1 - Importar o arquivo que foi gerado pelo sistema

![Imagem 4: 1 - Importar o arquivo que foi gerado pelo sistema](https://ajuda.sankhya.com.br/hc/article_attachments/7006484316183)

2 - Feita a importação do arquivo, informa-se quais blocos não serão recuperados pela ECD, de modo que neste caso, deve-se informar que os Blocos J e K serão sobrescritos pelo que foi gerado pelo sistema. Marcando os blocos J e K como sobrescrever:

![Imagem 5: 2 - Feita a importação do arquivo, informa-se quais blocos não serão recuperados pela ECD, de modo que neste caso,…](https://ajuda.sankhya.com.br/hc/article_attachments/7006561144343)

**Observação:** essa configuração no PGE só é necessária quando a empresa possui recuperação de dados da ECD; caso contrário, não é necessário realizar essa configuração.

3 - Em seguida o PGE irá carregar os dados da escrituração importada; feito isso, será realizado um novo questionamento ao usuário se deseja realizar a importação, pois alguns dados importados não serão carregados/calculados pelo PGE. Deve-se clicar em **"Não"**:

4 - Em seguida, o PGE explica que os dados dos blocos J e K, serão calculados com base no arquivo importado, e se existirem dados anteriores, estes serão apagados. Assim a seguinte mensagem será exibida:

**"Em caso de importação do bloco J ou K o balanço e a demonstração do exercício serão calculados. Caso haja dados anteriormente preenchidos, eles serão apagados."**

Deve-se clicar em "OK".

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109973-Gera%C3%A7%C3%A3o-dos-Blocos-J-e-K-para-ECF#top)

## Rotinas de Geração da ECD e ECF

Nas [Preferências de Contabilidade da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa), aba [ECF - Escrituração Contábil Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa#abaecf-escrituraocontbilfiscal), sub-aba Parâmetros de Tributação, o quadrante **"Forma de Tributação no período"**, conta os campos Forma Tributação, Trimestre e Exercício para serem utilizados como filtro:

![Imagem 6: Nas Preferências de Contabilidade da Empresa , aba ECF - Escrituração Contábil Fiscal , sub-aba Parâmetros de…](https://ajuda.sankhya.com.br/hc/article_attachments/7007058227863)

Caso estes filtros não sejam preenchidos, clicando-se em Aplicar, serão apresentados todos os parâmetros de tributação cadastrados.

Esta tela conta ainda com algumas validações a respeito do preenchimento de alguns campos. A saber:

Quando o campo **"Forma de Tributação"** for definido com opções diferentes de 5-Lucro Presumido ou 7-Lucro Presumido/Arbitrado e a marcação **"Optante pelo REFIZ"** estiver realizada, poderá ser apresentada a seguinte mensagem e o registro não será salvo:

**"De acordo com o Manual da ECF, a Empresa só pode ser optante pelo REFIZ quando possuir as formas de tributação Lucro Presumido ou Lucro Presumido/Arbitrado. Forma de tributação informada: [3 - Lucro Presumido/Real]. Para maiores informações consulte o manual."**

Nos casos em que o campo **"Escrituração"** for configurado com as opções C ou L, e se o campo **"Forma de tributação"** for uma das opções 1-Lucro Real, 2-Lucro Real/Arbitrado, 6-Lucro Arbitrado, 8-Imune do IRPJ ou 9-Isenta do IRPJ, será apresentada a seguinte mensagem e o registro não poderá ser salvo:

**"De acordo com o Manual da ECF, Empresas só podem ser optantes pelo REFIZ quando possuem a forma de tributação Lucro Presumido ou Lucro Presumido/Arbitrado. Forma de tributação informada [1 - Lucro Real]. Para maiores informações consulte o manual."**

Nas telas [Geração de Blocos para Integração - ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608034-Gera%C3%A7%C3%A3o-de-Blocos-para-Integra%C3%A7%C3%A3o-ECF) e [Geração de Arquivo - ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608014-Gera%C3%A7%C3%A3o-de-Arquivo-ECD), tem-se o botão **"Rel. c/ Plano de Cta. Ref."**, que ao ser acionado, o sistema apresenta um relatório informando as contas contábeis sem relacionamento com Plano de Contas Referencial.

Geração de Blocos para Integração - ECF:

![Imagem 7: Geração de Blocos para Integração - ECF:](https://ajuda.sankhya.com.br/hc/article_attachments/7007264113815)

Geração de Arquivo - ECD:

![Imagem 8: Geração de Arquivo - ECD:](https://ajuda.sankhya.com.br/hc/article_attachments/7007339723287)

Além disso, o sistema valida a existência de alguma diferença entre os valores totais dos lançamentos a débito e crédito. Solicitando-se a geração do arquivo em que exista alguma divergência, será exibida a seguinte mensagem:

**"Existem erros no fechamento de D/C por dia de movimento. A ECF gerada não será validada. Deseja visualizar o relatório, gerar o arquivo mesmo assim ou cancelar a operação?"**

Ao gerar a [ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608034-Gera%C3%A7%C3%A3o-de-Blocos-para-Integra%C3%A7%C3%A3o-ECF)/[ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607454-Configura%C3%A7%C3%A3o-para-Raz%C3%A3o-Auxiliar-ECD), se existir alguma Conta Contábil que possua o grupo de contas igual a 01-Contas de ativo, 02-Contas de passivo, 03-Patrimônio líquido e 04-Contas de resultado e que teve movimento ou saldo no período, sem sua respectiva conta contábil referencial vinculada, clicando-se em **"Gerar Arquivo"**, será apresentada a seguinte mensagem:

**"Existem contas contábeis sem vínculo de contas contábeis referencias. O ECD/ECF gerado não será validado. Deseja visualizar o relatório, gerar o arquivo mesmo assim ou cancelar a operação?"**

Na geração do arquivo da ECF/ECD, caso o sistema encontre alguma inconsistência, será feita a gravação do problema no registro de log de erro que é gerado.

- Caso o arquivo gerado contenha Contas Contábeis configuradas com um dos grupos de conta definidos como 05-Contas de Compensação ou 09-Outras, existindo alguma Conta Contábil Referencial vinculada, o sistema grava a seguinte mensagem de erro no arquivo de log:

Lista de Contas Contábeis que são contas de 'Compensação' e/ou 'Outras' e possuem conta contábil referencial vinculada: 'Código da conta contábil' + 'Descrição da conta' + 'Código da Conta Contábil Referencial' de cada conta que foi encontrada para essa situação.

- Caso o arquivo gerado possua Contas Contábeis configuradas com um dos grupos de conta definidos como 05-Contas de Compensação ou 09-Outras ou que a Conta Contábil de Encerramento de Resultado da empresa que está realizando a geração, possua valor de saldo final maior que 0 (zero), o sistema irá gravar a seguinte mensagem de erro no arquivo de log:

Lista de Contas Contábeis que são contas de 'Compensação', 'Outras' e 'Conta de Encerramento de Resultado' possuem valor de saldo final. Apresentar o 'Código da conta contábil' + 'Descrição da conta' + 'Data de Referência' em que a conta possui o saldo para cada conta.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109973-Gera%C3%A7%C3%A3o-dos-Blocos-J-e-K-para-ECF#top)
