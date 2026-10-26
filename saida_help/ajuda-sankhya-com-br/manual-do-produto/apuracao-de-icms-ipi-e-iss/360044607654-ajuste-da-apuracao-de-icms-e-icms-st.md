---
id: "360044607654"
titulo: "Ajuste da Apuração de ICMS e ICMS ST"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654-Ajuste-da-Apura%C3%A7%C3%A3o-de-ICMS-e-ICMS-ST"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Apuração de ICMS, IPI e ISS"
atualizado_em: "2026-10-13T19:07:46Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Ajuste da Apuração de ICMS e ICMS ST", "Livros Fiscais", "SEFAZ", "ICMS", "Impostos", "EFD", "br.com.sankhya.mgeliv.cad.ajusteapuracaoicms", "Ajuste da Apuração de ICMS e ICMS ST manual", "Ajustar apuração ICMS", "Gerar e ajustar registros", "Preencher campos obrigatórios"]
---

# Ajuste da Apuração de ICMS e ICMS ST

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312976202263) Módulo: Livros Fiscais > Arquivos
```

---

Esta tela tem como finalidade ajustar informações de apuração de ICMS relativas a **"Outros créditos e Débitos"**, **"Estornos de créditos e Débitos"** e **"Deduções"**. As informações lançadas nesta tela são utilizadas principalmente para a geração do Livro Fiscal e dos arquivos do SPED FISCAL, também conhecido como EFD-Escrituração Fiscal Digital.

Nesta tela você poderá lançar informações de apuração simplesmente preenchendo os campos, e os campos com (\*) são de preenchimento obrigatório.

A tela possui uma área principal e 3 abas. A área principal é composta por um número único de ajuste, gerado automaticamente, o código da empresa e a data de referência.

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654-Ajuste-da-Apura%C3%A7%C3%A3o-de-ICMS-e-ICMS-ST#abageral) |  | [Aba Controle Créditos Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654-Ajuste-da-Apura%C3%A7%C3%A3o-de-ICMS-e-ICMS-ST#abacontrolecrditosfiscais) |
| --- | --- | --- |
| [Aba Ajuste](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654-Ajuste-da-Apura%C3%A7%C3%A3o-de-ICMS-e-ICMS-ST#abaajuste) |  |  |

## Aba Geral

![Imagem 2: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/10902017896727)

Escolha o **"Tipo Apuração"** conforme as opções abaixo:

- Débito especial;
- Controle do ICMS extra-apuração;
- Deduções do imposto apurado;
- Outros débitos;
- Estorno de créditos;
- Outros créditos
- Estorno de débitos.

No campo **"Número processo"**, informe o número do processo, se houver.

**Nota:** na geração dos registros do bloco E, bloco C, 1922 e 1926, este campo se comporta da seguinte maneira:

- Arquivos gerados até o exercício 2022, o campo permite até 15 caracteres;
- Arquivos gerados a partir do exercício 2023 poderão ter até 60 caracteres.

O **"Código UF"** estará disponível para escolha somente se o tipo de imposto for ICMS ST.

Indique a **"Origem processo"** de acordo com as seguintes opções:

- Sefaz;
- Justiça Federal;
- Justiça Estadual;
- Outros.

Informe a **"Descrição do Processo"** ou ato de infração se houver.

O **"Tipo de Ajuste"** constitui-se de um código de quatro dígitos que são definidos pela UF do contribuinte. Na ausência desta definição, informar 9999. Deve ser informado por empresas obrigadas à geração de EFD (Escrituração Fiscal Digital) encontrada na aba EFD do Livro Fiscal, e são definidos e divulgados por cada UF através da Tabela de Ajuste.

Os campos **"Sub-Apuração"** e **"Indicador de Sub-Apuração"** indicarão se o ajuste pertence ou não a uma sub-apuração.

Será possível ainda gerar estornos de crédito nos itens 60 e 65, utilizando o campo tipo lista **“Registro do Ajuste na DIME SC”** que terá as seguintes opções:

- Item 60 - Outros Estornos de Crédito;
- Item 65 - Estorno de Crédito da Entrada em Decorrência da Utilização de Crédito Presumido.

**Observação:** essa tela é alimentada de forma automática no momento da geração do Livro de ICMS, portanto, ao gerar o Livro de ICMS o sistema buscará a informação do campo **“Registro do Ajuste na DIME SC”** da tela [Configurações de Ajustes de Apuração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o) e alimentará o campo **“Registro do Ajuste na DIME SC”** desta tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654-Ajuste-da-Apura%C3%A7%C3%A3o-de-ICMS-e-ICMS-ST#top)

## Aba Controle Créditos Fiscais

Possui uma área principal com um único campo Sequência (identificar as sequencias de controle) e 2 abas sendo:

![Imagem 3: Possui uma área principal com um único campo Sequência (identificar as sequencias de controle) e 2 abas sendo:](https://ajuda.sankhya.com.br/hc/article_attachments/10902355773591)

A sub-aba **"Geral"** contém informações sobre a geração do registro 1200 do EFD (campos da TGFAJN).

**Sub-aba Utilização de Créditos Fiscais**

O campo **“Nro. Nota”** permitirá ao usuário informar ou selecionar o **número único da nota fiscal** a ser vinculada à linha de crédito. A busca deve ser realizada na **tabela de Nota/Pedido**.

- Somente registros relacionados à empresa vinculada ao ajuste de apuração serão considerados.
- Ao selecionar um número único, ele será vinculado corretamente à linha de crédito correspondente.

O campo **“Chave NF-e”** deve ser utilizado para exibição e registro da **chave de acesso da nota fiscal** vinculada ao número único informado previamente.

- O sistema preenche automaticamente este campo com a chave de acesso correspondente ao número único da nota fiscal.
- O campo também deve permitir edição manual, possibilitando o registro da chave mesmo sem o preenchimento do número único.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654-Ajuste-da-Apura%C3%A7%C3%A3o-de-ICMS-e-ICMS-ST#top)

## Aba Ajuste

Esta aba contém informações sobre as notas do ajuste de Apuração (campos da TGFAJN).

**Observação:** o campo **"Dt. Docto"** dessa aba deve ser configurado como **"Campo obrigatório"** através da ![configuração](https://ajuda.sankhya.com.br/hc/article_attachments/15509014564631) **"Configuração da Tela"**, opção **"Abrir configurações do campo"** .

![Imagem 5: Observação: o campo "Dt. Docto" dessa aba deve ser configurado como "Campo obrigatório" através da "Configuração da…](https://ajuda.sankhya.com.br/hc/article_attachments/10902360326039)

É possível visualizar no canto direito da aba o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15509026176151) **"Outras opções..."** com a opção **"Pesquisar Notas para Detalhes do Ajuste"** que permite buscar notas para compor o ajuste.

Ao clicar neste botão, abrirá uma tela onde o usuário poderá filtrar as notas.

Ao acionar o botão **"Efetivar ajustes informados"**, o sistema atualizará na grade as notas selecionadas.

![Imagem 7: Ao acionar o botão "Efetivar ajustes informados" , o sistema atualizará na grade as notas selecionadas.](https://ajuda.sankhya.com.br/hc/article_attachments/10902444044311)

**Observação:** os **"Filtros para DIFAL/FCP"** estarão habilitados para preenchimento apenas se o campo **"Tipo imposto"** presente na aba Geral desta tela, estiver definido como **"ICMS DIFAL"** ou **"ICMS FCP"**.

Informe o **"UF Destino"** para que sejam buscadas somente notas que possuem o campo TGFLIV.UFDESTINO igual ao informado no filtro.

No campo **"Opções para o valor de ajuste"** tem-se as seguintes opções:

- **Valor Zero:** Trará "0" (zero) no valor do ajuste;
- **Valor DIFAL UF Remetente:** Se o **"Tipo imposto"** na aba Geral for **"ICMS DIFAL"**, o sistema trará o valor do campo TGFLIV.VLRICMSDIFALREM, caso contrário trará "0" (zero) no valor do ajuste;
- **Valor DIFAL/FCP UF Destino:** Se o **"Tipo imposto"** na aba Geral for **"ICMS DIFAL"**, o sistema trará o valor do campo TGFLIV.VLRICMSDIFALDEST; se o **"Tipo imposto"** for **"ICMS FCP"**, trará o valor do campo TGFLIV.VLRICMSFCP, caso contrário trará "0" (zero) no valor do ajuste.

Caso a marcação **"Apenas notas sem DIFAL/FCP?"** esteja efetuada, o sistema irá trazer somente notas que não possuam cálculo do DIFAL, ou seja, a soma dos campos TGFLIV.LIV.VLRICMSDIFALREM + TGFLIV.VLRICMSDIFALDEST + TGFLIV.VLRICMSFCP for igual a "0" (zero). Se o campo não estiver marcado, tem-se o comportamento contrário, ou seja, o sistema trará apenas as notas cuja soma dos campos for maior que "0" (zero).

**Nota:** quando se tratar de Notas de Transferência e na tela [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874) constar no campo **"Empresa/Parceiro"** = Empresa, tem-se que o **"Cód. Parceiro"** e o **"Nome Parceiro"** retornados no pop-up acima serão do Parceiro que encontra-se vinculado à empresa informada no campo Cód.Parceiro do Cadastro do Livro Fiscal. Sendo assim, na grade continuará sendo apresentado o Código do Parceiro, porém, será inserido o Parceiro que encontra-se cadastrado na tela Preferências da Empresa referente à empresa envolvida.

**Observação:** não se tratando de notas de transferência, será retornado o Cód. Parceiro e Nome Parceiro registrados no Cadastro do Livro Fiscal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654-Ajuste-da-Apura%C3%A7%C3%A3o-de-ICMS-e-ICMS-ST#top)
