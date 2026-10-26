---
id: "37701578065175"
titulo: "Como realizar e emissão de boleto rápido híbrido (código de barras e chave pix)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37701578065175-Como-realizar-e-emiss%C3%A3o-de-boleto-r%C3%A1pido-h%C3%ADbrido-c%C3%B3digo-de-barras-e-chave-pix"
trilha: "Universidade Sankhya > Jornada de Recebimentos"
atualizado_em: "2026-07-22T14:09:46Z"
rotulos: ["Movimentação Financeira", "Boleto", "Financeiro", "PIX", "API", "Sankhya"]
---

# Como realizar e emissão de boleto rápido híbrido (código de barras e chave pix)

| Categoria |
| --- |
| [O que é “Bolepix” qual a importância desse processo na Gestão Financeira?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701578065175-Como-realizar-e-emiss%C3%A3o-de-boleto-r%C3%A1pido-h%C3%ADbrido-c%C3%B3digo-de-barras-e-chave-pix#h_01KF183GGCBYMQ4GTZ3F0SXFCT) |
| [Quais problemas essas práticas resolvem?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701578065175-Como-realizar-e-emiss%C3%A3o-de-boleto-r%C3%A1pido-h%C3%ADbrido-c%C3%B3digo-de-barras-e-chave-pix#h_01KF1834J4KCJEJHKJK39SDASV) |
| [Quais os riscos de não as utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701578065175-Como-realizar-e-emiss%C3%A3o-de-boleto-r%C3%A1pido-h%C3%ADbrido-c%C3%B3digo-de-barras-e-chave-pix#h_01KF182YXAW5GH3JXPCRBVKT1H) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701578065175-Como-realizar-e-emiss%C3%A3o-de-boleto-r%C3%A1pido-h%C3%ADbrido-c%C3%B3digo-de-barras-e-chave-pix#h_01KFDV9FA7AV843W0KQHTNF1C7) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701578065175-Como-realizar-e-emiss%C3%A3o-de-boleto-r%C3%A1pido-h%C3%ADbrido-c%C3%B3digo-de-barras-e-chave-pix#h_01KF182RWW17BJ121650GJMV31) |
| [Agora é hora de executar o processo no ERP!](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701578065175-Como-realizar-e-emiss%C3%A3o-de-boleto-r%C3%A1pido-h%C3%ADbrido-c%C3%B3digo-de-barras-e-chave-pix#h_01KF182DN3CFJKJHFC62FQ5HMD) |
| [Emissão de boletos no portal de vendas ao confirmar a Nota.](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701578065175-Como-realizar-e-emiss%C3%A3o-de-boleto-r%C3%A1pido-h%C3%ADbrido-c%C3%B3digo-de-barras-e-chave-pix#h_01KF18289REPHYVH44534TT712) |
| [Impressão pela tela Impressão de Boletos.](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701578065175-Como-realizar-e-emiss%C3%A3o-de-boleto-r%C3%A1pido-h%C3%ADbrido-c%C3%B3digo-de-barras-e-chave-pix#h_01KF1822NQG99TDXHWM90HX1YW) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37701578065175-Como-realizar-e-emiss%C3%A3o-de-boleto-r%C3%A1pido-h%C3%ADbrido-c%C3%B3digo-de-barras-e-chave-pix#h_01KF181FA4267C8T9QH31J41AY) |

## Emissão de bolepix boleto rápido - API (Banco do Brasil, Itaú e Santander)

#### O que é “Bolepix” qual a importância desse processo na Gestão Financeira?

A emissão de boletos no Sankhya com QR code para pagamentos via Pix é um processo automatizado que simplifica e agiliza a cobrança. Durante a impressão do boleto, o sistema aciona o serviço **Boleto Rápido**, que registra o boleto no banco automaticamente, captura o **EMVPIX**, e imprime o código QR code no boleto.

Quando o pagamento é efetuado, o sistema realiza automaticamente a baixa do boleto e a conciliação financeira no módulo correspondente. Além disso, qualquer alteração ou cancelamento é enviado automaticamente para o banco, eliminando a necessidade de arquivos adicionais e aumentando a eficiência do processo.

#### Quais problemas essas práticas resolvem?

- **Falta de automação:** elimina a necessidade de enviar arquivos para o banco, realizando o registro e baixa automática, além de enviar atualizações e cancelamentos diretamente para o banco.
- **Erros humanos:** reduz falhas manuais na emissão, atualização e conciliação de boletos, garantindo maior precisão nos dados financeiros.
- **Dificuldade no pagamento:** oferece praticidade para o cliente, permitindo pagamentos rápidos e seguros com opções como Pix via QR code.
- **Falta de transparência:** proporciona atualizações em tempo real de todos os registros financeiros e operacionais, melhorando a visibilidade e o controle.
- **Cálculo manual de juros e multa:** automatiza o cálculo de valores adicionais em boletos vencidos, refletindo diretamente no sistema, sem a necessidade de ajustes manuais.

#### Quais os riscos de não as utilizar?

Sem automação, a emissão e conciliação de boletos tornam-se manuais, causando atrasos e aumentando os riscos de erros operacionais. A falta de integração com o banco pode gerar inconsistências financeiras, dificultando o controle e a confiabilidade dos dados.
A ausência de opções como o Pix via QR code, que hoje é a forma de pagamento mais prática e amplamente utilizada pelos clientes, dificulta a realização dos pagamentos, aumentando os atrasos e o risco de inadimplência. Além disso, sem cálculos automáticos de juros e multas, ajustes manuais consomem tempo e elevam as chances de falhas, afetando a eficiência operacional e a experiência do cliente.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1055572020)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa identificou a necessidade de modernizar seu processo de cobranças para reduzir atrasos nos pagamentos, oferecer mais praticidade aos clientes e melhorar o fluxo de caixa. Para isso, decidiu implementar a emissão de boletos rápidos com QR code para pagamentos via Pix, um método rápido e eficiente que atende às demandas do mercado atual.
A equipe financeira da empresa foi encarregada de configurar o sistema ERP Sankhya para integrar o serviço de **Boleto Rápido** com os bancos utilizados pela organização: **Banco do Brasil, Itaú e Santander**. O objetivo é garantir que todo o processo, desde a emissão até a conciliação dos boletos, ocorra de forma automática, confiável e sem a necessidade de envio manual de arquivos ao banco.

**Tarefa**: Configure a emissão de boletos rápidos com QR Code Pix no ERP Sankhya, e verifique se eles foram emitidos e transmitidos ao banco corretamente.

**Aviso importante!**

A simulação exige dados reais, como conta bancária e credenciais. Por isso, não realizaremos a movimentação prática no sistema.

#### Agora é hora de executar o processo no ERP!

##### Tarefa 1: Emissão de boletos no portal de vendas ao confirmar a Nota.

1. **Acessar a tela Portal de Vendas:**

- Vá para Comercial » Consulta » Portal de Vendas.

2. **Localizar a Nota de Venda:**

- Utilize os filtros disponíveis para buscar uma nota de venda não confirmada. Atente-se em buscar pelo tipo de Movimento Nota de Venda.
- Clique duas vezes sobre a nota para abri-la na **Central de Vendas**.

3. **Emitir o Boleto:**

- Ao clicar em Confirmar, selecione a opção de impressão do Boleto.

4. **Validar a Integração no Financeiro:**

- Na **Central de Vendas**: Na aba Financeiro, clique no botão Mov. Financeira, você será direcionado para a tela **Movimentação Financeira.**
- Confirme se os dados do boleto estão corretamente vinculados ao título financeiro na aba **Cobrança**.

##### Tarefa 2: Impressão pela tela Impressão de Boletos.

1. **Acessar a tela de Impressão de Boletos:**

- Vá para Financeiro » Rotinas » Impressão de Boletos.

2. **Configurar os filtros:**

- Na barra lateral esquerda, insira os seguintes dados:
- **Número financeiro** (referente ao número único)
- **Conta Bancária**

3. **Preencher os parâmetros do boleto:**

   - No menu **"Parâmetros Boleto"**, selecione:

     - **Agrupamento Boleto(s):** Um título por Boleto
     - **Gerar número do Boleto (nosso número)** - Marcado para registro do boleto
     - **Conta bancária -** Conta configurada para emissão do boleto.
     - **Modelo de Boleto:** O modelo de cobrança configurado.
     - **Ordenação Parceiro**
4. **Reimprimir o boleto:**

   - Clique no botão pré-visualizar boleto para visualizá-lo antes de imprimir ou no ícone da impressora para **imprimir** e escolha o formato desejado (PDF ou impressão física).
   - Verifique a impressão para confirmar que os dados do boleto estão corretos.

**Tarefa 3: Acompanhamento dos boletos registrados**

1. Acesse a tela **Acompanhamento de Boletos - API**: Financeiro > Consultas > Acompanhamento de Boletos - API
2. Utilize os filtros para localizar o boleto gerado. É necessário informar o campo **Data de Negociação.**
3. Confirme se o boleto foi registrado no banco e na sessão **Histórico do boleto** verifique se o status foi atualizado.

#### Correção e Repetição

- **Boleto com QR code:** deve estar visível e funcional para pagamento via Pix.
- **Registro no Banco:** O boleto deve ser registrado automaticamente no sistema do banco através da API.
- **Acompanhamento Confiável:** O status do boleto deve refletir corretamente no sistema, incluindo alterações realizadas.
