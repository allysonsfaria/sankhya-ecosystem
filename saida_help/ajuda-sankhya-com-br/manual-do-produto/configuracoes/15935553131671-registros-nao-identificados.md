---
id: "15935553131671"
titulo: "Registros não identificados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:40:59Z"
rotulos: ["Configuração", "Financeiro", "API de Serviços Gateway.", "Registros não identificados", "Alerta de segurança de integração", "br.com.sankhya.registros.nao.identificados", "registros sem origem identificada", "API de Serviços Gateway", "Alertas: Registros Sem Origem", "Rastreabilidade", "Sankhya Om", "Integridade de Dados"]
---

# Registros não identificados

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310480997399) Módulo: Configurações > Consultas             ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42310480999703) Versão disponível: A partir da 4.29
```

---

O objetivo dessa tela é possibilitar a governança de registros sem origem identificadas, podendo abranger: transações financeiras, dados de compras e de vendas que não podem ser rastreados de uma origem específica.

Cumpre salientar que esses registros não serão bloqueados ou restringidos de qualquer forma, na verdade, eles serão exibidos e processados normalmente no **Sankhya Om**.

Serão classificados como registros não identificados os documentos, como, notas ou financeiros, que forem inseridos diretamente no banco de dados do Sankhya.

O usuário pode inserir documentos assim por meio de integrações externas que não utilizam o Gateway ou por customizações como extensões (addons), botão de ação ou qualquer outra customização que utilize native SQL ou objetos de banco de dados como procedures e triggers para inserir os registros.

A identificação da origem dos registros é importante para a integridade do **Sankhya Om**, bem como para manter a rastreabilidade e segurança.

Essa tela possui as seguintes funcionalidades:

| Funcionalidades da tela |
| --- |
| [Apresentação dos Alertas de Registros Sem Identificação de Origem](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#Apresenta%C3%A7%C3%A3odosAlertasdeRegistrosSemIdentifica%C3%A7%C3%A3odeOrigem) |
| [Motivos para Alertas](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#MotivosparaAlertas) |
| [Benefícios de registros identificados](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#Benef%C3%ADciosderegistrosidentificados) |
| [Ação Recomendada](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#a%C3%A7%C3%A3orecomendada) |
| [Grade Pedidos e Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#GradePedidoseNotas) |
| [Grade Financeiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#GradeFinanceiros) |

---

## Apresentação dos Alertas de Registros Sem Identificação de Origem

Os alertas referentes aos registros sem identificação de origem serão apresentados no cabeçalho das rotinas: [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras), [Portal de Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609994-Portal-de-Pedidos), [Portal de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/7317826345367-Portal-de-Caixa), [Portal de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas), [Portal Armazéns](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns), [Antecipação de Recebíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052358113-Antecipa%C3%A7%C3%A3o-de-Receb%C3%ADveis) e [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) quando um registro sem origem identificada for detectado, com o propósito de auxiliar o usuário na identificação eficiente desses registros.

A mensagem aparecerá no topo das respectivas telas, da seguinte forma:

**"Registros sem origem identificada foram adicionados ao SankhyaOm. Para assegurar a integridade dos seus dados, saiba como prevenir essa situação no futuro. Saiba Mais"**

![Imagem 3: "Registros sem origem identificada foram adicionados ao SankhyaOm. Para assegurar a integridade dos seus dados, saiba…](https://ajuda.sankhya.com.br/hc/article_attachments/25443501216023)

**Observação:** a mensagem de alerta, no cabeçalho das telas citadas anteriormente, será apresentada apenas para novos clientes Sankhya. Mas não se preocupe, a tela Registros não Identificados, que relaciona todas as notas ou documentos financeiros que não tiverem a origem reconhecida, está disponível para todos os nossos clientes a partir da versão 4.29 do **Sankhya Om**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#top)

## Motivos para Alertas

Os alertas, acima mencionados, podem surgir por vários motivos, incluindo:

![Imagem 4: Inserção Direta de Dados: quando um usuário insere manualmente no banco de dados informações financeiras, registros de…](https://ajuda.sankhya.com.br/hc/article_attachments/16343891312151) **Inserção Direta de Dados:** quando um usuário insere manualmente no banco de dados informações financeiras, registros de vendas ou compras no sistema, eles podem não ser associados a uma fonte específica;
![Imagem 5: Inserção Direta de Dados: quando um usuário insere manualmente no banco de dados informações financeiras, registros de…](https://ajuda.sankhya.com.br/hc/article_attachments/16343891314199)**Integrações Externas via Banco de Dados:** integrações com outras plataformas ou sistemas podem gerar registros que não passam diretamente pelo API Gateway, tornando a origem menos clara, como, por exemplo: importações de arquivos realizados fora do **Sankhya Om** ou aplicativos mobile.
![Imagem 6: Inserção Direta de Dados: quando um usuário insere manualmente no banco de dados informações financeiras, registros de…](https://ajuda.sankhya.com.br/hc/article_attachments/18585828542615) **Customizações sem boas práticas:** customizações que não seguem as boas práticas, ou seja, que não utilizam de serviços nativos do **Sankhya Om**, pois inserem registros diretamente nas tabelas Cabeçalho da Nota e Financeiro. Este tipo de prática pode ser prejudicial à integridade do sistema e gerar os seguintes impactos:

- **Violação de Regras de Negócio:** inserções diretas podem ignorar regras de negócio implementadas para garantir a coerência e a integridade dos dados. Isso pode levar a inconsistências e a dados incorretos que afetam a operação do sistema.
- **Falta de Validações:** os serviços nativos do **Sankhya Om** realizam várias validações antes de permitir a inserção ou atualização de dados. Quando registros são inseridos diretamente, essas validações não ocorrem, o que pode resultar em dados inválidos ou corrompidos.
- **Cálculos Nativos:** muitos processos no **Sankhya Om** dependem de cálculos automáticos realizados durante a inserção ou atualização de registros. Inserções diretas podem evitar esses cálculos, resultando em valores incorretos ou em falta de dados importantes.
- **Impacto na Manutenção e Atualização:** customizações fora das boas práticas podem dificultar a manutenção do sistema e a aplicação de atualizações futuras. Isso porque as atualizações podem não considerar essas customizações não padrão, levando a falhas e incompatibilidades.
- **Desempenho:** existe a possibilidade de as inserções diretas não serem otimizadas da mesma forma que as operações realizadas através dos serviços nativos. Isso pode levar a problemas de desempenho, especialmente em sistemas com grandes volumes de dados.
- **Suporte e Diagnóstico:** problemas decorrentes de customizações inadequadas são mais difíceis de diagnosticar e resolver. O suporte técnico pode ter dificuldades em entender e corrigir problemas que surgem devido a essas práticas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#top)

## Benefícios para adequação

A adequação para identificação dos registros oferece benefícios significativos, incluindo:

- **Rastreabilidade:** melhora a capacidade de rastrear e verificar a origem de todas as transações e dados. O registro correto e completo de informações é essencial para rastrear o histórico das operações, sua completude transacional e garantir a transparência em suas atividades;
- **Segurança Financeira:** reduz o risco de registros fraudulentos ou não autorizados. Inserir registros diretamente no banco de dados ou por API não autenticada pode criar vulnerabilidades de segurança, expondo seus dados a riscos de acessos não autorizados ou manipulação indevida;
- **Integridade de Dados:** contribui para a integridade e precisão dos dados no sistema. A integridade dos dados é fundamental quando se trata de lidar com as complexas regras de negócio, transações, registros contábeis e fiscais, além do correto controle do estoque em sua organização. Manter a integridade dos dados significa que suas informações estão completas, precisas e seguras, garantindo a confiabilidade de todos os aspectos de suas operações.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#top)

## Ação Recomendada

Caso receba um alerta devido a registros sem identificação de origem, é importante tomar as seguintes ações:

(1)** Revisão dos Registros:** analise os registros em questão para determinar sua validade e correção. Esta revisão poderá ser realizada através dessa tela.

Se os registros parecerem corretos, nenhuma ação adicional é necessária, no entanto, ao identificar registros suspeitos, contate sua equipe de TI para análise e ajustes internos.

(1)** Atribuição de Origem:** se possível, solicite ao seu fornecedor da solução integrada do Sankhya o ajuste da integração para adequação da aplicação para utilizar o [Gateway Sankhya](https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya).

**(1)** **Customizações:** tais como addons, botão de ação, ação agendada, regra personalizada, por exemplo, devem utilizar serviços nativos do **Sankhya Om**, para serem utilizadas as regras de negócios, validações e cálculos nativos. Assim, o desenvolvimento de customizações devem utilizar as seguintes boas práticas:

- **Utilização de APIs e Serviços Nativos:** utilize as APIs e serviços nativos disponíveis no **Sankhya Om** para realizar inserções e atualizações de registros de notas e financeiros. Esses serviços já incluem todas as validações e regras de negócio necessárias. Além disso, possibilita a identificação correta de origem destes registros;
- **Customizações através dos padrões do framework:** utilize os padrões de governança e desenvolvimento do framework de customização recomendados pelo **Sankhya Om**. Estes padrões foram projetados para permitir customizações sem comprometer a integridade do sistema e a identificação da origem de registros gerados por customizações.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#top)

## Grade Pedidos e Notas

Nesta grade serão apresentados a lista de registros sem origem conhecida para movimentos dos tipos:

![Imagem 7: Nesta grade serão apresentados a lista de registros sem origem conhecida para movimentos dos tipos:](https://ajuda.sankhya.com.br/hc/article_attachments/25443046839191)

| 1-NF Depósito | B-Movimento bancário | J-Pedido de Requisição |
| --- | --- | --- |
| 2-PD Devol. | C-Compra | K-Pedido de Transferência |
| Procuração | D-Devolução de venda | L-Devolução de Requisição |
| Warrant | E-Devolução de compra | M-Devolução de Transf. |
| 3-Saídas | F-Produção | N-Entradas |
| 4-Faturamento | G-Pagamento | O-Pedido de compra |
| 8-RD8 | I-Financeiro | P-Pedido de venda |
| Q-Requisição | R-Recebimento | T-Transferência |
| V-Venda |  |  |

O botão  ![Imagem 8: O botão "Atualizar" recarrega a tela para que novos registros sejam exibidos.](https://ajuda.sankhya.com.br/hc/article_attachments/16161956292375) **"Atualizar"** recarrega a tela para que novos registros sejam exibidos.

O botão ![Imagem 9: O botão "Exportar grade para PDF" permite gerar relatórios em PDF, planilha XLS ou XLSX e cubo de dados.](https://ajuda.sankhya.com.br/hc/article_attachments/16161956293143) **"Exportar grade para PDF"** permite gerar relatórios em PDF, planilha XLS ou XLSX e cubo de dados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#top)

## Grade Financeiros

Aqui são apresentadas a lista de registros sem origem conhecida e títulos financeiros.

Para obter detalhes de algum registro específico, basta dar um duplo clique nele que a tela será redirecionada para a [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) ou [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#top)

---

![Imagem 10: Para saber mais sobre as boas práticas de integração estabelecidas pela Sankhya, e delimitar os riscos informados…](https://ajuda.sankhya.com.br/hc/article_attachments/18585845270039) Para saber mais sobre as boas práticas de integração estabelecidas pela Sankhya, e delimitar os riscos informados acima, explore nossos recursos detalhados:

**Integração:**

[Boas Práticas para Integração](https://developer.sankhya.com.br/reference/boas-pr%C3%A1ticas-para-integra%C3%A7%C3%A3o)

[API de Serviços Gateway](https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya)

[Configurações Gateway](https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway)

[Mapeamento de serviços](https://developer.sankhya.com.br/reference/mapeamento-de-servi%C3%A7o)

[Status do Gateway](https://status-gateway.sankhya.com.br/)

[Sala da comunidade para dúvidas](https://comunidade.sankhya.com.br/c/integracao/api-de-servicos/39)

[Recursos de Capacitação Técnica](https://developer.sankhya.com.br/docs/tech-academy-sankhya)

**Addons (Customização):**

[Documentação sobre addons](https://developer.sankhya.com.br/docs/add-on)

[Sala da comunidade para dúvidas](https://comunidade.sankhya.com.br/c/add-ons/37)

[Recursos de Capacitação Técnica](https://developer.sankhya.com.br/docs/certifica%C3%A7%C3%A3o-sankhya-developer)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671-Registros-n%C3%A3o-identificados#top)
