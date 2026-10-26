---
id: "40743969276439"
titulo: "Agente de Sugestão de Vendas: guia de Troubleshooting"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40743969276439-Agente-de-Sugest%C3%A3o-de-Vendas-guia-de-Troubleshooting"
trilha: "Manual do Produto > Comercial e Vendas > Vendas > Agente de Sugestão de Vendas > Guia de Troubleshooting"
atualizado_em: "2026-07-29T16:27:07Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "TOP", "Venda Mais", "Erro"]
---

# Agente de Sugestão de Vendas: guia de Troubleshooting

## Escopo do diagnóstico

Utilize este guia para investigar a ausência de sugestões, falhas de processamento e comportamento de fallback. O diagnóstico deve considerar quatro camadas:

1. **Infraestrutura e Requisitos:** versão do ERP e tipo de layout.
2. **Orquestração e Exibição:** webcomponent na Central de Vendas.
3. **Backend e Integração:** API de recomendação e regras persistidas (**TVIMBR**).
4. **Regras funcionais:** parâmetros estatísticos e elegibilidade de negócio.

## 1. Triagem rápida - Pré-requisitos de Infraestrutura

Antes de analisar logs, valide se o ambiente cumpre os requisitos mínimos discutidos no lançamento:

- **Versão do ERP:** O cliente deve estar na **versão 4.36** ou superior. Versões anteriores possuem falhas no gatilho do botão "Adicionar ao carrinho" que impedem o disparo do agente.
- **Compatibilidade de Layout:** O Agente de Sugestões **NÃO funciona no Layout Flex**. Certifique-se de que o usuário está utilizando o layout padrão da Central de Vendas.
- **Licenciamento:** Verifique se o produto **51 240 (Bia Ag de Sugestões de Vendas)** consta no contrato ativo do cliente.
- **Tipo de Operação (TOP):** O agente só é ativado para movimentações classificadas como **Venda** no Apoio à Decisão. Operações de **Devolução ou Bonificação** são ignoradas por regra de negócio.
- **Liberação do feature-gate**: Se a funcionalidade ainda estiver em fase de piloto, pode haver feature-gate que a habilita. Neste caso, após a liberação, é importante ‘Descartar cache’, na aba Geral da tela ‘Administração do Servidor’ para que nova validação dos gates seja realizada.

## 2. Diagnóstico de Ausência - Camada de exibição (Webcomponent)

Investigue estas causas quando o painel lateral não aparece ou permanece vazio:

- **Estado Lógico e Gatilhos:** O componente é reativo. Force uma mudança real no carrinho (remover ou incluir novo item) para disparar uma nova consulta.
- **Movimento Inelegível:** Confirme se a TOP do pedido está corretamente configurada com o tipo de movimento ‘Pedido de venda’.
- **Persistência de Erro Temporário:** Se houve um timeout na primeira tentativa, o sistema pode bloquear novas chamadas para o mesmo "estado de carrinho". Feche e reabra a Central de Vendas para resetar o cache do componente.
- **Inconsistência de Canais:** Se as sugestões aparecem na **Bia (Conversacional)** mas não no painel lateral, o problema é de injeção do Microfrontend e não da base de dados. Neste caso é preciso escalar para o time de produto e desenvolvimento.

## 3. Diagnóstico de Ausência - Camada de dados (Backend)

Investigue quando a API responde com sucesso, mas sem itens:

- **Geração de Sugestões de Venda:** verifique se essa tela está disponível no ambiente do cliente. Ela é habilitada em função da licença (produto 51240 ou pack 6071  (Bia Agents: Sugestões de Vendas)).
- Se a tela estiver disponível, mas, ao acessar, é exibida mensagem de falta de acesso, trata-se de feature gate habilitado. Neste caso, verifique com o time de produto e engenharia para a liberação e, depois, utilize a opção ‘Descartar Cache’ na tela Administração do Servidor para tentar novamente.
- **Execução "Sem Dados" ou "Falha":** Acesse  a tela **Geração de Sugestões de Venda** e verifique o status da última execução (programada para execução às 02:40 AM).
  - **Falha:** Erro técnico no processamento. Tente execução manual (com cautela devido ao volume de dados).
  - **Sem Dados:** Volume de cestas insuficiente ou coocorrências abaixo do limite estatístico.
- **Parâmetros Estatísticos (Configuração Remota):** Lembre-se que limites de Confiança, Lift e Contagem Mínima são **ajustados remotamente** pela equipe de engenharia. O suporte não deve tentar parametrizar estes valores localmente. Se o cliente não recebe sugestões e você acredita que há movimentações em volume suficiente para uma amostra estatisticamente relevante, escale para revisão global dos thresholds.
- **Validação via SQL (Workaround):** Enquanto a interface de visualização de pares de sugestões (Roadmap) não é lançada, realize consultas na tabela **TVIMBR** para confirmar se existem regras ativas para os produtos do carrinho, consultando os diferentes ‘CODPROD\_A’ para os quais foram gravadas regras de sugestões.

## 4. Análise de Fallback e Assertividade

O mecanismo de fallback é ativado para garantir cobertura quando os critérios originais são muito restritivos.

- **Identificação:** Verifique na tela de execução se o campo **Regras alternativas aplicadas (Fallback)** está como "Sim".
- **Impacto:** O fallback reduz a exigência estatística para mostrar mais produtos. Se o cliente reclamar de sugestões "óbvias" ou "irrelevantes", valide se o fallback está a ser acionado constantemente por falta de densidade de dados no histórico do cliente.

## 5. Checklist final para suporte N3

Antes de encaminhar para a Engenharia de Produto:

1. [ ] **Confirmar Versão:** O ERP está na 4.36?
2. [ ] **Validar Layout:** O cliente está usando o layout HTML5?
3. [ ] **Tela Geração de Sugestões de Vendas:** Disponível com detalhes de informações acessíveis?
4. [ ] **Status da Execução:** Qual o status e o número de "Pares Gerados" na última execução diária?
5. [ ] **Evidência SQL:** Existem registos na tabela **TVI MBR** para o ID do produto em questão?
6. [ ] **Contexto da TOP:** A operação está classificada corretamente como pedido de venda?

**Nota de Segurança Operacional:** Evite realizar execuções manuais de geração de sugestões durante o horário de pico em clientes com alto volume de notas, pois o processamento estatístico pode impactar a performance do banco de dados.
