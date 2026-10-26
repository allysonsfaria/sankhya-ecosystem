---
id: "360045116373"
titulo: "Registro de Apuração do IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116373-Registro-de-Apura%C3%A7%C3%A3o-do-IPI"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Apuração de ICMS, IPI e ISS"
atualizado_em: "2026-09-15T14:22:04Z"
rotulos: ["AJUDA DO SKW", "manual", "Relatórios", "Livros Fiscais", "Créditos", "Débitos", "IPI", "Impostos", "EFD", "CFOP", "Registro de Apuração do IPI", "br.com.sankhya.mgeliv.rel.registroapuracaoipi", "Registro de Apuração do IPI manual", "Informe empresa datas páginas e emissão", "Dados de IPI ajustes e registros EFD ICMS/ST", "Abrir Salvar Visualizar e Gerar Financeiro"]
---

# Registro de Apuração do IPI

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313082558999) Módulo: Livros Fiscais > Relatórios
```

---

Neste livro, serão gerados os valores totais referentes as notas de Entradas (créditos), notas de saídas (débitos) e os ajustes tanto a débito quanto a crédito, onde serão encontrados os valores finais do período e apurando neste caso, se o estabelecimento terá um saldo credor ou devedor de IPI.

| [Preenchimentos Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116373-Registro-de-Apura%C3%A7%C3%A3o-do-IPI#preenchimentosiniciais) |  | [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116373-Registro-de-Apura%C3%A7%C3%A3o-do-IPI#bot%C3%B5esdotopodatela) |
| --- | --- | --- |
| [Visualização do relatório](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116373-Registro-de-Apura%C3%A7%C3%A3o-do-IPI#visualiza%C3%A7%C3%A3odorelat%C3%B3rio) |  |  |

![Imagem 2: Visualização do relatório](https://ajuda.sankhya.com.br/hc/article_attachments/8219887516439)

## Preenchimentos Iniciais

Teremos os seguintes campos a serem preenchidos para geração do relatório:

Em **"Empresa"**, informe a empresa a que deseja gerar os dados.

Depois, preencha a **"Data Inicial"** que o sistema irá considerar para a busca de informações para a geração do relatório.

Informe também a **"Data Final"** para a busca dos dados para a geração do relatório.

Nos casos em que o relatório ainda não foi gerado, o campo **"Página Inicial"** estará preenchido com o número **"0"**. À medida que a geração dos relatórios forem executadas, ele será alimentado com a numeração da última página do período gerado anteriormente, porém, você também poderá editá-lo manualmente, se necessário.

A **"Página Final"** será alimentada automaticamente com a numeração da última página referente a última geração efetuada. Teremos a opção de gravar ou não esta informação para futuras emissões.

O campo **"Data Emissão"** apresentará automaticamente a data em que o relatório está sendo emitido.

Se marcação **"Imprimir data/hora da emissão?"** for realizada, fará com que a data e a hora da emissão do relatório sejam impressas em seu lado superior direito.

**Seção Demonstrativos**

A seção **"Demonstrativos"** será alimentada com o acionamento do botão **"Abrir"**, que traz os valores salvos na tabela TGFLOU (LivroOutros) considerando Tipo de Imposto = "P" (IPI).

![Imagem 3: A seção "Demonstrativos" será alimentada com o acionamento do botão "Abrir" , que traz os valores salvos na tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/4416286903831)

Serão apresentados os valores referentes a:

- Outros Débitos;
- Estorno de Débitos;
- Outros Créditos;
- Estorno de Créditos;
- Saldo Credor Ant..

Considere que, as informações da tela [Ajustes de IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607394) serão somadas no campo **"Outros Déb.Ajuste"** e **"Outros Cred.Ajustes"**, e assim, gerados os registros E530 e E531 no arquivo da EFD ICMS/ST. Sendo que, quando a opção do campo **"Cód. Ajuste"** da tela Ajuste de IPI for **"101-Estorno de Créditos"**, **"102-Transferência de Créditos"**, **"103-Ressarcimento / compensação de créditos"**, ou **"199-Outros Débitos"**, os valores referentes ao cadastro serão somados no campo Outros Déb.Ajuste, e o valor do campo **"Outros Créditos"** da tela Registro de Apuração IPI do registro E530 será zerado. Porém, quando o campo Cód. Ajuste for configurado com as seguintes opções:

- 1-Estorno de débito;
- 2-Créditos recebidos por transferência;
- 10-Crédito presumido de IPI - ressarcimento do PIS/PASED e da COFINS lei Nº9.363/1996;
- 11-Crédito presumido de IPI - Ressarcimento do PIS/PASED e da COFINS lei Nº10.276/2001;
- 12-Crédito presumido de IPI - Regiões incentivadas lei Nº9.826/1999;
- 13-Crédito presumido de IPI - Frete - MP2.158/2001;
- 19-Crédito presumido de IPI - Outros;
- 98-Créditos decorrentes de medida judicial; ou
- 99-Outros créditos.

Dessa forma, os valores referentes ao cadastro serão somados no campo Outros Créd.Ajuste. Destacamos ainda que, o registro E531 será gerado através dos itens cadastrados na aba **"Item do Ajuste do Ipi"**, localizada na tela Ajuste do IPI.

Além disso, temos as colunas contendo os dados de **"Observação"**, **"Ajuste"**, a **"Origem do Processo"**, bem como o **"Número do Processo"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116373-Registro-de-Apura%C3%A7%C3%A3o-do-IPI#top)

## Botões do topo da tela

No alto da tela, você pode notar alguns botões de suma importância para geração do relatório. São eles:

![Imagem 4: Abrir: Ao acionar este botão, serão recuperadas e apresentadas na seção Demonstrativos (apresentada acima) as…](https://ajuda.sankhya.com.br/hc/article_attachments/4416286915735) **Abrir:** Ao acionar este botão, serão recuperadas e apresentadas na seção Demonstrativos (apresentada acima) as informações relacionadas às apurações anteriores da empresa e período definidos.

![Imagem 5: Salvar: Por esta opção, será possível salvar os valores apurados do período, somados aos ajustes lançados já apurando o…](https://ajuda.sankhya.com.br/hc/article_attachments/4416286924439) **Salvar:** Por esta opção, será possível salvar os valores apurados do período, somados aos ajustes lançados já apurando o saldo e gravando os totais com seus respectivos tipos de apuração. Assim, para o mês seguinte, os saldos do mês anterior serão considerados. Além disso, estes valores também são base para geração dos registros do EFD Fiscal no registro de apuração deste.

![Imagem 6: Visualizar: Por este botão, faremos a visualização do relatório construído de acordo com os filtros e marcações…](https://ajuda.sankhya.com.br/hc/article_attachments/4416293142423) **Visualizar:** Por este botão, faremos a visualização do relatório construído de acordo com os filtros e marcações anteriormente efetuadas (abaixo, temos mais informações sobre este botão).

![Imagem 7: Gerar Financeiro do IPI a Recolher conforme Saldo Devedor: Através deste botão, será possível incluir no financeiro a…](https://ajuda.sankhya.com.br/hc/article_attachments/8220302254743) **Gerar Financeiro do IPI a Recolher conforme Saldo Devedor:** Através deste botão, será possível incluir no financeiro a movimentação do imposto apurado (IPI) de forma automática.

Ao acioná-lo, o sistema terá o seguinte comportamento:

1. Primeiramente, será verificado se a empresa indicada para a apuração possui dados de IPI a Recolher informados na tela Preferências da Empresa, aba EFD - Escrituração Fiscal Digital, [seção EFD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#se%C3%A7%C3%A3oefd):

- Se houver, será efetuado o lançamento do IPI a Recolher no financeiro;
- Caso não exista, será apresentada a seguinte mensagem:

**"Não existem valores de IPI apurados a recolher gravados, para a geração do Financeiro. Execute a opção "Gravar"."**

2. Em seguida, será verificado se já foi gerado o financeiro para a Empresa, Período de Referência e Código de Receita informados:

- Se não estiver gerado, será exibida uma mensagem comunicando que não há informações configuradas para a integração do financeiro na [seção EFD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#se%C3%A7%C3%A3oefd), aba Geração de Financeiro do IPI a Recolher das Preferências da Empresa;
- Já ao encontrar o registro, será apresentada a mensagem abaixo:

**"Já existe um registro para a empresa no período informado. Deseja substitui-lo?"**

Ao escolher a opção **"Sim"**, será analisado o status do título no financeiro. Se ele já estiver baixado e/ou contabilizado, será apresentada uma mensagem informando que não foi possível excluí-lo, devido o mesmo estar baixado e/ou contabilizado. Caso contrário, o sistema irá excluir o título e incluir um novo com as informações das preferências.

Clicando em **"Não"**, nenhuma operação será executada.

Após os financeiros gerados, serão preenchidos automaticamente os seguintes campos na tela [Movimentação financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874):

- No Painel Principal os campos **"Empresa"** e **"Parceiro"**, serão preenchidos com os mesmos códigos informados na apuração.
- Os campos **"Dt. Negociação"** e **"Dt. Entrada e Saída"**, localizados no Painel Principal e na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abageral), respectivamente, serão preenchidos com a **"Data Emissão"** da efetiva apuração do impostos a pagar.
- Na aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abalanamento), o campo **"Receita/Despesa"** será informado como **"Despesa"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116373-Registro-de-Apura%C3%A7%C3%A3o-do-IPI#top)

## Visualização do relatório

Depois de gerados os dados na tela e acionado o botão ![Imagem 8: Depois de gerados os dados na tela e acionado o botão "Visualizar" , o relatório apresentado demonstrará,…](https://ajuda.sankhya.com.br/hc/article_attachments/4416293142423) **"Visualizar"**, o relatório apresentado demonstrará, primeiramente, os totais por CFOP das **"Entradas"**, em seguida os totais por CFOP das **"Saídas"** e, ao final do relatório, os resumos dos **"Débitos e Ajustes"**, **"Créditos e Ajustes"** e **"Apuração do Saldo"**.

![Imagem 9: Depois de gerados os dados na tela e acionado o botão "Visualizar" , o relatório apresentado demonstrará,…](https://ajuda.sankhya.com.br/hc/article_attachments/360084043293)

![Imagem 10: Depois de gerados os dados na tela e acionado o botão "Visualizar" , o relatório apresentado demonstrará,…](https://ajuda.sankhya.com.br/hc/article_attachments/360082869274)

[[voltar ao](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116373-Registro-de-Apura%C3%A7%C3%A3o-do-IPI#top) [topo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116373-Registro-de-Apura%C3%A7%C3%A3o-do-IPI#top)[]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116373-Registro-de-Apura%C3%A7%C3%A3o-do-IPI#top)
