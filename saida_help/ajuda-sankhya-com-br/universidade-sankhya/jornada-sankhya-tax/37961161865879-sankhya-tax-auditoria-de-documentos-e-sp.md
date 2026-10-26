---
id: "37961161865879"
titulo: "Sankhya TAX - Auditoria de Documentos e SPEDs"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37961161865879-Sankhya-TAX-Auditoria-de-Documentos-e-SPEDs"
trilha: "Universidade Sankhya > Jornada Sankhya Tax"
atualizado_em: "2026-08-12T15:39:42Z"
rotulos: ["Configuração", "SPED", "Fiscal", "Sankhya Tax", "Auditoria", "Artigo atualizado KCS", "Fiscal/Contábil - KCS", "Documentos Eletrônicos"]
---

# Sankhya TAX - Auditoria de Documentos e SPEDs

## Auditoria de Documentos e SPEDs

#### Qual é o objetivo desta rotina?

A auditoria de documentos e SPEDs tem como finalidade garantir que as notas fiscais eletrônicas e obrigações acessórias cadastradas no ERP Sankhya sejam auditadas de forma automatizada e confiável. Por meio dela, cada documento é analisado sob o ponto de vista tributário, validando dados, consolidando informações e assegurando que os processos fiscais estejam em conformidade com a legislação vigente. Assim, a gestão tributária se torna mais ágil, padronizada e com visibilidade centralizada.

#### Quais problemas essa funcionalidade resolve?

- Dificuldade em analisar documentos fiscais individualmente e com precisão.
- Ausência de rastreabilidade em processos de integração fiscal.
- Demora na identificação de inconsistências em obrigações acessórias.
- Risco de divergências por falta de atualização nos arquivos XML importados.
- Limitação no controle de status de documentos fiscais enviados e processados.
- Retrabalho manual ao reenviar documentos sem acompanhamento automatizado.

#### Quais são os riscos de não utilizar a auditoria de documentos e SPEDs?

Ao deixar de utilizar a rotina de auditoria via ASIS, a empresa perde a oportunidade de centralizar e validar seus documentos fiscais de forma automatizada, ficando sujeita à inconsistências nos registros e atrasos no cumprimento de obrigações legais. Isso pode resultar em falhas na entrega de arquivos fiscais, maior exposição a autuações e aumento no esforço manual da equipe para corrigir problemas que poderiam ter sido prevenidos pelo processo de integração.

#### Cenário de aplicação

A **Axis LTDA.** está fechando o mês e precisa garantir que todas as notas fiscais já enviadas à SEFAZ estejam em conformidade para compor o SPED. O analista acessa a rotina de **Auditoria de Documentos e SPEDs** no ERP Sankhya e encontra algumas notas de saída interestaduais já transmitidas, mas que apresentam inconsistências apontadas pelo sistema, como erro de CST e advertência de CFOP. Com base nos diagnósticos e fundamentos legais exibidos na tela, a equipe consegue identificar rapidamente os ajustes necessários para corrigir o processo antes da geração da obrigação acessória.

**Tarefa:** Assista ao vídeo de demonstração prática e, em sua base de testes, utilize a rotina de **Auditoria de Documentos e SPEDs** para consultar documentos já enviados, verificar os apontamentos, analisar os fundamentos legais e acompanhar o status de auditoria até que estejam prontos para compor o SPED.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1124842632)

#### Antes da prática: fique atento(a)

A integração acontece de duas formas, de acordo com o contexto:

- **Documentos e obrigações anteriores à 30/01/2025:**

A integração é manual, realizada pelo botão **“Integrar”**, onde o usuário define critérios como empresa, documento, operação e data de referência.

- **Documentos e obrigações incluídos no ERP Sankhya após 30/01/2025:**

Com as configurações e credenciamento concluídos, a integração passa a ocorrer de forma automática.

**Documentos Elegíveis:**

- Notas fiscais autorizadas ou canceladas.
- Documentos XML disponíveis no sistema, seguindo o padrão estabelecido pelo Portal de Importação.

**Importante:**

- O período de armazenamento dos dados é orientado pela configuração do parâmetro **IAQTDPLIMP**, que determina por quantos dias o sistema manterá os arquivos armazenados no portal. O padrão é 30 dias, mas esse período pode ser ajustado conforme necessário.
- A ativação do parâmetro **IALOGDETINT - Registro de log detalhado da integração** irá garantir que todas as etapas de integração com a ASIS serão rastreadas, permitindo que o suporte identifique e realize correções de forma ágil e assertiva.

#### É o momento de aplicar o conhecimento adquirido! Confira as orientações para auditar Documentos e SPEDs

1. **Para integrar Notas Fiscais eletrônicas retroativas** (anteriores à 30/01/2025)

- Acesse a tela **Sankhya TAX - Auditoria de Documentos e SPEDs**

**Menu:** Configurações » Rotinas » Sankhya TAX - Auditoria de Documentos e SPEDs

- No menu lateral, abra a aba **Documentos Eletrônicos** e selecione o documento ( **NFe/NFCe**) que deseja integrar

**Crie o cadastro prévio de integração**

- Acione o botão “**Integrar**”
- Selecione a **Empresa Credenciada** que será integrada, em seguida escolha os **Documentos Disponíveis**
- Avance para a próxima etapa
- Selecione as referências de busca:

  - **Operação**
  - **Data Inicial**
  - **Data Final**
- Clique em **Salvar**.

2. **Para validar auditorias realizadas**

- Utilize os filtros para ajustar a grade de resultados conforme necessidade de visualização, definindo: 

  - **Status de Envio**
  - **Tipo de Movimento**
  - **Empresa**
  - **Período**
- Confira as colunas apresentadas e atente-se a:

  - **Status de Envio**
  - **Status Sefaz**
  - **Auditado**
  - **Erros**
  - **Advertência**
- Dê um duplo clique sobre o registro desejado para observar divergências apresentadas.

O detalhamento da auditoria é exibido no **painel inferior**, apresentando o diagnóstico de cada tópico analisado. Já o **painel superior** mostra informações da nota que facilitam sua identificação, como **Número Único** e **Número da Nota**.

- Se houver erro ou advertência, selecione o registro com um duplo clique para visualizar o fundamento legal do apontamento.

3. **Para reenviar notas com falha de integração**

- Verifique nas colunas o “**Status** **de Envio**” e “**Auditado**” a informação apresentada.
- A coluna **Auditado** apresenta as seguintes classificações: 

  - **Não**: para notas ainda sem retorno da API da ASIS;
  - **Sim**: para notas integradas e com retorno com sucesso;
  - **Erro**: para notas que falharem na integração.
- Identificando falha de integração, selecione a nota e acione o botão “**Reenviar**”

**Atenção!** O botão só pode ser utilizado uma vez a cada 5 minutos. 

4. **Auditoria Obrigações Acessórias**

- Assim como nos Documentos Fiscais, os dados da Escrituração gerada no ERP Sankhya são apresentados de acordo com a definição de busca nos filtros e apresenta todos os seus erros e advertências com seus respectivos embasamentos legais.
- O tratamento de falhas de integração nas obrigações acessórias seguem o mesmo padrão dos documentos fiscais.
