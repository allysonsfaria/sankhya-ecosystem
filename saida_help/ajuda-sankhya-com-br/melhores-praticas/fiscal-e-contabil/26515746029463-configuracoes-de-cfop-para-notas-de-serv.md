---
id: "26515746029463"
titulo: "Configurações de CFOP para notas de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26515746029463-Configura%C3%A7%C3%B5es-de-CFOP-para-notas-de-Servi%C3%A7o"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:41:39Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "CFOP", "NFS-e", "Configurações de CFOP para notas de Serviço", "CFOPAQUSERVDEN", "CFOPAQUSERVFOR", "CFOPPRESERVDEN", "CFOPPRESERVFOR"]
---

# Configurações de CFOP para notas de Serviço

(1)** Tela -** Comercial » Arquivo » Cadastros » CFOP

CFOP (Código Fiscal de Operações e Prestações) é um código que identifica a natureza de circulação da mercadoria ou a prestação de serviços, tanto em operações de entrada quanto de saída, seja no mercado interno ou externo. A correta configuração dos CFOPs garante que os documentos fiscais, como notas fiscais, sejam emitidos de acordo com as legislações tributárias e que os tributos sejam calculados de maneira correta.

#### **(1)** Parâmetros que Influenciam na rotina

O sistema utiliza parâmetros globais para definir os CFOPs que serão aplicados automaticamente nas operações. Esses parâmetros podem ser configurados para que o sistema identifique corretamente se a operação é de **entrada** ou **saída** e se ocorre **dentro** ou **fora do estado**.

**Principais Parâmetros de CFOP no Sistema**

- **CFOPAQUSERVDEN**: define o CFOP de aquisição de serviço **dentro do estado**.
- **CFOPAQUSERVFOR**: define o CFOP de aquisição de serviço **fora do estado**.
- **CFOPPRESERVDEN**: define o CFOP de prestação de serviço **dentro do estado**.
- **CFOPPRESERVFOR**: define o CFOP de prestação de serviço **fora do estado**.

O sistema utilizará os CFOPs configurados nesses parâmetros somente se **todas** as condições abaixo forem atendidas:

![Imagem 1: O valor do parâmetro for diferente de zero ;](https://ajuda.sankhya.com.br/hc/article_attachments/26560428444695) O valor do parâmetro for **diferente de zero**;

![Imagem 2: O sistema estiver calculando ISS para o serviço prestado;](https://ajuda.sankhya.com.br/hc/article_attachments/26560444916503) O sistema estiver calculando **ISS** para o serviço prestado;

**Link manual Tela de CFOP:** [Manual - CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP)

**Ebook Gestão Fiscal:** [Ebook - Gestão Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/6331356477463-Ebook-Gest%C3%A3o-Fiscal)
