---
id: "37880190322967"
titulo: "Como faturar o contrato para parceiros (CNPJ’s) distintos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880190322967-Como-faturar-o-contrato-para-parceiros-CNPJ-s-distintos"
trilha: "Universidade Sankhya > Jornada de Serviços"
atualizado_em: "2026-07-22T14:06:39Z"
rotulos: ["Configuração", "Parceiro", "Contrato", "Financeiro", "NFS-e"]
---

# Como faturar o contrato para parceiros (CNPJ’s) distintos

| Categoria |
| --- |
| [O que é e como funciona essa operação?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880190322967-Como-faturar-o-contrato-para-parceiros-CNPJ-s-distintos#h_01KFNAA6V4MM2NEGVKRD6C77S0) |
| [Quais problemas resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880190322967-Como-faturar-o-contrato-para-parceiros-CNPJ-s-distintos#h_01KFNAAGSF7BK3PR051P9Z3KHA) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880190322967-Como-faturar-o-contrato-para-parceiros-CNPJ-s-distintos#h_01KFNAAP9Z85093HT8BA0X5JFC) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880190322967-Como-faturar-o-contrato-para-parceiros-CNPJ-s-distintos#h_01KFNAB0ME1VPPC0P60DP06ZSB) |
| [Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880190322967-Como-faturar-o-contrato-para-parceiros-CNPJ-s-distintos#h_01KFNAB7537A4AZ4PFMTYVJW7E) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880190322967-Como-faturar-o-contrato-para-parceiros-CNPJ-s-distintos#h_01KFNABF9EYDF7JFM364EW4165) |

## Faturamento por grupo econômico (mais de um parceiro no mesmo contrato)

#### O que é e como funciona essa operação?

Em alguns contratos, o serviço prestado está ligado a mais de uma empresa do mesmo grupo econômico. Nesses casos, o faturamento pode ser dividido entre vários CNPJs, mesmo que o contrato tenha sido cadastrado com apenas um parceiro principal.

Essa divisão é feita por meio da configuração do grupo econômico, onde é possível definir o percentual de faturamento para cada CNPJ envolvido.

Por exemplo: se o contrato tiver o valor mensal de R$ 10.000,00 e estiver configurado com dois parceiros,  um com 60% e outro com 40%, o sistema vai gerar duas notas fiscais automaticamente: uma de R$ 6.000,00 e outra de R$ 4.000,00, cada uma para o respectivo CNPJ.

Essa operação é útil quando o serviço é utilizado por mais de uma empresa controlada pelo mesmo grupo ou quando o pagamento precisa ser dividido entre diferentes unidades jurídicas.

#### Quais problemas resolve?

- Retrabalho com faturamento manual para empresas do mesmo grupo, exigindo múltiplos lançamentos separados.
- Emissão de nota fiscal para o CNPJ incorreto, gerando questionamentos e atrasos no recebimento.
- Falta de controle sobre como o valor do contrato está sendo distribuído entre as empresas envolvidas.
- Dificuldade na conciliação contábil e fiscal, especialmente quando o serviço atende mais de uma empresa, mas é faturado apenas para uma.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1103874108)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto**: A Axis firmou um novo contrato de manutenção com o grupo empresarial Comercial Viana, que é composto por duas empresas juridicamente distintas: Comercial Viana Matriz e Comercial Viana Distribuição.

O contrato foi cadastrado com a empresa matriz como parceira principal, mas a diretoria do grupo solicitou que o valor fosse dividido igualmente entre os dois CNPJs para os próximos faturamentos, já que ambos utilizam o serviço e compartilham os custos.

Para atender essa demanda, será necessário configurar o grupo econômico no contrato, informando os dois CNPJs e o percentual de faturamento para cada um.

**Tarefas**: Sua tarefa é ajustar um contrato já cadastrado com a empresa Comercial Viana para que o faturamento seja dividido entre dois CNPJs do grupo.

#### Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya

1. **Configurações para faturamento por Grupo Econômico:**

- Acesse a tela **Preferências**
  Menu: Configurações » Avançado
- Busque pelo parâmetro **“USAGRUPECONCONT - Usa grupo econômico para Contratos e Serviços?”** e deixe-o “ligado”.

2. **Cadastro do grupo econômico no contrato:**

- Acesse a tela **Contratos**
  Menu: Contratos e Serviços » Arquivos
- Utilize o filtro **Parceiro** para buscar os contratos do parceiro Comercial Viana
- Selecione o contrato registrado no valor de R$3.000,00
- Na aba **Grupo Econômico**, clique em **+ Cadastrar Grupo Econômico** e preencha os seguintes campos:
- **Parceiro -** Comercial Viana Matriz
- **% de custo** - 60
- Salve as informações
- Faça o mesmo processo incluindo os 40% restantes para o parceiro **Comercial Viana Distribuição**

**Importante:** O somatório do % de custo deve ser igual a 100% e o parceiro do contrato também deve constar na relação inserida nesta aba. Outro ponto importante é que este recurso não terá funcionalidade caso o contrato em questão participe de um agrupamento no faturamento.

3. **Faturamento do contrato com grupo econômico:**

- Acesse a tela **Faturamento de Contratos**
  Menu: Contratos e Serviços » Rotinas
- Nos **Filtros Personalizados**, utilize o campo **Parceiro** para buscar o cliente Comercial Viana.
- Marque a flag **Considerar Contatos/Perfil/Serviço**
- Nos **Parâmetros Obrigatórios**, preencha as seguintes informações:

**Tipo de Operação** - VENDA NFS-E

**Tipo de Título -** 1

**Tipo de Negociação -** 16

**Observação Padrão -** 0

**Data para Faturamento -** Considere a data presente no campo **Referência próximo faturamento** da aba **Propriedades** na tela **Contratos.**

**Mês para Referência -** O mês para referência se trata do mês que ocorrerá o pagamento, sendo assim, mesma data usada no campo anterior.

**Série -** NF

- Clique em **Aplicar**
- Faça o faturamento
- Para validação da operação, confirme que foram geradas duas notas distintas para o mesmo contrato com parceiros diferentes, o valor será rateado conforme divisão feita no grupo econômico.

#### Correção e Repetição

- Após registro do grupo econômico veja se o faturamento ocorreu como esperado, caso não, refaça o processo revisando as informações preenchidas e fature novamente.
