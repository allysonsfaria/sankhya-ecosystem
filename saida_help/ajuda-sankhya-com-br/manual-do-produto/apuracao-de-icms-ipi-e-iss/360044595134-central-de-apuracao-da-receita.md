---
id: "360044595134"
titulo: "Central de Apuração da Receita"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Apuração de ICMS, IPI e ISS"
atualizado_em: "2026-09-15T14:22:49Z"
rotulos: ["AJUDA DO SKW", "manual", "Central de Apuração da Receita manual", "Configuração", "NF-e", "Livros Fiscais", "Simples Nacional", "Impostos", "br.com.sankhya.mgeliv.centralapuracao", "NFS-e", "Configuração de parâmetros", "Visualização de receitas", "Processamento de notas", "Apuração de Receitas"]
---

# Central de Apuração da Receita

```
 Módulo: Livros Fiscais > Arquivos
```

---

Esta tela permite que você visualize as receitas de mercado interno e externo e também avalie o andamento do seu faturamento por cada tipo de anexo utilizado pela empresa.

Acesse os links abaixo para navegar nas funcionalidades desta tela:

| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita#Painelprincipal) |  | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita#abageral) |
| --- | --- | --- |
| [Aba Apuração do Simples Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita#abaapuraodosimplesnacional) |  | [Botão Processar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita#botoprocessar) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita#botooutrasopes...) |  |  |

## Painel Principal

![Imagem 1: Painel Principal](https://ajuda.sankhya.com.br/hc/article_attachments/360102193894)

Inicialmente, temos o **"Nro. Apuração"** que representa o código que identifica a apuração no sistema.

No campo **"Empresa"** informe a instituição que utiliza o Simples Nacional.

A **"Referência"** da apuração será sempre o primeiro dia do mês.

O **"Status da Apuração"** será apresentado como Aberta ou Fechada. O sistema será responsável por alterar esse campo e haverá apenas uma apuração aberta por vez.

O sistema irá preencher o campo **"Tipo da Inserção"** com as opções **"Manual"** ou **"Automática"**. A primeira apuração que você criará será a Manual, pois ela irá dizer ao sistema que comece a realizar a apuração da receita. As próximas apurações serão criadas pelo sistema de forma Automática.

O **"Fator R"** é responsável por definir o anexo de tributação, baseando-se na mão de obra empregada na atividade da empresa. Se o Fator R for maior ou igual a 0,28 (28%), o enquadramento será no Anexo III, se for menor o enquadramento será no Anexo V. Esse valor será utilizado para definir os Anexos III ou V caso a empresa os utilize, se nenhum produto/serviço utilizar esses anexos este valor não será necessário. A fórmula para o cálculo deste valor é a seguinte:

FATOR R: (folha de salário dos 12 meses anteriores) / (receita bruta acumulada, mercado interno e externo, dos 12 meses anteriores)

**Observação:** este campo deve ser calculado e posteriormente preenchido manualmente.

Ao habilitar a marcação **"Ativo"**, o sistema executa a geração da apuração da próxima referência e realiza a criação das novas partilhas com base nas receitas brutas anteriores. Se a apuração não estiver ativa, ao virar o mês a apuração seguinte não será criada, portanto, as novas alíquotas/partilhas a serem utilizadas pela Empresa também não serão criadas.

Ao salvar um registro após preencher os campos obrigatórios da opção **"Configurar Apuração"** do botão ![Imagem 2: Ao salvar um registro após preencher os campos obrigatórios da opção "Configurar Apuração" do botão "Outras Opções..."…](https://ajuda.sankhya.com.br/hc/article_attachments/13839203346839) **"Outras Opções..."**, será exibido o pop-up **"Informações das Receitas Brutas Anteriores"**:

[GIF animado: Imagem 3: Ao salvar um registro após preencher os campos obrigatórios da opção "Configurar Apuração" do botão "Outras Opções..."…](https://ajuda.sankhya.com.br/hc/article_attachments/13839992991511)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita#top)

## Aba Geral

Antes de iniciarmos as configurações dessa aba, é importante ressaltarmos que você deve se atentar ao preenchimento do anexo pertencente a empresa nos produtos/serviços (Tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos), campo **"Tipo de partilha/anexo"**) comercializados, para que seja considerado corretamente na apuração.

A partir da apuração processada, será vinculada automaticamente a partilha/anexo nas [Preferências da empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893) na aba [Simples nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abasimplesnacional)) nas competências seguintes de acordo com o mês de referência, conforme apurado.

![Imagem 4: A partir da apuração processada, será vinculada automaticamente a partilha/anexo nas Preferências da empresa na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003324662)

#### Mercado Interno

O campo **"Total da Receita Bruta Mensal"** exibe a receita bruta do mercado interno (acúmulo das notas da referência que fazem parte da receita bruta da empresa que já foram apuradas).

No campo **"Total da Receita Bruta Mensal Projetada"** é apresentada a receita bruta do mercado interno projetada para toda a referência com base na receita bruta apurada até o momento.

Através do campo **"Total da Receita Bruta Acumulada (11 meses)"**, observe a receita bruta do mercado interno acumulada das últimas 11 referências.

---

#### Mercado Externo

Observe no campo **"Total da Receita Bruta Mensal"** a receita bruta do mercado externo (acúmulo das notas da referência que fazem parte da receita bruta da empresa que já foram apuradas).

O campo **"Total da Receita Bruta Mensal Projetada"** exibe a receita bruta do mercado interno projetada para toda a referência com base na receita bruta apurada até o momento.

Temos no campo **"Total da Receita Bruta Acumulada (11 meses)"**, a receita bruta do mercado interno acumulada das últimas 11 referências.

---

#### Totais

A soma das receitas brutas mensais da referência dos mercados interno e externo será apresentada no campo **"Total da Receita Bruta Mensal"**.

A soma das receitas brutas mensais projetadas da referência dos mercados interno e externo é exibida no campo **"Total da Receita Bruta Mensal Projetada"**.

A soma das receitas brutas mensais acumuladas da referência dos mercados interno e externo é demonstrada por meio do campo Total da Receita Bruta Acumulada (11 meses).

---

#### Importante: Regras de Validação para Apuração (Documentos Convencionais)

A regra de inclusão de documentos na apuração foi ajustada para documentos Convencionais, dependendo da configuração na TOP (Tipo de Operação):

**1. Documentos Convencionais:** Para notas fiscais (NF-e, CT-e, NFS-e) configuradas como **"Convencional (Não Usa NF-e)"** na aba NF-e/NFC-e/CF-e da tela Tipo de Operação - TOP, o sistema **NÃO** validará o STATUS (Aprovado) ou a geração no Livro Fiscal. A única condição para a apuração é que a flag **Considerar na Apuração do Simples?** esteja marcada na aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal) da tela [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP).

**2. Demais Documentos (Normais):** Para notas fiscais configuradas como **"Normal"** ou diferente de Convencional, o sistema **mantém as validações,** exigindo:

- O STATUS do documento deve estar como **Aprovado**;.
- O documento deve estar **gerado no Livro Fiscal** correspondente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita#top)

## Aba Apuração do Simples Nacional

Nesta aba é possível visualizar os dados de apuração separados pelo tipo de Anexo utilizado pela empresa.

![Imagem 5: Nesta aba é possível visualizar os dados de apuração separados pelo tipo de Anexo utilizado pela empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/1500003324762)

O campo **"Tipo de Partilha/Anexo"** será preenchido com as partilhas cadastradas para as empresas (conforme orientação [Múltiplas Partilhas/Anexos para Empresas do Simples Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600794)) e de acordo com o cadastrado nos produtos/serviços comercializados (Tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos), campo **"Tipo de partilha/anexo"**), podendo ser apenas um tipo de anexo ou mais (se for mais que um anexo, será um registro para cada).

Essa informação é preenchida automaticamente conforme cadastro da empresa e os produtos comercializados no determinado período.

De acordo com a apuração, se houver alteração de partilha/anexo, será inserida uma nova partilha automaticamente e será vinculado nas [Preferências da empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Simples nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abasimplesnacional), conforme a referência apurada.

---

#### Mercado Interno

Utilize o campo **"Total da Receita Bruta Mensal"** para analisar a receita bruta do mercado interno (acúmulo das notas da referência que fazem parte da receita bruta da empresa que já foram apuradas) considerando o Tipo de Partilha/Anexo em que estamos posicionados.

É possível verificar no Total da Receita Bruta Mensal Projetada a receita bruta do mercado interno projetada para toda a referência com base na receita bruta apurada até o momento considerando o Tipo de Partilha/Anexo em que estamos posicionados.

O campo **"Faixa do Anexo"** mostra a faixa do anexo em que a empresa se enquadra considerando mercado interno. Você pode visualizar os valores e faixas de cada um dos anexos do Simples Nacional, acionando o botão ![Imagem 6: O campo "Faixa do Anexo" mostra a faixa do anexo em que a empresa se enquadra considerando mercado interno. Você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/4410497309719) **"Ir para Anexos e Faixas e do Simples Nacional"**.

Você pode visualizar no campo **"Alíquota Efetiva"** a alíquota efetiva que a empresa utiliza com base nas receitas brutas do mercado interno das referências anteriores.

**Observação:** este campo serve para apoio ao cálculo da guia Documento de Arrecadação do Simples Nacional - DAS, referente ao recolhimento do simples nacional no mês de referência calculada.

---

#### Mercado Externo

Ao analisar o campo Total da Receita Bruta Mensal tem-se a visão da receita bruta do mercado externo (acúmulo das notas da referência que fazem parte da receita bruta da empresa que já foram apuradas) considerando o Tipo de Partilha/Anexo em que estamos posicionados.

No campo Total da Receita Bruta Mensal Projetada é apresentada a receita bruta do mercado externo projetada para toda a referência com base na receita bruta apurada até o momento, considerando o Tipo de Partilha/Anexo em que estamos posicionados.

O campo Faixa do Anexo mostra a faixa do anexo em que a empresa se enquadra considerando mercado externo.

Tem-se no campo **"Alíquota Efetiva"** a alíquota efetiva que a empresa utiliza com base nas receitas brutas do mercado externo das referências anteriores.

**Observação:** este campo serve para apoio ao cálculo da guia Documento de Arrecadação do Simples Nacional - DAS, referente ao recolhimento do simples nacional no mês de referência calculada.

---

#### Totais

A soma das receitas brutas mensais da referência dos mercados interno e externo considerando o Tipo de Partilha/Anexo em que estamos posicionados, é exibida no campo Total da Receita Bruta Mensal.

Através do campo Total da Receita Bruta Mensal Projetada visualize a soma das receitas brutas mensais projetadas da referência dos mercados interno e externo considerando o Tipo de Partilha/Anexo em que estamos posicionados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita#top)

## Botão Processar

Este botão irá buscar as notas que compõem a receita da empresa e que estão pendentes (que ainda não foram processadas na tela [Notas p/ Apuração da Receita](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595034-Notas-p-Apura%C3%A7%C3%A3o-da-Receita)) e irá processá-las. Deste modo, serão atualizados os valores gerais e por anexo das receitas brutas da apuração.

![Imagem 7: Este botão irá buscar as notas que compõem a receita da empresa e que estão pendentes (que ainda não foram processadas…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003317242)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita#top)

## Botão Outras Opções...

O botão **"Outras Opções..."** é representado pelo ícone ![Imagem 8: O botão "Outras Opções..." é representado pelo ícone e está localizado na parte superior direita da tela. São…](https://ajuda.sankhya.com.br/hc/article_attachments/16256930882071) e está localizado na parte superior direita da tela. São apresentadas as seguintes opções:

**Abrir Apuração por Nota**

Ao acionar esta opção será apresentada a mensagem:

**"Certifique que todos os produtos faturados estão com Tipo de Partilha/Anexo Cadastrados (Produtos > Impostos > Tipo de Partilha/Anexo)."**

Caso você não queira visualizar mais esta mensagem, assinale a marcação **"não visualizar mais esta mensagem"**.

Assim, ao clicar em **"OK"** será aberta a tela [Notas p/ Apuração da Receita](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595034) posicionada na apuração por nota.

**Configurar Apuração**

Esta opção exibe um pop-up na qual você pode configurar as partilhas que foram desconsideradas (5 - Serviços de Atividades Físicas, Computação, Adm. e Loc. de Imóveis de Terceiros, Outros e 6 - Serviços da Atividade Intelectual como Medicina, Consultorias, Engenharia, Outros).

![Imagem 9: Esta opção exibe um pop-up na qual você pode configurar as partilhas que foram desconsideradas (5 - Serviços de…](https://ajuda.sankhya.com.br/hc/article_attachments/16256930886679)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595134-Central-de-Apura%C3%A7%C3%A3o-da-Receita#top)

![Imagem 10: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16256930889623) Acesse também:

[Notas p/ Apuração da Receita](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595034-Notas-p-Apura%C3%A7%C3%A3o-da-Receita)
